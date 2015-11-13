import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    'cleanup', Path(__file__).resolve().parents[1] / 'scripts/clean_legacy.py')
cleanup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cleanup)


class CleanupTests(unittest.TestCase):
    def test_targets_exclude_current_history_and_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('repo', 'rebuild-repo', 'cache/archives',
                         'rewrite-recovery-20260922T1420', 'rewrite-recovery-notes'):
                (root / name).mkdir(parents=True)
            self.assertEqual({p.name for p in cleanup.legacy_targets(root)},
                             {'repo', 'rewrite-recovery-20260922T1420'})

    def test_refuses_symlink_target_or_parent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'real').mkdir()
            (root / 'repo').symlink_to(root / 'real', target_is_directory=True)
            for target in (root / 'repo', root / 'repo/child'):
                with self.assertRaisesRegex(RuntimeError, 'symlink'):
                    cleanup.check_target(root, target)

    def test_duplicate_archive_must_match_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'actual_tar.xz').mkdir()
            (root / 'cache/archives').mkdir(parents=True)
            original = root / 'actual_tar.xz/vivaldi-source_8.2.4133.tar.xz'
            original.write_bytes(b'original')
            with self.assertRaisesRegex(RuntimeError, 'identical copy'):
                cleanup.check_archives(root)
            cached = root / 'cache/archives' / original.name
            cached.write_bytes(b'changed')
            with self.assertRaisesRegex(RuntimeError, 'identical copy'):
                cleanup.check_archives(root)
            cached.write_bytes(b'original')
            cleanup.check_archives(root)

    def test_only_release_workspaces_are_disposable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('1.0.435-123', 'notes', 'tag-1.0.435-123'):
                (root / 'rebuild-work' / name).mkdir(parents=True)
            self.assertEqual([p.name for p in cleanup.stale_workspaces(root)],
                             ['1.0.435-123'])
