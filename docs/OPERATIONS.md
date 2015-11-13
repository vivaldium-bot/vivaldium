# Operations

Run `./vivaldium status` for the latest stage per release. Follow
`rebuild-state/logs/current.log` for importer output and
`rebuild-state/logs/watch.log` for the periodic summary.

The normal local workflow is:

```bash
uv sync --frozen
./vivaldium discover
./vivaldium download --all --workers 2
./vivaldium rebuild --all
./vivaldium verify --all
```

All operational scripts are Python and use uv. `./vivaldium` is a Python
launcher, not a shell script. Use `uv run --frozen python scripts/check.py` for
the complete test command and `uv run --frozen python importer/watch.py` for
periodic progress (`--once` prints one snapshot). To publish each verified
release and retry pending pushes, run `./vivaldium rebuild --all --publish-each`.

For a persistent logged run and Python watcher:

```bash
uv run --frozen python scripts/service.py start --publish-each
uv run --frozen python scripts/service.py status
tail -F rebuild-state/logs/current.log
```

`service.py stop` stops the recorded process. `rebuild-state/logs/watch.log`
contains periodic summaries; `service.log` contains supervisor failures. The
supervisor records success only when its worker exits successfully; starting a
background process does not establish that any release was completed.

Import the user-provided changelog kit with:

```bash
uv run --frozen python scripts/import_changelogs.py vivaldi-desktop-changelog-kit.zip
```

Only the inventory is read from the ZIP; its scripts are never executed.
`config/changelogs.json` retains the inventory hash and official article links.
Final release commit descriptions and `.vivaldium/changelog.json` include a
date-compatible, matching major/minor announcement. Unmatched early snapshots
are recorded as unmatched. These are release-family references, not evidence of
original commit boundaries or assignments of advertised features to patches.
No AI service is used. Article dates do not replace source-index timestamps.

Actions uses a self-hosted runner labelled `vivaldium`, with uv installed by
`astral-sh/setup-uv`. Set repository variable `VIVALDI_DATA_DIR` to persistent
storage outside the checkout, `VIVALDI_SSH_KEY_PATH` to the runner's private key
path, and optional secret `VIVALDI_BOT_TOKEN` to a token owned by `vivaldium-bot`.
The runner must have the SSH key and a verified GitHub known-host entry already
installed. Manual runs publish only when requested; scheduled runs publish.
An existing source manifest stays frozen during backfill. These files do not
register a runner automatically.

Publication targets `https://github.com/vivaldium-bot/vivaldium.git` (SSH transport:
`git@github.com:vivaldium-bot/vivaldium.git`). Pushes use `~/.ssh/vivaldium` by
default; `VIVALDI_SSH_KEY` can override the path. The SSH handshake must identify
`vivaldium-bot`. Git pushes need no API token. This repository already exists;
there is no repository deletion/recreation command.

`./vivaldium auth-check` reports the SSH account, public-key fingerprint and
destination. If `GITHUB_TOKEN` is present in the environment or root `.env`, it
also verifies the token's account and repository access. Environment takes
precedence. `.env` is parsed as literal data, never sourced; other keys are unused.
Tokens and private keys are never printed or included in generated releases.

Preview or perform the repeatable local cleanup:

```bash
uv run --frozen python scripts/clean_legacy.py
uv run --frozen python scripts/clean_legacy.py --apply
uv run --frozen python scripts/clean_legacy.py --apply --stale-work
```

Cleanup permanently deletes its exact legacy targets without creating backups.
It verifies duplicate source archives against the retained cache, refuses active
processes using its targets, and refuses symlink targets and mounted directories.
The last command also removes importer-created release workspaces under the
importer's exclusive lock; it refuses that part while an import is running.
Add `--wait` to wait for the importer to exit before cleaning stale workspaces.
