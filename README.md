# Vivaldium

Reconstructed Vivaldi publication history. This repository retains all published source outside `chromium/` and complete patches against the exact Chromium Git superproject tag. Published dependency files absent from that base are retained as additions. Original Vivaldi commit history is unavailable; synthetic intermediate commits are not build claims. Run `uv run .vivaldium/materialize.py OUTPUT_DIR [CACHE_DIR]` from a tagged tree. See [operations](docs/OPERATIONS.md) for the Python/uv importer and monitoring commands.
