# Final live OSS-first primary snapshot, 2026-07-21

Snapshot completed UTC: `2026-07-21T00:53:15Z`

All eleven canonical GitHub REST repository endpoints were queried concurrently with the authenticated `gh` CLI. Every response returned its expected canonical repository identity, `archived=false`, and `disabled=false`. Stars are mutable adoption context and contribute exactly zero rubric points.

| Tool | Canonical repository | Stars | API SPDX | Last push |
|---|---|---:|---|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT | `2026-07-21T00:48:07Z` |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,446 | MIT | `2026-07-21T00:52:26Z` |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,254 | MIT | `2026-07-20T22:33:44Z` |
| DeepEval | https://github.com/confident-ai/deepeval | 16,984 | Apache-2.0 | `2026-07-20T18:36:22Z` |
| AutoGen | https://github.com/microsoft/autogen | 59,851 | CC-BY-4.0 | `2026-04-15T11:59:09Z` |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,919 | Apache-2.0 | `2026-02-24T07:47:19Z` |
| OpenAI Evals | https://github.com/openai/evals | 18,957 | NOASSERTION | `2026-04-14T15:29:57Z` |
| Langfuse | https://github.com/langfuse/langfuse | 31,516 | NOASSERTION | `2026-07-20T22:57:59Z` |
| DSPy | https://github.com/stanfordnlp/dspy | 36,262 | MIT | `2026-07-20T15:18:05Z` |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION | `2026-07-21T00:18:32Z` |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,342 | MIT | `2026-07-13T20:18:15Z` |

Relative to the prior `2026-07-21T00:12:42Z` snapshot, DeepEval and OpenAI Evals each gained one star. Mutable push times advanced for Codex Tribunal, promptfoo, and Phoenix. No repository changed archived/disabled state or API SPDX classification.

## Root-file controls

- AutoGen's current root README states that the project is in maintenance mode, will receive no new features or enhancements, is community managed, and recommends Microsoft Agent Framework for new projects. The repository remains unarchived, so maintenance mode is a documented product state rather than the GitHub archive flag.
- OpenAI Evals' root README states that custom code submissions are currently not accepted while model-graded YAML submissions remain accepted. Its `LICENSE.md` is MIT for repository code and explicitly lists separately licensed datasets, including some non-commercial data.
- Langfuse's root `LICENSE` assigns separate terms to `ee/`, `web/src/ee/`, and `worker/src/ee/`, with MIT Expat terms outside those directories.
- Phoenix's root `LICENSE` is Elastic License 2.0 and prohibits offering a substantial feature set as a hosted or managed service. The matrix therefore calls it source-available rather than OSI open source.

These are primary repository observations, not legal advice.

## Stable 100-point rubric

| Dimension | Weight | Fit question |
|---|---:|---|
| Type Fit | 25 | How directly does the project cover knowledge, critique, and UI/UX review? |
| Adversarial Depth | 20 | Does it provide specialized, isolated, bias-aware adversarial evaluation rather than generic role labels? |
| Evidence | 20 | Are provenance, executable proof, citations, and unresolved gaps explicit and repeatable? |
| Extensibility | 15 | Are personas, skills, backends, metrics, or provider routes validated and reusable? |
| Repeatability | 10 | Are schemas, commands, datasets, and gates stable enough to rerun? |
| Integration | 10 | Can an operator adopt the relevant surface without rebuilding the surrounding stack? |

The rubric totals `100`. Stars contribute `0`. Current metadata and root controls did not invalidate any feature assessment, so the existing component values remain unchanged. The CSV arithmetic remains differentiated and bounded at `0..100`, with exactly one crown.

## Bounded selection

Codex Tribunal remains the project-authored `85/100` crown only for the declared narrow requirement: a small dependency-free three-type review contract, reusable skill, explicit persona library, stable output schemas, and evidence-gap discipline. It is not the best red-team system, semantic metric framework, production orchestrator, benchmark runner, or observability platform.

The OSS-first recommendation is composition, not replacement by a giant stack:

- add promptfoo when adversarial CI/red-team coverage is required;
- add Microsoft Agent Framework when production multi-agent workflows, checkpointing, human control, or provider routing are required;
- add DeepEval or Ragas for semantic application/RAG metrics;
- add Langfuse or Phoenix for traces and datasets after reviewing their license/product constraints;
- add OpenAI Evals or lm-evaluation-harness for benchmark execution;
- add DSPy for program/prompt optimization.

Only the missing adjacent capability should be added. Composing all alternatives at once would contradict the smallest-correct-change and OSS-first principles.
