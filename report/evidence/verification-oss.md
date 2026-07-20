# Verification-pass OSS-first snapshot

Completed UTC: `2026-07-20T22:17:14Z`

## Candidate and primary metadata freeze

The use-case-specific candidate set remains Codex Tribunal, promptfoo, Microsoft Agent Framework, DeepEval, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness. It spans the proposed thin review contract, adversarial eval/CI, production agent runtime, metrics/benchmarks, LM-program optimization, and observability. All eleven canonical GitHub REST repository endpoints were queried concurrently through the authenticated `gh` CLI. Every endpoint returned `archived=false` and `disabled=false`.

| Tool | Canonical repository | Stars | API SPDX | Last push |
|---|---|---:|---|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT | `2026-07-20T22:12:09Z` |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,446 | MIT | `2026-07-20T22:07:36Z` |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,252 | MIT | `2026-07-20T21:57:35Z` |
| DeepEval | https://github.com/confident-ai/deepeval | 16,982 | Apache-2.0 | `2026-07-20T18:36:22Z` |
| AutoGen | https://github.com/microsoft/autogen | 59,850 | CC-BY-4.0 | `2026-04-15T11:59:09Z` |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,918 | Apache-2.0 | `2026-02-24T07:47:19Z` |
| OpenAI Evals | https://github.com/openai/evals | 18,955 | NOASSERTION | `2026-04-14T15:29:57Z` |
| Langfuse | https://github.com/langfuse/langfuse | 31,512 | NOASSERTION | `2026-07-20T20:55:18Z` |
| DSPy | https://github.com/stanfordnlp/dspy | 36,261 | MIT | `2026-07-20T15:18:05Z` |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION | `2026-07-20T22:16:11Z` |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,341 | MIT | `2026-07-13T20:18:15Z` |

Stars are mutable adoption context and contribute exactly zero rubric points. Compared with the immediately preceding committed `22:08:10Z` snapshot, every star value was unchanged; only Codex Tribunal and Phoenix reported newer pushes. The structured snapshot and every CSV row therefore advanced to the single completed timestamp while retaining the evidence-based score components.

## Primary license and product-status controls

- Codex Tribunal's live root license begins `MIT License`.
- AutoGen's live root license is Creative Commons Attribution 4.0. Its current README is visibly marked `Maintenance Mode`, directs new users to Microsoft Agent Framework, limits contributions to fixes/security/docs, and describes community management.
- OpenAI Evals' live root license applies MIT to the software but explicitly excludes listed datasets and points to their individual licenses.
- Langfuse's live root license assigns `ee/`, `web/src/ee/`, and `worker/src/ee/` to a separate license and makes content outside those exclusions MIT Expat.
- Phoenix's live root license is Elastic License 2.0 and prohibits providing a hosted or managed service exposing a substantial feature set. It is source-available, not OSI open source.

These are repository observations, not legal advice.

## Stable 100-point rubric

The six bounded dimensions remain Type Fit `25`, Adversarial Depth `20`, Evidence `20`, Extensibility `15`, Repeatability `10`, and Integration `10`. Each row's integer components sum to its published total. The totals remain differentiated: `85, 78, 72, 68, 64, 61, 59, 58, 57, 56, 53`.

Codex Tribunal remains the one eligible crown at `85/100` for the declared narrow review-contract/persona/skill use case. This is a project-authored comparative fit rubric, not its runtime local-rules score, community validation, or a semantic benchmark. promptfoo remains stronger for mature red-team/eval CI; Microsoft Agent Framework for production multi-agent workflows and telemetry; DeepEval/Ragas/OpenAI Evals/lm-evaluation-harness for richer evaluation surfaces; Langfuse/Phoenix for observability; and DSPy for LM-program optimization. The OSS-first decision is therefore to keep Tribunal thin and compose those systems rather than reproduce them.
