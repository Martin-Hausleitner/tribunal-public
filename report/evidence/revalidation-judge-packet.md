# Conclusion-free judge packet: live brief revalidation

Collection date: `2026-07-20`

Starting public commit: `9f1dc36899a530ad4477784b3d12e1fd5c302da1`

Review scope: `/home/coder/tribunal-public` only. Treat the new uncommitted change under `openspec/changes/revalidate-trib-codex-trib-lib-brief/` as planning context. Do not use or modify any other repository, do not edit files, and do not inspect sibling verdicts.

## Requested product contract

Codex Tribunal presents itself as a small, dependency-free Python OSS library and reusable skill for hard-critical reviews through three primary modes:

- `knowledge`: facts, primary evidence, citations, and explicit gaps;
- `critique`: hostile risk/design review and fake-green resistance;
- `ui_ux`: workflow, interaction, visual/accessibility evidence boundaries;
- plus `comparison` for OSS matrices with exactly one evidence-eligible crown.

It exposes a source CLI, a `tribunal` console entry point, a Python API, a `JudgeBackend` seam, deterministic local rules, JSON/Markdown serialization, nine persona JSON files, and a synthetic Karpathy-inspired critic. The real person did not author or endorse that persona, and no output may be attributed to him.

## Observed inputs, not conclusions

- Git began on `master` at the full starting commit above; `origin` is the public GitHub repository.
- Public project files to inspect directly: `tribunal.py`, `README.md`, `pyproject.toml`, `tests/test_tribunal.py`, `skill/SKILL.md`, `personas/*.json`, `report/codex-trib-lib-matrix.csv`, and `report/codex-trib-lib-tribunal.md`.
- Existing tests/gates and historical evidence are present, but this judge must distinguish historical claims from direct current file inspection.
- The authenticated canonical NotebookLM notebook ID is `80cffd38-0185-4f4d-ae00-bbc67c4bc515`; its public link is `https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515`.
- Before this pass attempted ingestion, direct inventory returned `640` sources: status `2` = `598`, status `3` = `42`. Twelve local-file uploads failed; twelve text submissions were initially accepted but later appeared empty/failed, with duplicate failures; one SHA-pinned public URL was HTTP-reachable but NotebookLM rejected ingestion. None is claimed as processed grounding.
- Four selected-source NotebookLM queries completed. Knowledge returned 22 source IDs and 58 citation mappings. Critique, UX, and contradiction control returned complete prose but zero formal source/citation metadata; their prose is not independent proof. The UX prose repeated an alleged missing `LocalRulesBackend.evaluate` blocker that the selected executable-control source contradicted; current execution must decide.
- Existing report and README explicitly bound `local-rules` to structural setup, not target semantics, visual inspection, provider independence, live NotebookLM retrieval, or durable billing/tracing.
- Existing matrix scores and stars are inputs awaiting a fresh primary GitHub refresh in this pass. Stars receive zero rubric points.
- No clean-install or current test result is asserted in this packet; those gates run after the judges and can close or reproduce judge concerns.

## Required independent output contract

Return all fields below and cite exact in-scope files, line numbers where useful, and commands actually run:

1. Role and engine/model identity.
2. Score from 0 to 100 for the assigned perspective.
3. Recommendation: `SHIP`, `SHIP WITH CONDITIONS`, or `DO NOT SHIP`.
4. Direct findings, ordered by severity.
5. Evidence supporting each finding.
6. Reproduced source/runtime defects, explicitly separated from production risks, historical facts, and optional improvements.
7. Unresolved evidence gaps.
8. Independence limits: fresh session/process, packet isolation, provider/model family, and anything not proven.

Do not infer a sibling verdict, average, final crown, or report conclusion. Do not present a failed provider call as model output.
