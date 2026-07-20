# Final live revalidation baseline

- Recorded UTC: `2026-07-20T19:33:14Z`
- Working branch: `master`
- Audited base commit: `b4bce6464001a59e8ea6b7430b03cf5f780c98a8`
- Remote `origin/master`: `b4bce6464001a59e8ea6b7430b03cf5f780c98a8`
- Public repository: https://github.com/Martin-Hausleitner/tribunal-public
- Repository visibility/default branch: `PUBLIC` / `master`

The base commit was created while this revalidation's OpenSpec artifacts were being prepared. It contains only the previously observed report cross-link and `report/evidence/revalidation-e2e.md`; no runtime, skill, persona, test, gate, matrix, or prior judge artifact changed between the initially observed `c77b434` and this base. The shared-worktree transition was re-read instead of overwritten.

## Initial dirty-path boundary

At the stable baseline, `git status --short --branch` showed only the new untracked directory `openspec/changes/revalidate-live-codex-tribunal-library/`. The report and earlier E2E ledger were already committed and synchronized with the remote. Subsequent files in this change are additive evidence or explicit report/OpenSpec updates.

## Tooling observed live

| Surface | Version/result |
|---|---|
| Python | `3.12.3` |
| OpenSpec | `1.4.1` |
| NotebookLM CLI | `nlm 0.8.9` |
| Required judge CLI | `grok 0.2.102 (ab5ebf69ac) [stable]` |
| Approved fallback CLI | `agy 1.1.4` |
| GitHub CLI | `gh 2.88.0` |

Authentication and public reachability are probed in their dedicated live tasks. Account names, tokens, cookies, and local credential paths are intentionally absent from public evidence.

## Canonical artifact inventory

The audited release surface contains:

- `tribunal.py`, `pyproject.toml`, `README.md`, and `LICENSE`;
- nine JSON personas including the disclosed Karpathy-inspired synthetic critic;
- the reusable `skill/SKILL.md`;
- repository examples and `tests/test_tribunal.py`;
- skill, CSV, and report gates under `scripts/`;
- prior completed OpenSpec changes and this 38-task revalidation change;
- the report, authoritative CSV matrix, GitHub JSON snapshot, NotebookLM ledgers, external-judge provenance, and source/install E2E ledgers under `report/`.

## Contract check

`openspec validate revalidate-live-codex-tribunal-library --strict` exited `0` before live work. The conclusion-free judge input is frozen separately in [`final-revalidation-judge-packet.md`](final-revalidation-judge-packet.md).
