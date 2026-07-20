# Verification judge: harsh criticism and risk

## 1. Assigned role and inspected scope

**Role:** Harsh criticism and risk.

**Inspected:** the runtime, README, skill, committed packaging metadata at frozen HEAD, personas, examples, tests, gates, the current OpenSpec change, the permitted verification ledgers/snapshot, and the matrix. The judge reported running tests, gates, and a package build in its read-only plan environment.

## 2. Severity-ordered findings

1. **Critical claim:** A generic top-level `personas` package risks namespace collision with third-party distributions.
2. **High claim:** Direct filesystem globbing is not proven for zipapp/PEX/compressed-resource execution.
3. **High claim:** `_markdown_code` does not HTML-escape metadata before code-span wrapping, which the judge characterized as XSS.
4. **High claim:** deliberate Markdown whitespace normalization loses multiline formatting; JSON remains the lossless surface.
5. **High, reproduced defect:** NotebookLM URL validation accepted query strings and fragments despite the documented canonical form.
6. **High boundary:** a custom backend self-declares score/evidence gaps; schema validation cannot make those claims true.
7. **Medium boundary:** persona rotation repeats after the available pool and does not establish statistical independence.

## 3. Checked 100-point rubric

| Component | Score |
|---|---:|
| Type Fit | 15/25 |
| Adversarial Depth | 10/20 |
| Evidence Provenance | 12/20 |
| Persona/Skill Extensibility | 10/15 |
| Observability/Repeatability | 5/10 |
| Integration Cost | 5/10 |
| **Total** | **57/100** |

Checked arithmetic: `15 + 10 + 12 + 10 + 5 + 5 = 57`.

## 4. Evidence and observations

The judge reported `18` passing tests/subtests, a successful build and wheel layout inspection, direct runtime/source review, the CSV and skill gates, and the permitted evidence ledgers.

## 5. Gaps and unsupported claims

- No claimed or verified zipapp/PEX execution surface exists.
- A syntactic NotebookLM reference is not content grounding.
- Markdown metadata safety requires reasoning about the actual renderer/code-span contract, not merely the absence of pre-escaping inside `_markdown_code`.

## 6. Recommendation

`Block`

Priorities proposed by the judge: unique package namespace, `importlib.resources`, metadata HTML handling, multiline Markdown preservation, and strict canonical NotebookLM URL validation.

## 7. Provenance

`agy` fresh read-only plan process; Google `Gemini 3.5 Flash (High)`.

## 8. Isolation attestation

I did not inspect any other verification judge output.

## Synthesis-control note

This file preserves the hostile verdict rather than silently correcting it. The canonical-URL defect was directly reproduced and fixed after the freeze. Namespace/zipapp concerns are real distribution trade-offs but not claimed current surfaces. The XSS claim is not accepted without a conforming Markdown-renderer reproduction because the value is emitted inside an adaptive code span. The whitespace behavior and backend trust boundary are already disclosed contracts.
