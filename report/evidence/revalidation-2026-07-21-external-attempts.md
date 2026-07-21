# External Tribunal attempt ledger (2026-07-21)

The published conclusion-free packet was frozen before every accepted judge process:

- Packet: `report/evidence/revalidation-2026-07-21-judge-packet.md`
- SHA-256: `a5cda94bf1b2bbff444e37f15767357565c981bf700d9247bab3e74b118dddbf`
- Frozen UTC: `2026-07-20T23:35:58Z`

Each accepted role used a fresh `agy --mode plan --sandbox --print` process, the same packet, one role-specific rubric, and an explicit prohibition on sibling verdicts and excluded report/history surfaces. Accepted outputs contain the exact isolation attestation.

## Attempt disposition

| Role | Process/model | Result | Disposition |
|---|---|---|---|
| Knowledge | `grok --single -m grok-4.5 --effort high` | HTTP `402 Payment Required`; balance exhausted before model output | Excluded; no verdict prose |
| Critique | same Grok invocation | HTTP `402` before model output | Excluded; no verdict prose |
| UX | same Grok invocation | HTTP `402` before model output | Excluded; no verdict prose |
| Knowledge | Gemini 3.1 Pro High | Complete output, but falsely repeated the packet's requested Grok provenance instead of actual `agy` provenance | Excluded as provenance-invalid |
| Critique | Claude Opus 4.6 Thinking | Individual quota reached before model output | Excluded; no verdict prose |
| UX | GPT-OSS 120B Medium | Individual quota reached before model output | Excluded; no verdict prose |
| Knowledge | Gemini 3.1 Pro High, fresh retry | Sandbox connection could not read the mounted packet; no scored verdict | Excluded as incomplete |
| Critique | Gemini 3.5 Flash High, fresh retry | Timed out while reading authorized files; no complete eight-section verdict | Excluded as incomplete |
| UX | Gemini 3.5 Flash Medium, fresh retry | Complete eight-section output, `94/100`, `Ship with conditions`, provenance and isolation valid | Accepted |
| Knowledge | Gemini 3.5 Flash Low, fresh retry | Complete eight-section output, `80/100`, `Ship`, provenance and isolation valid | Accepted |
| Critique | Gemini 3.5 Flash High, fresh retry | Complete eight-section output, `73/100`, `Ship with conditions`, provenance and isolation valid | Accepted subject to direct disposition |

Checked arithmetic:

- Knowledge: `20+16+15+12+8+9=80`.
- Critique: `20+12+14+11+8+8=73`.
- UX: `24+18+18+14+10+10=94`.

## Independence boundary

The accepted set proves three separate fresh CLI processes, identical frozen input, role separation, prohibited sibling inputs, and explicit self-attestation. All three accepted outputs are Google Gemini-family responses. It does not prove provider-family diversity, provider-memory isolation, statistical independence, calibrated scores, or absence of correlated error. Scores are not averaged; current source and executable reproduction control synthesis.

## Resource guard

The VCVM guard reported `session_used=9`, `session_left=91`, `weekly_used=73`, `weekly_left=27`, and `fast=not_seen`. No Codex/OMX team burst or fast mode was started. The brief explicitly authorizes `agy` perspectives when Grok cannot run.

A continuation heartbeat at `2026-07-21T00:06:42Z` reported `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=82`, `weekly_left=18`, `weekly_reset=567782s`, and `fast=not_seen`. The configured Mac guard path was absent on this VCVM. No new expensive judge/team burst or fast mode was started; the already completed isolated verdicts above were audited instead.
