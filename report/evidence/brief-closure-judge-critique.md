# Harsh criticism / risk independent verdict

## 1. Assigned perspective and inspected scope

**Perspective:** Harsh criticism and risk, tasked with falsifying the bounded ship claim and separating current defects from explicit non-goals and future live-backend risks.

The judge inspected the frozen packet plus `tribunal.py`, packaging, README, license, skill, all personas, examples, tests, gate scripts, the live IDR ledger, GitHub snapshot, and CSV matrix. It did not inspect sibling verdicts or final synthesis.

## 2. Severity-ordered findings

### Critical

1. **The comparison self-crowns an immature library.** The matrix places Tribunal above mature OSS. The CSV gate proves arithmetic and structure, not whether the self-assigned rubric values are plausible. The crown can mislead unless its narrow declared use case and non-external scoring are unmissable.
2. **Separate calls are not independent models.** All local views use the same backend instance and process. The documentation discloses the limit, but `Independent Judges` language can still imply more than call/payload separation.
3. **There is no live-backend prompt-injection defense.** Markdown escaping protects rendering, not an LLM prompt boundary. A custom live backend must treat target text as hostile.

### High

4. **The local backend is structurally incapable of substantive rejection.** It always returns `40` or `50` and visible evidence gaps; it validates the harness rather than target quality.
5. **Tests cover orchestration contracts, not judgment quality.** This is appropriate for the bundled backend but leaves the value of any real semantic backend unproved.
6. **Engine capacity is deliberately stateless.** A live deployment needs an external trusted cost/quota boundary.
7. **Persona selection is deterministic and repeats after the nine-person pool.** More rounds do not guarantee genuinely new cognitive coverage.
8. **The so-called debate is post-hoc aggregation.** It counts gaps and collates findings rather than running interactive contradiction resolution.

### Medium / low

9. Markdown text normalization can flatten or incompletely escape some formatting constructs, though the judge did not establish an executable security exploit.
10. `version = 1.0.0` with a Beta classifier and the absence of a `py.typed` marker are release-maturity/type-consumer concerns rather than functional blockers.

## 3. Component scores

| Component | Score | Rationale |
|---|---:|---|
| Type Fit | 18/25 | Delivers the declared harness, but its self-crown and tautological local backend weaken the tribunal claim. |
| Adversarial Depth | 9/20 | No substantive local judging, model independence, live prompt defense, or interactive debate. |
| Evidence Provenance | 14/20 | Strong validation/gaps and real contradiction controls; matrix scores remain self-assessed. |
| Persona/Skill Extensibility | 12/15 | Validated personas and clean backend contract; routed skills are labels only. |
| Observability/Repeatability | 6/10 | Deterministic and gated, but no durable live trace/checkpoint/run correlation. |
| Integration Cost | 6/10 | Small core, but live value requires the integrator to build the evaluation backend. |
| **Total** | **65/100** | Below the rubric's unconditional-positive threshold. |

## 4. Evidence actually inspected

The judge read all permitted release surfaces: the 833-line runtime, 391-line test suite, README, packaging, skill, nine personas, examples, three gate scripts, OpenSpec artifacts, baseline/IDR evidence, GitHub snapshot, and matrix.

## 5. Evidence gaps and unsupported claims

- No live backend execution was observed through the library's `JudgeBackend` contract.
- Matrix scores have no independent/community calibration.
- The packet's compile statement was not re-executed by this judge, though source inspection found no syntax problem.
- No browser, TUI, viewport, assistive-technology, or human-study evidence supports a visual UX claim.
- No security audit of an actual live-provider prompt boundary exists.
- Local `Independent Judges`, UI/UX, and adversarial-depth capability markers are generous if read as semantic or visual proof rather than declared orchestration support.

## 6. Recommendation

**Ship with Conditions.**

1. Label the crowned matrix visibly as a narrow, structural-contract self-assessment with no external calibration; do not imply general product superiority.
2. Downgrade or clearly qualify the Tribunal UI/UX capability marker unless actual visual evidence exists.
3. Put `orchestration contract, not judgment engine` prominently near the headline and matrix.
4. Document hostile-target/prompt-injection responsibility for live-backend integrators.

Recommended but non-blocking: reconcile Beta/v1.0 metadata, consider `py.typed`, exercise non-trivial backend score/gap variation, and add run correlation for live deployments.

## 7. Independence statement

I did not inspect any other brief-closure judge output.

Provider provenance: authorized fallback, fresh `agy` session, Claude Opus 4.6 (Thinking). The score is the external judge's opinion, not an independently calibrated measurement.
