# NotebookLM live-audit evidence

## Canonical notebook verification

- Verified UTC: `2026-07-20T17:56:31Z`
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Public link: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Sharing state: public link enabled
- Source count before this audit: `330`
- Source count after live-audit additions: `336`

Notebook identity, source count, sharing state, and URL were read from the authenticated NotebookLM CLI. Private collaborator/account details are deliberately omitted.

## Corpus audit and additions

All twelve required targeted sources were present before the new additions: promptfoo, DeepEval, DSPy, Langfuse, Phoenix, AutoGen, Ragas, OpenAI Evals, lm-evaluation-harness, the multi-agent-debate paper, NN/g usability heuristics, and W3C WCAG 2.2. The corpus also retained processed local README, skill, runtime, proposal, design, and capability-spec sources from the earlier release run.

This audit added and waited for successful processing of six current local artifacts:

1. `report/codex-trib-lib-tribunal.md`
2. live-audit OpenSpec `proposal.md`
3. live-audit OpenSpec `design.md`
4. live-audit capability `spec.md`
5. live-audit OpenSpec `tasks.md`
6. `report/evidence/live-audit-baseline.md`

After processing, `331` sources had status `2` (processed) and five had status `3` (failed). Every newly added source and every required targeted source was processed. The five failures were duplicated or secondary Medium articles, including two duplicate AutoGen-commentary entries; they are excluded from decision evidence and do not create a primary-source gap.

## Live cross-queries

The following sections are populated only from new NotebookLM calls made after the six current sources were processed. Returned source/citation metadata and any overclaims are audited explicitly.
