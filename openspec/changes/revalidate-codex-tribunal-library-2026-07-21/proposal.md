## Why

The repository already contains the Codex Tribunal library and earlier publication evidence, but the brief requires live, mutable proof from NotebookLM, current OSS metadata, three independent adversarial judges, executable package behavior, and the public remote. A fresh fail-closed verification is therefore needed before claiming that the requested deliverable remains complete on 2026-07-21.

## What Changes

- Revalidate the canonical authenticated NotebookLM notebook with current primary OSS sources and multiple role-specific cross-queries.
- Attempt three fresh, mutually isolated Grok judgments for knowledge/correctness, harsh criticism/risks, and CLI UX/implementability; if Grok returns no model output, use the brief-authorized `agy` perspective fallback and retain exact provenance.
- Refresh the GitHub metadata snapshot and apply the stable 100-point feature rubric with exactly one crowned recommendation.
- Update `report/codex-trib-lib-tribunal.md` and pass-specific evidence so every live claim is traceable to this run.
- Exercise source, build, clean-install CLI, installed Python API, and expected-failure paths with a real comparison case.
- Gate, commit, push, and retrieve the exact SHA-pinned public report blob.

## Capabilities

### New Capabilities

- `live-brief-revalidation`: Defines the fresh IDR, independent Tribunal, reproducible scoring, executable E2E proof, and immutable publication requirements for this verification pass.

### Modified Capabilities

None.

## Impact

The change affects OpenSpec artifacts, `report/codex-trib-lib-tribunal.md`, the comparison matrix only if current primary evidence changes it, and new evidence ledgers under `report/evidence/`. Runtime code and tests change only if this pass reproduces a scoped defect. External systems in scope are authenticated NotebookLM, GitHub primary metadata, three brief-authorized Grok judge calls plus the explicitly allowed `agy` fallbacks when no Grok output is available, Python packaging, Git, and the public GitHub blob surface.
