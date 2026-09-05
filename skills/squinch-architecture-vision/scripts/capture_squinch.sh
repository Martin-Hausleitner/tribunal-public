#!/usr/bin/env bash
set -euo pipefail

SOURCE=${1:-build/mega/tribunal-mega.squinch}
OUT=${2:-build/architecture}
SQUINCH_VERSION=${SQUINCH_VERSION:-0.2.0}
mkdir -p "$OUT/screenshots"

if command -v squinch >/dev/null 2>&1; then
  SQ=(squinch)
else
  SQ=(npx --yes "squinch@${SQUINCH_VERSION}")
fi

"${SQ[@]}" check "$SOURCE"
"${SQ[@]}" render "$SOURCE" -o "$OUT/tribunal-architektur.html"
"${SQ[@]}" render "$SOURCE" -o "$OUT/tribunal-architektur.svg"

CHROME=""
for c in google-chrome google-chrome-stable chromium chromium-browser; do
  if command -v "$c" >/dev/null 2>&1; then CHROME=$(command -v "$c"); break; fi
done
if [[ -z "$CHROME" ]]; then
  echo "browser capture unavailable: Chrome/Chromium not found" >&2
  exit 3
fi

HTML="file://$(python3 - <<'PY' "$OUT/tribunal-architektur.html"
from pathlib import Path
import sys
print(Path(sys.argv[1]).resolve())
PY
)"

capture() {
  local view=$1 width=$2 height=$3 suffix=$4 budget=${5:-5000}
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-dark-mode \
    --window-size="${width},${height}" --virtual-time-budget="$budget" \
    --screenshot="$OUT/screenshots/${view}-${suffix}.png" \
    "${HTML}#${view}" >/dev/null 2>&1
}

# Focused detail views: horizontal internals, no auto-context.
for view in tribunal hans agent oam; do
  capture "$view" 1920 1400 desktop 6000
done

# Curated cross-system views.
for view in endtoend visualqa; do
  capture "$view" 1920 1400 desktop 6000
done

# Primary navigation altitude and responsive viewer chrome.
capture landscape 1920 1200 desktop 5000
capture landscape 2560 1440 wide 5000
capture landscape 1280 800 compact 5000
capture landscape 430 932 narrow 5000

# All top-level systems should remain readable; engineeringcore intentionally expands internals.
capture everything 2560 1600 desktop 7000
capture engineeringcore 2560 3000 deep 12000

python3 - <<'PY' "$OUT"
from pathlib import Path
import hashlib, json, sys
root=Path(sys.argv[1])
files=[]
for p in sorted(root.rglob('*')):
    if p.is_file():
        files.append({"path":str(p.relative_to(root)),"bytes":p.stat().st_size,
                      "sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'artifact-manifest.json').write_text(json.dumps({"files":files}, indent=2)+'\n')
print(json.dumps({"artifact_count":len(files),"output":str(root)}, indent=2))
PY
