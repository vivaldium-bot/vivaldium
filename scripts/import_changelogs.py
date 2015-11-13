#!/usr/bin/env python3
"""Import the supplied release inventory as data, without running ZIP contents."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def import_kit(path, destination):
    with zipfile.ZipFile(path) as archive:
        if archive.namelist().count('manifest.json') != 1:
            raise ValueError('kit must contain exactly one manifest.json')
        if archive.getinfo('manifest.json').file_size > 2_000_000:
            raise ValueError('kit inventory is unexpectedly large')
        raw = archive.read('manifest.json')
    entries = json.loads(raw)
    if not isinstance(entries, list):
        raise ValueError('kit inventory must be a list')
    seen = set()
    rows = []
    for item in entries:
        row = {key: item[key] for key in ('product', 'date', 'tag', 'title', 'source', 'type')}
        if any(not isinstance(value, str) or not value or any(ord(c) < 32 for c in value)
               for value in row.values()):
            raise ValueError('invalid inventory field')
        dt.date.fromisoformat(row['date'])
        url = urlparse(row['source'])
        if url.scheme != 'https' or url.netloc != 'vivaldi.com' or not url.path.startswith('/blog/'):
            raise ValueError('release references must link to the official Vivaldi blog')
        if row['source'] in seen:
            raise ValueError('duplicate release reference: ' + row['source'])
        seen.add(row['source'])
        rows.append(row)
    result = {
        'format': 1,
        'origin': 'User-supplied Vivaldi Desktop changelog kit; metadata inventory, not original Git history',
        'manifest_sha256': hashlib.sha256(raw).hexdigest(),
        'entries': sorted(rows, key=lambda row: (row['date'], row['tag'], row['source'])),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + '\n')
    temporary.replace(destination)
    return len(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kit', type=Path)
    args = parser.parse_args()
    count = import_kit(args.kit, ROOT / 'config/changelogs.json')
    print(f'Imported {count} release references into config/changelogs.json')
