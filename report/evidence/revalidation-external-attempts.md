# External judge attempts: live brief revalidation

Collection date: `2026-07-20`

Common conclusion-free packet: [revalidation-judge-packet.md](revalidation-judge-packet.md)

## Mandated Grok path

Three separate read-only commands were issued with the required provider/model/effort shape:

- knowledge/correctness: `grok --single <role prompt> -m grok-4.5 --effort high`
- harsh criticism/risk: `grok --single <role prompt> -m grok-4.5 --effort high`
- UI/UX/implementability: `grok --single <role prompt> -m grok-4.5 --effort high`

Each exited `1` before model output with HTTP `402 Payment Required`: `Grok Build usage balance exhausted`. No Grok prose exists and none is represented as a verdict.

## Authorized agy fallback sequence

| Role | Model | Result | Disposition |
|---|---|---|---|
| Knowledge/correctness | Gemini 3.1 Pro (High) | Complete eight-field verdict, 95/100, SHIP WITH CONDITIONS | Accepted |
| Criticism/risk first fallback | Claude Sonnet 4.6 (Thinking) | Individual quota reached before answer; reset reported by CLI | Excluded |
| UI/UX first fallback | GPT-OSS 120B (Medium) | Individual quota reached before answer; reset reported by CLI | Excluded |
| Criticism/risk retry | Gemini 3.5 Flash (High) | Complete eight-field verdict, 70/100, SHIP WITH CONDITIONS | Accepted |
| UI/UX retry | Gemini 3.5 Flash (Low) | Only procedural work narration; no score, recommendation, findings, gaps, or final verdict | Excluded |
| UI/UX final retry | Gemini 3.5 Flash (Medium) | Complete eight-field verdict, 94/100, SHIP WITH CONDITIONS | Accepted |

All accepted runs used a fresh command/session, read-only plan mode, the common packet, and a role-specific prompt that forbade sibling verdicts. All accepted runs are Gemini-family models. This proves process/prompt isolation only; it does not prove provider-family diversity, statistical independence, provider-memory isolation, or absence of correlated bias.

## Validation and synthesis boundary

Each accepted output contains the assigned role, engine/model identity, numeric score, recommendation, ordered findings, direct evidence or commands, reproduced-defect separation, unresolved gaps, and independence limits. Judge claims remain opinions until current primary or executable controls reproduce them. In particular:

- the three-person panel restriction with a concise exit-2 error is an intended contract, not a crash;
- orchestrator provenance strings in evidence are an intentional trace surface, not target evidence supplied by the backend;
- `UI/UX ✅` in the comparison matrix means native fit for routing and evidence-gap handling, not proof of a rendered or accessible interface;
- packaging namespace/deprecation warnings, Markdown newline flattening, synchronous live-backend latency, persona discovery, and lack of bundled live providers remain bounded risks or improvement candidates and are checked against current E2E/build output before synthesis.
