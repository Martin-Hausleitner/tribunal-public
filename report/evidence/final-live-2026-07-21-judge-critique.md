# Accepted harsh-critique/risk verdict

- Role: Harsh criticism and risk
- Packet SHA-256: `912f24d6b2503c5e07605f198df0ca4875a840bc9daff7617c7df42669c1aa74`
- Engine: `agy 1.1.4`
- Model: `Gemini 3.5 Flash (High)`
- Session: fresh isolated read-only plan/print process
- Recommendation: `Ship with conditions`
- Score: `73/100`
- Inspected scope declared by judge: frozen packet plus the packet-permitted current source, docs, personas, examples, tests, gates, OpenSpec, and current-pass evidence files

## Severity-ordered findings

### High

1. **Structural provenance scoring can be misunderstood.** `LocalRulesBackend` adds ten structural points for a syntactically valid NotebookLM URL while performing no retrieval. A consumer that ignores the explicit gaps and backend name could mistake `50` for better semantic evidence than `40`.
2. **Provider correlation is not enforced.** One injected backend receives all judge requests. Persona/request separation does not establish model-family diversity or independent errors.
3. **Skill routes are declarations.** Strings such as `web-search`, `notebooklm`, or `architecture` are recorded but not discovered or executed by the core.

### Medium

4. **Configured capacity is stateless across runs.** It is a per-call judge-slot planner, not durable quota, rate-limit, billing, retry, or token control.
5. **Backend prose remains untrusted downstream input.** Markdown escaping is a rendering control; JSON necessarily preserves backend values for consumers and does not prevent downstream prompt injection.
6. **Adjacent OSS has material license/maintenance qualifications.** AutoGen is maintenance-only, OpenAI Evals has dataset exceptions, Langfuse excludes enterprise directories from MIT, and Phoenix is ELv2 source-available.

### Low

7. **`DebateSummary` can be over-read.** The implementation is post-hoc synthesis, not interactive cross-examination, although current docs and serialized `kind` disclose this.

## Checked scoring

| Dimension | Score | Weight | Judge rationale |
|---|---:|---:|---|
| Type Fit | 22 | 25 | Strong structural coverage; bundled backend cannot compare semantics. |
| Adversarial Depth | 12 | 20 | Distinct personas but no family diversity, active debate, or injection defense. |
| Evidence Provenance | 13 | 20 | Explicit gaps/provenance; URL point and untrusted backend prose require care. |
| Persona/Skill Extensibility | 11 | 15 | Clean persona data; routed skill strings are host-owned. |
| Observability/Repeatability | 7 | 10 | Stable schemas/gates; no tracing or durable quota. |
| Integration Cost | 8 | 10 | Zero dependencies; live semantic backend is host work. |
| **Total** | **73** | **100** | `22+12+13+11+7+8=73` |

## Evidence, risks, and limitations

The judge declared read-only inspection of all packet-permitted source, docs, persona, test, gate, and evidence surfaces. It reported a green unit suite and concise CLI error behavior; the root pass independently reruns those gates before relying on them.

- False-green risk exists only when consumers strip backend/gap provenance from the structural score.
- Same-backend correlation remains an integration boundary.
- No visual/accessibility runner or live NotebookLM pipeline is bundled.
- No provider-memory or statistical independence is proved.
- The `10,000` character and `32` requested-round bounds remain explicit.

## Prioritized actions

1. Keep the local structural warning prominent wherever `local-rules` is used.
2. Require real provider/model provenance and family diversity in deployments that claim it; do not imply that the core enforces it.
3. Complete source/build/install/report gates before release.

## Isolation attestation

I did not inspect any sibling judge output.
