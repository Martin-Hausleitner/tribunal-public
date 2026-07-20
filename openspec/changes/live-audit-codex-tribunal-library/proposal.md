## Why

The completed Codex Tribunal library still needs a fresh, independently auditable live run against the current brief: canonical NotebookLM IDR, three adversarial perspectives, verified OSS metadata, a real end-to-end proof, and a published report. Separating this run from the earlier implementation change preserves provenance and prevents stale evidence from being mistaken for current validation.

## What Changes

- Create or validate one canonical NotebookLM notebook, ingest authoritative and OSS sources, run cross-queries, and record the live notebook URL.
- Run three isolated high-effort judge perspectives covering knowledge/correctness, hard criticism/risks, and UX/feasibility, preserving their disagreements and engine provenance.
- Re-verify OSS candidates, repository links, feature coverage, snapshot star counts, and the differentiated 100-point comparison with exactly one crowned recommendation.
- Exercise the recommended Tribunal library and skill through a real user-facing end-to-end test case and preserve reproducible proof/logs.
- Publish a refreshed `report/codex-trib-lib-tribunal.md`, commit all required evidence, push it, and verify the remote blob URL.

## Capabilities

### New Capabilities

- `live-tribunal-audit`: A repeatable live audit contract combining NotebookLM IDR, three independent adversarial verdicts, verified OSS scoring, observable E2E proof, and publication evidence.

### Modified Capabilities

None. There are no canonical specifications under `openspec/specs/`; the prior completed change remains an unarchived historical implementation record.

## Impact

- Affects the canonical report and its supporting research, judge, metadata, and E2E evidence under `report/`.
- May require surgical fixes to `tribunal.py`, personas, `skill/SKILL.md`, tests, or documentation if the live audit exposes a failure.
- Uses external NotebookLM, Grok or the brief-approved `agy` fallback, GitHub metadata, and the configured Git remote.
