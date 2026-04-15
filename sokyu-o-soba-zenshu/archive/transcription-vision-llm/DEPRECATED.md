# DEPRECATED — Phase 2 vision-LLM transcription

The files in this folder are a vision-LLM transcription of the manuscript
images for *Sōkyū-ō Sōba Zenshū* (宗久翁相場全集), produced by a
multimodal LLM (Claude Opus 4.6) reading the JPGs directly. They share
the same failure modes documented for the *Sanen Kinsen Hiroku* Phase 2
transcription: `(?)`-marked uncertain readings and occasional
interpolation from the English translation rather than direct
character-by-character readings of the cursive.

**As of 2026-04-15, superseded by mechanical OCR.**

The authoritative transcription is now the output of [NDL 古典籍OCR-Lite](https://github.com/ndl-lab/ndlkotenocr-lite)
applied to `../../original-manuscript/`. See `../../transcription/`.

To regenerate: `./ocr.sh sokyu-o-soba-zenshu` from the project root.

This folder is retained for historical reference only. **Do not treat
it as a source of truth.**
