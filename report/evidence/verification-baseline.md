# Codex Tribunal brief verification baseline

Captured before this pass's NotebookLM queries, GitHub metadata refresh, or external judge sessions. No credential, cookie, token, account identifier, or collaborator identity is retained.

## Repository state

- Baseline UTC: `2026-07-20T21:52:48Z`
- Branch: `master`
- Starting full HEAD: `9f1dc36899a530ad4477784b3d12e1fd5c302da1`
- Remote: `origin https://github.com/Martin-Hausleitner/tribunal-public.git`
- The inherited tracked worktree was clean at the first observation. This pass then created only `openspec/changes/verify-complete-codex-tribunal-library-brief/` before live work.
- A separate untracked directory, `openspec/changes/revalidate-trib-codex-trib-lib-brief/`, appeared later while this pass was running. It was not created, read, edited, validated, staged, or claimed by this pass and must remain excluded from the intended diff.

## Resource guard

The VCVM guard exited `0` at `2026-07-20T21:44:05Z` with `status=LIMIT_GUARD`, `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=59`, `weekly_left=41`, `weekly_reset=576331s`, and `fast=not_seen`. Weekly use is above the 50% threshold, so this pass starts no expensive Codex/OMX team burst. The brief-authorized `agy` path is used for all three fresh role judgments. No fast mode is used.

## Tool and authentication surface

| Surface | Observation |
|---|---|
| `nlm` | `0.8.9`; authenticated check exited `0` |
| Canonical NotebookLM identity | `80cffd38-0185-4f4d-ae00-bbc67c4bc515`, title `Tribunal IDR 2026-07-04` |
| Canonical public link | `https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515`; sharing API returned `is_public=true` and `access_level=public` |
| `grok` | `0.2.102 (ab5ebf69ac) [stable]`; not invoked because the resource guard controls this pass and the brief allows `agy` perspectives |
| `agy` | `1.1.4`; available models included Gemini 3.1 Pro, Gemini 3.5 Flash, Claude Sonnet/Opus 4.6, and GPT-OSS 120B variants |
| `openspec` | `1.4.1` |
| Python / build | Python `3.12.3`; build `1.5.0` |
| GitHub CLI | `2.88.0` |

## Starting artifact anchors

| Artifact | SHA-256 |
|---|---|
| `report/codex-trib-lib-tribunal.md` | `336e51e26aebf271e2312ba54fbaa021b2aada4d38fe1b9d20db6010cbf5da7f` |
| `report/codex-trib-lib-matrix.csv` | `3df2c3e52d1061c966a45502420ccae15fde14b3015a6dace3a27e7f7d2c451e` |
| `report/evidence/github-snapshot.json` | `26bf9ffd2a0f575bb0a4c37216fe7b427ff6e4b4e1e3001bf849d935a7795206` |
| `tribunal.py` | `208e268668da86ac2b6c26a65c87b2586137ed24b7f05d744ba24624e25ede28` |
| `skill/SKILL.md` | `ee9c3013bafa5dc04be1b8320c05f0cb88f78280492928938ec93074b668a016` |
| `personas/andrej-karpathy.json` | `98140b93007bf0265ad0c9440d499cfc408aaa372e4c2014ea59d95d60baadeb` |
| `tests/test_tribunal.py` | `9cdc02b673bd69c12a9a2adf78c9e3401702bd1772ad50762ba2baf2527a1d2b` |

## Planning gate

`openspec validate verify-complete-codex-tribunal-library-brief --strict` exited `0`: `Change 'verify-complete-codex-tribunal-library-brief' is valid`. Proposal, design, capability scenarios, and 53 checkable tasks were complete before any new NotebookLM query or judge synthesis.

## 30-minute guard heartbeat

At `2026-07-20T22:14:52Z` both configured paths were attempted. The Mac path `/Users/mh/.codex/codex-weekly-guard.sh` is absent on this VCVM and returned exit `1`; no Mac state is inferred. The VCVM guard returned exit `0` with `status=LIMIT_GUARD`, `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=65`, `weekly_left=35`, `weekly_reset=574507s`, and `fast=not_seen`. The pass remains on the already authorized `agy` path with no new expensive Codex/OMX team burst.

## Notebook baseline and concurrency note

The first exact notebook detail call returned `640` sources. The first full source-list reduction returned `640` total, `598` processed (`status=2`), and `42` failed (`status=3`). While this pass added sources, other unowned activity changed the shared notebook: a later inventory returned `658` total, `600` processed, and `58` failed. Counts are therefore timestamped observations, not a stable invariant. Every query in this pass uses an explicit selected source-ID set so unrelated concurrent additions cannot silently enter its grounding corpus.

## Judge packet freeze

The conclusion-free packet `report/evidence/verification-judge-packet.md` was frozen before any fresh `agy` role session at `2026-07-20T22:21:07Z` with SHA-256 `f5ad6478b25e1078e93b0250bc70630984100b608dc92211fc9f9bf423ba1d6d`. All three roles receive that exact packet and are forbidden from reading sibling verdicts or prior synthesis artifacts.
