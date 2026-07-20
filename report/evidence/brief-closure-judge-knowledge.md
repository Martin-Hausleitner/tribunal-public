# Knowledge / correctness independent verdict

## 1. Assigned perspective and inspected scope

**Perspective:** Knowledge/correctness.

**Inspected:** `brief-closure-judge-packet.md`, `brief-live-notebooklm.md`, `tribunal.py`, `README.md`, `pyproject.toml`, and `personas/andrej-karpathy.json`.

## 2. Severity-ordered findings

1. **High: NotebookLM provenance is syntactic, not semantic.** `validate_notebooklm_url` validates the canonical URL shape but does not query the corpus. `LocalRulesBackend` keeps the resulting semantic evidence gap visible.
2. **High: Generated NotebookLM claims require executable controls.** The live ledger shows invented syntax/package/backend defects; the bounded library correctly refuses to present NotebookLM prose as runtime truth.
3. **Medium: Reference repositories are strictly validated.** Persona loading requires bare HTTPS GitHub repository URLs.
4. **Medium: Synthetic-persona identity is disclosed.** The Karpathy-inspired persona carries a serialized non-authorship/non-endorsement disclaimer.
5. **Medium: Structural scoring cannot fake semantic success.** The bundled backend remains capped at `50/100` and states that it did not evaluate factual correctness or target semantics.

## 3. Component scores

| Component | Score |
|---|---:|
| Type Fit | 25/25 |
| Adversarial Depth | 20/20 |
| Evidence Provenance | 20/20 |
| Persona/Skill Extensibility | 15/15 |
| Observability/Repeatability | 10/10 |
| Integration Cost | 10/10 |
| **Total** | **100/100** |

## 4. Evidence actually inspected

- `report/evidence/brief-closure-judge-packet.md`
- `report/evidence/brief-live-notebooklm.md`
- `tribunal.py`
- `README.md`
- `pyproject.toml`
- `personas/andrej-karpathy.json`

## 5. Evidence gaps and unsupported claims

- The dependency-free local backend does not semantically evaluate the target.
- A valid NotebookLM URL is provenance; the library does not fetch or verify its contents.
- Live judgment requires an injected evidence-capable backend.
- Generated research synthesis remains untrusted until checked against executable or primary evidence.

## 6. Recommendation

**Ship.**

1. Release the core for its bounded structural contract.
2. Delegate source retrieval and semantic correctness to injected backends.
3. Preserve the local score ceiling and visible evidence gaps.

## 7. Independence statement

I did not inspect any other brief-closure judge output.

Provider provenance: authorized fallback, fresh `agy` session, Gemini 3.1 Pro (High). The score is the external judge's opinion, not an independently calibrated measurement.
