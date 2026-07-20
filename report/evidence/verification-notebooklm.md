# Verification-pass NotebookLM IDR

IDR: ja

- Recorded UTC: `2026-07-20T22:14:42Z`
- Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Authenticated CLI: `nlm 0.8.9`
- Public sharing: `is_public=true`, `access_level=public`; the returned public link exactly matched the canonical link

No credential, account identifier, collaborator identity, cookie, or token is retained.

## Mutable corpus and source ingestion

The canonical notebook is shared and changed concurrently during this pass. The first exact detail/source-list observations were `640` total, `598` processed (`status=2`), and `42` failed (`status=3`). The final direct reduction after all four accepted queries was `669` total, `600` processed, and `69` failed. These changing values are retained, not normalized into a fictional stable count.

This pass attempted four planning-source file uploads. `Verification proposal HEAD 9f1dc36 2026-07-20` (`0f4bb0a5-6582-448f-9968-d9f8231b5805`) and `Verification design HEAD 9f1dc36 2026-07-20` (`972ccb26-3f06-4892-8edf-8eac17d9db17`) were processed. The nested capability-spec and task-file uploads returned `INVALID_ARGUMENT` and produced no source. A materially different inline capability-bundle import returned a source ID but later settled at failed status `3`; it was excluded. A later direct-control file upload also returned `INVALID_ARGUMENT`. No failed source was selected for a query.

Because other unowned work was changing the shared notebook and global counts, every accepted query used a fresh conversation UUID and an explicit set of processed source IDs. The sets combined current project source snapshots, the two processed current-pass OpenSpec sources, canonical repositories for the ten established alternatives, and role-appropriate primary research. Selected usability/research sources included Nielsen Norman Group's ten heuristics, W3C WCAG 2.2 Quick Reference, the multi-agent-debate paper, and an ACL position-bias study.

## Rejected default-conversation attempt

The first knowledge attempt omitted a new conversation UUID. It returned conversation `1ebabb83-484f-405b-8b24-a26cfa5b9afb`, `sources_used=[]`, no citation mappings, and content from sources outside the selected set. It was rejected completely. A four-source fresh-conversation preflight then returned three selected source IDs and 18 citation mappings, proving that explicit fresh conversation isolation restored selected-source grounding.

## Cross-query 1: knowledge and correctness

**Conversation:** `6faecb5e-c034-46ad-9dae-dbce14cf91e0`

**Question:** Audit HEAD `9f1dc36` using only selected current project, all ten canonical alternative-repository, multi-agent-debate, and judge-bias sources. Establish supported structural guarantees, explicit non-capabilities, current quoted source defects, a capability-not-popularity comparison, and the minimum honest ship boundary without reusing historical stars, scores, provider attempts, or corpus counts.

**Returned grounding:** 17 selected source IDs and 72 citation mappings.

**Retained answer:** The core provides separate backend requests, deterministic persona/round routing, bounded inputs, a structural-only score, strict positive-marker conditions, and explicit semantic/retrieval/visual/independence/quota/observability limits. The established alternatives cover complementary eval, red-team, runtime, and observability surfaces that the thin core should compose rather than rebuild. AutoGen's selected README placed it in maintenance mode and directed new work to Microsoft Agent Framework.

**Manual exclusions:** The answer converted a normalized backslash excerpt into a fatal Python syntax defect and treated paper metrics as local-system support. It also called separate initial views a `strict state machine`, which overstates the contract. Direct compilation and source controls reject the code claim; literature results remain external research, not local measurement.

## Cross-query 2: hostile criticism and risk

**Conversation:** `1c49b3b0-36ef-4d73-b85a-b6f39cc0dabb`

**Question:** Try to falsify the bounded ship claim using only selected current code/report/skill/matrix, OSS, debate, and bias sources. Separate reproducible defects from documented non-goals and live-backend risks; require exact quotations and executable reproduction for every alleged current defect.

**Returned grounding:** 6 selected source IDs and 22 citation mappings.

**Retained answer:** Matrix fit and runtime structural score are different declared instruments; persona repetition, stateless capacities, syntactic-only URLs, and lack of local retrieval are published boundaries. Common-mode family error, provider provenance, injection handling, bias calibration, persistent budgets, and unclaimed zipapp/PEX resource behavior remain legitimate deployment pressure.

