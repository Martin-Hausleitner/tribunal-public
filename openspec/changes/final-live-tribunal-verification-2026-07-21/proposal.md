## Why

The repository contains a published Codex Tribunal library and prior verification evidence, but the brief requires live, mutable proof from NotebookLM, current OSS metadata, three independent adversarial judges, executable package behavior, and the public remote. A final fail-closed pass is needed so completion is based on evidence observed in this run rather than inherited claims.

## What Changes

- Reverify the authenticated canonical NotebookLM notebook, its public link, processed source set, and multiple role-specific cross-queries.
- Refresh primary GitHub metadata for the OSS-first comparison and reapply the published 100-point rubric with numeric stars and exactly one crown.
- Run three fresh isolated Grok 4.5 High judgments for knowledge/correctness, harsh criticism/risks, and UX/implementability; use only the brief-authorized `agy` perspective fallback if Grok produces no model verdict, while retaining exact provenance.
- Reconcile the three judgments into a traceable synthesis, recommendation, feature matrix, Mermaid decision flow, and implementation plan in `report/codex-trib-lib-tribunal.md`.
- Exercise source, build, clean-install CLI, installed API, expected-error, skill, matrix, and report surfaces with a concrete E2E comparison case.
- Commit, push, and retrieve the exact SHA-pinned public report blob before reporting completion.

## Capabilities

### New Capabilities

- `final-live-brief-verification`: Defines the live IDR, independent Tribunal, OSS scoring, real E2E proof, and immutable publication requirements for this final verification pass.

### Modified Capabilities

None.

## Impact

The change affects OpenSpec artifacts, current-pass evidence under `report/evidence/`, `report/codex-trib-lib-tribunal.md`, and the comparison matrix if primary metadata or scoring changes. Runtime code, personas, skill files, and tests change only if fresh execution reproduces a scoped defect. External systems in scope are authenticated NotebookLM, GitHub primary endpoints, three brief-authorized Grok judge calls and the explicitly allowed `agy` fallback, Python packaging, Git, and the public GitHub blob surface.
