#!/usr/bin/env python3
"""Manage a logged backfill and its Python watcher without shell background jobs."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(os.environ.get('VIVALDI_DATA_DIR', ROOT)).resolve()
STATE = DATA / 'rebuild-state'
RECORD = STATE / 'service.json'


def start_ticks(pid):
    try:
        return Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()[19]
    except FileNotFoundError:
        return None


def alive(record):
    return bool(record.get('pid') and start_ticks(record['pid']) == record.get('start_ticks'))


def save(record):
    temporary = RECORD.with_suffix('.tmp')
    temporary.write_text(json.dumps(record, indent=2) + '\n')
    temporary.replace(RECORD)


def supervise(args):
    logdir = STATE / 'logs'
    logdir.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, '-u', str(ROOT / 'importer/main.py'), 'rebuild']
    command += ['--version', args.version] if args.version else ['--all']
    if args.publish_each:
        command.append('--publish-each')
    with (logdir / 'current.log').open('ab', buffering=0) as log, (logdir / 'watch.log').open('ab', buffering=0) as watchlog:
        worker = subprocess.Popen(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        watcher = subprocess.Popen([sys.executable, '-u', str(ROOT / 'importer/watch.py')], cwd=ROOT, stdout=watchlog, stderr=subprocess.STDOUT, start_new_session=True)
        stopping = False

        def stop(*_):
            nonlocal stopping
            stopping = True
            for child in (worker, watcher):
                if child.poll() is None:
                    os.killpg(child.pid, signal.SIGTERM)

        signal.signal(signal.SIGTERM, stop)
        signal.signal(signal.SIGINT, stop)
        record = {'pid': os.getpid(), 'start_ticks': start_ticks(os.getpid()), 'worker_pid': worker.pid, 'watcher_pid': watcher.pid, 'status': 'running', 'publish_each': args.publish_each}
        save(record)
        try:
            result = worker.wait()
        finally:
            if watcher.poll() is None:
                watcher.terminate()
            watcher.wait()
        record.update(status='stopped' if stopping else 'completed' if result == 0 else 'failed', exit_code=result)
        save(record)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('start', 'run', 'stop', 'status'))
    parser.add_argument('--publish-each', action='store_true')
    parser.add_argument('--version')
    args = parser.parse_args()
    STATE.mkdir(parents=True, exist_ok=True)
    record = json.loads(RECORD.read_text()) if RECORD.exists() else {}
    if args.command == 'status':
        print(json.dumps({**record, 'alive': alive(record)}, indent=2))
    elif args.command == 'stop':
        if alive(record):
            os.kill(record['pid'], signal.SIGTERM)
            print('Sent stop to the recorded supervisor; current main and tags are retained.')
        else:
            print('No recorded supervisor is running.')
    elif args.command == 'run':
        with (STATE / 'service.lock').open('w') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise SystemExit('A supervisor is already running')
            raise SystemExit(supervise(args))
    else:
        if alive(record):
            raise SystemExit('A supervisor is already running')
        command = ['uv', 'run', '--frozen', 'python', '-u', str(Path(__file__).resolve()), 'run']
        if args.publish_each:
            command.append('--publish-each')
        if args.version:
            command += ['--version', args.version]
        (STATE / 'logs').mkdir(exist_ok=True)
        with (STATE / 'logs/service.log').open('ab', buffering=0) as log:
            child = subprocess.Popen(command, cwd=ROOT, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        for _ in range(50):
            if child.poll() is not None:
                raise SystemExit('Supervisor failed to start; see rebuild-state/logs/service.log')
            current = json.loads(RECORD.read_text()) if RECORD.exists() else {}
            if alive(current):
                print(f'Supervisor PID {current["pid"]}; follow {STATE / "logs/current.log"}')
                return
            time.sleep(0.1)
        raise SystemExit('Supervisor startup was not confirmed; inspect service.log')


if __name__ == '__main__':
    main()
