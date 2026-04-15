#!/usr/bin/env bash
# Run NDL 古典籍OCR-Lite (github.com/ndl-lab/ndlkotenocr-lite) on a book's
# manuscript images.
#
# Usage:
#   ./ocr.sh <book>                         # all pages in <book>/original-manuscript/
#   ./ocr.sh <book> <filename>              # single page (full filename)
#
# <book> must be a directory at the project root containing
#   original-manuscript/ (source JPGs) and transcription/ (destination).
#
# Examples:
#   ./ocr.sh sanen-kinsen-hiroku
#   ./ocr.sh sanen-kinsen-hiroku page_00004.jpg
#   ./ocr.sh sokyu-o-soba-zenshu
#   ./ocr.sh sokyu-o-soba-zenshu 0010_0000.jpg
#
# Output goes to <book>/transcription/ as {basename}.txt (plain),
# .json (with bboxes + confidences), .xml (layout), and _tei.xml (TEI-P5).

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOL="/Users/grob/Documents/projects/japanese-ocr-tool/ndlkotenocr-lite"
PY="$TOOL/.venv/bin/python3"
SRC="$TOOL/src"

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <book> [filename]" >&2
  echo "  where <book> is a directory at the project root with original-manuscript/" >&2
  exit 1
fi

BOOK="$1"
IN="$HERE/$BOOK/original-manuscript"
OUT="$HERE/$BOOK/transcription"

if [[ ! -d "$IN" ]]; then
  echo "error: $IN does not exist" >&2
  exit 1
fi

mkdir -p "$OUT"

if [[ $# -eq 1 ]]; then
  cd "$SRC" && "$PY" ocr.py --sourcedir "$IN" --output "$OUT"
else
  cd "$SRC" && "$PY" ocr.py --sourceimg "$IN/$2" --output "$OUT"
fi