**Manual exclusions:** Despite the prompt, the answer invented four fatal defects from normalized excerpts: an unterminated string, collapsed imports, an invalid empty regex, and an empty delimiter. It also promoted three-family routing into a mandatory local-core fix. Exact source and execution reject all four code claims; provider-family policy belongs at a configured live boundary.

## Cross-query 3: CLI UX and implementability

**Conversation:** `e7c6e336-8830-42ca-b9bd-a1f8725c2fbb`

**Question:** Audit observable modes, bounds, help/error behavior, serialization, identity disclosure, packaging, evidence workflow, and operator friction. Separate terminal evidence from viewport, keyboard, assistive-technology, contrast, and human-task claims; treat Nielsen/WCAG as criteria rather than passed tests; compare build-versus-compose with promptfoo and Microsoft Agent Framework.

**Returned grounding:** 11 selected source IDs and 40 citation mappings.

**Retained answer:** The CLI exposes four modes, bounded rounds/targets, standard argparse help, concise status-2 failures, deterministic Markdown/JSON surfaces, conventional setuptools packaging, and explicit host responsibility for routed skills. It correctly states that a headless CLI cannot prove viewport, focus, contrast, target-size, reflow, assistive-technology, or human-task behavior. promptfoo is stronger for mature eval/red-team CI; Microsoft Agent Framework is stronger for production agent workflows and telemetry.

**Manual exclusions:** The answer invented the same syntax and missing-method failures, misclassified documented Markdown whitespace normalization as a release blocker, and falsely claimed it had published a Studio report. No such artifact was requested or verified. These claims are excluded.

## Cross-query 4: contradiction and source attribution

**Conversation:** `6040a346-dc57-48c4-86bb-241c2786451f`

**Question:** Resolve the prior alleged string/import/regex/delimiter/missing-method defects and the Pydantic, raw-Markdown, semantic score, live retrieval, visual proof, provider independence, durable quota, and Karpathy-identity claims. The question supplied the separately observed compile, import, exact-source, symbol, persona-count, and rendering controls and required them to be labeled external executable evidence rather than NotebookLM citations.

**Returned grounding:** 6 selected source IDs and 23 citation mappings.

**Retained answer:** It correctly classified the syntax/import/regex/delimiter/missing-method claims as normalization artifacts; confirmed dependency-free dataclasses/manual validation; separated structural scoring, syntactic-only NotebookLM provenance, visual proof, provider independence, and identity safety as explicit boundaries; and retained durable quota, real retrieval, credential propagation, provider provenance, and injection controls as future integration risks. It also produced the requested evidence hierarchy: executable observation first, exact source second, project specification third, generated characterization last.

## Direct controls that outrank generated prose

The complete control ledger is [`verification-direct-controls.md`](verification-direct-controls.md). Decision-relevant observations were:

- `python -m py_compile tribunal.py tests/test_tribunal.py personas/__init__.py` exited `0`.
- `LocalRulesBackend.evaluate` was callable; `_parse_capacities`, `_load`, `_normalize_hardness`, and `judge` existed; nine personas loaded.
- Exact files contained separate imports, valid escaped marker strings, a literal-backtick regex, and a non-empty longer backtick delimiter.
- `_markdown_text` escaped Markdown markers and `_markdown_code` safely wrapped a three-backtick input in four backticks.

## IDR conclusion

The live research supports retaining the bounded recommendation: Codex Tribunal is useful as a small, inspectable orchestration contract, persona/skill library, and deterministic proof surface, while promptfoo, mature evaluation libraries, Microsoft Agent Framework, and observability platforms should supply larger adjacent capabilities. It does not support calling the local backend a semantic verifier, NotebookLM client, visual accessibility tester, statistically independent jury, persistent budget authority, or production trace system.

NotebookLM's selected-source metadata was valuable, but three independent role answers reproduced the same confident false blockers from lossy source normalization. The fourth control corrected them only after receiving external executable facts. Therefore processed status and citations establish provenance, not correctness; all current-code and release claims remain subordinate to direct gates and clean-install E2E.
