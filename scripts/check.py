#!/usr/bin/env python3
"""Run the same meaningful checks locally and in Actions."""
from pathlib import Path
import py_compile
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
for folder in ('importer', 'scripts'):
    for path in sorted((ROOT / folder).glob('*.py')):
        py_compile.compile(str(path), doraise=True)
py_compile.compile(str(ROOT / 'vivaldium'), doraise=True)
subprocess.run([sys.executable, '-m', 'unittest', 'discover', 'importer', '-v'], cwd=ROOT, check=True)
subprocess.run([sys.executable, 'importer/main.py', '--help'], cwd=ROOT, check=True)
