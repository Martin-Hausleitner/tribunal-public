---
name: tribunal
description: Hard-critical Tribunal workflow for knowledge, critique, UI/UX, and comparison reviews using three isolated judges, Nx rounds, explicit provenance, and strict anti-fake gates.
---

# Tribunal Skill

Use this skill when a task needs a rigorous meta-analysis, product/library comparison, UI/UX teardown, or proof review. A Tribunal is not a friendly review. It is a direct, non-sycophantic panel that keeps missing evidence visible.

## Tribunal Types

- `knowledge`: facts, research, citations, primary-source checks.
- `critique`: harsh architecture, product, implementation, and proof teardown.
- `ui_ux`: interface, workflow, visual quality, accessibility, and repeated-use ergonomics.
- `comparison`: tool/product/library matrix with real links, real stars, differentiated scores, and exactly one crown.

## Required Process

1. Pick the Tribunal type, Nx multiplier, and hardness. Default to `rounds=1` and `hardness=standard`; use `hardness=hard` or `brutal` for high-risk claims.
2. Build three isolated judge requests per round and invoke the configured backend separately for each unique persona. Do not expose one judge's conclusion to another before debate. A deterministic local backend proves orchestration only; it does not count as substantive LLM or source research.
3. Route skills before judging:
   - Knowledge: web search, NotebookLM, primary-source review.
   - Critique: architecture, production-code-audit, Karpathy-inspired technical critic.
   - UI/UX: high-end-visual-design, minimalist-ui, ui-ux-pro-max, design-taste-frontend, web-design-guidelines.
   - Comparison: competitive-landscape, CSV/report gate, source verification.
4. Use NotebookLM or an equivalent source corpus for substantive deep research. Record the canonical notebook identity, processed sources, questions, and answers. A URL is provenance only unless a live evidence-capable judge actually queries its contents. Never invent a NotebookLM link.
5. Synthesize only after all judges finish. Name recurring failures, disagreements, and strongest points. Label this as post-hoc synthesis; the current library contract does not provide interactive inter-agent debate.
6. Produce a verdict with judge/backend/engine provenance, findings, evidence, evidence gaps, and a single recommendation or crown when warranted.

## Personas

Use personas from `personas/` when available:

- Karpathy-inspired Technical Critic: minimal, technical, implementation-first architecture pressure based on public repositories. This synthetic persona is neither authored nor endorsed by Andrej Karpathy and must not impersonate him.
- Knowledge Analyst: source and citation enforcement.
- Systems Architect: maintainability, OSS boundaries, runtime proof.
- Security Auditor: provenance and anti-fake review.
- UI Specialist and Minimalist UI Architect: visual design quality.
- UX Specialist, UX Researcher, Operator Flow UX Reviewer: workflow and usability.

## Anti-Fake Gates

- A claim without a source is `❌` or an explicit blocker, not a pass.
- A weak but partially supported area is `⚠️`.
- A verified capability can be `✅`.
- A comparison has exactly one `👑`; no ties with multiple crowns.
- CSV cells must use bare GitHub URLs, numeric stars, emoji capability cells, and differentiated scores.
- UI/UX claims require visual or interaction evidence; code inspection alone is insufficient.

## Direct Criticism Boundary

“Uncensored” means plain, hard, non-sycophantic criticism. It does not waive factual, legal, privacy, identity, or safety constraints. Never invent evidence, expose secrets, impersonate a real person, or turn confidence into a fake pass. State the defect directly, cite what proves it, and keep uncertainty explicit.

## Library Surface

The Tribunal library is installed locally.

Run an offline orchestration Tribunal:

```bash
python tribunal.py \
  --mode comparison \
  --rounds 2 \
  --hardness hard \
  --target "Tribunal OSS library comparison"
```

The bundled `local-rules` backend reports structural readiness and evidence gaps. Its transparent structural ceiling is 50/100, so its score is never a semantic target rating. For semantic review, inject a `JudgeBackend` that returns `BackendResult` objects and records its real provider/engine provenance. Unique personas plus separate calls do not prove cross-family independence; enforce that in the live backend when required. Supply a NotebookLM URL only after the notebook exists and its source/query ledger has been verified.

Run Phase 1 core modes:

```bash
python examples/phase1_core_modes.py
```

Run the CSV gate:

```bash
python scripts/csv_gate.py report/codex-trib-lib-matrix.csv
```
