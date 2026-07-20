# External Tribunal attempt ledger (2026-07-21)

The conclusion-free packet was frozen before any accepted judge process:

- Packet: `report/evidence/revalidation-2026-07-21-judge-packet.md`
- SHA-256: `59de53373a1386b2d14ed7d8d82ad6f9493d1d2247eefebd93df1069bb8b1521`

Each role received the same packet, one role-specific rubric, read-only plan/sandbox mode, and an explicit prohibition on inspecting sibling verdicts. Accepted outputs contain an explicit isolation attestation.

## Attempt disposition

| Role | Process/model | Result | Disposition |
|---|---|---|---|
| Knowledge | `grok --single -m grok-4.5 --effort high` | HTTP `402 Payment Required`; usage balance exhausted before model output | Excluded; no verdict prose |
| Critique | `grok --single -m grok-4.5 --effort high` | HTTP `402 Payment Required`; usage balance exhausted before model output | Excluded; no verdict prose |
| UX | `grok --single -m grok-4.5 --effort high` | HTTP `402 Payment Required`; usage balance exhausted before model output | Excluded; no verdict prose |
| Knowledge | fresh `agy --mode plan --sandbox --print`, Gemini 3.1 Pro High | Complete eight-section output, `80/100`, `CONDITIONAL`, isolation attested | Accepted |
| Critique | fresh `agy`, Claude Sonnet 4.6 Thinking | Individual quota reached before model output | Excluded; no verdict prose |
| Critique | fresh `agy --mode plan --sandbox --print`, Gemini 3.5 Flash High | Complete eight-section output, `40/100`, `BLOCK`, isolation attested | Accepted subject to reproduction |
| UX | fresh `agy --mode plan --sandbox --print`, Gemini 3.5 Flash Medium | Complete eight-section output, `92/100`, `CONDITIONAL`, isolation attested | Accepted subject to executable gates |

## Independence boundary

The accepted set proves three separate fresh CLI processes, identical frozen input, role separation, no sibling-verdict input, and explicit self-attestation. All three accepted answers are Google Gemini-family outputs. It therefore does not prove provider-family diversity, provider-memory isolation, statistical independence, or absence of correlated model error. Scores are not averaged; reproduced findings and direct evidence control synthesis.

## Resource guard

The VCVM guard reported `session_used=9`, `session_left=91`, `weekly_used=73`, `weekly_left=27`, and `fast=not_seen`. No Codex/OMX team burst or fast mode was started. The brief explicitly authorizes three `agy` perspectives when Grok cannot run.
