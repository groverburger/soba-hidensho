# DEPRECATED — Phase 2 vision-LLM transcription

The files in this folder are a vision-LLM transcription of the manuscript
images, produced by a multimodal LLM (Claude Opus 4.6) reading the JPGs
directly. They contained many `(?)`-marked uncertain readings and, in
places where readings were filled in, interpolations from the English
translation rather than direct character-by-character readings of the
cursive.

**As of 2026-04-14, superseded by mechanical OCR.**

The authoritative transcription is now the output of [NDL 古典籍OCR-Lite](https://github.com/ndl-lab/ndlkotenocr-lite)
(National Diet Library, Japan — *koten OCR lite*: an RTMDet text-region
detector + PARSeq recognizer trained on Edo-period and earlier classical
Japanese texts), applied directly to the manuscript JPGs. See
`../../transcription/` for the per-page text (`.txt`), bounding boxes and
confidences (`.json`), layout XML (`.xml`), and TEI-P5 (`_tei.xml`).

To regenerate: `./ocr.sh sanen-kinsen-hiroku` from the project root.

This folder is retained for historical reference only — it documents the
Phase 2 method and the failure modes that motivated the move to a
specialist OCR pipeline. **Do not treat it as a source of truth.**
