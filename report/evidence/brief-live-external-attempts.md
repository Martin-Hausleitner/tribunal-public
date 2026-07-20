# Brief live external tribunal attempt ledger

Recorded UTC: `2026-07-20T21:06:39Z`

## Frozen input and isolation

Every attempt received the relevant role assignment plus [`brief-live-judge-packet.md`](brief-live-judge-packet.md), frozen before any role output at starting snapshot `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`. The packet omits prior/sibling verdicts, scores, crown, synthesis, and final recommendation. Accepted outputs came from separate fresh `agy` sessions and identify the inspected scope and required non-inspection attestation.

## Required Grok path

Three independent role processes used the mandated model and effort:

```text
grok --single <role prompt> -m grok-4.5 --effort high
```

The actual commands additionally enforced plan/read-only behavior, disabled memory, web search, and subagents. Knowledge, criticism, and UX each reached the Grok provider and exited `1` before returning any model prose:

```text
API error (status 402 Payment Required): Grok Build usage balance exhausted
```

No Grok prose exists and none is represented as a verdict.

## Authorized `agy` fallback dispositions

| Perspective | Fresh model/session | Result | Disposition |
|---|---|---|---|
| Knowledge/correctness | Gemini 3.1 Pro (High), plan/read-only sandbox | Complete seven-part output, `98/100`, Ship with conditions | Accepted |
| Harsh criticism/risk | Claude Sonnet 4.6 (Thinking), first session | Complete output, `72/100`, but searched/read unrelated Tribunal repositories before locating the packet | Excluded for scope/independence violation |
| CLI/UI-UX feasibility | GPT-OSS 120B (Medium), first session | Generic request for a task; no role analysis, evidence, rubric, or attestation | Excluded as incomplete |
| Harsh criticism/risk | Claude Sonnet 4.6 (Thinking), fresh project restricted to absolute repo path | Complete seven-part output, `73/100`, Ship with conditions; only packet-permitted files listed | Accepted |
| CLI/UI-UX feasibility | GPT-OSS 120B (Medium), fresh restricted project | Complete shape, `59/100`, but explicitly opened only the packet and invented missing help, entry point, packaging, and input validation | Excluded for uninspected/contradicted evidence |
| CLI/UI-UX feasibility | Gemini 3.5 Flash (Low), fresh restricted project with mandatory exact file list | Complete seven-part output, `99/100`, Ship; directly listed and cited required CLI/README/package/test/example surfaces | Accepted |

Checked totals: knowledge `25+18+20+15+10+10=98`; criticism `20+13+14+13+6+7=73`; UX `25+20+19+15+10+10=99`.

## Acceptance and independence boundary

The accepted set contains exactly one knowledge, one criticism, and one UX verdict. It proves separate fresh sessions, a common conclusion-free input, explicit file-scope attestations, and two provider families: Google Gemini for knowledge/UX and Anthropic Claude for criticism. It does not prove statistical independence, provider-memory isolation, or three-family diversity. Scores are not averaged into consensus; reproducible findings and evidence quality control synthesis.

Excluded outputs remain availability and quality-control evidence only. The high accepted scores do not override current executable gaps; the critical judge's dissent and later E2E/gates remain independent release conditions.
