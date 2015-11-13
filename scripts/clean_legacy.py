#!/usr/bin/env python3
"""Remove obsolete local artifacts; preview by default, --apply to delete.

The project root comes from this script, never from a command-line path.
Current source caches, release history, secrets and journals are excluded.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ('repo', 'state', 'work', 'actual_tar.xz',
          'rebuild-state/recovery', 'cache/depot_tools')


def legacy_targets(root):
    targets = [root / name for name in LEGACY]
    targets += sorted(p for p in root.iterdir()
                      if re.fullmatch(r'rewrite-recovery-\d{8}T\d{4,6}Z?', p.name))
    return [p for p in targets if os.path.lexists(p)]


def check_target(root, target):
    relative = target.relative_to(root)
    if not relative.parts or '..' in relative.parts:
        raise RuntimeError('refusing broad deletion target')
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise RuntimeError(f'refusing symlink cleanup target: {current}')
        if current.is_mount():
            raise RuntimeError(f'refusing mounted cleanup target: {current}')
    # Nested mounts are not owned scratch; do not recurse across them either.
    if target.is_dir():
        for parent, dirs, _ in os.walk(target, followlinks=False):
            for name in dirs:
                child = Path(parent) / name
                if not child.is_symlink() and child.is_mount():
                    raise RuntimeError(f'refusing nested mount: {child}')


def check_processes(targets):
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit() or int(proc.name) == os.getpid():
            continue
        try:
            cwd = (proc / 'cwd').resolve(strict=True)
            argv = (proc / 'cmdline').read_bytes().split(b'\0')
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            continue
        for target in targets:
            prefix = os.fsencode(target)
            if cwd == target or target in cwd.parents or any(
                    a == prefix or a.startswith(prefix + b'/') for a in argv):
                raise RuntimeError(f'PID {proc.name} uses {target}; stop it before cleanup')


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def check_archives(root):
    original = root / 'actual_tar.xz'
    if not original.is_dir():
        return
    for archive in original.iterdir():
        if archive.is_file() and archive.name.endswith(('.tar.xz', '.tar.gz')):
            cached = root / 'cache/archives' / archive.name
            if not cached.is_file() or digest(archive) != digest(cached):
                raise RuntimeError(f'archive cache is missing an identical copy of {archive.name}')


def stale_workspaces(root):
    work = root / 'rebuild-work'
    if not work.is_dir():
        return []
    # Only version/PID directories created by this importer. Unknown directories
    # and Git worktrees need separate handling and are never guessed disposable.
    return sorted(p for p in work.iterdir()
                  if re.fullmatch(r'\d+(?:\.\d+)+-\d+', p.name))


def remove_targets(root, targets, apply):
    for target in targets:
        check_target(root, target)
    check_processes(targets)
    for target in targets:
        print(json.dumps({'action': 'delete' if apply else 'would-delete',
                          'path': str(target)}), flush=True)
        if apply:
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--stale-work', action='store_true',
                        help='also remove old release workspaces while importer is idle')
    parser.add_argument('--wait', action='store_true',
                        help='wait for the running importer before cleaning old workspaces')
    args = parser.parse_args()
    if not (ROOT / 'importer/main.py').is_file() or not (ROOT / 'vivaldium').is_file():
        raise RuntimeError('not a Vivaldium project root')
    lockdir = ROOT / 'rebuild-state'
    lockdir.mkdir(exist_ok=True)
    with (lockdir / 'cleanup.lock').open('a') as guard:
        fcntl.flock(guard, fcntl.LOCK_EX | fcntl.LOCK_NB)
        targets = legacy_targets(ROOT)
        for target in targets:
            check_target(ROOT, target)
        if args.apply:
            check_archives(ROOT)
        remove_targets(ROOT, targets, args.apply)
        if args.stale_work:
            with (lockdir / 'lock').open('a') as lock:
                try:
                    if args.wait:
                        print('Waiting for the importer lock before workspace cleanup',flush=True)
                    fcntl.flock(lock, fcntl.LOCK_EX | (0 if args.wait else fcntl.LOCK_NB))
                except BlockingIOError:
                    raise RuntimeError('importer is active; rerun --stale-work after it exits')
                remove_targets(ROOT, stale_workspaces(ROOT), args.apply)


if __name__ == '__main__':
    main()
