import importlib.util, io, shutil, tarfile, tempfile, unittest
from unittest.mock import patch
from pathlib import Path

spec=importlib.util.spec_from_file_location('imp',Path(__file__).with_name('main.py'))
imp=importlib.util.module_from_spec(spec);spec.loader.exec_module(imp)

class RebuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp=Path(tempfile.mkdtemp());self.oldwork=imp.WORK;self.oldstate=imp.STATE;imp.WORK=self.tmp/'work';imp.STATE=self.tmp/'state';imp.WORK.mkdir()
    def tearDown(self):
        imp.WORK=self.oldwork;imp.STATE=self.oldstate;shutil.rmtree(self.tmp)
    def test_patch_roundtrip_preserves_modes_symlinks_and_ignored_files(self):
        base=self.tmp/'base';target=self.tmp/'target';patchdir=self.tmp/'patches';base.mkdir();(base/'chrome').mkdir()
        (base/'chrome/file').write_bytes(b'old\r\n');(base/'chrome/removed').write_bytes(b'x');(base/'chrome/link').symlink_to('file');(base/'.gitignore').write_text('chrome/ignored\n');(base/'chrome/ignored').write_bytes(b'keep')
        shutil.copytree(base,target,symlinks=True);(target/'chrome/file').write_bytes(b'new\0binary');(target/'chrome/file').chmod(0o755);(target/'chrome/removed').unlink();(target/'chrome/link').unlink();(target/'chrome/link').symlink_to('new target');(target/'chrome/added').write_bytes(b'added')
        imp.patches(base,target,patchdir);rebuilt=self.tmp/'rebuilt';shutil.copytree(base,rebuilt,symlinks=True)
        for name in (patchdir/'series').read_text().splitlines():imp.run(['git','apply',patchdir/name],cwd=rebuilt)
        self.assertEqual(imp.fingerprint(target),imp.fingerprint(rebuilt))
    def test_fingerprint_ignores_empty_directories_but_not_symlink_targets(self):
        one=self.tmp/'one';two=self.tmp/'two';one.mkdir();two.mkdir();(one/'empty').mkdir();(one/'link').symlink_to('target');(two/'link').symlink_to('target')
        self.assertEqual(imp.fingerprint(one),imp.fingerprint(two));(two/'link').unlink();(two/'link').symlink_to('other');self.assertNotEqual(imp.fingerprint(one),imp.fingerprint(two))

    def test_extract_rejects_write_through_archive_symlink(self):
        archive=self.tmp/'unsafe.tar';payload=b'x'
        with tarfile.open(archive,'w') as tar:
            link=tarfile.TarInfo('root/redirect');link.type=tarfile.SYMTYPE;link.linkname='outside';tar.addfile(link)
            file=tarfile.TarInfo('root/redirect/file');file.size=len(payload);tar.addfile(file,io.BytesIO(payload))
        with self.assertRaisesRegex(RuntimeError,'symlink ancestor'):
            imp.extract(archive,self.tmp/'out')

    def test_extract_uses_final_duplicate_regular_member(self):
        archive=self.tmp/'duplicate.tar'
        with tarfile.open(archive,'w') as tar:
            for data in (b'first',b'final'):
                entry=tarfile.TarInfo('root/path');entry.size=len(data);tar.addfile(entry,io.BytesIO(data))
        out=self.tmp/'out';imp.extract(archive,out)
        self.assertEqual((out/'path').read_bytes(),b'final')

    def test_github_token_is_literal_and_environment_wins(self):
        (self.tmp/'.env').write_text('OPENROUTER_KEY=unused\nGITHUB_TOKEN="github_pat_fixture"\n')
        with patch.object(imp,'ROOT',self.tmp), patch.dict(imp.os.environ,{},clear=True):
            self.assertEqual(imp.github_token(),'github_pat_fixture')
            with patch.dict(imp.os.environ,{'GITHUB_TOKEN':'github_pat_environment'}):
                self.assertEqual(imp.github_token(),'github_pat_environment')
            (self.tmp/'.env').write_text('GITHUB_TOKEN=$(touch should_never_exist)\n')
            with self.assertRaisesRegex(RuntimeError,'literal token'):
                imp.github_token()
            self.assertFalse((self.tmp/'should_never_exist').exists())

    def test_move_between_groups_includes_old_path_deletion(self):
        base=self.tmp/'base';target=self.tmp/'target';base.mkdir();target.mkdir()
        (base/'chrome').mkdir();(target/'third_party').mkdir()
        (base/'chrome/moved').write_bytes(b'identical contents\n')
        (target/'third_party/moved').write_bytes(b'identical contents\n')
        patchdir=self.tmp/'patches';imp.patches(base,target,patchdir)
        rebuilt=self.tmp/'rebuilt';shutil.copytree(base,rebuilt)
        for name in (patchdir/'series').read_text().splitlines():
            imp.run(['git','apply',patchdir/name],cwd=rebuilt)
        self.assertEqual(imp.fingerprint(target),imp.fingerprint(rebuilt))

    def test_unusual_paths_and_type_transitions(self):
        base=self.tmp/'base';target=self.tmp/'target';base.mkdir();target.mkdir()
        for name in ('space name', 'tab\tname', 'line\nname', '"quoted', 'café'):
            (base/name).write_bytes(b'before')
            (target/name).write_bytes(b'after\x00')
        (base/'chrome').write_text('file becoming directory')
        (target/'chrome').mkdir();(target/'chrome/child').write_text('child')
        (base/'file').write_text('becomes symlink');(target/'file').symlink_to('space name')
        (base/'link').symlink_to('file');(target/'link').write_text('becomes file')
        (base/'third_party').write_text('dependency root becoming rendering subtree')
        (target/'third_party/WebKit').mkdir(parents=True)
        (target/'third_party/WebKit/file').write_text('rendering normally precedes dependencies')
        patchdir=self.tmp/'patches';imp.patches(base,target,patchdir)
        rebuilt=self.tmp/'rebuilt';shutil.copytree(base,rebuilt,symlinks=True)
        for name in (patchdir/'series').read_text().splitlines():
            imp.run(['git','apply',patchdir/name],cwd=rebuilt)
        self.assertEqual(imp.fingerprint(target),imp.fingerprint(rebuilt))

if __name__=='__main__':unittest.main()
