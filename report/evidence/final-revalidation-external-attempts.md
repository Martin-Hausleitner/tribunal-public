# Final external tribunal attempt ledger

Recorded UTC: `2026-07-20`

## Frozen input and isolation

Every attempt received the role-specific assignment plus [`final-revalidation-judge-packet.md`](final-revalidation-judge-packet.md). That packet is pinned to base commit `b4bce6464001a59e8ea6b7430b03cf5f780c98a8`, omits prior/sibling verdicts and synthesis, and restricts readable surfaces. Each accepted output was produced in a separate fresh process/session before any accepted verdict file was written.

## Required Grok path

Three independent commands used the required model and effort:

```text
grok --single <role-specific prompt> -m grok-4.5 --effort high
```

Knowledge, critique, and UX each exited `1` before returning model prose:

```text
API error (status 402 Payment Required): Grok Build usage balance exhausted
```

No Grok output exists and none is represented as a verdict.

## Approved `agy` fallback attempts

| Perspective | Model/session | Result | Disposition |
|---|---|---|---|
| Knowledge/correctness | Gemini 3.1 Pro (High), fresh plan/read-only sandbox | Complete seven-part output, `88/100`, Ship with conditions | Accepted |
| Harsh criticism/risk | Claude Sonnet 4.6 (Thinking), fresh plan/read-only sandbox | Individual quota reached before answer; reset reported in roughly 24 minutes | Excluded |
| CLI UX/feasibility | GPT-OSS 120B (Medium), fresh plan/read-only sandbox | Individual quota reached before answer; reset reported in roughly 24 minutes | Excluded |
| Harsh criticism/risk | Gemini 3.5 Flash (High), fresh plan/read-only sandbox | Complete role output, `64/100`, Block | Accepted |
| CLI UX/feasibility | Gemini 3.5 Flash (Low), fresh plan/read-only sandbox | Complete role output, `96/100`, Ship | Accepted |

All accepted totals were recomputed: `20+16+20+15+8+9=88`, `18+11+12+11+6+6=64`, and `25+18+18+15+10+10=96`. Each output identifies scope, findings, evidence, gaps, recommendation, and the required non-inspection sentence.

## Independence limit

The three accepted results prove separate process/session and conclusion-free input isolation. They do not prove provider-memory isolation, statistical independence, or provider-family diversity: all accepted final-revalidation judges are Gemini-family models because the required Grok path returned 402 and the Claude/GPT-OSS fallback quotas blocked before answer generation. This limitation materially lowers the consensus claim; disagreements and reproducible facts control synthesis rather than score averaging.
