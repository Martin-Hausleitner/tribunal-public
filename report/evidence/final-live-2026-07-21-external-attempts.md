# Final live external Tribunal attempt ledger, 2026-07-21

The conclusion-free packet was frozen before every judge process:

- Packet: `report/evidence/final-live-2026-07-21-judge-packet.md`
- SHA-256: `912f24d6b2503c5e07605f198df0ca4875a840bc9daff7617c7df42669c1aa74`
- Starting source HEAD: `990a8df200716a446472faf4110a2e896c52ab40`

Every process received the same packet path/hash, one role-specific rubric, read-only scope, an explicit sibling-output prohibition, and an exact isolation attestation requirement.

## Attempt disposition

| Role | Invocation/model | Result | Disposition |
|---|---|---|---|
| Knowledge | `grok --single -m grok-4.5 --effort high` | HTTP `402 Payment Required`: Grok Build balance exhausted before model output | Excluded; no verdict prose |
| Critique | same isolated Grok invocation | HTTP `402` before model output | Excluded; no verdict prose |
| UX | same isolated Grok invocation | HTTP `402` before model output | Excluded; no verdict prose |
| Knowledge | fresh `agy` / Gemini 3.1 Pro High | Complete packet-only verdict; `85/100`; `Ship with conditions`; correct packet hash, provenance, arithmetic, gaps, and isolation attestation | Accepted |
| Critique | fresh `agy` / Claude Sonnet 4.6 Thinking | Individual quota reached with reset estimate `15m56s`; no model verdict | Excluded; no verdict prose |
| UX | fresh `agy` / GPT-OSS 120B Medium | Individual quota reached with reset estimate `15m56s`; no model verdict | Excluded; no verdict prose |
| Critique | fresh `agy` / Gemini 3.5 Flash High | Complete permitted-source verdict; `73/100`; `Ship with conditions`; correct packet hash, provenance, arithmetic, gaps, and isolation attestation | Accepted subject to direct disposition |
| UX | fresh `agy` / Gemini 3.5 Flash Medium | Complete permitted-source verdict; `85/100`; `Ship with conditions`; correct packet hash, provenance, arithmetic, gaps, and isolation attestation | Accepted subject to direct disposition |

## Checked arithmetic

- Knowledge: `20+16+18+14+9+8=85`.
- Critique: `22+12+13+11+7+8=73`.
- UX: `21+17+17+13+8+9=85`.

## Isolation and provider boundary

The accepted set proves three separate fresh CLI processes, identical frozen input, role separation, prohibited sibling inputs, and explicit self-attestation. Knowledge used Gemini 3.1 Pro while criticism and UX used distinct Gemini 3.5 Flash effort profiles. All accepted responses remain Google Gemini-family outputs. This does not prove provider-family diversity, provider-memory isolation, statistical independence, calibrated scores, or absence of correlated error.

Scores are not averaged. Current source, primary metadata, and direct reproduction control the synthesis.

## Resource guard

The VCVM guard reported `session_used=9`, `session_left=91`, `session_reset=0s`, `weekly_used=88`, `weekly_left=12`, `weekly_reset=565402s`, and `fast=not_seen`. No Codex/OMX team burst or fast mode was started. The brief explicitly authorizes `agy` perspectives when Grok cannot return a verdict.
