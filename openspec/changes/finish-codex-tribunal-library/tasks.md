## 1. Core Verdict Contracts

- [x] 1.1 Add strict NotebookLM, quota, persona-document, requested-persona, and backend-result validation to `tribunal.py`.
- [x] 1.2 Add explicit judge request/backend contracts and record backend, engine, and persona-slug provenance in every view.
- [x] 1.3 Replace speculative provider defaults with the honest `local-rules` default and explicit-capacity allocation.
- [x] 1.4 Make three unique persona evaluations per round produce persona-specific findings and defer synthesis until all views exist.
- [x] 1.5 Preserve stable JSON and Markdown output with final numeric score and all new provenance fields.
- [x] 1.6 Make per-run capacity reusable, bound rounds/targets, escape Markdown targets, and render clean CLI input failures.

## 2. Personas, Skill, and Documentation

- [x] 2.1 Update the Karpathy-inspired persona and README with public references and an explicit no-authorship/no-endorsement disclaimer.
- [x] 2.2 Update `skill/SKILL.md` for independent judging, live evidence provenance, safe direct criticism, and exact anti-fake contracts.
- [x] 2.3 Update examples and README CLI/API documentation to match the implemented offline and injected-backend behavior.
- [x] 2.4 Preserve persona disclaimers, require real GitHub URLs, and add standard Python package metadata with bundled persona data.

## 3. Executable Gates

- [x] 3.1 Add standard-library unit tests for modes, Nx/hardness, independence, routing, validation, allocation, and serialization.
- [x] 3.2 Strengthen the CSV gate for score bounds, rank uniqueness/order, required capability markers, snapshot metadata, and one crown.
- [x] 3.3 Add skill and final-report validation scripts with mandatory-section and invariant checks.
- [x] 3.4 Run targeted tests, compilation, all three core CLI modes, and negative gate cases; fix every introduced failure.

## 4. Live NotebookLM IDR

- [x] 4.1 Create or identify one canonical NotebookLM notebook and record its verified identity and link.
- [x] 4.2 Add and process primary/project sources for tribunal orchestration, evaluations, observability, evidence, and UX alternatives.
- [x] 4.3 Run independent cross-source queries for correctness, risks, UX/implementation, differentiation, and scoring; preserve a source/query ledger.

## 5. Independent External Tribunal

- [x] 5.1 Build one evidence packet from the repository state, OpenSpec, NotebookLM ledger, and competitor metadata without pre-synthesized conclusions.
- [x] 5.2 Attempt the required Grok 4.5 knowledge/correctness path, then run the brief-allowed isolated `agy` fallback and save its complete verdict.
- [x] 5.3 Attempt the required Grok 4.5 harsh-critique/risk path, then run the brief-allowed isolated `agy` fallback and save its complete verdict.
- [x] 5.4 Attempt the required Grok 4.5 UX/implementability path, then run the brief-allowed isolated `agy` fallback and save its complete verdict.

## 6. Synthesis and Report

- [x] 6.1 Query GitHub for a timestamped star/license snapshot of at least six relevant OSS alternatives.
- [x] 6.2 Apply the declared 100-point rubric, produce the gated CSV matrix, and award exactly one use-case-bounded crown.
- [x] 6.3 Write `report/codex-trib-lib-tribunal.md` with IDR, three verdicts, debate, matrix, recommendation, Mermaid flow, plan, limits, and reproduction steps.
- [x] 6.4 Run the report, CSV, skill, OpenSpec, test, compilation, and live CLI gates against the final artifacts.

## 7. Public Delivery

- [x] 7.1 Add ignore/release hygiene, inspect the complete tracked diff for secrets and unrelated changes, and reconcile every OpenSpec task.
- [x] 7.2 Commit the complete release, create or configure the public GitHub remote, and push the branch.
- [x] 7.3 Verify the pushed commit and report blob over GitHub and record the successful blob URL for handoff.
