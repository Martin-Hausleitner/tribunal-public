# Verification judge: knowledge and correctness

## 1. Assigned role and inspected scope

**Role:** Knowledge and correctness / Knowledge Analyst.

**Inspected:** `tribunal.py`, `personas/knowledge-analyst.json`, `skill/SKILL.md`, the frozen verification packet, verification baseline/NotebookLM/direct-control ledgers, and the comparison CSV. The judge stated that it excluded prior/sibling verdicts, unowned worktree edits, and synthesis ledgers.

## 2. Severity-ordered findings

1. **High:** NotebookLM's lossy source normalization produced confident false syntax, import, regex, delimiter, and missing-method blockers. Exact source and `py_compile` controls overrule those claims.
2. **Medium:** The shared notebook's global inventory changed concurrently. Explicit processed source-ID selection limits query inputs but does not freeze the notebook globally.
3. **Low, positive boundary:** `local-rules` is structurally capped at 50/100 and therefore cannot issue the runtime crown that requires every judge to reach at least 80 with no gaps.
4. **Low, positive identity control:** The Karpathy-inspired persona is explicitly synthetic/unendorsed and its disclaimer is serialized.

## 3. Checked 100-point rubric

| Component | Score |
|---|---:|
| Type Fit | 25/25 |
| Adversarial Depth | 20/20 |
| Evidence Provenance | 18/20 |
| Persona/Skill Extensibility | 15/15 |
| Observability/Repeatability | 8/10 |
| Integration Cost | 9/10 |
| **Total** | **95/100** |

Checked arithmetic: `25 + 20 + 18 + 15 + 8 + 9 = 95`.

## 4. Evidence and observations

The judge directly inspected the structural ceiling and marker logic, persona schema and disclosure, skill host-boundary wording, the four-query NotebookLM ledger, direct compilation controls, baseline, and matrix format.

## 5. Gaps and unsupported claims

- NotebookLM-normalized source text is not reliable code-syntax evidence.
- `local-rules` cannot retrieve external URLs, evaluate truth, verify accessibility, or establish target semantics.
- Multiple persona requests do not establish statistical independence or model-family diversity.

## 6. Recommendation

`Ship`

Priorities: retain executable/source controls over generated characterizations, and require a real evidence-capable backend before any semantic score or runtime crown.

## 7. Provenance

`agy` fresh read-only plan process; Google `Gemini 3.1 Pro (High)`.

## 8. Isolation attestation

I did not inspect any other verification judge output.
