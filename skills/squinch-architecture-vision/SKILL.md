---
name: squinch-architecture-vision
description: Build, render and visually validate very large interactive Squinch architecture diagrams as self-contained HTML. Use for tribunal-architektur.html, Hans/Agent-Concept/OAM/Tribunal mega maps, architecture deep-research, branch/variant maps, brand/icon-rich dark-mode diagrams, screenshot-based QA, routing repair, or iterative visual architecture work.
license: MIT
compatibility: Squinch CLI 0.2.x, Git, Chromium/Chrome, and a host with image/vision inspection.
metadata:
  version: "1.1.0"
  canonical_output: "tribunal-architektur.html"
  render_truth: "squinch-source"
---

# Squinch Architecture Vision

Build **Squinch source first** and deliver a **self-contained interactive HTML**. PNG screenshots are QA evidence, never the canonical output.

## Mandatory preflight — official upstream first

Before editing a large diagram, inspect the current official Squinch release, `CHANGELOG.md`, upstream `SKILL.md`, `docs/SPEC.md`, and the Lookbook cases relevant to the requested visual problem. Never rely only on an older copied grammar note.

For Squinch 0.2.x, explicitly exploit the features that fit the model: dark/light paired themes, semantic zoom, `scope`, `expand`, `only`, `context off`, flows, zones, `rows` + `cols`, `route`, `channel`, `glyph`, `domain`, `preview`, titleblocks, notes, tag lenses and the five icon packs. Batch unknown icon lookups with `squinch icons search "term, term, ..."` instead of guessing ids.

Read `references/brand-color-layout.md` before any visual polish pass.

## Non-negotiable output contract

1. Keep canonical `.squinch` source in Git or generate it deterministically from a versioned semantic blueprint.
2. Run the real Squinch checker before claiming renderability. Warnings are defects unless explicitly justified.
3. Render one self-contained HTML carrying all declared views and the viewer; start in dark mode when that is the user preference.
4. Render SVG as deterministic inspection/export companion; optionally render a paired light-theme landscape for contrast checks.
5. Capture screenshots from the HTML itself, not from a mock, image generator or separately redrawn diagram.
6. Inspect screenshots with actual vision and write concrete findings.
7. Fix source/layout/routing problems and rerender. Never stop after the first visually valid compile.
8. Final delivery includes HTML, source/blueprint, QA screenshots, visual-QA notes, metrics, source map, commit/PR and known limitations.

## Workflow

### 1. Reconcile current truth, variants and research

Read current default-branch heads first, then recent commits, open PRs and relevant branches. Preserve concurrent work; never flatten every active branch into one speculative truth.

Classify every input as `CURRENT`, `TARGET`, `VARIANT`, `RESEARCH`, `LEGACY`, `HOLD`, `EXTERNAL` or `ASSUMPTION`. Encode that classification in tags, views and source receipts. A branch can be visible without being treated as merged.

For private hosts, keep branch names, internal source links and private architecture content in a private repository. This public skill may contain reusable mechanics and synthetic reference models only.

### 2. Model semantics before cosmetics

Prefer nested systems/containers over a giant flat graph. Stable ids are the API. Top-level systems define semantic altitude; scoped views open internals. Cross-cutting curated views tell stories without forcing one canvas to do every job.

Use source ids in descriptions or companion `SOURCE-MAP.md` rather than inventing arbitrary external-link syntax. Native Squinch links are internal view/zoom links; do not hand-patch generated HTML to add unsupported behavior.

### 3. Color deliberately, not decoratively

Use only Squinch's adaptive color vocabulary: `red`, `amber`, `green`, `teal`, `blue`, `violet`, `pink`, `gray`, `accent`.

Use element colors for stable domain identity and **tag color lenses** for truth/status views. Recommended truth lens:

- `#current` → green
- `#target` / `#planned` → blue
- `#variant` → violet
- `#research` / `#idea` → teal
- `#conditional` → amber
- `#hold` / `#blocked` → red
- `#projection` / `#legacy` → gray
- `#human` / `#review` → pink
- `#authoritative` → accent

Color must never be the only carrier of meaning.

### 4. Use real brands where the installed pack actually has them

