## Why

The repository contains an unverified draft of an OSS Tribunal library, persona collection, and reusable skill, but it has no specification, release history, live research ledger, independent model verdicts, or published comparison report. Completing it now turns the draft into an auditable artifact whose claims can be rerun and whose recommendation is grounded in a real NotebookLM corpus and adversarial review.

## What Changes

- Define and verify a dependency-free Python API and CLI for three primary tribunal types: knowledge/correctness, hard critique/risk, and UI/UX feasibility.
- Require three genuinely independent judge results per round, explicit hardness/Nx behavior, evidence gaps, a post-judgment synthesis, and honest engine provenance.
- Package a reusable persona library including a clearly labeled Andrej Karpathy-inspired technical critic, plus a Codex-compatible Tribunal skill that routes work by tribunal type.
- Run live NotebookLM deep research in one canonical notebook, ingest primary and relevant OSS sources, and preserve cross-query findings and the real notebook link.
- Attempt three isolated Grok 4.5 high-effort tribunal perspectives for knowledge, hard criticism, and UX/implementation, use the brief-allowed isolated `agy` fallback if Grok is unavailable, then synthesize them without hiding disagreements.
- Deliver a sourced OSS feature matrix with bare GitHub links, snapshot star counts, a differentiated 100-point rubric, exactly one crowned recommendation, and a Mermaid implementation flow.
- Add executable behavioral tests and report gates, document repeatable usage, publish all artifacts to GitHub, and report a verified blob URL.

## Capabilities

### New Capabilities

- `tribunal-verdict-engine`: Public Python and CLI contracts for three tribunal types, three independent judges per round, Nx/hardness pressure, evidence-aware verdicts, and quota/provenance-aware engine planning.
- `tribunal-personas-and-skill`: Validated JSON persona discovery and routing, including a Karpathy-inspired implementation-first critic, together with an installable Tribunal `SKILL.md` workflow.
- `live-idr-comparison-report`: Canonical NotebookLM research, three independent external tribunal verdicts, sourced OSS comparison scoring, one crown, repeatable matrix gates, and a publication-ready Markdown report.

### Modified Capabilities

None. This repository has no existing OpenSpec capability specifications.

## Impact

- Affects `tribunal.py`, the CLI and Python API, `personas/*.json`, `skill/SKILL.md`, examples, tests, validation scripts, README, and new `report/` evidence artifacts.
- Adds OpenSpec planning artifacts but keeps the runtime library dependency-free.
- Uses live external systems explicitly required by the brief: NotebookLM, Grok, GitHub metadata/API, and a GitHub remote for publication.
- Publication creates or updates a public GitHub repository and exposes the report and source artifacts under the MIT license.
