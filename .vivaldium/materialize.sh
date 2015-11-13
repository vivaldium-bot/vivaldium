#!/usr/bin/env bash
set -euo pipefail
exec python3 "$(dirname "$0")/importer.py" materialize --release "$(dirname "$0")/.." "$@"
