<p align="center">
  <img src="assets/logo.png" alt="Soba Hidensho (相場秘伝書)" width="640">
</p>

<p align="center"><em>First English translations of two Edo-period Japanese rice-trading manuscripts.</em></p>

---

This repository hosts the first English translations of two Edo-period Japanese texts on rice-market speculation. Both belong to a genre traders called *soba hidensho* (相場秘伝書), or "secret market transmissions": family-property manuscripts, hand-copied in cursive *kuzushiji* script that most readers today cannot decipher, and circulated only among merchant networks. The genre was designed to stay within a single world of meaning. One of the texts even has a chapter titled 此書、他見無用の事, "This Book Must Not Be Shown to Others."

Three centuries later, the manuscripts sit in digital archives. Freely available in principle, sealed in practice: a cursive script that most readers cannot decipher even in Japanese, plus a classical language few specialists outside Japan translate. The Western trading literature has consequently been confused about who wrote what for roughly thirty-five years, since these texts first surfaced in English in the late 1980s. The translations published here are an attempt to address that gap.

## The two books

The two volumes represent the two independent traditions of the *soba hidensho* corpus, distinguished clearly in Japanese scholarship but conflated in English-language sources since the early 1990s.

**[sanen-kinsen-hiroku/](./sanen-kinsen-hiroku/)** &nbsp;·&nbsp; *Sanen Kinsen Hiroku* (三猿金泉秘録), "Three Monkeys Gold Spring Secret Record."

Attributed to Ushida Gonzaburō (牛田権三郎) and revised by Narukawa Takenosuke (鳴川猛之助). The 1851 manuscript translated here is held at Kyoto University, Tanimura Collection (RB00012360). Western trading books since Nison's *Japanese Candlestick Charting Techniques* (1991) have attributed this text to Honma Munehisa, the legendary Sakata trader. The manuscript itself names a completely different author from a completely different lineage: Ushida, an Osaka Dōjima trader from Ise province. The book's translator's introduction lays out the case in full.

**[sokyu-o-soba-zenshu/](./sokyu-o-soba-zenshu/)** &nbsp;·&nbsp; *Sōkyū-ō Sōba Zenshū* (宗久翁相場全集), "Complete Collected Works on Markets by Master Sōkyū."

This text *is* Honma's tradition. Honma Sōkyū (1717–1803) was a Sakata rice trader whose methods on the Osaka Dōjima and Sakata exchanges are considered among the earliest systematic approaches to market analysis anywhere. The edition translated here is the 1910 Hayasaka Nikiku collation published by Shingidō in Tokyo, scanned and held by the National Diet Library (pid/804042). 158 articles across two volumes, with extensive Meiji-era commentary alongside Honma's original aphorisms.

## Method

Translation proceeds in two stages, deliberately kept separate.

**1. OCR.** Manuscript page JPGs are passed through [NDL 古典籍OCR-Lite](https://github.com/ndl-lab/ndlkotenocr-lite), a *kuzushiji* OCR toolchain released by Japan's National Diet Library (RTMDet for text-region detection, PARSeq for character recognition, both as ONNX). CPU-only, no GPU required. Output lands in `<book>/transcription/` as per-page `.txt`, `.json` (bounding boxes and per-character confidences), `.xml` (layout), and TEI-P5. Run it with:

```bash
./ocr.sh sanen-kinsen-hiroku
```

**2. Translation.** Claude Opus 4.6 (via Claude Code) reads the OCR transcription and produces the English in `<book>/translation/`. The model consults the manuscript images only to sanity-check OCR artifacts, never as the primary input.

### Why two stages

An earlier iteration of the pipeline used a single multimodal model to read the cursive page and emit English in one pass. The output read fluently, but the approach concealed a silent failure mode: when the model could not in fact read a character, it would interpolate a confident-looking reading from surrounding context, sometimes back-translating from its own prior English output of the same passage. Uncertainty did not survive the vision pass; illegibility was smoothed over rather than flagged.

Splitting the pipeline restores that signal. The OCR stage can only see pixels and cannot invent a character based on context, because it has no context. When the OCR fails, the translation stage sees a clearly mis-OCRd character and flags it. The earlier vision-LLM versions of both books are preserved in each book's `archive/` folder, labeled DEPRECATED, as a record of the failure mode.

## Repository layout

```
.
├── README.md                       # this file
├── assets/                         # logo and shared images
├── ocr.sh                          # OCR wrapper: ./ocr.sh <book>
├── sanen-kinsen-hiroku/            # Book 1 (see its own README)
│   ├── original-manuscript/        #   page JPGs
│   ├── transcription/              #   NDL OCR output
│   ├── translation/                #   English translation + STYLE.md
│   ├── typeset/                    #   LaTeX, PDF, covers, figures
│   └── archive/                    #   DEPRECATED earlier passes
├── sokyu-o-soba-zenshu/            # Book 2 (same shape)
└── reference/                      # gitignored: third-party PDFs
```

## OCR setup

The wrapper expects a Python venv at `~/japanese-ocr-tool/ndlkotenocr-lite/.venv`. To recreate:

```bash
git clone https://github.com/ndl-lab/ndlkotenocr-lite ~/japanese-ocr-tool/ndlkotenocr-lite
cd ~/japanese-ocr-tool/ndlkotenocr-lite
python3 -m venv .venv
.venv/bin/pip install onnxruntime pillow numpy pyyaml lxml reportlab \
                     networkx dill ordered-set pyparsing tqdm pypdfium2 protobuf
```

The two ONNX model files (~80 MB total) ship with the upstream repository at `src/model/`. Tested on Intel Mac, Apple Silicon, Windows, and Linux.

## Status and corrections

Both translations are usable. Neither has been verified character-by-character against the manuscript by a trained *kuzushiji* specialist, and the project makes no such claim. The function of the audit trail (manuscript images, OCR with per-character confidences, translation files, and the full Claude Code conversation transcripts) is precisely to support that verification: any specialist who wishes to check the work can do so directly against the published evidence.

The translations are intended not as a replacement for expert scholarship but as an access enabler: a first rendering that opens the archive and invites correction. Corrections are welcome via GitHub Issues.
