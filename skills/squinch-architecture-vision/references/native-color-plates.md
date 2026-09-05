# Native semantic colour plates — 2026-09-05

## Evidence

Read upstream Squinch `docs/SPEC.md`, `docs/DESIGN.md`, the official Skill and `packages/core/src/packs/registry.ts` at snapshot `d0abb9eee77463ebaf95ddb0bfaa46121547b3f1`. The installed compiler is the published `squinch@0.2.0`, not a locally modified build. Official examples were rendered and screenshotted before source changes.

The DSL accepts nine named hues, not hex values. The public pack contract separately accepts `monochrome` and per-icon `color` metadata. The exported `registerPack(manifest, loader)` API lets a host register a native pack explicitly. Do not assume that a `pack ... from` declaration alone automatically loads a disk pack in every host.

## Pattern

1. Install the approved pinned Squinch distribution into an isolated dependency directory.
2. Run `native_color_pack.py` against the model and that distribution's `@squinch/pack-sys` directory.
3. Keep `icon_original` and the generated per-asset SHA-256 proof.
4. Declare `pack atlas from "./icons/atlas"` in the generated source.
5. Set `SQUINCH_NODE_MODULES` to the approved dependency directory's node_modules and `SQUINCH_ATLAS_PACK` to the generated pack.
6. Invoke Node with `--import scripts/register_color_pack.mjs`, followed by the ordinary Squinch CLI entrypoint and its normal check/render arguments.

Example (paths are host choices, not installed global defaults):

```sh
python native_color_pack.py model/architecture.json vendor/node_modules/@squinch/pack-sys icons/atlas
SQUINCH_NODE_MODULES="$PWD/vendor/node_modules" \
SQUINCH_ATLAS_PACK="$PWD/icons/atlas" \
node --import ./register_color_pack.mjs \
  ./vendor/node_modules/squinch/bin/squinch.js check architecture.squinch
```

The host registration changes no renderer source. SVG artwork is copied byte-for-byte from the pinned ISC-licensed generic pack. Only model icon references and the new pack's JSON colour metadata change. Installed vendor packs, generated HTML and native font files are not edited. Do not distribute standalone font files with skill bundles.

## Colour selection

Use the native light-palette hue values for colour plates with white knockout marks: red `#B5544C`, amber `#A06B12`, green `#3F8A5C`, teal `#1F8A80`, blue `#3A6EA8`, violet `#6B5FC9`, pink `#B04A8A`, gray `#7A776E`, accent `#5A57C9`. These are pack metadata, NOT DSL hex syntax. Verify actual dark-canvas readability by screenshots; this note is not a blanket accessibility certification.

In the private atlas test, 264 icon/hue variants were built from unchanged artwork. That number is a particular model's output, not an upstream icon-count claim. Native product marks stayed unchanged; absent brands received generic icons, not guessed logo IDs.

## Observed layout lessons

A long left-to-right chain at Fit became tiny despite valid compilation. An eight-stage IDR layout improved with three downward row groups. The audio pipeline improved after separating capture, analysis, revision and retention groups. Excessive auto-context was removed from focused views without deleting model relations. Global rank grids caused real upward-edge constraint errors; the fix was to remove those hints, not disable the checker.

A huge complete index remains a navigation/zoom surface. Its pixels must never be used as proof of detailed readability. Native flow presentations are planned story steps unless connected to independently verified real events.
