# Brief live verdict: knowledge and correctness

Engine: authorized `agy` fallback, Gemini 3.1 Pro (High)  
Session: fresh plan/read-only sandbox  
Score: `98/100`  
Recommendation: **Ship with conditions**

## 1. Assigned perspective and inspected scope

Knowledge/correctness audit of `brief-live-judge-packet.md`, `brief-live-baseline.md`, `brief-live-notebooklm.md`, `brief-live-oss.md`, and `tribunal.py`.

## 2. Severity-ordered findings

1. **High:** NotebookLM falsely generated a Python syntax error, missing `LocalRulesBackend.evaluate`, dead `validate_github_repo_url`, missing persona package data, and a Pydantic dependency. Exact source and executable controls contradict all five.
2. **High:** NotebookLM failed the explicit source-count control by turning `560 total / 549 processed / 11 failed` into `549` total.
3. **Medium:** The live OSS ledger preserves the significant AutoGen, OpenAI Evals, Langfuse, and Phoenix license/status qualifications.
4. **Low:** The local backend boundary is explicit: deterministic structural readiness capped at `40/50`, not semantic verification.

## 3. Component scores

| Component | Score |
|---|---:|
| Type Fit | 25/25 |
| Adversarial Depth | 18/20 |
| Evidence Provenance | 20/20 |
| Persona/Skill Extensibility | 15/15 |
| Observability/Repeatability | 10/10 |
| Integration Cost | 10/10 |
| **Checked total** | **98/100** |

## 4. Evidence inspected

The judge verified the dataclass core, backend and validator definitions, target escaping, baseline anchors, NotebookLM contradiction ledger, and OSS license/metadata ledger.

## 5. Evidence gaps and unsupported claims

- The bundled backend does not semantically evaluate a target or render visual UI.
- A NotebookLM URL is provenance only; the Python core does not fetch it.
- The thin library does not replace a production runtime, durable workflow store, or trace platform.

## 6. Recommendation and actions

**Ship with conditions.** Compose mature runtime/evaluation OSS for live semantics and durability; retain strict compile/anti-fake controls in CI; keep the NotebookLM reference explicitly described as unverified runtime provenance.

## 7. Attestation

I did not inspect any other brief-live judge output.
