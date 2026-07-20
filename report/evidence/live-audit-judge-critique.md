# Live-audit judge verdict: hard criticism and risk

**Engine:** `agy` / `Claude Sonnet 4.6 (Thinking)`  
**Execution:** fresh isolated read-only plan session; replacement for an earlier Claude Opus run that returned only a summary  
**Input:** `report/evidence/live-audit-judge-packet.md` plus independently inspected repository surfaces  
**Normalization:** Local `file://` links are rendered as repository paths. The model's conflation of the prior release's shell-damaged UX prompt with the current run is preserved as a judge claim and corrected only in the later synthesis.

## Perspective and Scope

Hard Criticism and Risk: security, identity, fake-green behavior, stale claims, missing failure controls, and release blockers across the complete public surface.

## Findings (severity-ordered)

### CRITICAL — C1: Judge-process independence is weaker than the framing

All required Grok calls failed with HTTP 402. The brief-approved fallback completed knowledge with Gemini 3.1 Pro, criticism with Claude, and UX with Gemini 3.5 Flash after a discarded GPT-OSS attempt. Two accepted judges therefore share a provider family, and no re-randomization, bias calibration, or position-swap was applied. The README correctly states that isolation is not automatically cross-model or cross-provider independence, but a synthesis could still imply more adversarial consensus than this composition supports.

### CRITICAL — C2: UX selection followed discarded attempts

The judge treats acceptance of the first task-conformant replacement as a selection confound. Discarding a non-answer is legitimate, but the failed-attempt chain must remain visible and the UX verdict must not be weighted as if it came from a neutral random draw.

### HIGH — H1: OpenSpec tasks 4–8 were incomplete at judge snapshot

The independent runs, library/skill audit, E2E, report, and publication tasks remained unchecked while the judge ran. The judge correctly refuses to call the live-audit change complete before its own ledger and gates are closed. This is an in-flight status finding rather than evidence that already completed work never occurred.

### HIGH — H2: Documented CLI E2E uses only the structural backend

Every retained public CLI row used `local-rules`, returned 40–50, `⚠️`, and explicit gaps. The prior custom-backend positive-marker path used a hand-crafted test backend, not a live LLM. Readers must not confuse a matrix crown or finished audit prose with a semantic verdict from the bundled runtime.

### HIGH — H3: A compliant backend can self-assert a green marker

`validate_backend_result` accepts an empty `evidence_gaps` list. A backend that returns `score >= 80` and no declared gaps can receive `✅` or `👑` without the library independently verifying its evidence. The README discloses this boundary, but the library cannot make semantic abuse hard by itself.

### HIGH — H4: `ui-specialist` contains a suspect repository reference

`personas/ui-specialist.json` references `https://github.com/dip/cmdk`; the judge identifies `https://github.com/pacocoursey/cmdk` as the known canonical repository. The current loader checks URL shape, not reachability or redirect target, so a syntactically valid but stale reference can pass.

### MEDIUM — M1: NotebookLM proof remains external to runtime judge evidence

NotebookLM queries and their manual corrections live in a separate evidence ledger. The bundled backend only records a URL and explicitly says it did not query content. The final report must trace the external query/correction evidence and must not imply that the runtime performed it.

### MEDIUM — M2: `strongest_points` can be dominated by one view

`_debate` sorts views by score and greedily collects up to three findings. A high-scoring single judge can therefore dominate the strongest-points list even when lower-scoring judges disagree. The result is post-hoc synthesis, not consensus.

### MEDIUM — M3: Capacity is per-run, not durable quota

`EngineManager.allocate` copies capacity for every allocation call. The README documents per-run statelessness, but an API consumer could still mistake configured capacities for cross-run quota enforcement. Trusted durable quota belongs outside the core.

### MEDIUM — M4: The Markdown report crown gate is string-based

`scripts/report_gate.py` requires exactly one literal crown but does not bind it to the score-table winner. The CSV gate is stronger and must be run jointly; no single gate currently proves both artifacts share the same score data.

### LOW — L1: Markdown normalization flattens multiline backend strings

`_markdown_text` collapses whitespace. JSON remains lossless, but multiline or structured findings lose layout in Markdown.

### LOW — L2: Current live-audit OpenSpec validation was not yet evidenced

The retained old E2E ledger validated the earlier `finish-codex-tribunal-library` change. The fresh change still needed its own strict validation after task completion.

### LOW — L3: Karpathy disclaimer is absent from Markdown views

The disclaimer is validated and retained on the runtime `Persona`, but `VerdictReport.to_markdown()` does not serialize it. A standalone generated Markdown verdict can show the synthetic persona's judgment without its non-impersonation notice.

## Rubric Scores

| Component | Max | Score | Rationale |
|---|---:|---:|---|
| Type Fit | 25 | 19 | Genuine narrow fit and honest local boundary; live composition does not fully realize heterogeneous independence. |
| Adversarial Depth | 20 | 10 | Strong structural tests, but self-asserted gaps/scores, greedy synthesis, and no live bias controls. |
| Evidence Provenance | 20 | 13 | Truthful attempt ledgers, dated NotebookLM/GitHub evidence; audit still in flight and fallback composition needs stronger synthesis disclosure. |
| Persona/Skill Extensibility | 15 | 11 | Nine validated personas and a clear backend contract; suspect repo reference and unsurfaced disclaimer. |
| Observability/Repeatability | 10 | 5 | Deterministic outputs and tests, but current live-audit closure/E2E/OpenSpec gates were not yet complete at snapshot. |
| Integration Cost | 10 | 7 | Dependency-free package and minimal Protocol; no async and per-run capacity can surprise. |
| **Total** | **100** | **65** | Below the rubric's 70-point unconditional-crown threshold at this in-flight snapshot. |

## Evidence Inspected

- Frozen live-audit packet
- All 826 lines of `tribunal.py`
- `README.md`, `skill/SKILL.md`, all nine personas
- Full test module and all three gate scripts
- Live NotebookLM ledger, GitHub snapshot, Grok attempt ledgers, old E2E ledger, baseline
- Live-audit OpenSpec proposal, design, tasks, and capability spec
- Packaging and both examples

## Explicit Evidence Gaps and Unsupported Claims

1. Live E2E re-execution and current OpenSpec strict validation were not complete at the judge snapshot.
2. The judge could not assess sibling verdict correctness by design.
3. No calibration proves that two accepted Gemini-family perspectives behave independently.
4. The suspect `cmdk` reference needed a live canonical-URL check.
5. The final refreshed synthesis report was not yet available for inspection.

## Recommendation: Ship with conditions

The dependency-free core can ship as a deterministic orchestration and backend-extension contract. It must not ship as a semantically validated or statistically independent audit engine.

### Priority 1

1. Close the live-audit task ledger and current gates.
2. State the two-Gemini fallback composition and failed/discarded attempts in synthesis.
3. Verify and correct `personas/ui-specialist.json` repository provenance.

### Priority 2

4. Surface the Karpathy disclaimer in standalone Markdown verdicts.
5. Strengthen API documentation for per-run capacity.
6. Document that report and CSV gates must run jointly.

### Priority 3

7. Preserve a regression test demonstrating that positive markers remain live-backend assertions.
8. Consider an opt-in structured Markdown rendering path for multiline backend findings.

I did not inspect any other live-audit judge output.
