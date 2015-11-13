import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('transactions_importer', Path(__file__).with_name('main.py'))
imp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(imp)


class TransactionTests(unittest.TestCase):
    def test_commit_verification_and_deterministic_atomic_tagging(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            upstream = root / 'upstream'
            upstream.mkdir()
            imp.run(['git', 'init', '-q'], cwd=upstream)
            (upstream / 'chrome').mkdir()
            (upstream / 'chrome/VERSION').write_text('MAJOR=1\nMINOR=2\nBUILD=3\nPATCH=4\n')
            (upstream / 'chrome/file').write_bytes(b'base\n')
            imp.run(['git', 'add', '.'], cwd=upstream)
            imp.run(['git', '-c', 'user.name=fixture', '-c', 'user.email=f@f', 'commit', '-qm', 'base'], cwd=upstream)
            imp.run(['git', 'tag', '1.2.3.4'], cwd=upstream)
            base_commit = imp.run(['git', 'rev-parse', 'HEAD'], cwd=upstream).decode().strip()
            results = []
            for iteration in range(2):
                runroot = root / str(iteration)
                work = runroot / 'work'
                work.mkdir(parents=True)
                with patch.multiple(imp, WORK=work, STATE=runroot / 'state', REPO=runroot / 'repo', UPSTREAM=upstream):
                    base = work / 'base'
                    imp.export_upstream(base_commit, base)
                    source = work / 'source'
                    shutil.copytree(base, source / 'chromium')
                    (source / 'chromium/chrome/file').write_bytes(b'changed\n')
                    (source / '.gitignore').write_text('ignored\n')
                    (source / '.gitattributes').write_text('* text eol=crlf filter=hostile\n')
                    (source / 'ignored').write_bytes(b'unchanged raw\r\n')
                    (source / 'link').symlink_to('ignored')
                    archive = work / 'archive'
                    archive.write_bytes(b'fixture archive')
                    rel = {'version': '1.0.435', 'url': 'https://example.test/source', 'publisher_checksums': {}, 'source_date': '2016-04-08T09:39:02Z', 'timestamp_source': 'fixture'}
                    candidate = work / 'candidate'
                    info = imp.build_candidate(rel, archive, source, base, base_commit, candidate)
                    head, old = imp.commit_release(candidate, info)
                    self.assertIsNone(old)
                    self.assertIsNone(imp.ref('refs/heads/main'))
                    self.assertIsNone(imp.ref('refs/tags/1.0.435'))
                    # Failure cannot make a candidate a public release boundary.
                    with patch.object(imp, 'materialize', side_effect=RuntimeError('fixture failure')):
                        with self.assertRaisesRegex(RuntimeError, 'fixture failure'):
                            imp.verify_commit('1.0.435', head)
                    self.assertIsNone(imp.ref('refs/heads/main'))
                    self.assertIsNone(imp.ref('refs/tags/1.0.435'))
                    imp.verify_commit('1.0.435', head)
                    imp.finalize_release(info, head, old)
                    self.assertEqual(imp.ref('refs/heads/main'), head)
                    release_ids = [(head, imp.ref('refs/tags/1.0.435'))]
                    exported = work / 'committed'
                    imp.export_git_tree(imp.REPO, head, exported)
                    self.assertEqual(imp.fingerprint(candidate / 'vivaldi'), imp.fingerprint(exported / 'vivaldi'))
                    self.assertTrue((exported / '.vivaldium/materialize.py').is_file())
                    self.assertFalse((exported / '.vivaldium/materialize.sh').exists())
                    portable_cache = runroot / 'portable-cache'
                    portable_cache.mkdir()
                    (portable_cache / 'chromium.git').symlink_to(upstream, target_is_directory=True)
                    portable_output = runroot / 'portable-output'
                    # Execute the committed Python/uv entrypoint, not this test's
                    # already imported implementation, using only pinned cache data.
                    imp.run([exported / '.vivaldium/materialize.py', portable_output, portable_cache], cwd=root)
                    self.assertEqual(imp.fingerprint(source), imp.fingerprint(portable_output))
                    # A successor can remove an entire patch group. Its series
                    # still starts from its own upstream base, not the old delta.
                    (source / 'chromium/chrome/file').write_bytes(b'base\n')
                    (source / 'ignored').unlink()
                    rel2 = {**rel, 'version': '1.0.436', 'source_date': '2016-04-09T09:39:02Z'}
                    next_candidate = work / 'next-candidate'
                    info2 = imp.build_candidate(rel2, archive, source, base, base_commit, next_candidate)
                    self.assertEqual(info2['patches'], [])
                    head2, old2 = imp.commit_release(next_candidate, info2)
                    self.assertEqual(old2, head)
                    self.assertEqual(imp.ref('refs/heads/main'), head)
                    self.assertIsNone(imp.ref('refs/tags/1.0.436'))
                    imp.verify_commit('1.0.436', head2)
                    imp.finalize_release(info2, head2, old2)
                    self.assertEqual(imp.ref('refs/heads/main'), head2)
                    release_ids.append((head2, imp.ref('refs/tags/1.0.436')))
                    results.append(release_ids)
            self.assertEqual(results[0], results[1])

    def test_changelog_does_not_attach_future_or_unrelated_announcements(self):
        early = imp.release_context({'version': '1.0.303', 'source_date': '2015-11-13T13:55:17Z'})
        self.assertEqual(early['references'], [])
        stable = imp.release_context({'version': '1.0.435', 'source_date': '2016-04-08T09:39:02Z'})
        self.assertEqual([row['tag'] for row in stable['references']], ['1.0'])
        unknown = imp.release_context({'version': '999.0.1', 'source_date': '2026-09-22T00:00:00Z'})
        self.assertEqual(unknown['references'], [])

    def test_resume_publication_does_not_rewind_main(self):
        expected_calls = []
        with patch.object(imp, 'publication_auth', return_value=({}, {})), \
             patch.object(imp, 'run', return_value=b'newer refs/heads/main\n'), \
             patch.object(imp, 'ref', side_effect=lambda name: name), \
             patch.object(imp, 'publish', side_effect=lambda version, head, old: expected_calls.append(old) or 'newer'):
            imp.publish_all([{'version': '1.0.303'}, {'version': '1.0.435'}])
        self.assertEqual(expected_calls, ['newer', 'newer'])


if __name__ == '__main__':
    unittest.main()
