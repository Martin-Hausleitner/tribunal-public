# Brand, colour and layout guide for Squinch mega diagrams

This guide records the reusable public rules. Re-check upstream Squinch before long runs; do not treat this file as a fork of the grammar.

## Current upstream baseline checked 2026-09-05

Squinch workspace version: 0.2.0. Dark is the default render theme; interactive HTML bundles light and dark. Current distribution exposes five packs with roughly 1,313 icons overall. The Lookbook covers 36 reference cases including dense meshes, logos, channels, full detail, coplanar frames, rows/cols and colour lenses.

## Native colour vocabulary

Only use:

`red amber green teal blue violet pink gray accent`

Never use hex in `.squinch` source. The nine hues are paired for light/dark themes. Use colour as annotation, not as the sole meaning.

### Stable domain colour suggestions

- `accent`: human/operator, authoritative lifecycle spine
- `blue`: Git, runtime, execution, browser, infrastructure
- `green`: durable knowledge, accepted/reusable components
- `violet`: orchestration, agents, Matrix, providers/variants
- `amber`: audio, conditions, rollout, resource pressure
- `pink`: Tribunal, evidence, visual review, human correction
- `teal`: research, OpenSpec, observability, semantic processing
- `red`: security, veto, blockers, destructive authority
- `gray`: projections, legacy, archives, supporting history

### Truth/status lens

Prefer tags plus view-level colours:

```squinch
view truth {
  include *
  color #current green
  color #target blue
  color #variant violet
  color #research teal
  color #conditional amber
  color #hold red
  color #projection gray
  color #review pink
  color #authoritative accent
  legend auto
}
```

This keeps status separate from each system's normal domain colour.

## Brands

Use `pack logos` only for marks that the installed pack really contains. Current curated examples useful to this ecosystem include:

- source/CI: `logos/github`, `logos/gitlab`, `logos/git`, `logos/githubactions`, `logos/bitbucket`, `logos/jenkins`, `logos/circleci`, `logos/sonarqube`, `logos/renovate`
- UI/runtime: `logos/react`, `logos/nextdotjs`, `logos/typescript`, `logos/javascript`, `logos/python`, `logos/rust`, `logos/go`, `logos/swift`, `logos/kotlin`, `logos/dotnet`
- platform: `logos/docker`, `logos/kubernetes`, `logos/terraform`, `logos/ansible`, `logos/cloudflare`, `logos/vercel`, `logos/googlecloud`, `logos/helm`
- data/storage: `logos/postgres`, `logos/redis`, `logos/sqlite`, `logos/clickhouse`, `logos/neo4j`, `logos/minio`, `logos/ceph`
- observability: `logos/grafana`, `logos/prometheus`, `logos/opentelemetry`, `logos/datadog`, `logos/sentry`, `logos/jaeger`
- collaboration/services: `logos/discord`, `logos/zoom`, `logos/atlassian`, `logos/jira`, `logos/google`, `logos/apple`

The curated pack intentionally does not contain every trademark. If a product such as Microsoft/Copilot, Notion, Spotify, OpenAI/ChatGPT, Anthropic/Claude, Matrix or another requested brand has no verified installed id, use a generic `sys/*` icon or `box`. Never copy an arbitrary logo from the web into this public skill.

For vendor platforms with no redistributable native icon set, compose a generic capability with a verified brand badge only when the brand mark exists:

```squinch
warehouse = sys/database "Warehouse" {
  badge: logos/databricks
}
```

## Useful 0.2.0 icon search

Before guessing icons, batch queries:

```sh
squinch icons search "agent, brain, audio, vision, security, database, workflow, browser"
```

The 0.2.0 sys pack specifically added AI-friendly concepts/aliases such as GPU, brain/brain-cog, chatbot/bot-message-square, database-search, file-search, memory-stick, target/eval, scan-text/OCR, audio-lines/TTS and image/vision.

## Card language

Use a top-level system as a semantic-zoom card. Improve collapsed cards with:

```squinch
system example "Example" {
  glyph: sys/workflow
  domain: "delivery"
  preview: auto
}
```

Provider/product icons belong mainly on leaves. Landscape identity comes from card shape, label, glyph, domain and colour — not dozens of brand marks at once.

## Layout progression

1. Model edges first, no layout.
2. Render and inspect.
3. Use `context off` if a focused view is swamped by neighbours.
4. Use `rows` to establish semantic ranks.
5. Add `cols` when a true grid is useful.
6. Use `channel` for a many-to-one/one-to-many trunk.
7. Use `route ... from ... to ...` for a specific stubborn edge.
8. Use `place`/`align` sparingly.

Do not globally freeze a large model with manual constraints.

## View pattern library

A mega map should have several altitudes:

- landscape: collapsed top-level systems, calm and clickable
- system detail: `scope system`, optionally `expand *`, usually `context off`
- truth lens: same systems coloured by CURRENT/TARGET/VARIANT/HOLD
- flow lens: `show flow ...` on only the involved systems
- department lens: business function → systems/processes
- branch observatory: repository branches/PR variants, never mixed with runtime truth
- visual QA: source → check → render → HTML → browser screenshots → vision → fix → rerender
- engineering core: intentionally dense expanded subset
- all systems: top-level cards only; do not use one giant full-leaf raster as the only navigation method

## Dark-mode QA

The final interactive HTML should open in dark mode when using the 0.2.x default. Visual QA must inspect contrast, coloured spines/edges, muted context, brand plates, notes, legends and selected/highlighted states. A light companion render is useful for detecting palette-specific problems, but dark is the primary user-facing baseline for this skill.
