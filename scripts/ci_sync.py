#!/usr/bin/env python3
"""Actions entrypoint with literal environment inputs and persistent storage."""
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = os.environ.get('VIVALDI_DATA_DIR')
    if not data or not Path(data).is_absolute():
        raise SystemExit('Set VIVALDI_DATA_DIR to persistent absolute storage outside the Actions checkout')
    version = os.environ.get('INPUT_VERSION', '').strip()
    if version and not re.fullmatch(r'\d+(?:\.\d+)+', version):
        raise SystemExit('Invalid release version')
    command = [sys.executable, '-u', str(ROOT / 'importer/main.py')]
    catalog = Path(data) / 'rebuild-state/catalog/active.json'
    if not catalog.exists():
        subprocess.run([*command, 'discover'], check=True)
    # Keep an existing historical manifest frozen until that backfill finishes.
    args = ['rebuild', '--version', version] if version else ['rebuild', '--all']
    if os.environ.get('INPUT_PUBLISH') == 'true' or os.environ.get('GITHUB_EVENT_NAME') == 'schedule':
        args.append('--publish-each')
    subprocess.run([*command, *args], check=True)


if __name__ == '__main__':
    main()
