# Brief-closure external judge attempt ledger

- Recorded UTC: `2026-07-20`
- Frozen packet: [`brief-closure-judge-packet.md`](brief-closure-judge-packet.md)
- Frozen repository base: `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`

Every accepted judge used a fresh process/session, one assigned role, the same conclusion-free packet, read-only/plan mode, and no sibling verdict or synthesis. Exit status and incomplete outputs remain separate from accepted verdicts.

## Required Grok path

Three parallel commands used the mandated provider, model, and effort:

```text
grok --single <role-specific prompt> -m grok-4.5 --effort high
```

Knowledge, criticism, and UX each reached the Grok provider and exited `1` before any model prose with:

```text
API error (status 402 Payment Required): Grok Build usage balance exhausted
```

No Grok text is presented as a verdict.

## Authorized `agy` fallback

| Role | Fresh model/session | Exit/result | Disposition |
|---|---|---|---|
| Knowledge/correctness | Gemini 3.1 Pro (High), plan/read-only | Complete seven-part result, `100/100`, `Ship` | Accepted |
| Harsh criticism/risk | Claude Opus 4.6 (Thinking), plan/read-only | Complete seven-part artifact, `65/100`, `Ship with Conditions` | Accepted |
| CLI/UI/UX feasibility | GPT-OSS 120B (Medium), plan/read-only | Could not see the repository workspace; no verdict | Excluded |
| CLI/UI/UX feasibility | Gemini 3.5 Flash (High), plan/read-only | Returned `96/100`, but inline packet quoting triggered shell parsing and the output used neither an allowed verdict nor the exact independence statement | Excluded |
| CLI/UI/UX feasibility | Gemini 3.5 Flash (Low), fresh plan/read-only | Complete seven-part result, `95/100`, `Ship` | Accepted |

The accepted component sums were recomputed: `25+20+20+15+10+10=100`, `18+9+14+12+6+6=65`, and `25+18+19+15+8+10=95`. Each accepted file identifies role, scope, severity-ordered findings, inspected evidence, gaps, recommendation, actions, and the required independence statement.

## Independence limit

The accepted set proves distinct external sessions, conclusion-free initial input, and no sibling-output access. It spans two provider/model families: Gemini for knowledge and UX, Claude for criticism. It does not prove provider-memory isolation, statistical independence, calibrated scoring, or three-family diversity. The large disagreement (`65` through `100`) is preserved and reconciled through concrete evidence rather than averaged into consensus.
