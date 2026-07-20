# Brief live-closure baseline

- Captured UTC: `2026-07-20T20:31:51Z`
- Branch: `master`
- Starting commit: `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`
- Remote: `origin https://github.com/Martin-Hausleitner/tribunal-public.git`
- Starting worktree: only the new untracked `openspec/changes/complete-live-codex-tribunal-library-brief/` planning change
- Weekly guard: `LIMIT_GUARD`; `session_used=9`, `session_left=91`, `weekly_used=51`, `weekly_left=49`, `weekly_reset=580632s`, `fast=not_seen`

## Tool baseline

- `nlm 0.8.9`
- `grok 0.2.102 (ab5ebf69ac) [stable]`
- `openspec 1.4.1`
- `Python 3.12.3`
- `build 1.5.0`

No credential, cookie, access token, or local authentication path is retained here.

## Artifact inventory

- Public delivery: `report/codex-trib-lib-tribunal.md` and `report/codex-trib-lib-matrix.csv`
- Prior evidence: 31 Markdown ledgers and one GitHub JSON snapshot under `report/evidence/`
- Runtime and packaging: `tribunal.py`, `pyproject.toml`, `README.md`, and examples
- Tests and gates: `tests/test_tribunal.py` and `scripts/csv_gate.py`
- Persona library: nine JSON personas, including `andrej-karpathy.json`, plus `personas/__init__.py`
- Reusable skill: `skill/SKILL.md`

## OpenSpec-first gate

Before any fresh NotebookLM query or external judge call, the distinct change `complete-live-codex-tribunal-library-brief` contained proposal, design, capability spec, and a 37-item implementation checklist. `openspec validate complete-live-codex-tribunal-library-brief --strict` returned:

```text
Change 'complete-live-codex-tribunal-library-brief' is valid
```
