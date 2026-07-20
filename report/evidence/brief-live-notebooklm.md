# Brief live NotebookLM IDR

IDR: ja

- Recorded UTC: `2026-07-20T20:49:06Z`
- Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Authenticated CLI: `nlm 0.8.9`
- Public sharing: enabled; the returned public link exactly matched the canonical URL
- Conversation ID returned by all four calls: `1ebabb83-484f-405b-8b24-a26cfa5b9afb`

The exact notebook ID resolved through the authenticated CLI. Account and collaborator identity were deliberately excluded; only `is_public=true`, `access_level=public`, the public link, and collaborator count were observed.

## Corpus and source control

The canonical notebook is shared and was mutable during collection. An early notebook-detail call reported `541` sources while other in-scope work was still adding material. This pass added thirteen uniquely titled, processed sources:

- four pre-research OpenSpec artifacts: proposal, design, capability spec, and task checklist;
- eight current project snapshots from starting HEAD `2c27f51`: README, public report, skill, runtime, package metadata, tests, Karpathy-inspired persona, and CSV matrix;
- one direct contradiction-control source containing the observed compile, import, symbol-use, and wheel-listing results.

The authoritative final `nlm source list ... --json` inventory after those additions was `560` total, `549` processed (`status=2`), `11` failed (`status=3`), and no source in another state. All thirteen sources added by this pass were processed. The eleven failures were inherited duplicate/secondary Medium or Scribd pages and were not selected for any query. The selected source set also contained processed canonical roots for promptfoo, DeepEval, DSPy, Langfuse, Phoenix, AutoGen, Microsoft Agent Framework, Ragas, OpenAI Evals, and lm-evaluation-harness, plus primary usability and multi-judge research.

The changing early counts are retained rather than normalized away. Direct final CLI JSON, the thirteen exact source IDs, primary repository metadata, and executable project behavior outrank generated source-count prose.

## Cross-query 1: knowledge and correctness

**Question:** Audit HEAD `2c27f51` using only the selected current project snapshots and primary OSS/research sources; separate structural guarantees from semantic correctness, NotebookLM retrieval, visual UX, provider-family independence, and production observability; compare capabilities rather than popularity; return supported, contradicted, unresolved, and minimum-ship conclusions without historical scores, stale counts, unrelated repositories, or study metrics as local facts.

**Returned grounding:** `12` source IDs and `49` citation mappings.

**Retained result:** The dependency-free core has three primary modes plus comparison, separate backend calls, validated personas with a serialized synthetic-persona disclaimer, bounded structural scoring, strict positive-marker conditions, syntax-only NotebookLM provenance, PEP 517 packaging, and explicit non-capabilities. The honest recommendation is to ship the thin structural orchestration/skill boundary and compose mature OSS for semantic evaluation, adversarial CI, durable workflows, and observability.

**Manual exclusions:** The answer incorrectly said target text was not escaped, reused historical Grok/fallback facts, repeated mutable stars from the prior report, and imported study correlation/attack metrics despite the prompt. It also treated report statements as current external observations. None is current proof.

## Cross-query 2: hostile criticism and risk

**Question:** Try to falsify the bounded ship claim; separate reproducible current defects from explicit non-goals and future live-backend risks; inspect rendering, packaging, persona identity, scoring, provenance, injection, quota semantics, license caveats, and recovery; rank only source-attributed current findings and do not reuse historical provider, star, corpus, or literature values as local facts.

**Returned grounding:** `10` source IDs and `28` citation mappings.

**Retained result:** Common-mode judge errors, style sensitivity, retrieval/prompt injection, provider/model provenance, trusted durable budgets, and trace recovery are real risks for a future live deployment. NotebookLM URL presence remains provenance rather than retrieval proof. Phoenix's ELv2 and Langfuse's enterprise-directory exception require deployment-specific license review. These do not falsify the declared local structural scope.

