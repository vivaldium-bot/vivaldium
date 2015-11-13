#!/usr/bin/env python3
"""Deterministic reconstruction of published Vivaldi source archives."""
from __future__ import annotations
import argparse, concurrent.futures, datetime as dt, fcntl, hashlib, html.parser, json, os, re, shlex, shutil, subprocess, sys, tarfile, tempfile, time
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]; DATA=Path(os.environ.get('VIVALDI_DATA_DIR',ROOT)).resolve(); CACHE=DATA/'cache'; ARCHIVES=CACHE/'archives'; UPSTREAM=CACHE/'chromium.git'
STATE=DATA/'rebuild-state'; WORK=DATA/'rebuild-work'; REPO=DATA/'rebuild-repo'
INDEX='https://vivaldi.com/source/'; CHROMIUM='https://github.com/chromium/chromium.git'; REMOTE='git@github.com:vivaldium-bot/vivaldium.git'
KEY=Path(os.environ.get('VIVALDI_SSH_KEY') or str(Path.home()/'.ssh/vivaldium'))
FORMAT=7; ARCHIVE_RE=re.compile(r'vivaldi-source_([0-9]+(?:\.[0-9]+)+)\.tar\.(?:xz|gz)$',re.I)
GROUPS=[(name,tuple(prefixes)) for name,prefixes in json.loads((ROOT/'config/groups.json').read_text())['groups']]

def run(args,cwd=None,input=None,env=None):
    if str(args[0])=='git':args=[args[0],'-c','core.hooksPath=/dev/null','-c','commit.gpgSign=false','-c','tag.gpgSign=false',*args[1:]]
    p=subprocess.run([str(x) for x in args],cwd=cwd,input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env={**os.environ,'GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':'/dev/null','GIT_LITERAL_PATHSPECS':'1','LC_ALL':'C',**(env or {})})
    if p.returncode:raise RuntimeError('%s: %s'%(' '.join(map(str,args)),p.stderr.decode(errors='replace').strip()))
    return p.stdout
