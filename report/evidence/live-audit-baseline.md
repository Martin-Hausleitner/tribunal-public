# Live audit baseline

- Audit started UTC: `2026-07-20T17:52:16Z`
- Working branch: `master`
- Pre-audit commit: `29d3a6223cd9b559f14c80c27807019a77710b6f`
- Public remote: https://github.com/Martin-Hausleitner/tribunal-public
- Pre-audit local, tracking, and GitHub `master` SHA: identical at the commit above
- Pre-audit report blob: https://github.com/Martin-Hausleitner/tribunal-public/blob/29d3a6223cd9b559f14c80c27807019a77710b6f/report/codex-trib-lib-tribunal.md

## Repository inventory

The tracked release includes `tribunal.py`, `pyproject.toml`, nine validated JSON personas, `skill/SKILL.md`, two executable examples, one unit-test module, three report/skill/CSV gates, the prior OpenSpec change, the final report, a score matrix, and external-research/E2E evidence. At audit start the only worktree addition was the new untracked OpenSpec change `openspec/changes/live-audit-codex-tribunal-library/`; no tracked file had a local modification.

## Live tooling and authentication probes

| Surface | Observed result |
|---|---|
| NotebookLM CLI | `nlm 0.8.9`; authentication check succeeded; notebooks were listable |
| Required judge path | `grok 0.2.102`; authenticated; `grok-4.5` listed as available/default |
| Approved fallback | `agy` executable available; authenticated model catalog was listable |
| GitHub | `gh 2.88.0`; authenticated; repository reported `PUBLIC` with default branch `master` |
| Python | `Python 3.12.3` |
| OpenSpec | `1.4.1` |
| Test/report surfaces | `pytest`, `tests/test_tribunal.py`, `scripts/report_gate.py`, `scripts/csv_gate.py`, and `scripts/skill_gate.py` present |

Authentication outputs were inspected live but account names, token material, cookies, and profile paths are intentionally excluded from this public ledger.

## Evidence conventions

- Immutable live-run facts are stored under `report/evidence/` in Markdown or JSON.
- External-judge files contain the role, exact engine path, snapshot/input identity, returned verdict, and explicit limitations.
- Mutable adoption metadata includes a UTC snapshot and is never used as a score input.
- Commands are recorded without secrets; outputs are normalized only to remove terminal control codes, private account identifiers, and credentials.
- Synthesis occurs only after the three independent judge outputs are frozen.
