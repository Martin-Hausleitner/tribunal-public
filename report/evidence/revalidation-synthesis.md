# Revalidation synthesis and finding disposition

Collection date: `2026-07-20`

## Evidence classes

- NotebookLM: research synthesis with explicit grounding metadata and ingestion limits.
- GitHub: current primary repository, license, activity, archive, and star metadata.
- External judges: adversarial opinions from isolated role sessions.
- Executable proof: source CLI, malformed input, unit/compile/gates, clean PEP 517 build, exact-wheel install, console, and Python API.

Executable and primary evidence control any contradiction.

## Accepted tribunal

| Role | Engine | Score | Recommendation |
|---|---|---:|---|
| Knowledge/correctness | Gemini 3.1 Pro (High) | 95/100 | SHIP WITH CONDITIONS |
| Harsh criticism/risk | Gemini 3.5 Flash (High) | 70/100 | SHIP WITH CONDITIONS |
| UI/UX/implementability | Gemini 3.5 Flash (Medium) | 94/100 | SHIP WITH CONDITIONS |

All accepted sessions were fresh and conclusion-free but share the Gemini family. No family independence is claimed.

## Finding disposition

- **Structural versus semantic boundary:** accepted. `local-rules` stays explicitly structural and warning-marked.
- **Matrix self-assessment / UI semantics:** accepted as a disclosure risk. The one crown is a use-case fit result; `UI/UX ✅` is mode/persona/gap-contract fit, not visual success.
- **Backend trust and family diversity:** accepted. Custom backend scores/gaps and provider provenance require trusted external policy.
- **Sequential live-backend latency:** accepted production risk; no speculative concurrency layer was added to the dependency-free core.
- **Single-person panel exit 2:** rejected as a defect. A Tribunal requires three unique personas and the error is concise, expected, and tested.
- **Orchestrator metadata in evidence:** rejected as accidental pollution. It is intentional engine/routing/hardness provenance appended separately from backend result evidence.
- **Missing `LocalRulesBackend.evaluate`:** rejected. Source, tests, source CLI, installed console, and installed API all execute it.
- **Setuptools license deprecation:** reproduced and fixed with `setuptools>=77`, SPDX `MIT`, explicit license file, and removal of the deprecated classifier. Clean rebuild has no deprecation.
- **Top-level `personas` namespace:** accepted remaining packaging risk; renaming requires a planned breaking migration.
- **Markdown whitespace flattening:** accepted intentional documented behavior; JSON remains lossless.
- **Dynamic persona help and bundled live adapters:** optional improvements, not current contract failures.
- **Visual/accessibility proof:** unresolved by design and must remain external.

## Final verdict

Ship Codex Tribunal for the bounded offline orchestration and reusable-skill scope. Keep the core thin; compose promptfoo for mature red-team/CI checks, Microsoft Agent Framework for production workflows, and a vetted observability platform for durable traces. Inject semantic backends only behind trusted provider, budget, provenance, calibration, and evidence controls.

The unchanged `85/100` matrix crown is narrowly eligible after all deterministic gates; it is neither a runtime semantic result nor an independent benchmark. Publication still depends on final tests, current report/evidence gates, completed OpenSpec tasks, exact staging, push, remote-SHA equality, and retrieval of the immutable report blob.

