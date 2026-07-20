# Brief live closure baseline

Captured at `2026-07-20T20:31:59Z`, before any new NotebookLM query, GitHub refresh, or external judge call.

## Repository state

- Branch: `master`
- Starting full HEAD: `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`
- Remote: `origin https://github.com/Martin-Hausleitner/tribunal-public.git`
- Starting worktree: only the new untracked `openspec/changes/complete-live-codex-tribunal-library-brief/` planning directory; the inherited tracked tree was clean.
- New change: `complete-live-codex-tribunal-library-brief`, schema `spec-driven`, repo-local edit scope.

## Weekly guard heartbeat

The required VCVM guard returned exit `0` at `2026-07-20T20:31:59Z`: `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=51`, `weekly_left=49`, `weekly_reset=580632s`, `fast=not_seen`, status `LIMIT_GUARD`. Because weekly usage is at least 50%, this run uses no new expensive Codex/OMX team burst; it keeps the mandatory three Grok attempts and favors the explicitly authorized `agy` path for any fallback. No fast mode was observed.

## Tool surface

| Tool | Observed version |
|---|---|
| `nlm` | `0.8.9` (reported latest) |
| `grok` | `0.2.102 (ab5ebf69ac) [stable]` |
| `agy` | `1.1.4` |
| `openspec` | `1.4.1` |
| Python | `3.12.3` |
| `build` | `1.5.0` |
| GitHub CLI | `2.88.0` |

No credential, cookie, token, or environment value was captured.

## Canonical artifact inventory

The starting tree contains the requested public report and CSV matrix, a JSON GitHub snapshot, 30 prior evidence ledgers, the `tribunal.py` runtime, installable package metadata, three gate scripts, source and installed-package examples, unit tests, the reusable `skill/SKILL.md`, and nine persona JSON files including `personas/andrej-karpathy.json`. Historical evidence remains contextual only; this pass records fresh external and executable observations.

Starting SHA-256 anchors:

| Artifact | SHA-256 |
|---|---|
| `report/codex-trib-lib-tribunal.md` | `e9a9fe0076cc10bf2bc224707dafd6f2d6b2d55bd55aad381161264785ad3300` |
| `report/codex-trib-lib-matrix.csv` | `5275c7c7f3ba6f5d45d6e240c053042d90b0f2704eee9c626bb0416a68638f05` |
| `report/evidence/github-snapshot.json` | `fc4b955fd5f71e13fb08b6ba76711e3d7392ee00bec54b3bb97d72ba2d1c256c` |
| `tribunal.py` | `208e268668da86ac2b6c26a65c87b2586137ed24b7f05d744ba24624e25ede28` |
| `skill/SKILL.md` | `ee9c3013bafa5dc04be1b8320c05f0cb88f78280492928938ec93074b668a016` |
| `personas/andrej-karpathy.json` | `98140b93007bf0265ad0c9440d499cfc408aaa372e4c2014ea59d95d60baadeb` |
| `tests/test_tribunal.py` | `9cdc02b673bd69c12a9a2adf78c9e3401702bd1772ad50762ba2baf2527a1d2b` |

## Planning gate

`openspec validate complete-live-codex-tribunal-library-brief --strict` exited `0`: `Change 'complete-live-codex-tribunal-library-brief' is valid`. Proposal, design, capability scenarios, and the apply checklist were therefore complete before live evidence collection began.
