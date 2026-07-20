# Frozen evidence packet for final independent revalidation judges

Frozen UTC: `2026-07-20T19:33:14Z`  
Repository snapshot base: `b4bce6464001a59e8ea6b7430b03cf5f780c98a8`

This packet contains verifiable inputs and disclosed boundaries only. It deliberately omits all prior judge prose, role scores, rank/crown decisions, final recommendations, and synthesis. Judges must not inspect `report/codex-trib-lib-tribunal.md` or any file whose name contains `judge-knowledge`, `judge-critique`, `judge-ux`, `external-attempts`, or `synthesis`.

## Assignment

Independently audit a public MIT-licensed Codex Tribunal Python library and reusable skill for exactly one assigned perspective: knowledge/correctness, hard criticism/risk, or CLI UX/implementation feasibility. The declared scope includes three primary modes, an optional comparison mode, a disclosed Karpathy-inspired synthetic persona, evidence-aware structured verdicts, NotebookLM research provenance, an OSS-first comparison contract, and public CLI/API/package paths.

## Permitted project surfaces

- `tribunal.py`, `README.md`, `skill/SKILL.md`, `personas/*.json`, and `pyproject.toml`.
- `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- `openspec/changes/live-audit-codex-tribunal-library/` and `openspec/changes/revalidate-live-codex-tribunal-library/` except task completion marks added after this freeze.
- `report/evidence/notebooklm-live-audit.md` and `report/evidence/notebooklm-revalidation.md` as generated research ledgers that require manual contradiction control.
- `report/evidence/live-audit-e2e.md` and `report/evidence/revalidation-e2e.md` as executable-proof claims to challenge against source behavior.
- `report/evidence/github-snapshot.json` and `report/codex-trib-lib-matrix.csv` as structured metadata/scoring inputs; do not inherit their winner as your conclusion.

## Verified runtime boundaries

- Public modes are `knowledge`, `critique`, `ui_ux`, and additional `comparison`.
- Each round selects three distinct persona slugs and makes three separate `JudgeBackend.evaluate` calls before `post-hoc-synthesis`.
- Separate calls and unique personas establish payload/process isolation only; they do not establish provider-memory isolation, distinct model families, statistical independence, factual correctness, or consensus debate.
- The standard-library-only `local-rules` backend checks structural readiness, records gaps, and has a `40/100` ceiling without a NotebookLM URL and `50/100` with one. It does not fetch that URL, inspect target semantics, or render pixels.
- Hardness minimums are one, one, two, and four effective rounds for `light`, `standard`, `hard`, and `brutal`. Nine bundled personas repeat after three rounds; an explicit three-person panel repeats every round.
- JSON and Markdown include persona/backend/engine/source provenance, findings, evidence, gaps, score, synthesis, and marker. A positive marker requires every view at least 80 with no backend-declared gap, but an empty gap list is not independently verified truth.
- The Karpathy-inspired critic cites three public repositories, preserves a runtime disclaimer, disclaims authorship/endorsement, and must not attribute generated conclusions to Andrej Karpathy.
- Routed skill names are host declarations. The core does not discover, verify installation of, or invoke external Codex skills.
- Capacity inputs plan per-run judge slots and fail closed inside that plan; they are not tokens, billing quotas, provider discovery, or durable cross-run enforcement.
- No bundled live provider, cross-family router, browser/TUI, persistent trace store, durable workflow state, cryptographic log chain, or prompt-injection defense is claimed.

## Live research facts available at freeze

- Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- The authenticated `nlm 0.8.9` revalidation ledger records notebook ID/title, public sharing, `336` total sources, `331` processed, and five failed duplicates/secondary items.
- The last four cross-queries returned knowledge `15/46`, critique `15/33`, UX `0/0`, and contradiction-control `8/24` source-ID/citation-mapping counts. The UX answer therefore cannot count as grounded research evidence.
- Manual control rejected stale `330` counts, an unrelated 70-row registry, stateful-quota claims, provider-family independence claims, and study-specific correlation/churn metrics misapplied to this project.
- Current code and direct execution outrank NotebookLM prose when they conflict.

## Live OSS metadata available at freeze

The authoritative snapshot is timestamped `2026-07-20T19:15:00Z` and contains eleven canonical, unarchived repositories. Its numeric star values are dated adoption context and contribute zero rubric points. Repository-level license qualifications in the JSON/CSV must be checked against primary license files, especially AutoGen's component-specific terms, OpenAI Evals dataset exceptions, Langfuse enterprise directories, and Phoenix's Elastic License 2.0 source-available status.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

A component cannot exceed its weight. A deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes a positive recommendation. Stars provide no rubric points.

## Required independent output

Return self-contained Markdown with:

1. assigned perspective and inspected scope;
2. severity-ordered findings with concrete file/source references;
3. all six component scores and a checked total out of 100;
4. evidence actually inspected;
5. explicit evidence gaps and unsupported claims;
6. `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. the exact sentence `I did not inspect any other final-revalidation judge output.`

Do not edit files. Do not inspect forbidden conclusion artifacts. Do not expose hidden chain-of-thought; provide concise, auditable rationale only.
