# Visual QA for Squinch HTML

## Screenshot matrix

Capture the actual self-contained HTML after the last source change.

Required desktop views at 1920×1080 or larger:
- landscape
- tribunal
- hans
- agent
- oam
- endtoend
- visualqa
- everything

Also capture:
- landscape at 2560×1440 or larger;
- one compact 1280×800 viewer screenshot;
- one narrow 430×932 viewer screenshot to inspect chrome/tabs, even if the architecture canvas itself is intentionally desktop-first.

## Review rubric

Score each screenshot 0–3 for each dimension.

- **Hierarchy:** can the eye find the primary system and understand grouping?
- **Routing:** are major flows traceable without hunting through crossings?
- **Density:** is information dense but still locally readable?
- **Typography:** are critical labels intact and readable?
- **Color:** are neighboring concerns distinguishable without rainbow noise?
- **Whitespace:** neither cramped nor dominated by empty space?
- **Context:** do external/context cards support rather than overwhelm the scope?
- **Navigation:** are view tabs/breadcrumb/zoom cues usable?
- **Truth cues:** are target/current/host responsibilities and non-authority boundaries explicit?

Total score target: 23/27 or better for primary views. `everything` may score lower on density because it is intentionally exhaustive, but it must not have P0/P1 defects.

## Severity

- **P0:** content missing, wrong view, broken viewer, unrendered source, critical semantic misrepresentation.
- **P1:** critical label clipped, major overlap, central flow impossible to trace, large off-canvas region, legend blocks key content.
- **P2:** avoidable crossings, awkward whitespace, local density spike, weak color separation, minor clipped noncritical label.
- **P3:** polish: wording, spacing, note placement, aesthetic balance.

P0/P1 block delivery. P2 requires fix or documented reason. P3 may be deferred.

## Iteration discipline

1. Capture screenshots.
2. Inspect with vision.
3. Write findings before editing.
4. Map each finding to source id/view/layout rule.
5. Make the smallest semantic/layout change.
6. Run `squinch check` again.
7. Rerender HTML/SVG.
8. Recapture affected screenshots.
9. Compare against previous screenshots.
10. Repeat until gates pass.

Never "fix" a routing problem by falsifying architecture relationships. Prefer view selection and layout hints over deleting truthful edges.
