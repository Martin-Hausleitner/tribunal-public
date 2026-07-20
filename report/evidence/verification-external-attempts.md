# Verification-pass external judge attempt ledger

Recorded after all three accepted role outputs. The shared conclusion-free packet was frozen at SHA-256 `f5ad6478b25e1078e93b0250bc70630984100b608dc92211fc9f9bf423ba1d6d` before any accepted role process began.

## Required path and isolation

The weekly guard was already above 50%, so no expensive Codex/OMX burst was started. The brief explicitly allows three `agy` perspectives instead of Grok workers. Each accepted role used a fresh `agy --mode plan --sandbox --print` process, the same packet, role-specific instructions, and no sibling verdict or synthesis. All sessions were told not to edit repository files.

## Attempt dispositions

| Role | Model/process | Result | Disposition |
|---|---|---|---|
| Knowledge | Gemini 3.1 Pro High, first malformed CLI invocation | Generic model greeting; role prompt was not bound to `--print` | Excluded as no verdict |
| Critique | requested Claude Sonnet 4.6 Thinking, first malformed CLI invocation | Generic greeting | Excluded as no verdict |
| UX | requested GPT-OSS 120B Medium, first malformed CLI invocation | Generic greeting | Excluded as no verdict |
| Knowledge | Gemini 3.1 Pro High, corrected fresh invocation | Complete eight-part output, `95/100`, `Ship`, required attestation | Accepted |
| Critique | Claude Sonnet 4.6 Thinking, corrected fresh invocation | Individual quota reached before model answer | Excluded; no model prose |
| UX | GPT-OSS 120B Medium, corrected fresh invocation | Individual quota reached before model answer | Excluded; no model prose |
| Critique | Gemini 3.5 Flash High, fresh invocation | Complete eight-part hostile output, `57/100`, `Block`, required attestation | Accepted subject to later finding reproduction |
| UX | Gemini 3.5 Flash Low, fresh invocation | Wrote/referred to a separate CLI brain artifact and returned only a summary, not the required eight sections | Excluded as incomplete |
| UX | Gemini 3.5 Flash Medium, fresh invocation | Complete eight-part output, `85/100`, `Ship`, required attestation | Accepted subject to final gate rerun |

Checked accepted totals:

- Knowledge: `25+20+18+15+8+9=95`.
- Critique: `15+10+12+10+5+5=57`.
- UX: `25+13+18+15+7+7=85`.

## Independence boundary

The accepted set proves three separate fresh processes, common conclusion-free input, role-specific scope, and explicit non-inspection attestations. All accepted outputs ultimately came from Google Gemini-family models because Anthropic Claude and GPT-OSS quota-blocked before answers. It therefore proves no provider-family diversity, provider-memory isolation, statistical independence, or bias calibration. Scores are not averaged into a fictional consensus; reproduced findings and later executable evidence control synthesis.
