# Project layout

`vivaldium` is the only command entrypoint. `importer/` holds implementation,
tests and monitoring. `scripts/` contains maintenance commands. `config/` contains deterministic
versioned grouping rules. `.github/` contains CI and scheduled-resume workflows.

The active rebuild owns these operational directories:

- `cache/`: retained source archives and Chromium objects.
- `rebuild-state/`: catalog snapshots, logs, journals, and locks.
- `rebuild-work/`: importer-owned temporary and failed-release workspaces.
- `rebuild-repo/`: the fresh local reconstructed Git history.

Obsolete repositories, extracted duplicates, experimental workspaces and recovery
bundles are removed by `scripts/clean_legacy.py`. The canonical source archives
remain in `cache/archives/`. There is no legacy compatibility materializer;
use `vivaldium materialize` or `uv run .vivaldium/materialize.py OUTPUT_DIR [CACHE_DIR]`
from a tagged release. Project automation is Python, managed by `pyproject.toml`,
`.python-version` and `uv.lock`. Shell scripts in published source remain intact.
