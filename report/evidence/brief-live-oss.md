# Brief live OSS-first snapshot and rubric check

Completed UTC: `2026-07-20T20:51:06Z`

## Candidate freeze

The candidate set was frozen before the live batch from the existing use-case-specific matrix: Codex Tribunal, promptfoo, Microsoft Agent Framework, DeepEval, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness. These cover the declared thin Tribunal, adversarial CI, production agent runtime, evaluation metrics/benchmarks, LM-program optimization, and observability categories. Adding near-duplicates would not change the build-versus-compose decision.

All eleven canonical repository endpoints were queried from the primary GitHub REST API through the authenticated `gh` CLI in one concurrent batch. The completion timestamp was taken only after all calls returned. Every repository reported `archived=false` and `disabled=false`.

## Live metadata

| Tool | Canonical repository | Stars | API license | Last push |
|---|---|---:|---|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT | `2026-07-20T20:36:06Z` |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,442 | MIT | `2026-07-20T18:15:45Z` |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,250 | MIT | `2026-07-20T20:34:52Z` |
| DeepEval | https://github.com/confident-ai/deepeval | 16,981 | Apache-2.0 | `2026-07-20T18:36:22Z` |
| AutoGen | https://github.com/microsoft/autogen | 59,850 | CC-BY-4.0 | `2026-04-15T11:59:09Z` |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,918 | Apache-2.0 | `2026-02-24T07:47:19Z` |
| OpenAI Evals | https://github.com/openai/evals | 18,955 | NOASSERTION | `2026-04-14T15:29:57Z` |
| Langfuse | https://github.com/langfuse/langfuse | 31,509 | NOASSERTION | `2026-07-20T17:16:51Z` |
| DSPy | https://github.com/stanfordnlp/dspy | 36,258 | MIT | `2026-07-20T15:18:05Z` |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION | `2026-07-20T20:43:47Z` |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,341 | MIT | `2026-07-13T20:18:15Z` |

Compared with the preceding snapshot, only mutable adoption/activity facts changed: Agent Framework `+2` stars and a newer push, DeepEval `+2`, AutoGen `+1`, Langfuse `+1`, DSPy `+2`, Codex Tribunal and Phoenix had newer pushes. Stars remain context and contribute exactly zero rubric points.

## Primary license and status qualifications

- Codex Tribunal's primary license file begins `MIT License`.
- AutoGen's current README says `Maintenance Mode`, no new features/enhancements, community management, and directs new users to Microsoft Agent Framework. Its root license is Creative Commons Attribution 4.0; component-level use needs separate review.
- OpenAI Evals' root file starts with MIT but explicitly excludes listed datasets and directs users to the source datasets' individual licenses.
- Langfuse's root license assigns `ee/`, `web/src/ee/`, and `worker/src/ee/` to a separate license; content outside those directories is MIT Expat.
- Phoenix's root license is Elastic License 2.0 and prohibits providing a hosted/managed service that exposes a substantial feature set. It is source-available, not OSI open source.

These are repository-level observations, not legal advice.

## 100-point rubric and crown

The documented rubric was recalculated from the six integer dimensions in the authoritative CSV: Type Fit `25`, Adversarial Depth `20`, Evidence `20`, Extensibility `15`, Repeatability `10`, and Integration `10`. Every row's component sum equals its total. The unchanged, differentiated totals are `85, 78, 72, 68, 64, 61, 59, 58, 57, 56, 53`.

Codex Tribunal remains the one eligible crown at `85/100` for the declared narrow use case, not as the universally best tool. Its local-runtime `40/50` structural readiness score is a separate instrument. promptfoo remains better for mature red-team/CI assertions; Microsoft Agent Framework for durable production agent workflows; DeepEval/Ragas/OpenAI Evals/lm-evaluation-harness for richer evaluation and benchmark surfaces; Langfuse/Phoenix for observability; DSPy for LM-program optimization.

`python scripts/csv_gate.py report/codex-trib-lib-matrix.csv` exited `0`:

```text
csv-gate PASS: 11 rows, one crown=Codex Tribunal, score spread=53-85, snapshot=2026-07-20T20:51:06Z
```

`python -m json.tool report/evidence/github-snapshot.json` also exited `0`. The JSON snapshot and CSV share the completion timestamp and current star values. Report-table synchronization is completed during synthesis and enforced by the report gate.
