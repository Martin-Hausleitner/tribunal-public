# Codex Tribunal live revalidation baseline (2026-07-21)

Captured before this pass's content queries and external judge sessions. No credential, cookie, token, account identifier, collaborator identity, or private notebook title is retained.

## Repository and guard

- Baseline UTC: `2026-07-20T23:13:26Z`
- Branch: `master`
- Starting full HEAD: `56df1b0c99e3c75546585ad5e4aea6f784081db5`
- Remote: `origin https://github.com/Martin-Hausleitner/tribunal-public.git`
- Local HEAD equaled `origin/master`. The tracked tree was clean; the only untracked path was this pass's OpenSpec directory, `openspec/changes/revalidate-codex-tribunal-library-2026-07-21/`.
- VCVM guard at `2026-07-20T23:10:48Z`: `status=LIMIT_GUARD`, `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=73`, `weekly_left=27`, `weekly_reset=570842s`, `fast=not_seen`.
- The configured Mac guard path `/Users/mh/.codex/codex-weekly-guard.sh` was absent on this VCVM. No Mac state is inferred.
- Weekly usage is above the 50% threshold, so no expensive Codex/OMX team burst and no fast mode is used. The brief-authorized isolated Grok CLI path is used for the three judges.

## Tool surface

| Tool | Observed version/state |
|---|---|
| Python | `3.12.3` |
| `nlm` | `0.8.9`; authenticated check exited `0` |
| `grok` | `0.2.102 (ab5ebf69ac) [stable]` |
| OpenSpec | `1.4.1` |
| GitHub CLI | `2.88.0` |
| Git | `2.43.0` |

## Canonical NotebookLM identity and capacity

- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Public link: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Sharing check: `is_public=true`, `access_level=public`; the returned public link matched exactly.
- Account inventory: exactly `500` notebooks. A uniquely titled notebook creation probe failed safely with API code `3` / `INVALID_ARGUMENT`; no notebook was created.
- Initial canonical inventory: `874` total sources, `600` processed (`status=2`), and `274` failed (`status=3`).
- Pass manifest source add returned ID `ac80cbf6-cad3-491d-b8da-734ba78ec48b`, then settled with empty content in failed status `3`.
- Post-attempt inventory: `875` total, `600` processed, `275` failed. The failed source is excluded from every query and cited nowhere as research.
- Because the shared notebook is mutable and already at its processed-source ceiling, all accepted queries use explicit processed source IDs and fresh conversation IDs.

## Starting artifact anchors

| Artifact | SHA-256 |
|---|---|
| `report/codex-trib-lib-tribunal.md` | `163e7f09af0f50264c228f23a68caa792921c0edde03fac88544fd389673beda` |
| `report/codex-trib-lib-matrix.csv` | `db8639d2efcc0fa6a1c61860925e26841e0346cabadd1909816f65ade4a269d5` |
| `report/evidence/github-snapshot.json` | `9b2b5067e452eb6eeb5aee9c421bf2c4eabe3571e71a744fbcfbb733fa177e9c` |
| `tribunal.py` | `8476651c58b273722fb338e085cfe26a8363a5167d971047aac7b55f471d0657` |
| `skill/SKILL.md` | `ee9c3013bafa5dc04be1b8320f05f0cb88f78280492928938ec93074b668a016` |
| `personas/andrej-karpathy.json` | `98140b93007bf0265ad0c9440d499cfc408aaa372e4c2014ea59d95d60baadeb` |
| `tests/test_tribunal.py` | `8c09846d70417da3997ebf6785500cd9027b4094e31086aa0bcab3b4b5aa3341` |

The earlier report and ledgers are historical evidence only. Every mutable claim in the new handoff must point to this pass or be explicitly labeled historical.
