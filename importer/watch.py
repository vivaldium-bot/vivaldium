#!/usr/bin/env python3
"""Print a periodic reconstruction summary; use --once for a single snapshot."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import signal
import threading

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(os.environ.get('VIVALDI_DATA_DIR', ROOT)).resolve()


def snapshot():
    latest = {}
    published = set()
    path = DATA / 'rebuild-state/events.jsonl'
    if path.exists():
        with path.open() as stream:
            for line in stream:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue  # The writer may be appending its last record.
                if event.get('version'):
                    latest[event['version']] = event
                    if event['stage'] == 'published':
                        published.add(event['version'])
    print(dt.datetime.now(dt.timezone.utc).isoformat(), flush=True)
    print(f'{len(published)} releases have publication records; free {shutil.disk_usage(DATA).free // 2**30} GiB', flush=True)
    for version in sorted(latest, key=lambda v: tuple(map(int, v.split('.')))):
        row = latest[version]
        print(version, row['stage'], row.get('error', ''), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--interval', type=float, default=30)
    args = parser.parse_args()
    if args.interval <= 0:
        parser.error('--interval must be positive')
    stop = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stop.set())
    signal.signal(signal.SIGINT, lambda *_: stop.set())
    while True:
        snapshot()
        if args.once or stop.wait(args.interval):
            break


if __name__ == '__main__':
    main()
