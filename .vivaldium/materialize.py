#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = []
# ///
"""Reconstruct a tagged release: materialize.py OUTPUT_DIR [CACHE_DIR]."""
from pathlib import Path
import runpy
import sys

root = Path(__file__).resolve().parent
sys.argv = [str(root / 'importer.py'), 'materialize', '--release', str(root.parent), *sys.argv[1:]]
runpy.run_path(str(root / 'importer.py'), run_name='__main__')
