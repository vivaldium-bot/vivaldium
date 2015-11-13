#!/usr/bin/env python3
"""Rebuild existing reconstructed tags with improved synthetic descriptions.

The source payload and patches are exported from already verified tags. Only
Vivaldium's generated metadata, tooling, and synthetic commit messages change.
The replacement repository is verified before any local or remote ref moves.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
IMPORTER_PATH = ROOT / 'importer/main.py'
spec = importlib.util.spec_from_file_location('vivaldium_importer', IMPORTER_PATH)
imp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(imp)


def replace_tree(source: Path, destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        if destination.is_dir() and not destination.is_symlink():
            shutil.rmtree(destination)
        else:
            destination.unlink()
    if source.is_dir() and not source.is_symlink():
        shutil.copytree(source, destination, symlinks=True)
    elif source.is_symlink():
        os.symlink(os.readlink(source), destination)
    else:
        shutil.copy2(source, destination, follow_symlinks=False)


def refresh_control_files(tree: Path, info: dict) -> dict:
    """Update only generated/reconstruction-controlled files in an exported tag."""
    for name in ('.github', 'importer', 'config', 'docs', 'scripts'):
        source = ROOT / name
        if source.exists():
            replace_tree(source, tree / name)
    for name in ('vivaldium', 'pyproject.toml', 'uv.lock', '.python-version', '.gitignore'):
        shutil.copy2(ROOT / name, tree / name, follow_symlinks=False)
    (tree / 'vivaldium').chmod(0o755)
    meta = tree / '.vivaldium'
    info = {**info, 'format': imp.FORMAT}
    info['release_context'] = imp.release_context(info)
    imp.atomic(meta / 'release.json', info)
    imp.atomic(meta / 'changelog.json', info['release_context'])
    shutil.copy2(IMPORTER_PATH, meta / 'importer.py')
    shutil.copy2(ROOT / 'importer/materialize.py', meta / 'materialize.py')
    (meta / 'materialize.py').chmod(0o755)
    report = [
        f'# Vivaldi {info["version"]} reconstructed release',
        '',
        'This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.',
        '',
        '## Published release context',
        '',
        imp.context_description(info['release_context']),
        '',
    ]
    (meta / 'release-report.md').write_text('\n'.join(report))
    (tree / 'README.md').write_text(
        '# Vivaldium\n\nReconstructed Vivaldi publication history. This repository retains all published source outside `chromium/` and complete patches against the exact Chromium Git superproject tag. Published dependency files absent from that base are retained as additions. Original Vivaldi commit history is unavailable; synthetic intermediate commits are not build claims. Run `uv run .vivaldium/materialize.py OUTPUT_DIR [CACHE_DIR]` from a tagged tree.\n'
    )
    return info


def tags_in_order(repo: Path) -> list[str]:
    rows = imp.run(['git', 'tag', '--list'], cwd=repo).decode().splitlines()
    return sorted(rows, key=imp.vkey)


def publish_replacement(repo: Path, versions: list[str]) -> None:
    env, _ = imp.publication_auth()
    remote_lines = imp.run(['git', 'ls-remote', imp.REMOTE, 'refs/heads/main', 'refs/tags/*'], env=env).decode().splitlines()
    remote = {name: oid for oid, name in (line.split() for line in remote_lines)}
    local_main = imp.run(['git', 'rev-parse', 'refs/heads/main'], cwd=repo).decode().strip()
    leases = ['--force-with-lease=refs/heads/main:' + remote.get('refs/heads/main', '')]
    refspecs = [f'{local_main}:refs/heads/main']
    for version in versions:
        ref = 'refs/tags/' + version
        leases.append('--force-with-lease=' + ref + ':' + remote.get(ref, ''))
        refspecs.append(f'{ref}:{ref}')
    arguments = ['git', 'push', '--atomic', *leases, imp.REMOTE, *refspecs]
    imp.run(arguments, cwd=repo, env=env)
    check = {name: oid for oid, name in (line.split() for line in imp.run(['git', 'ls-remote', imp.REMOTE, 'refs/heads/main', 'refs/tags/*'], env=env).decode().splitlines())}
    if check.get('refs/heads/main') != local_main:
        raise RuntimeError('remote main differs after replacement push')
    for version in versions:
        ref = 'refs/tags/' + version
        if check.get(ref) != imp.run(['git', 'rev-parse', ref], cwd=repo).decode().strip():
            raise RuntimeError('remote tag differs after replacement push: ' + version)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true', help='force-update main and reconstructed tags after local verification')
    args = parser.parse_args()
    original = imp.REPO
    versions = tags_in_order(original)
    if not versions:
        raise RuntimeError('no reconstructed tags to rewrite')
    work = Path(tempfile.mkdtemp(prefix='vivaldium-message-rewrite-', dir=imp.WORK))
    replacement = work / 'repo'
    old_repo = imp.REPO
    source_commits = {
        version: imp.run(['git', 'rev-parse', 'refs/tags/' + version + '^{}'], cwd=original).decode().strip()
        for version in versions
    }
    try:
        imp.REPO = replacement
        for version in versions:
            tree = work / ('tree-' + version)
            imp.export_git_tree(original, source_commits[version], tree)
            info = json.loads((tree / '.vivaldium/release.json').read_text())
            info = refresh_control_files(tree, info)
            head, parent = imp.commit_release(tree, info)
            imp.verify_commit(version, head)
            imp.finalize_release(info, head, parent)
            print(json.dumps({'stage': 'rewritten-verified', 'version': version, 'sha': head}), flush=True)
        if args.publish:
            publish_replacement(replacement, versions)
            print(json.dumps({'stage': 'replacement-published', 'versions': versions}), flush=True)
        # Swap only after every replacement tag has materialized successfully.
        archive = work / 'previous-repo'
        os.replace(original, archive)
        os.replace(replacement, original)
        shutil.rmtree(archive)
        print(json.dumps({'stage': 'replacement-installed', 'versions': versions}), flush=True)
    finally:
        imp.REPO = old_repo
        if work.exists():
            shutil.rmtree(work, ignore_errors=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('error:', error, file=sys.stderr)
        raise SystemExit(1)