Prefer verified `logos/*` marks for products such as GitHub, GitLab, Git, GitHub Actions, React, Docker, Kubernetes, PostgreSQL, Redis, Grafana, OpenTelemetry, Discord, Zoom, Google and Apple. Use `badge:` when a generic capability plus vendor mark communicates better than a brand-only node.

If a requested brand is absent from the installed pack, use a suitable `sys/*` icon or `box` and keep the product name as text. Never fabricate an icon id, vendor SVG or trademark asset.

### 5. Scale deliberately

For a true ecosystem mega-map, 25–40 top-level systems, 120–220 containers, 500–1,000 leaves, hundreds of meaningful relations and 30–70 curated views are acceptable when evidence supports them. If rendering cost becomes excessive, move domain data into a Squinch project directory and keep cross-system story views curated.

Do not create 100k meaningless lines for a vanity metric. Semantic zoom, source maps and branch/variant lenses are the scaling mechanisms.

### 6. Route for legibility

Start with auto-layout. Default to orthogonal lines. Add `rows`, `cols`, `place`, `align`, `route` and `channel` only after a screenshot proves a concrete routing problem.

Use `context off` for focused inspection views when auto-context overwhelms the scope. Use `rows` + `cols` for real grids. Use `channel` for many-to-one buses. Prefer separate views over deleting truthful relations.

### 7. Mandatory architecture lenses

At minimum create: calm landscape, current-vs-target truth lens, one scoped view per major system, end-to-end delivery, control/authority, durable workflow/PR, Git/merge-conflict, MCP/A2A/platform interop, IDR/deep research, evidence/provenance, security/privacy, secrets/access, OAM daily capture, OAM ASR/speaker intelligence, OAM revision/review/archive, Matrix/RTC realtime, Hans knowledge flow, branch/variant observatory, recent-change observatory, company/departments, device/host fabric, visual architecture QA, and an exhaustive engineering lens.

### 8. Render and capture

Use `scripts/capture_squinch.sh` or an equivalent host command. Produce `tribunal-architektur.html`, `tribunal-architektur.svg`, screenshot matrix, artifact manifest and source map. Never claim a screenshot exists if Chromium failed.

Avoid one unbounded gigantic raster. Extremely tall Chromium screenshots can return blank output. Use scoped views and several reliable screenshots instead; the self-contained HTML remains the full canonical artifact.

### 9. Vision QA loop

Read `references/visual-qa.md`. Inspect every required screenshot with vision. Record P0/P1/P2/P3 findings against exact view/source ids.

Inspect clipped labels, overlap, edge-label collision, crossings, routing through cards, tiny auto-fit scale, giant gaps, weak color separation, misleading hierarchy, overdominant context cards, viewer/tab overflow, dark-mode contrast, excessive brand noise, false CURRENT/TARGET cues and missing navigation paths.

P0/P1 block delivery. P2 requires a fix or explicit rationale. After source changes, rerender and recapture affected views.

### 10. Truthfulness and independent review

A clean compile proves syntax/layout constraints, not architecture truth. A screenshot proves rendering, not factual correctness. Keep source evidence, render evidence and visual-QA evidence separate.

Where the host can run real independent reviewers, use separate architecture, evidence, security, visual-legibility and owner-fidelity reviews. If no subagent/reviewer runtime exists, do not claim one; perform clearly separated domain passes and leave the independent-review gate explicit.

### 11. Git delivery

Public reusable mechanics live here. Private mega-models live in the owning private architecture repository and may pin this skill by exact Gitlink. Update parent pins only after the child commit is final and verified. Keep coverage/pin ledgers consistent.

## Reference files

- `references/brand-color-layout.md` — official feature/brand/color policy and lookbook patterns.
- `references/visual-qa.md` — screenshot matrix, scoring and iteration rules.
- `prompts/mega-diagram.md` — long-running exhaustive architecture prompt.
- `scripts/generate_mega_squinch.py` — synthetic public reference generator.
- `scripts/capture_squinch.sh` — real compiler + browser capture pipeline.

## Done means

The user can open one HTML file, start in a readable dark landscape, switch views/themes, click into systems, trace end-to-end flows, inspect CURRENT/TARGET/VARIANT differences, and reach every dense subsystem through semantic zoom. The final screenshots were visually inspected **after the final source change**.
