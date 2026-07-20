# Authenticated NotebookLM IDR revalidation

Collection date: `2026-07-20`

IDR: ja

Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515

## Authenticated identity and sharing

The sanitized `nlm 0.8.9` checks observed:

- authentication valid under the configured default profile;
- canonical notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`;
- title: `Tribunal IDR 2026-07-04`;
- public-link access enabled;
- public link exactly matches the canonical URL above.

Account identifiers and credentials are intentionally not retained.

## Mutable source inventory

The direct baseline inventory before this pass attempted ingestion was:

- total: `640`
- status `2` (processed): `598`
- status `3` (failed): `42`

The canonical notebook is shared and changed while work ran. The closing direct inventory was:

- total: `669`
- status `2` (processed): `600`
- status `3` (failed): `69`
- uniquely titled fresh revalidation records: `24`, all status `3`
- selected processed query sources: `29/29`

The closing inventory, not generated prose, is authoritative for this timestamp. Because the notebook was concurrently mutable, the total delta is not assigned solely to this process.

## Source-ingestion attempts

The brief required current sources to be added. Three materially different paths were attempted and none produced a processed fresh source:

1. **Local files:** twelve `nlm source add --file ... --wait --json` calls covered Proposal, Design, Spec, Tasks, README, runtime, package metadata, tests, skill, Karpathy-inspired persona, matrix, and report. Markdown/CSV paths returned API `INVALID_ARGUMENT`; Python/TOML/JSON paths also reported unsupported file types.
2. **Text sources:** the same twelve contents were safely sent through `--text` with unique titles and starting-commit provenance. The CLI returned source IDs with exit `0`, but later inventory showed two records per title, all status `3`; direct `source get` returned empty content and `source_type: unknown`. They are not counted as processed.
3. **Public SHA-pinned URL:** the public GitHub blob was independently HTTP-reachable with status `200`, but NotebookLM rejected both raw and blob ingestion with `Could not add url source`.

No failed source was deleted, no failed record was treated as grounding, and no fourth ingestion variation was attempted after three distinct failures. The queries instead used 29 already processed primary, research-control, and same-day project snapshots.

## Selected query sources

| Class | Source ID | Title | URL/origin |
|---|---|---|---|
| primary-oss-or-ux | `4fd90dd9-426b-4d47-aaa3-c972c98f14fe` | 10 Usability Heuristics for User Interface Design - NN/G | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| primary-oss-or-ux | `25abb192-77ce-4e55-8529-a3ab5e131930` | GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub | https://github.com/Arize-ai/phoenix |
| primary-oss-or-ux | `b4d2fe1b-8174-42c7-8983-dc1510d84d44` | GitHub - EleutherAI/lm-evaluation-harness: A framework for few-shot evaluation of language models. · GitHub | https://github.com/EleutherAI/lm-evaluation-harness |
| primary-oss-or-ux | `f0cb48fe-9660-4200-8422-317343fd382b` | GitHub - confident-ai/deepeval: The LLM Evaluation Framework · GitHub | https://github.com/confident-ai/deepeval |
| primary-oss-or-ux | `1a88fad5-66a9-4d49-b7d6-39c6869eaa6b` | GitHub - langfuse/langfuse: 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 · GitHub | https://github.com/langfuse/langfuse |
| primary-oss-or-ux | `73fd8d4d-1865-4901-9b88-15fcf9eb9da0` | GitHub - microsoft/agent-framework: A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. · GitHub | https://github.com/microsoft/agent-framework |
| primary-oss-or-ux | `a7a42d60-b8af-4070-8c34-64631606592b` | GitHub - microsoft/autogen: A programming framework for agentic AI · GitHub | https://github.com/microsoft/autogen |
| primary-oss-or-ux | `a17d1fb1-6a62-437f-bb6b-e3d1e292e6d8` | GitHub - openai/evals: Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks. | https://github.com/openai/evals |
| primary-oss-or-ux | `c79ca1bc-c92e-4932-9bdf-b8ebb403e74b` | GitHub - promptfoo/promptfoo: Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple declarative configs with command line and CI/CD integration. Used by OpenAI and Anthropic. · GitHub | https://github.com/promptfoo/promptfoo |
| primary-oss-or-ux | `2e4919cf-0aa2-4e80-b6b1-ae24289173ab` | GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub | https://github.com/stanfordnlp/dspy |
| primary-oss-or-ux | `9e65e710-a488-4705-8822-10ac6d4aa220` | vibrantlabsai/ragas: Supercharge Your LLM Application Evaluations - GitHub | https://github.com/vibrantlabsai/ragas |
| project-snapshot | `6a038cfd-5a30-45ff-9648-6e9dac1e3d23` | Brief live closure design 2c27f51 2026-07-20 | local snapshot |
| project-snapshot | `be78b788-c0b9-4721-bdb8-45c84e67f649` | Brief live closure proposal 2c27f51 2026-07-20 | local snapshot |
| project-snapshot | `b2428a55-8113-47d1-8ef9-4a01759ce933` | Brief live closure spec 2c27f51 2026-07-20 | local snapshot |
| project-snapshot | `8c376f8a-2577-406c-bc6e-dc1452d17d9f` | Brief live closure tasks 2c27f51 2026-07-20 | local snapshot |
| project-snapshot | `98e1478b-127b-4f80-b8bc-6232a3669d50` | Brief live direct contradiction controls 2c27f51 2026-07-20 | local snapshot |
| project-snapshot | `72d0f205-5e93-4d14-958a-f0f14af674ec` | Tribunal Karpathy persona HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `9990d9b8-f7da-4cab-adb9-852f1edff3b4` | Tribunal README HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `4a053d0f-9bf1-46b5-9e9f-0eaa00a98d37` | Tribunal brief and acceptance protocol | local snapshot |
| project-snapshot | `4c3aaf91-eebb-4330-8101-34e02a13699c` | Tribunal matrix HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `4e994a0b-4717-44b9-8008-6eb82242f816` | Tribunal package HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `ceb5e5be-0f42-470d-a772-5f7af1062d1c` | Tribunal report HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `022aec98-d024-4c6d-af64-d81456e19873` | Tribunal runtime HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `8c3eb945-6d06-4587-806e-c12ef836d69a` | Tribunal skill HEAD 2c27f51 brief closure | local snapshot |
| project-snapshot | `bc34d15b-a9f8-4696-b6bd-f935c2eb63b7` | Tribunal tests HEAD 2c27f51 brief closure | local snapshot |
| research-control | `346a0ae4-85e9-43f1-9b46-3bae43d980b9` | A Survey on Agent-as-a-Judge - arXiv | https://arxiv.org/pdf/2601.05111 |
| research-control | `92a44e33-1f12-4454-a4c2-e5e97feb8f98` | A Systematic Study of Position Bias in LLM-as-a-Judge - ACL Anthology | https://aclanthology.org/2025.ijcnlp-long.18.pdf |
| research-control | `9e0d249b-225f-4fd8-ba28-77e26bd773a9` | Ask Don't Tell: Reducing Sycophancy in Large Language Models \| AISI Work | https://www.aisi.gov.uk/blog/ask-dont-tell-reducing-sycophancy-in-large-language-models-2 |
| research-control | `3962bfae-d4c9-4421-b681-b3073ac0c6e3` | Auditable Agents - arXiv | https://arxiv.org/pdf/2604.05485 |

These sources include all ten external OSS repositories, NN/g heuristics, four research/bias/audit controls, nine current-day project snapshots, four brief OpenSpec snapshots, and one direct executable contradiction-control snapshot. The project snapshots bind to earlier same-day commit `2c27f51`; they do not by themselves prove behavior at the starting commit `9f1dc36`, so current executable checks overrule discrepancies.

## Cross-queries and returned grounding metadata

All four commands used the same comma-separated list of 29 processed source IDs. NotebookLM returned the same conversation ID for all four; this pass therefore claims cross-topic querying, not conversation isolation.

| Query | Exit | Answer chars | sources_used | Citation mappings | References | Conversation |
|---|---:|---:|---:|---:|---:|---|
| knowledge | 0 | 11524 | 22 | 58 | 58 | `1ebabb83-484f-405b-8b24-a26cfa5b9afb` |
| critique | 0 | 11810 | 0 | 0 | 0 | `1ebabb83-484f-405b-8b24-a26cfa5b9afb` |
| ux | 0 | 10044 | 0 | 0 | 0 | `1ebabb83-484f-405b-8b24-a26cfa5b9afb` |
| control | 0 | 8464 | 0 | 0 | 0 | `1ebabb83-484f-405b-8b24-a26cfa5b9afb` |

### Knowledge/correctness

The formally grounded answer supports the thin structural contract, persona disclaimer, dependency-free package metadata, explicit local-backend limits, and OSS composition. It also imports historical provider results and study metrics from selected sources; these remain source descriptions, not current provider or local performance measurements.

### Harsh criticism/risk

The answer usefully stresses common-mode judges, self-declared backend scores/gaps, prompt injection and sycophancy, provider provenance, trace/budget durability, and license/identity risks. Because the returned formal source/citation arrays were empty, its filename-style bracket references are not accepted as independent grounding.

### UI/UX feasibility

The answer identifies CLI discoverability, bounded inputs, concise errors, serialization/provenance, synchronous-workflow friction, persona disclosure, and the need for external visual/accessibility/human-task testing. It also repeats the false claim that `LocalRulesBackend.evaluate` is missing. The selected executable contradiction source and current source/E2E runs directly refute that blocker.

### Contradiction/source-attribution control

The ten requested classifications returned, in order:

```text
CONTRADICTED
CONTRADICTED
CONTRADICTED
CONTRADICTED
CONTRADICTED
CONTRADICTED
CONTRADICTED
SUPPORTED
CONTRADICTED
CONTRADICTED
```

Thus only claim 8, that package metadata declares the console entry point and persona JSON, was supported. The control correctly rejected semantic local-rules, automatic provider independence, URL-equals-query, visual/accessibility proof, Karpathy authorship/endorsement, matrix-crown-equals-runtime-pass, durable quota, identical Markdown/JSON preservation, and snapshot-only clean-install proof. Its formal grounding arrays were nevertheless empty, so current code/build/E2E remains authoritative.

## Manual reconciliation rule

Primary APIs and executable observations outrank generated prose. Applied corrections:

- Current direct inventory is `669/600/69`, not a model-generated total.
- `LocalRulesBackend.evaluate` exists and current source/installed CLI calls execute it successfully.
- The NotebookLM URL validator proves shape only; this ledger proves the authenticated query separately.
- `local-rules` scores structure and cannot establish semantic truth, visual UX, provider diversity, or durable quota.
- `UI/UX ✅` in the external matrix means dedicated review-mode fit, not a rendered/accessibility pass.
- The Karpathy-inspired persona is synthetic, neither authored nor endorsed by Andrej Karpathy, and its disclaimer must survive every output surface.
- Mutable GitHub stars and historical study metrics are context, not local efficacy points.
- Clean wheel/console/API behavior is established only by [revalidation-e2e-2026-07-20.md](revalidation-e2e-2026-07-20.md).

## IDR conclusion

The selected evidence supports shipping Codex Tribunal as a bounded, auditable offline orchestration contract and reusable skill, with mature OSS composed for semantic evaluation, live agent runtime, and observability. It does not support claims of native semantic verification, visual accessibility testing, provider-family independence, durable quotas/traces, or production calibration. The failed fresh-source ingestion and three queries with empty formal grounding metadata remain explicit limitations rather than being repaired in prose.