def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()
def atomic(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n');os.replace(tmp,path)
def vkey(v):return tuple(map(int,v.split('.')))
def event(stage,**fields):
    row={'at':dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z'),'stage':stage,**fields};STATE.mkdir(parents=True,exist_ok=True)
    with open(STATE/'events.jsonl','a') as f:f.write(json.dumps(row,sort_keys=True)+'\n')
    print(json.dumps(row,sort_keys=True),flush=True)
def catalog_path(name='active'):return STATE/'catalog'/(name+'.json')

class Page(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
    def handle_starttag(self,t,a):
        a=dict(a);t=t.lower()
        if t=='tr':self.row={'text':{},'checksums':{}}
        elif self.row is not None and t=='td':
            c=a.get('class','').split();self.cell='modified' if 'modified' in c else 'size' if 'filesize' in c else None
        elif self.row is not None and t=='a':
            if ARCHIVE_RE.search(urlparse(a.get('href','')).path):self.row['href']=a['href']
            for k,v in a.items():
                if k.startswith('data-') and re.fullmatch(r'[0-9a-fA-F]{16,128}',v):self.row['checksums'][k[5:]]=v.lower()
    def handle_data(self,d):
        if self.row is not None and self.cell:self.row['text'][self.cell]=self.row['text'].get(self.cell,'')+d
    def handle_endtag(self,t):
        if t.lower()=='td':self.cell=None
        if t.lower()=='tr' and self.row is not None:
            if self.row.get('href'):self.rows.append(self.row)
            self.row=None
def parse_catalog(body):
    p=Page();p.feed(body);result={}
    for row in p.rows:
        url=urljoin(INDEX,row['href']);m=ARCHIVE_RE.search(urlparse(url).path)
        if not m:continue
        v=m.group(1);modified=row['text'].get('modified','').strip()
        if not modified:raise RuntimeError('missing source-index date for '+v)
        item={'version':v,'url':url,'filename':Path(urlparse(url).path).name,'publisher_checksums':row['checksums'],'source_date':dt.datetime.strptime(modified,'%Y-%m-%d %H:%M:%S').replace(tzinfo=dt.timezone.utc).isoformat().replace('+00:00','Z'),'timestamp_source':'Vivaldi source index Modified field, interpreted as UTC'}
        if v in result and result[v]['url']!=url:raise RuntimeError('conflicting URLs for '+v)
        result[v]=item
    return sorted(result.values(),key=lambda x:vkey(x['version']))
def discover():
    body=urlopen(Request(INDEX,headers={'User-Agent':'vivaldium-rebuild/5'}),timeout=90).read().decode('utf8','replace');data={'format':FORMAT,'index_url':INDEX,'index_sha256':hashlib.sha256(body.encode()).hexdigest(),'releases':parse_catalog(body)}
    key=data['index_sha256'][:16];atomic(catalog_path(key),data);atomic(catalog_path(),data);(STATE/'catalog'/(key+'.html')).write_text(body);event('discovered',catalog=key,count=len(data['releases']));return data
def catalog():
    if not catalog_path().exists():raise RuntimeError('run discover first')
    return json.loads(catalog_path().read_text())

def safe(s):
    p=PurePosixPath(s)
    if p.is_absolute() or '..' in p.parts or not p.parts:raise RuntimeError('unsafe archive path: '+s)
    return p
def validate_archive(path):
    with tarfile.open(path,'r:*') as t:
        for m in t:
            safe(m.name)
            if m.isdev() or m.isfifo() or m.ischr() or m.isblk():raise RuntimeError('unsupported archive member: '+m.name)
            if m.islnk():safe(m.linkname)
def publisher_digest(rel):
    for alg in ('sha512','sha256','sha1','md5'):
        if alg in rel['publisher_checksums']:return alg,rel['publisher_checksums'][alg]
    return None,None
def calc(path,alg):
    h=hashlib.new(alg)
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()
def download(rel):
    ARCHIVES.mkdir(parents=True,exist_ok=True);dst=ARCHIVES/rel['filename'];part=dst.with_name(dst.name+'.part');alg,want=publisher_digest(rel)
    if dst.exists():
        validate_archive(dst)
        if alg and calc(dst,alg)!=want:raise RuntimeError('cached archive checksum conflict: '+rel['version'])
        return
    for attempt in range(5):
        try:
            run(['curl','--fail','--location','--retry','2','--continue-at','-','--output',part,rel['url']]);validate_archive(part)
            if alg and calc(part,alg)!=want:raise RuntimeError('publisher checksum mismatch')
            got=sha(part);os.replace(part,dst);event('downloaded',version=rel['version'],archive_sha256=got,bytes=dst.stat().st_size);return
        except Exception:
            if attempt==4:raise
            time.sleep(2**attempt)
def extract(archive,out):
    if out.exists():raise RuntimeError('workspace exists: '+str(out))
    out.mkdir(parents=True);root=None;known={};pending=[];duplicates=[]
    with tarfile.open(archive,'r:*') as t:
        for m in t:
            p=safe(m.name);root=root or p.parts[0]
            if p.parts[0]!=root:raise RuntimeError('multiple archive roots')
            if len(p.parts)==1:continue
            rel=PurePosixPath(*p.parts[1:]);dst=out.joinpath(*rel.parts)
            def parent():
                cur=out
                for part in rel.parts[:-1]:
                    cur=cur/part
                    if cur.is_symlink():raise RuntimeError('archive writes through symlink ancestor: '+m.name)
                dst.parent.mkdir(parents=True,exist_ok=True)
            def replace_leaf():
                if os.path.lexists(dst):
                    if dst.is_dir() and not dst.is_symlink():raise RuntimeError('archive file conflicts with directory: '+m.name)
                    dst.unlink();duplicates.append(str(rel))
            if m.isdir():
                parent()
                if dst.is_symlink():raise RuntimeError('archive directory conflicts with symlink: '+m.name)
                dst.mkdir(parents=True,exist_ok=True);continue
            if m.issym():parent();replace_leaf();os.symlink(m.linkname,dst);known[str(rel)]=dst;continue
            if m.islnk():pending.append((rel,m.linkname));continue
            if not m.isfile():raise RuntimeError('unsupported archive member: '+m.name)
            parent();replace_leaf()
            with t.extractfile(m) as inp,open(dst,'xb') as output:shutil.copyfileobj(inp,output)
            os.chmod(dst,0o755 if m.mode&0o111 else 0o644);known[str(rel)]=dst
    while pending:
        next_pending=[];progress=False
        for rel,target in pending:
            q=safe(target);q=PurePosixPath(*q.parts[1:]) if q.parts[0]==root else q;src=known.get(str(q))
            if src and src.is_file() and not src.is_symlink():
                dst=out.joinpath(*rel.parts)
                if any((out.joinpath(*rel.parts[:n])).is_symlink() for n in range(1,len(rel.parts))):raise RuntimeError('hardlink writes through symlink ancestor: '+str(rel))
                if os.path.lexists(dst):
                    if dst.is_dir() and not dst.is_symlink():raise RuntimeError('archive hardlink conflicts with directory: '+str(rel))
                    dst.unlink()
                dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);known[str(rel)]=dst;progress=True
            else:next_pending.append((rel,target))
        if not progress:raise RuntimeError('invalid/cyclic hardlink')
        pending=next_pending
    if not root:raise RuntimeError('empty archive')
    if any(p.name=='.git' for p in out.rglob('.git')):raise RuntimeError('archive contains .git')
    if duplicates:event('archive-duplicate-members',archive=archive.name,count=len(duplicates),paths=duplicates)
def tree_entries(root):
    rows=[]
    for p in root.rglob('*'):
        if p.is_dir() and not p.is_symlink():continue
        rel=os.fsencode(str(p.relative_to(root)))
        if p.is_symlink():rows.append((rel,b'l',os.fsencode(os.readlink(p))))
        elif p.is_file():rows.append((rel,b'f',sha(p).encode(),b'x' if p.stat().st_mode&0o111 else b'-'))
        else:raise RuntimeError('unsupported source entry: '+str(p))
    return sorted(rows,key=lambda x:x[0])
def fingerprint(root):
    h=hashlib.sha256(b'vivaldium-tree-v1\0')
    for row in tree_entries(root):
        for field in row:h.update(str(len(field)).encode()+b':'+field+b'\0')
    return h.hexdigest()
def copy_children(src,dst,skip=()):
    dst.mkdir(parents=True,exist_ok=True)
    for p in src.iterdir():
        if p.name in skip:continue
        q=dst/p.name
        if p.is_dir() and not p.is_symlink():shutil.copytree(p,q,symlinks=True)
        elif p.is_symlink():os.symlink(os.readlink(p),q)
        else:shutil.copy2(p,q,follow_symlinks=False)

def chromium_version(src):
    values=dict(x.split('=',1) for x in (src/'chromium/chrome/VERSION').read_text().splitlines() if '=' in x);return '.'.join(values[x] for x in ('MAJOR','MINOR','BUILD','PATCH'))
def chromium_commit(version):
    if not UPSTREAM.exists():run(['git','init','--bare',UPSTREAM])
    tag='refs/tags/'+version
    present=subprocess.run(['git','-C',UPSTREAM,'rev-parse','--verify',tag+'^{commit}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
    if not present:run(['git','-C',UPSTREAM,'fetch','--no-tags','--depth=1',CHROMIUM,f'+{tag}:{tag}'])
    return run(['git','-C',UPSTREAM,'rev-parse',tag+'^{commit}']).decode().strip()
def export_upstream(commit,out):
    export_git_tree(UPSTREAM,commit,out)
def export_git_tree(repository,commit,out):
    out.mkdir(parents=True);raw=run(['git','-C',repository,'ls-tree','-rz',commit]).split(b'\0')[:-1];objects=[]
    for row in raw:
        meta,path=row.split(b'\t',1);mode,typ,obj=meta.split()
        if mode!=b'160000':objects.append((mode,obj,path))
    # Stream one blob at a time: historical Chromium trees are several GiB and
    # buffering `cat-file --batch` output can otherwise exhaust the runner.
    proc=subprocess.Popen(['git','-C',str(repository),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        for mode,obj,path in objects:
            proc.stdin.write(obj+b'\n');proc.stdin.flush();header=proc.stdout.readline().split()
            if len(header)!=3 or header[1]!=b'blob':raise RuntimeError('unexpected upstream object response')
            size=int(header[2]);data=proc.stdout.read(size);trailer=proc.stdout.read(1)
            if len(data)!=size or trailer!=b'\n':raise RuntimeError('truncated upstream object')
            dst=out/os.fsdecode(path);dst.parent.mkdir(parents=True,exist_ok=True)
            if mode==b'120000':os.symlink(os.fsdecode(data),dst)
            else:dst.write_bytes(data);os.chmod(dst,0o755 if mode==b'100755' else 0o644)
        proc.stdin.close()
        if proc.wait():raise RuntimeError('upstream object export failed: '+proc.stderr.read().decode(errors='replace'))
    finally:
        if proc.poll() is None:proc.kill();proc.wait()
        for stream in (proc.stdin,proc.stdout,proc.stderr):stream.close()
def group(path):
    for name,prefixes in GROUPS:
        if any(path==x.rstrip('/') or path.startswith(x) for x in prefixes):return name
    raise RuntimeError('ungrouped '+path)
def patches(base,target,dest):
    temp=Path(tempfile.mkdtemp(prefix='vivaldium-diff-',dir=WORK));repo=temp/'repo';shutil.copytree(base,repo,symlinks=True);env={'GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':'/dev/null','LC_ALL':'C','TZ':'UTC'}
    try:
        run(['git','init','-q'],cwd=repo,env=env);(repo/'.git/info/attributes').write_text('* -text -filter -ident\n')
        def stage(tree):
            run(['git','read-tree','--empty'],cwd=repo,env=env);rows=[];regular=[]
            for p in tree.rglob('*'):
                if '.git' in p.relative_to(tree).parts or (p.is_dir() and not p.is_symlink()):continue
                path=os.fsencode(str(p.relative_to(tree)));mode=b'120000' if p.is_symlink() else (b'100755' if p.stat().st_mode&0o111 else b'100644')
                if p.is_symlink():rows.append((mode,run(['git','hash-object','-w','--stdin'],cwd=repo,input=os.fsencode(os.readlink(p)),env=env).strip(),path))
                else:regular.append((mode,path))
            # Hash ordinary files in one literal Git invocation. Paths containing
            # newlines retain a per-file fallback because this Git build exposes
            # --stdin-paths but not a NUL-delimited variant.
            batched=[x for x in regular if b'\n' not in x[1]];special=[x for x in regular if b'\n' in x[1]]
            if batched:
                objects=run(['git','hash-object','-w','--no-filters','--stdin-paths'],cwd=repo,input=b''.join(b'./'+x[1]+b'\n' for x in batched),env=env).splitlines()
                if len(objects)!=len(batched):raise RuntimeError('literal object batch count mismatch')
                rows.extend((mode,obj,path) for (mode,path),obj in zip(batched,objects))
            for mode,path in special:rows.append((mode,run(['git','hash-object','-w','--stdin'],cwd=repo,input=(tree/os.fsdecode(path)).read_bytes(),env=env).strip(),path))
            rows=[mode+b' '+obj+b'\t'+path+b'\0' for mode,obj,path in rows]
            run(['git','update-index','-z','--add','--index-info'],cwd=repo,input=b''.join(rows),env=env)
        stage(repo);run(['git','-c','user.name=x','-c','user.email=x@y','commit','-qm','base'],cwd=repo,env=env)
        for p in list(repo.iterdir()):
            if p.name!='.git':shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()
        copy_children(target,repo);stage(repo)
        # Discover paths with the same rename policy used for patch generation.
        # Otherwise rename destinations can hide deletions of the old paths.
        indexed={os.fsdecode(x) for x in run(['git','diff','--cached','--no-renames','--name-only','-z','HEAD'],cwd=repo,env=env).split(b'\0')[:-1]}
        baseline={os.fsdecode(x[0]) for x in tree_entries(base)}
        published={os.fsdecode(x[0]) for x in tree_entries(target)}
        changed=sorted(indexed | (baseline ^ published));buckets={n:[] for n,_ in GROUPS};changed_set=set(changed)
        # A file/symlink becoming a directory (or the reverse) is one atomic
        # application unit, even when descendants normally belong elsewhere.
        transitions={}
        for p in changed:
            parts=p.split('/')
            ancestor=next(('/'.join(parts[:n]) for n in range(1,len(parts)) if '/'.join(parts[:n]) in changed_set),None)
            transitions[p]=ancestor or p
        for p in changed:buckets[group(transitions[p])].append(p)
        dest.mkdir();report=[];series=[]
        for order,(name,_) in enumerate(GROUPS,1):
            def diff(items):return run(['git','diff','--cached','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','HEAD','--',*items],cwd=repo,env=env)
            def split_added_file(path):
                """Represent one oversized file addition as ordered append patches.

                A single Git patch above GitHub's object limit cannot be stored.
                For a newly added file, a sequence of exact, strict patches
                from empty -> prefix -> final remains applicable and preserves the
                published final bytes. Each intermediate state is a normal Git
                binary patch, so this also preserves binary additions exactly.
                """
                exists=subprocess.run(['git','cat-file','-e','HEAD:'+path],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
                src=repo/path
                if exists or not src.is_file() or src.is_symlink():raise RuntimeError('indivisible patch exceeds 90 MiB: '+path)
                mini=Path(tempfile.mkdtemp(prefix='vivaldium-large-',dir=temp));out=mini/path;out.parent.mkdir(parents=True,exist_ok=True);mode=0o755 if src.stat().st_mode&0o111 else 0o644;chunks=[]
                try:
                    run(['git','init','-q'],cwd=mini,env=env);(mini/'.git/info/attributes').write_text('* -text -filter -ident\n');run(['git','-c','user.name=x','-c','user.email=x@y','commit','--allow-empty','-qm','empty'],cwd=mini,env=env)
                    with open(src,'rb') as inp,open(out,'ab') as output:
                        while data:=inp.read(16*1024*1024):
                            output.write(data);output.flush();os.chmod(out,mode);run(['git','add','-Af','--',path],cwd=mini,env=env);blob=run(['git','diff','--cached','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','HEAD','--',path],cwd=mini,env=env)
                            if len(blob)>90*1024*1024:raise RuntimeError('oversized split fragment: '+path)
                            chunks.append(([path],blob));run(['git','-c','user.name=x','-c','user.email=x@y','commit','-qm','append'],cwd=mini,env=env)
                    return chunks
                finally:shutil.rmtree(mini,ignore_errors=True)
            def split(units):
                items=[p for unit in units for p in unit]
                blob=diff(items)
                if len(blob)<=40*1024*1024:return [(items,blob)]
                if len(units)==1:
                    if len(blob)<=90*1024*1024:return [(items,blob)]
                    if len(items)==1:return split_added_file(items[0])
                    raise RuntimeError('indivisible path transition exceeds 90 MiB: '+items[0])
                middle=len(units)//2
                return split(units[:middle])+split(units[middle:])
            parts=[]
            paths=sorted(buckets[name])
            units={}
            for path in paths:units.setdefault(transitions[path],[]).append(path)
            units=list(units.values())
            for start in range(0,len(units),512):parts.extend(split(units[start:start+512]))
            for ordinal,(items,blob) in enumerate(parts,1):
                filename=f'{order:04d}-{name}-{ordinal:04d}.patch';(dest/filename).write_bytes(blob);series.append(filename);report.append({'group':name,'filename':filename,'paths':items,'bytes':len(blob),'sha256':sha(dest/filename)})
        (dest/'series').write_text(''.join(x+'\n' for x in series));return report
    finally:shutil.rmtree(temp,ignore_errors=True)
def short(paths):return ', '.join(paths[:12])+(' and %d more'%(len(paths)-12) if len(paths)>12 else '')
def release_context(info):
    """Match a dated release-family announcement without inferring Git commits."""
    inventory=ROOT/'config/changelogs.json'
    if not inventory.is_file():return {'match':'unavailable','references':[]}
    data=json.loads(inventory.read_text());family='.'.join(info['version'].split('.')[:2]);date=info['source_date'][:10]
    matches=[row for row in data['entries'] if row['product']=='Vivaldi Desktop' and row['type']=='desktop-release' and row['tag']==family and row['date']<=date]
    if len(matches)>1:raise RuntimeError('ambiguous changelog family: '+family)
    notes=ROOT/'config/release-notes.json';synopses={}
    if notes.is_file():
        note_data=json.loads(notes.read_text())
        if note_data.get('inventory_sha256')==data.get('manifest_sha256'):
            synopses={row['source']:row for row in note_data.get('notes',[])}
    references=[]
    for row in matches:
        reference={**row}
        if row['source'] in synopses:
            reference['synopsis']=synopses[row['source']]['synopsis']
            reference['source_html_sha256']=synopses[row['source']]['source_html_sha256']
            model_note=synopses[row['source']].get('openrouter',{})
            if model_note.get('source_html_sha256')==reference['source_html_sha256'] and isinstance(model_note.get('summary'),str):
                reference['openrouter_summary']=model_note['summary']
                reference['openrouter_model']=model_note['model']
        references.append(reference)
    return {'match':'release-family' if references else 'no-compatible-reference','inventory_sha256':sha(inventory),'release_note_snapshot_sha256':sha(notes) if notes.is_file() else None,'references':references,'limitation':'Inferred release-family context only; not an exact archive-build match or attribution of features to subsystem patches. Announcement dates do not replace source-index dates.'}
def context_description(context):
    rows=context.get('references',[])
    if not rows:return 'No date-compatible release-family announcement is mapped to this source archive.'
    return '\n'.join('Release context (family '+x['tag']+', announced '+x['date']+'): '+x['title']+'\n'+(('OpenRouter release summary ('+x['openrouter_model']+'): '+x['openrouter_summary']+'\n') if x.get('openrouter_summary') else '')+(('Official announcement synopsis: '+x['synopsis']+'\n') if x.get('synopsis') else '')+'Source: '+x['source'] for x in rows)+'\nThis is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.'
def release_subject(info):
    return 'feat(release): publish Vivaldi '+info['version']+' source archive'
def build_candidate(rel,archive,source,base,commit,out):
    out.mkdir();copy_children(source,out/'vivaldi',('chromium',));report=patches(base,source/'chromium',out/'patches');basepaths={os.fsdecode(x[0]) for x in tree_entries(base)};changes=[{'path':p,'group':r['group'],'patch':r['filename'],'absent_from_upstream':p not in basepaths} for r in report for p in r['paths']]
    if (ROOT/'.github').is_dir():shutil.copytree(ROOT/'.github',out/'.github',symlinks=True)
    shutil.copy2(ROOT/'vivaldium',out/'vivaldium');(out/'vivaldium').chmod(0o755)
    (out/'importer').mkdir();shutil.copy2(Path(__file__),out/'importer/main.py')
    for script in sorted((ROOT/'importer').glob('*.py')):
        if script.name!='main.py':shutil.copy2(script,out/'importer'/script.name)
    for name in ('pyproject.toml','uv.lock','.python-version','.gitignore'):
        shutil.copy2(ROOT/name,out/name)
    shutil.copytree(ROOT/'config',out/'config')
    for folder in ('docs','scripts'):
        if (ROOT/folder).is_dir():shutil.copytree(ROOT/folder,out/folder,ignore=shutil.ignore_patterns('__pycache__'))
    meta=out/'.vivaldium';meta.mkdir();info={'format':FORMAT,'version':rel['version'],'source_url':rel['url'],'source_sha256':sha(archive),'publisher_checksums':rel['publisher_checksums'],'source_date':rel['source_date'],'timestamp_source':rel['timestamp_source'],'published_tree_fingerprint':fingerprint(source),'chromium_tree_fingerprint':fingerprint(source/'chromium'),'vivaldi_tree_fingerprint':fingerprint(out/'vivaldi'),'chromium':{'version':chromium_version(source),'tag':chromium_version(source),'commit':commit,'source':CHROMIUM,'substrate':'tracked Chromium Git superproject tree; gitlinks omitted'},'patches':report,'history_type':'reconstructed; original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable'}
    info['release_context']=release_context(info)
    atomic(meta/'release.json',info);atomic(meta/'changelog.json',info['release_context']);atomic(meta/'changes.json',changes);atomic(meta/'groups.json',{'format':1,'groups':GROUPS});shutil.copy2(Path(__file__),meta/'importer.py')
    script=meta/'materialize.py';shutil.copy2(ROOT/'importer/materialize.py',script);script.chmod(0o755)
    lines=[f'# Vivaldi {rel["version"]} reconstructed release','', 'This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.','',f'* Chromium base: `{info["chromium"]["tag"]}` at `{commit}`.',f'* Published archive SHA-256: `{info["source_sha256"]}`.',f'* Complete normalized fingerprint: `{info["published_tree_fingerprint"]}`.','* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.','']
    lines += ['## Published release context','',context_description(info['release_context']),'']
    for name,_ in GROUPS:
        rows=[x for x in report if x['group']==name]
        if rows:
            paths=[p for x in rows for p in x['paths']];lines += [f'## {name}',f'{len(paths)} changed paths in {len(rows)} patch files ({sum(x["bytes"] for x in rows)} patch bytes).','',f'Paths: {short(paths)}.','']
    (meta/'release-report.md').write_text('\n'.join(lines));(out/'README.md').write_text('# Vivaldium\n\nReconstructed Vivaldi publication history. This repository retains all published source outside `chromium/` and complete patches against the exact Chromium Git superproject tag. Published dependency files absent from that base are retained as additions. Original Vivaldi commit history is unavailable; synthetic intermediate commits are not build claims. Run `uv run .vivaldium/materialize.py OUTPUT_DIR [CACHE_DIR]` from a tagged tree. See [operations](docs/OPERATIONS.md) for the Python/uv importer and monitoring commands.\n');return info
def materialize(release,out,cache=None):
    if out.exists():raise RuntimeError('output exists: '+str(out))
    info=json.loads((release/'.vivaldium/release.json').read_text());global UPSTREAM;old=UPSTREAM
    try:
        if cache:UPSTREAM=Path(cache)/'chromium.git'
        commit=chromium_commit(info['chromium']['tag'])
        if commit!=info['chromium']['commit']:raise RuntimeError('upstream tag resolves differently')
        out.mkdir(parents=True);export_upstream(commit,out/'chromium');rows={x['filename']:x for x in info['patches']}
        for name in (release/'patches/series').read_text().splitlines():
            patch=release/'patches'/name
            if name not in rows or not patch.is_file() or sha(patch)!=rows[name]['sha256']:raise RuntimeError('invalid patch '+name)
            run(['git','-c','core.attributesfile=/dev/null','apply','--check',patch],cwd=out/'chromium');run(['git','-c','core.attributesfile=/dev/null','apply',patch],cwd=out/'chromium')
        copy_children(release/'vivaldi',out);got=fingerprint(out)
        if got!=info['published_tree_fingerprint']:raise RuntimeError('fingerprint mismatch '+got+' != '+info['published_tree_fingerprint'])
        return got
    finally:UPSTREAM=old

def init_repo():
    if not (REPO/'.git').exists():REPO.mkdir(parents=True,exist_ok=True);run(['git','init','-q','-b','main'],cwd=REPO)
    run(['git','config','user.name','Vivaldi Devs'],cwd=REPO);run(['git','config','user.email','sync@vivaldium.org'],cwd=REPO)
    run(['git','config','core.autocrlf','false'],cwd=REPO);run(['git','config','core.filemode','true'],cwd=REPO)
    (REPO/'.git/info/attributes').write_text('* -text -filter -ident -working-tree-encoding\n')
def ref(name):
    p=subprocess.run(['git','rev-parse','--verify',name],cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    return p.stdout.decode().strip() if p.returncode==0 else None

def github_token():
    """Read just the GitHub token; never execute .env or expand its contents."""
    if os.environ.get('GITHUB_TOKEN'):
        return os.environ['GITHUB_TOKEN']
    path=ROOT/'.env'
    if not path.is_file():return None
    for line in path.read_text().splitlines():
        line=line.strip()
        if line.startswith('export '):line=line[7:].lstrip()
        name,sep,value=line.partition('=')
        if not sep or name.strip()!='GITHUB_TOKEN':continue
        value=value.strip()
        if value.startswith(('\"',"'")):
            quote=value[0];end=value.find(quote,1)
            if end<0:raise RuntimeError('GITHUB_TOKEN has an unterminated quote in .env')
            value=value[1:end]
        else:value=value.split(' #',1)[0].strip()
        if not re.fullmatch(r'[A-Za-z0-9_]+',value):
            raise RuntimeError('GITHUB_TOKEN must be a literal token value')
        return value
    return None

def github_get(path,token):
    req=Request('https://api.github.com'+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','User-Agent':'vivaldium-rebuild/6'})
    return json.loads(urlopen(req,timeout=30).read())

def publication_auth():
    if not KEY.is_file():raise RuntimeError('VIVALDI_SSH_KEY does not name a private key')
    ssh=['ssh','-F','/dev/null','-i',str(KEY),'-o','IdentitiesOnly=yes','-o','IdentityAgent=none','-o','BatchMode=yes','-o','UpdateHostKeys=no']
    auth=subprocess.run([*ssh,'-T','git@github.com'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    greeting=(auth.stdout+auth.stderr).decode(errors='replace')
    if auth.returncode!=1 or 'Hi vivaldium-bot! You\'ve successfully authenticated' not in greeting:
        raise RuntimeError('SSH key must authenticate as vivaldium-bot: '+greeting.strip())
    token=github_token()
    token_login=None
    if token:
        token_login=github_get('/user',token)['login']
        if token_login.casefold()!='vivaldium-bot':raise RuntimeError('GITHUB_TOKEN must belong to vivaldium-bot; got '+token_login)
        repo=github_get('/repos/vivaldium-bot/vivaldium',token)
        if not repo.get('permissions',{}).get('push'):raise RuntimeError('GITHUB_TOKEN account lacks push access to the destination')
    public=run(['ssh-keygen','-y','-f',KEY])
    fingerprint=run(['ssh-keygen','-lf','-','-E','sha256'],input=public).decode().split()[1]
    return {'GIT_SSH_COMMAND':shlex.join(ssh)}, {'ssh_account':'vivaldium-bot','token_account':token_login,'ssh_fingerprint':fingerprint,'remote':REMOTE}
def commit_release(tree,info):
    init_repo();old=ref('refs/heads/main');stage='staging-'+info['version']
    run(['git','checkout','-q','-B',stage,old] if old else ['git','checkout','-q','--orphan',stage],cwd=REPO)
    for p in list(REPO.iterdir()):
        if p.name!='.git':shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()
    copy_children(tree,REPO)
    env={'GIT_AUTHOR_NAME':'Vivaldi Devs','GIT_AUTHOR_EMAIL':'sync@vivaldium.org','GIT_COMMITTER_NAME':'Vivaldi Devs','GIT_COMMITTER_EMAIL':'sync@vivaldium.org','GIT_AUTHOR_DATE':info['source_date'],'GIT_COMMITTER_DATE':info['source_date']}
    def body(group,detail):return detail+'\n\nThis is synthetic reconstruction from a published Vivaldi source archive. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate commits are not claimed buildable; the release tag is the verified boundary.\n\nHistory-Type: reconstructed\nVivaldi-Version: '+info['version']+'\nVivaldi-Source-SHA256: '+info['source_sha256']+'\nChromium-Commit: '+info['chromium']['commit']+'\nReconstruction-Group: '+group+'\nSource-Date: '+info['source_date']+'\nTimestamp-Source: '+info['timestamp_source']
    def commit(subject,group,paths,detail):
        run(['git','add','-Af','--',*paths],cwd=REPO,env=env)
        if subprocess.run(['git','diff','--cached','--quiet'],cwd=REPO).returncode:run(['git','commit','-m',subject,'-m',body(group,detail)],cwd=REPO,env=env)
    for root in sorted(p.name for p in (REPO/'vivaldi').iterdir()):
        kind='build' if root in ('BUILD.gn','DEPS','LICENSE','README.md') else 'feat'
        commit(f'{kind}(vivaldi): import {root} from {info["version"]}','vivaldi/'+root,['vivaldi/'+root],f'Import the published Vivaldi source area `{root}` from source archive {info["version"]}.\n\nThis synthetic commit groups source by its top-level directory for review. It does not recover an original Vivaldi commit boundary.')
    for name,_ in GROUPS:
        rows=[x for x in info['patches'] if x['group']==name]
        if rows:
            paths=sorted({p for x in rows for p in x['paths']})
            kind='build' if name=='build' else 'feat'
            commit(f'{kind}(chromium-{name}): apply Vivaldi {info["version"]} delta','chromium/'+name,['patches/'+x['filename'] for x in rows],f'Apply the published Chromium {name} delta for Vivaldi source archive {info["version"]}, against pinned Chromium {info["chromium"]["version"]}.\n\nIt covers {len(paths)} distinct changed paths in {len(rows)} patch files ({sum(x["bytes"] for x in rows)} bytes). Representative paths: {short(paths)}.\n\nThe patch series is complete against this release\'s Chromium base. Files absent from the upstream superproject remain additions; that does not establish Vivaldi authorship.')
    run(['git','add','-Af'],cwd=REPO,env=env);run(['git','commit','--allow-empty','-m',release_subject(info),'-m',body('final','Publish the verified Vivaldi '+info['version']+' source archive with its patch order, provenance, reconstruction report, and portable materializer.\n\n'+context_description(info.get('release_context',{})))],cwd=REPO,env=env)
    head=ref('HEAD');atomic(STATE/'transactions'/(info['version']+'.json'),{'head':head,'old':old,'source_sha256':info['source_sha256']});return head,old
def finalize_release(info,head,old):
    """Called only after exporting and verifying the actual committed objects."""
    env={'GIT_COMMITTER_NAME':'Vivaldi Devs','GIT_COMMITTER_EMAIL':'sync@vivaldium.org','GIT_COMMITTER_DATE':info['source_date']}
    ident=run(['git','var','GIT_COMMITTER_IDENT'],cwd=REPO,env=env).decode().strip()
    tag_data=f'object {head}\ntype commit\ntag {info["version"]}\ntagger {ident}\n\nVivaldi {info["version"]} reconstructed publication release\n'
    tag=run(['git','mktag'],cwd=REPO,input=tag_data.encode()).decode().strip()
    commands=f'start\nupdate refs/heads/main {head} {old or "0"*40}\ncreate refs/tags/{info["version"]} {tag}\nprepare\ncommit\n'
    run(['git','update-ref','--stdin'],cwd=REPO,input=commands.encode())
    run(['git','symbolic-ref','HEAD','refs/heads/main'],cwd=REPO)
    run(['git','update-ref','-d','refs/heads/staging-'+info['version'],head],cwd=REPO)
    event('tagged',version=info['version'],sha=head,tag=tag)
def publish(version,head,expected):
    env,identity=publication_auth()
    if ref('refs/tags/'+version+'^{}')!=head:raise RuntimeError('publication commit does not match tag')
    lines=run(['git','ls-remote',REMOTE,'refs/heads/main',f'refs/tags/{version}'],env=env).decode().splitlines();remote=next((x.split()[0] for x in lines if x.endswith('refs/heads/main')),None)
    if remote!=expected:raise RuntimeError(f'remote main moved: expected {expected}, got {remote}')
    remote_tag=next((x.split()[0] for x in lines if x.endswith('refs/tags/'+version)),None)
    local_tag=ref('refs/tags/'+version)
    # A resumed backfill must never rewind main to an already published release.
    descendant=remote and subprocess.run(['git','merge-base','--is-ancestor',head,remote],cwd=REPO,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
    desired=remote if descendant else head
    if remote_tag==local_tag and remote==desired:
        journal=STATE/'events.jsonl'
        if journal.exists():
            with journal.open() as records:
                for line in records:
                    try:proof=json.loads(line)
                    except json.JSONDecodeError:continue
                    if proof.get('stage')=='published' and proof.get('remote')==REMOTE and proof.get('sha')==head and proof.get('tag')==local_tag:
                        event('publication-current',version=version,sha=head,tag=local_tag,remote_main=desired)
                        return desired
    verify_tag(version)
    if remote_tag!=local_tag or remote!=desired:
        objects=run(['git','rev-list','--objects','--no-object-names',head],cwd=REPO)
        sizes=run(['git','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],cwd=REPO,input=objects)
        oversized=[line.decode() for line in sizes.splitlines() if line.split()[1]==b'blob' and int(line.split()[2])>=100*1024*1024]
        if oversized:raise RuntimeError('GitHub blob limit exceeded: '+', '.join(oversized))
        event('publishing',version=version,sha=head,remote_main=remote)
        run(['git','push','--atomic',f'--force-with-lease=refs/heads/main:{remote or ""}',f'--force-with-lease=refs/tags/{version}:{remote_tag or ""}',REMOTE,f'{desired}:refs/heads/main',f'refs/tags/{version}:refs/tags/{version}'],cwd=REPO,env=env)
    confirmed=dict((name,oid) for oid,name in (line.split() for line in run(['git','ls-remote',REMOTE,'refs/heads/main',f'refs/tags/{version}'],env=env).decode().splitlines()))
    if confirmed.get('refs/heads/main')!=desired or confirmed.get('refs/tags/'+version)!=local_tag:raise RuntimeError('remote ref readback differs after publication')
    event('published',version=version,sha=head,tag=local_tag,remote=REMOTE,remote_main=desired)
    return desired
def process(rel,push,commit_tree=True):
    workspace=WORK/(rel['version']+'-'+str(os.getpid()));source=workspace/'source';base=workspace/'base';candidate=workspace/'candidate'
    completed=False
    try:
        archive=ARCHIVES/rel['filename'];extract(archive,source);event('extracted',version=rel['version'])
        commit=chromium_commit(chromium_version(source));export_upstream(commit,base);event('upstream-resolved',version=rel['version'],commit=commit)
        info=build_candidate(rel,archive,source,base,commit,candidate);event('patches-generated',version=rel['version'])
        materialize(candidate,workspace/'candidate-verified');event('candidate-verified',version=rel['version'])
        if commit_tree:
            head,old=commit_release(candidate,info);verify_commit(rel['version'],head);finalize_release(info,head,old)
            if push:publish_all([rel])
        else:
            event('extraction-ready',version=rel['version'],candidate=str(candidate));return
        completed=True
    except Exception as e:
        event('failed',version=rel['version'],error=str(e),workspace=str(workspace));raise
    finally:
        if completed:shutil.rmtree(workspace,ignore_errors=True)

def verify_commit(version,head):
    checkout=WORK/('tag-'+version+'-'+str(os.getpid()))
    result=WORK/('verify-'+version+'-'+str(os.getpid()))
    try:
        export_git_tree(REPO,head,checkout)
        got=materialize(checkout,result)
        info=json.loads((checkout/'.vivaldium/release.json').read_text())
        if info['version']!=version:raise RuntimeError('tag provenance version mismatch: '+version)
        event('committed-tree-verified',version=version,fingerprint=got,sha=head)
        return info
    finally:
        if result.exists():shutil.rmtree(result,ignore_errors=True)
        if checkout.exists():shutil.rmtree(checkout)
def verify_tag(version):
    tag='refs/tags/'+version
    if not ref(tag):raise RuntimeError('missing tag '+version)
    info=verify_commit(version,ref(tag+'^{commit}'))
    event('verified',version=version,fingerprint=info['published_tree_fingerprint'],tag=ref(tag))
    return info

def publish_all(rels):
    """Publish in catalog order, leasing each release against its predecessor."""
    env,_=publication_auth()
    remote_lines=run(['git','ls-remote',REMOTE,'refs/heads/main'],env=env).decode().splitlines()
    expected=remote_lines[0].split()[0] if remote_lines else None
    for rel in rels:
        head=ref('refs/tags/'+rel['version']+'^{}')
        if not head:raise RuntimeError('missing annotated tag '+rel['version'])
        expected=publish(rel['version'],head,expected)

def status():
    latest={};p=STATE/'events.jsonl'
    if p.exists():
        for line in p.read_text().splitlines():
            x=json.loads(line)
            if x.get('version'):latest[x['version']]=x
    for version in sorted(latest,key=vkey):print(version,latest[version]['stage'],latest[version].get('error',''))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=('discover','download','extract-patches','rebuild','verify','sync','publish','auth-check','status','materialize'));ap.add_argument('--all',action='store_true');ap.add_argument('--version');ap.add_argument('--publish-each',action='store_true');ap.add_argument('--workers',type=int,default=2);ap.add_argument('--release');ap.add_argument('output',nargs='?');ap.add_argument('cache',nargs='?');a=ap.parse_args()
    for p in (ARCHIVES,STATE/'catalog',WORK):p.mkdir(parents=True,exist_ok=True)
    if a.command=='materialize':
        if not a.release or not a.output:raise SystemExit('materialize requires --release RELEASE OUTPUT [CACHE]')
        print(materialize(Path(a.release).resolve(),Path(a.output).resolve(),a.cache));return
    if a.command=='status':status();return
    if a.command=='auth-check':print(json.dumps(publication_auth()[1],sort_keys=True));return
    with open(STATE/'lock','w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        if a.command=='discover':discover();return
        if a.command=='sync':
            discover();a.command='rebuild';a.publish_each=True
        rels=catalog()['releases'];rels=[x for x in rels if not a.version or x['version']==a.version]
        if not rels:raise RuntimeError('no matching releases')
        if a.command=='download':
            with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,a.workers)) as pool:
                list(pool.map(download,rels))
            return
        if a.command in ('extract-patches','rebuild'):
            for rel in rels:
                if a.command=='rebuild' and ref('refs/tags/'+rel['version']):
                    info=json.loads(run(['git','show','refs/tags/'+rel['version']+':.vivaldium/release.json'],cwd=REPO))
                    if info['version']!=rel['version'] or info['source_url']!=rel['url']:raise RuntimeError('existing tag provenance conflicts with catalog')
                    if sha(ARCHIVES/rel['filename'])!=info['source_sha256']:raise RuntimeError('imported archive checksum conflict: '+rel['version'])
                    if a.publish_each:publish_all([rel])
                    else:verify_tag(rel['version'])
                    continue
                download(rel)
                transaction=STATE/'transactions'/(rel['version']+'.json')
                if a.command=='rebuild' and transaction.exists():
                    pending=json.loads(transaction.read_text())
                    if pending['old']!=ref('refs/heads/main'):raise RuntimeError('pending transaction parent changed')
                    if pending['source_sha256']!=sha(ARCHIVES/rel['filename']):raise RuntimeError('pending transaction archive changed')
                    info=verify_commit(rel['version'],pending['head']);finalize_release(info,pending['head'],pending['old'])
                    if a.publish_each:publish_all([rel])
                    continue
                process(rel,a.command=='rebuild' and a.publish_each,a.command=='rebuild')
            return
        if a.command=='verify':
            for rel in rels:
                verify_tag(rel['version'])
            return
        if a.command=='publish':
            publish_all(rels)
            return
if __name__=='__main__':
    try:main()
    except Exception as e:print('error:',e,file=sys.stderr);sys.exit(1)
