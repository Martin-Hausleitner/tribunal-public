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
  local view=$1 width=$2 height=$3 suffix=$4 budget=${5:-6000}
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-dark-mode \
    --window-size="${width},${height}" --virtual-time-budget="$budget" \
    --screenshot="$OUT/screenshots/${view}-${suffix}.png" \
    "${HTML}#${view}" >/dev/null 2>&1
}

# Focused detail views: 2x2 subsystem grids, no auto-context.
for view in tribunal hans agent oam; do
  capture "$view" 1920 1800 desktop 7000
done

# Curated cross-system views need enough height to cover all ranks.
capture endtoend 1920 2400 desktop 8000
capture visualqa 1920 1600 desktop 7000

# Primary navigation altitude and responsive viewer chrome.
capture landscape 1920 1800 desktop 7000
capture landscape 2560 2200 wide 7000
capture landscape 1280 1000 compact 7000
capture landscape 430 932 narrow 7000

# All top-level systems remain readable; engineeringcore intentionally expands internals.
capture everything 2560 2000 desktop 8000
capture engineeringcore 2560 5600 deep 15000

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