**Manual exclusions:** The answer invented four current defects from normalized/truncated source excerpts: a Python syntax error, missing `personas/__init__.py`/wheel data, a missing `LocalRulesBackend.evaluate`, and dead `validate_github_repo_url`. It also prescribed Pydantic, empty evidence gaps, cross-family routing, and literature statistics as mandatory core fixes. Direct controls contradicted all four alleged code defects.

## Cross-query 3: CLI and UI/UX feasibility

**Question:** Audit the observable CLI/API, modes, hardness, help/error behavior, serializations, skill, persona disclosure, install path, and evidence workflow; separate terminal proof from browser, viewport, keyboard, assistive-tech, contrast, and human-study claims; identify friction and build-versus-compose boundaries without stale verdicts, provider attempts, stars, counts, or study metrics as local facts.

**Returned grounding:** `10` source IDs and `37` citation mappings.

**Retained result:** The CLI exposes bounded modes/rounds/target length, concise expected errors, conventional help, deterministic output, and an installable entry point. It cannot prove visual polish, responsive layout, WCAG behavior, assistive-technology behavior, cognitive load, or task success. Progress indication and reusable configuration could improve a future live-provider CLI, while promptfoo, Microsoft Agent Framework, Langfuse, or Phoenix cover larger adjacent surfaces.

**Manual exclusions:** The response again invented the same three blocking runtime/package failures, claimed a Pydantic v2 core, treated historical Grok/Gemini evidence as current, and promoted optional progress/dotfile/provider ideas into current release requirements. Those claims were rejected.

## Cross-query 4: contradiction and source attribution

**Question:** Resolve the three answers claim by claim against exact source and direct executable controls: compilation, `personas/__init__.py` and wheel data, `LocalRulesBackend.evaluate`, `validate_github_repo_url` use, dataclasses versus Pydantic, target escaping, per-run capacity disclosure, optional UX ideas, historical provider facts, mutable stars/literature metrics, and the direct `560/549/11` inventory.

**Returned grounding:** `8` source IDs and `31` citation mappings.

**Confirmed corrections:** The control correctly rejected the alleged syntax failure, missing persona package data, missing backend method, dead validator, Pydantic dependency, raw-target claim, durable-capacity claim, mandatory progress/dotfile/cross-provider claim, historical-provider-as-current claim, and star/literature-as-local-measurement claim. It retained the bounded structural score, strict marker gate, syntax-only notebook reference, separate initial calls, dependency-free packaging, and synthetic Karpathy-persona disclosure.

**Residual control error:** Even after being given `560 total / 549 processed / 11 failed`, the answer labeled those values contradicted and then called `549` the total. This is false. The direct final `source list` JSON is authoritative. The control also cannot turn an exact-source citation into executable proof by itself; the cited compile/import/wheel observations remain the proof.

## Direct controls that outrank generated prose

- `python -m py_compile tribunal.py personas/__init__.py` exited `0`.
- Importing the runtime reported `callable(LocalRulesBackend().evaluate) == True` and loaded `9` personas.
- Exact search found `_markdown_text` at line 22 and target escaping at line 156.
- `LocalRulesBackend.evaluate` exists at line 495.
- `validate_github_repo_url` is called at line 333 and defined at line 455.
- The wheel listing contains `personas/__init__.py` and all nine persona JSON files.
- The final direct notebook inventory is `560/549/11`, not `549` total.

## IDR conclusion

The live IDR supports the existing bounded recommendation and demonstrates why anti-fake controls are mandatory. Codex Tribunal is fit as a small offline orchestration contract, installable CLI/API, persona library, and reusable hard-criticism skill once the current executable gates pass. It is not a semantic verifier, live NotebookLM client, visual UX tester, statistically independent jury, durable quota authority, or trace platform. Existing OSS should supply adversarial CI, production agent runtime, evaluation metrics, and observability rather than being rebuilt inside the thin core.

NotebookLM was useful for cross-source discovery but repeatedly transformed normalized source excerpts into confident fake blockers, ignored explicit freshness constraints, and even failed a prompted arithmetic/source-count control. Therefore no generated claim is accepted without primary metadata or executable confirmation.
