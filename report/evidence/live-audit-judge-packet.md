# Frozen evidence packet for live-audit judges

Frozen UTC: `2026-07-20T18:04:59Z`  
Repository snapshot base: `a8caf856425dc88be124a58e9be1aee2a8cf3df6`

This common packet is conclusion-free: it contains verified review inputs, disclosed limits, and the scoring rubric, but no sibling verdict, final synthesis, candidate total, rank, or crown. Each judge must independently inspect the relevant repository files and return its own decision.

## Assignment

Audit a public MIT-licensed Codex Tribunal library and reusable skill for three primary perspectives: knowledge/correctness, hard criticism/risk, and UI/UX feasibility. The release must have honest engine provenance, a disclosed Karpathy-inspired synthetic persona, live NotebookLM research, an OSS-first comparison, a real public-interface E2E proof, and a published report.

## Current project surfaces

- `tribunal.py`: dependency-free Python API and CLI.
- `README.md`: public contracts, modes, hardness/Nx behavior, backend boundary, packaging, limits, and gates.
- `personas/*.json`: nine validated persona documents.
- `skill/SKILL.md`: reusable routing and anti-fake workflow.
- `pyproject.toml`, `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- `report/codex-trib-lib-tribunal.md`: prior published synthesis, which must be challenged rather than trusted.
- `report/evidence/notebooklm-live-audit.md`: fresh corpus/source/query ledger with manual contradiction audit.
- `report/evidence/github-snapshot.json`: new live repository, activity, README, license, and feature metadata.
- `openspec/changes/live-audit-codex-tribunal-library/`: fresh proposal, design, spec, and task contract.

## Verified runtime boundaries

- Public modes are `knowledge`, `critique`, `ui_ux`, and optional `comparison`.
- Three distinct persona slugs are selected per round and sent through separate `JudgeBackend.evaluate` calls before post-hoc synthesis.
- The bundled `local-rules` backend reports structural readiness and explicit evidence gaps; it performs no semantic target, URL-content, or visual inspection.
- Unique personas and separate calls do not enforce different model families or statistical independence.
- Hardness minimums are 1/1/2/4 rounds for light/standard/hard/brutal. With nine bundled personas, the fourth round repeats the first; an explicit three-person panel repeats every round.
- Reports retain backend/engine/source provenance, findings, evidence, gaps, final score, and marker in JSON/Markdown.
- Expected input errors are intended to exit `2` with concise stderr; this audit has not yet rerun the final E2E gate.
- Positive markers require every judge score to be at least 80 and every declared evidence-gap list to be empty. An empty list remains a backend assertion, not independent truth.
- The Karpathy-inspired critic is explicitly synthetic, cites public repositories, carries a runtime disclaimer, and forbids impersonation or attribution to Andrej Karpathy.
- No bundled live provider, cross-family router, browser/TUI, trace database, dynamic billing/quota discovery, cryptographic log chain, durable workflow runtime, or prompt-injection defense exists.

## Fresh NotebookLM facts

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Live audit verified title `Tribunal IDR 2026-07-04`, public sharing, and `336` sources after adding six current release/OpenSpec artifacts.
- All twelve targeted primary/project/criteria URLs were present and processed. Five failed sources were secondary/duplicated Medium articles and are excluded from decision evidence.
- Four fresh cross-queries covered correctness/independence, hostile risks, CLI UX, and contradiction/source attribution.
- NotebookLM supported the structural/semantic boundary and the need for external live proof, but also repeated superseded findings and misread explicit non-capabilities as claims. The manual corrections in the ledger are part of the evidence.

## Live OSS candidate evidence

The candidate set is Codex Tribunal, promptfoo, Microsoft Agent Framework, DeepEval, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness. Stars, activity, canonical README links, and license text were queried live at `2026-07-20T18:04:59Z`; stars receive zero points. AutoGen's current README says it is in maintenance mode and recommends Microsoft Agent Framework for new projects. Phoenix is ELv2 source-available, not OSI open source. OpenAI Evals has dataset-specific license exceptions; Langfuse excludes declared enterprise directories from its MIT grant.

## Rubric supplied to every judge

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Total: 100. A judge may challenge category assignments. A deterministic-gate failure, materially fabricated provenance, score below 70, or hidden category mismatch vetoes a crown.

## Required independent output

Return self-contained Markdown with:

1. assigned perspective and scope;
2. severity-ordered findings with concrete file or source references;
3. rubric component scores totaling 100;
4. evidence actually inspected;
5. explicit evidence gaps and unsupported claims;
6. ship, block, or ship-with-conditions recommendation with prioritized actions;
7. the exact sentence `I did not inspect any other live-audit judge output.`

Do not edit files. Do not inspect `report/evidence/live-audit-judge-*.md`. Do not expose hidden chain-of-thought; provide concise auditable rationale only.
