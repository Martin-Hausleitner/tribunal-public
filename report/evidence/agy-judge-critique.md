# Tribunal Verdict — Judge 2: Harsh Critique and Risk

**Engine:** `agy` / `Claude Sonnet 4.6 (Thinking)`  
**Perspective:** Harsh Critique and Risk Tribunal  
**Scope:** `tribunal.py`, `personas/*.json`, `skill/SKILL.md`, tests, gate scripts, examples, README, OpenSpec, NotebookLM IDR  
**Score: 64 / 100 — BLOCK for publication**

## Critical Findings (Publication Blockers)

**C1. Zero commits, no remote, no blob URL.**  
Confirmed by `git status`: the working tree is entirely untracked with no remote configured. Every claim about "the published Tribunal library" is unsupported by any public artifact. This is not a minor gap — it is the primary failure for a project whose release specification requires a verified blob URL.

**C2. The final report and CSV do not exist.**  
`report/codex-trib-lib-tribunal.md` and `report/codex-trib-lib-matrix.csv` are absent. The gate scripts that enforce them are real and working — but they gate on artifacts that haven't been written. The "three independent verdicts," "one crowned winner," and "100-point rubric" are all outstanding deliverables.

## High Findings (Architecture/Correctness)

**H1. `brutal` mode silently repeats personas — README claim is false.**  
Verified by execution: with 9 personas and 4 rounds, offset `9 % 9 = 0` means round 4 is **identical** to round 1. The README states brutal "applies broader persona pressure instead of repeating the same three judges." That claim is factually false. Fix: add at least 13 personas or reword the README truthfully.

**H2. Requested panel rotation is a structural no-op.**  
With exactly 3 requested slugs and `rounds > 1`, `offset % 3 = 0` for every round. All rounds get the same 3 personas. No warning, no test, no documentation covers this.

**H3. Local backend score formula is pseudo-scientific noise.**  
`score = 48 + min(10, len(routed_skills))`. Max achievable: 62/100. The score is a function of skill-list length, not evidence quality. Crown threshold is 80 — the local backend can structurally never award a crown, which is honest but needs clearer documentation.

**H4. `reference_repos` are bare slugs in 8 of 9 personas, including non-existent ones.**  
`google/notebooklm` does not exist as a public GitHub repo. `wikipedia` is not a repository. `PersonaLibrary._load()` validates them only as non-empty strings — no URL enforcement.

**H5. `disclaimer` field is silently dropped from the `Persona` dataclass.**  
The Karpathy persona JSON contains an explicit disclaimer; the `Persona` dataclass does not. It is silently discarded after JSON parsing. A live backend accessing `persona.disclaimer` raises `AttributeError`. The identity-safety protection is documentation-only, not runtime-enforced.

## Medium Findings (Abuse Surfaces)

**M1. Target string embeds verbatim in Markdown — injection surface.**  
Verified: `'<script>alert(1)</script>'` appears in the H1 header unchanged. Any downstream HTML renderer is vulnerable. Fix: two lines of escaping.

**M2. Panel selection is fully deterministic and publicly predictable.**  
CRITIQUE mode always produces `['andrej-karpathy', 'security-auditor', 'systems-architect']`. Exploitable for prompt-tuning with live backends.

**M3. No max-rounds, no max-target-length, no budget ceiling.**  
Default engine capacity is `None` (unlimited). `rounds=100` would invoke a live backend 300 times without any guard.

**M4. Stars column in CSV gate accepts `0` or `1` — no plausibility check.**  
Format enforced, plausibility not. Fabricated star counts pass validation.

## Low Findings

**L1.** No linting or static type checking. `py_compile` catches only syntax errors.  
**L2.** The `andrej-karpathy` slug appears verbatim in all JSON outputs — reputational and identity-safety risk at publication.  
**L3.** `_debate` synthesis produces template boilerplate with the local backend — structurally looks like real debate, delivers nothing semantic.  
**L4.** `SKILL.md` conflates skill-name routing labels with callable installed capabilities.

## Score: 64 / 100

| Dimension | Max | Score |
|---|---:|---:|
| Type Fit | 25 | 19 |
| Adversarial Depth | 20 | 10 |
| Evidence Provenance | 20 | 12 |
| Persona/Skill Extensibility | 15 | 10 |
| Observability/Repeatability | 10 | 6 |
| Integration Cost | 10 | 7 |

## Recommendation: BLOCK → Ship With Conditions

The library core design is honest and well-tested. The backend contract is clean. But the release specification promises a published report, three external verdicts, a scored CSV, a blob URL, and a crowned winner — none of which exist at snapshot time.

**10 prioritized actions:** (1) commit and push, (2) write and gate the report and CSV, (3) fix brutal rotation documentation, (4) fix `reference_repos` format/fictional entries, (5) add `disclaimer` to `Persona` dataclass, (6) rename `andrej-karpathy` slug, (7) sanitize target for Markdown injection, (8) add max-rounds/max-length guards, (9) add `ruff` to gates, (10) document requested-panel rotation no-op.

I did not inspect any other Tribunal judge output.
