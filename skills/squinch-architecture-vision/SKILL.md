---
name: squinch-architecture-vision
description: Build, render and visually validate very large interactive Squinch architecture diagrams as self-contained HTML. Use when the user asks for tribunal-architektur.html, a huge Squinch map, click-to-zoom architecture, Hans/Agent-Concept/OAM/Tribunal system maps, screenshot-based diagram QA, better routing, more colors, or an iterative visual architecture pass.
license: MIT
compatibility: Squinch CLI 0.2.x, Git, a browser capable of headless screenshots, and a host with image/vision inspection for the visual QA loop.
metadata:
  version: "1.0.0"
  canonical_output: "tribunal-architektur.html"
---

# Squinch Architecture Vision

Build the diagram as **Squinch source first** and deliver a **self-contained interactive HTML**. PNG screenshots are QA evidence, never the canonical output.

## Non-negotiable output contract

1. Keep a canonical `.squinch` source in Git or generate it deterministically from a versioned semantic blueprint.
2. Run the real Squinch checker before claiming renderability.
3. Render one self-contained HTML carrying all declared views and the viewer.
4. Render SVG as a deterministic inspection/export companion.
5. Capture screenshots from the HTML itself, not from a mock or a separately redrawn image.
6. Inspect the screenshots with vision and write concrete findings.
7. Fix source/layout/routing problems and rerender. Do not stop after the first visually valid compile.
8. Final delivery includes HTML, source, QA screenshots, visual-QA notes, metrics, commit/PR and known limitations.

## Workflow

### 1. Reconcile before drawing

Read the current branch/PR and all relevant architecture sources. For the Hans ecosystem, inspect only the smallest relevant slices of Hans, Agent-Concept, Omni Audio Matrix, Tribunal, OpenSpec, Matrix/browser surfaces and the current Squinch skill/spec. Preserve concurrent work; never flatten active branches into one speculative truth.

Classify every input as current fact, planned target state, historical/legacy reference, unresolved assumption, or external inspiration. Make current/target/host-responsibility boundaries visible in labels or notes.

### 2. Model semantics before cosmetics

Prefer nested systems/containers over a giant flat graph. Use stable ids as the API. Use top-level systems for semantic zoom and scoped views for internals. Create cross-cutting curated views rather than forcing one unreadable universal canvas to do every job.

Use Squinch's native color vocabulary only: `red`, `amber`, `green`, `teal`, `blue`, `violet`, `pink`, `gray`, `accent`. Color is emphasis, never the only meaning.

### 3. Scale deliberately

A useful large map commonly has 12–30 top-level systems, 50–150 containers, 150–500 leaves, 150–600 meaningful edges and 15–40 declared views. If more detail is needed, split model files inside one Squinch project directory.

Do not make a 100k-line file solely to satisfy a size number. Semantic zoom is the scalability mechanism.

### 4. Route for legibility

Default to orthogonal lines. Use `rows`, `cols`, `place`, `align`, `route` and `channel` only where they materially improve a view. Avoid excessive manual hints that make edits brittle.

Create at minimum landscape, one scoped view per major system, end-to-end delivery flow, control plane, evidence/provenance, security/authority, audio/OAM, Hans knowledge flow, visual architecture QA, enterprise/department lens and a fully expanded engineering view.

### 5. Render and capture

Use `scripts/capture_squinch.sh` or an equivalent host-specific command. Required artifacts are `tribunal-architektur.html`, `tribunal-architektur.svg`, primary-view screenshots, one wide engineering screenshot and one narrow viewer screenshot.

Never claim screenshots were produced if the browser command failed.

### 6. Vision QA loop

Read `references/visual-qa.md`. Inspect every required screenshot with actual image understanding. Record findings using severity P0/P1/P2/P3 and exact view names.

At minimum inspect clipped or ellipsized critical labels, node/card overlap, edge/label collisions, excessive crossings, unreadable hubs, giant empty voids, misleading hierarchy, color imbalance, context cards that dominate scope, legends/notes covering content, missing views and responsive viewer problems.

P0/P1 block delivery. P2 requires a fix or explicit rationale. After changes, rerender the affected view and visually compare again.

### 7. Truthfulness gates

A successful `squinch check` proves syntax/semantic validity, not architecture truth. A screenshot proves rendering, not factual correctness. A beautiful view may still be wrong.

Keep source/architecture evidence, compile/render evidence and visual-QA evidence as separate receipts. Never use an AI-generated poster as evidence that the Squinch HTML is correct.

### 8. Git delivery

Commit the semantic blueprint/source, skill/support files and QA notes. Prefer CI-generated HTML/screenshots as build artifacts when generated output should not live in source control. If the user asks for a downloadable HTML, download the verified CI artifact and hand off that exact file.

When a parent such as Hans pins this skill as a submodule, update the parent Gitlink only after the child commit is final and verified. Keep the parent coverage/pin ledger consistent.

## Reference files

- `references/visual-qa.md` — screenshot matrix, scoring and iteration rules.
- `prompts/mega-diagram.md` — long-running master prompt for exhaustive architecture work.
- `scripts/generate_mega_squinch.py` — deterministic reference mega-model generator.
- `scripts/capture_squinch.sh` — real compiler + browser capture pipeline.

## Done means

The user can open a single HTML file, switch views/themes, click into systems, understand the system at multiple altitudes, and trace important end-to-end paths. The final screenshots have been visually inspected after the last source change, not before it.
