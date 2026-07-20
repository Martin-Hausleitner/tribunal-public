# OSS-first revalidation snapshot

Completed UTC: `2026-07-20T22:08:10Z`

## Candidate freeze

The live batch retained the eleven use-case-specific candidates already selected before scoring: Codex Tribunal, promptfoo, Microsoft Agent Framework, DeepEval, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness. Together they cover the thin local Tribunal contract, red-team/CI assertions, production multi-agent runtime, evaluation metrics and benchmark harnesses, LM-program optimization, and observability. No candidate was added merely to change the winner.

All eleven canonical repository endpoints returned successfully from the primary GitHub REST API through the authenticated `gh` CLI in one concurrent batch. Every repository reported `archived=false` and `disabled=false`. Stars are dated adoption context and contribute exactly zero rubric points.

## Live metadata

| Tool | Repository | Stars | API SPDX | Last push |
|---|---|---:|---|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT | `2026-07-20T22:00:11Z` |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,446 | MIT | `2026-07-20T22:07:36Z` |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,252 | MIT | `2026-07-20T21:57:35Z` |
| DeepEval | https://github.com/confident-ai/deepeval | 16,982 | Apache-2.0 | `2026-07-20T18:36:22Z` |
| AutoGen | https://github.com/microsoft/autogen | 59,850 | CC-BY-4.0 | `2026-04-15T11:59:09Z` |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,918 | Apache-2.0 | `2026-02-24T07:47:19Z` |
| OpenAI Evals | https://github.com/openai/evals | 18,955 | NOASSERTION | `2026-04-14T15:29:57Z` |
| Langfuse | https://github.com/langfuse/langfuse | 31,512 | NOASSERTION | `2026-07-20T20:55:18Z` |
| DSPy | https://github.com/stanfordnlp/dspy | 36,261 | MIT | `2026-07-20T15:18:05Z` |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION | `2026-07-20T21:23:56Z` |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,341 | MIT | `2026-07-13T20:18:15Z` |

Since the prior `21:07:01Z` snapshot, promptfoo gained 3 stars; Microsoft Agent Framework and DeepEval gained 1 each; Langfuse and DSPy gained 2 each. Codex Tribunal, promptfoo, Agent Framework, and Phoenix reported newer pushes. These mutable changes did not alter any rubric dimension.

## Primary license/status qualifications

Live root-license reads reconfirmed:

- AutoGen uses Creative Commons Attribution 4.0 at the repository root. Its current README prominently states maintenance mode, no new features/enhancements, community management, and recommends Microsoft Agent Framework for new projects.
- OpenAI Evals begins with MIT but explicitly excludes listed datasets and directs users to their individual licenses.
- Langfuse assigns `ee/`, `web/src/ee/`, and `worker/src/ee/` to a separate license; other content is MIT Expat.
- Phoenix uses Elastic License 2.0 and forbids providing a hosted or managed service exposing a substantial feature set. It is source-available, not OSI open source.

These are repository-level observations, not legal advice.

## 100-point audit

The published rubric remains:

- Type Fit: 25
- Adversarial Depth: 20
- Evidence: 20
- Extensibility: 15
- Repeatability: 10
- Integration: 10

The current differentiated totals are `85, 78, 72, 68, 64, 61, 59, 58, 57, 56, 53`. A mechanical audit confirmed every component is an integer within its cap, each six-component sum equals the row total, all totals are distinct, all rows share the new snapshot timestamp, and exactly one row contains `👑`.

Codex Tribunal remains the narrow use-case winner at `85/100`; this is an external fit assessment, not the `local-rules` runtime score and not semantic or visual proof. `UI/UX ✅` means the project has a dedicated review mode, personas, skill routing, and evidence-gap contract; it does not assert that a browser or accessibility check passed. The build-versus-compose conclusion is unchanged: keep the Tribunal core thin; use promptfoo for mature red-team/CI assertions, Microsoft Agent Framework for durable production workflows, evaluation frameworks for semantic metrics, and Langfuse/Phoenix for trace/observability needs subject to their licenses.

## Gate observations

```text
csv-gate PASS: 11 rows, one crown=Codex Tribunal, score spread=53-85, snapshot=2026-07-20T22:08:10Z
rubric-audit PASS [85, 78, 72, 68, 64, 61, 59, 58, 57, 56, 53] 2026-07-20T22:08:10Z
python -m json.tool report/evidence/github-snapshot.json: exit 0
```

