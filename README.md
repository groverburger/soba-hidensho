# Edo-Period Japanese Rice-Trading Manuscripts — English Translations

This repository houses two translation projects covering Edo-period (and
earlier) Japanese texts on the art of rice-market speculation. Each book
is a self-contained subdirectory with its own source manuscript,
transcription, English translation, and typeset edition.

## Books

### [sanen-kinsen-hiroku/](./sanen-kinsen-hiroku/) — 三猿金泉秘録

*The Three Monkeys Gold Spring Secret Record* — attributed to Ushida
Gonzaburō (牛田権三郎), revised by Narukawa Takenosuke (鳴川猛之助),
published 1851. The first English translation of the actual text under
this title, which Western trading literature has for decades misattributed
to Honma Munehisa. Source manuscript: RB00012360, Tanimura Collection,
Kyoto University. See that folder's README for the full scholarly case.

### [sokyu-o-soba-zenshu/](./sokyu-o-soba-zenshu/) — 宗久翁相場全集

*The Complete Collection of the Elder Sōkyū on the Market* — a second
translation project in progress.

## Method

Translation is a two-stage pipeline:

1. **Transcription — mechanical OCR.** Source manuscript JPGs are passed
   through [NDL 古典籍OCR-Lite](https://github.com/ndl-lab/ndlkotenocr-lite),
   a specialist toolchain released by Japan's National Diet Library
   (RTMDet text-region detection + PARSeq character recognition, ONNX,
   CPU-only). The OCR step is purely mechanical — the model does not
   know the English translation exists and cannot interpolate from
   context it doesn't have. Run:

   ```bash
   ./ocr.sh sanen-kinsen-hiroku     # or sokyu-o-soba-zenshu
   ```

   Output lands in `<book>/transcription/` as per-page `.txt` / `.json`
   (bboxes + confidences) / `.xml` (layout) / `_tei.xml` (TEI-P5 batch).

2. **Translation — LLM from the OCR text.** Claude Opus 4.6 (via Claude
   Code) reads the mechanical transcription and produces English
   translations under `<book>/translation/`, with manuscript images
   consulted only to sanity-check OCR artifacts — not as the primary
   input to the LLM.

### Why this method

An earlier version of the pipeline used an LLM to read the cursive
manuscript pages *directly*. This worked in a narrow sense — the model
produced fluent-sounding Japanese — but introduced a silent failure
mode: when a character was genuinely illegible, the LLM would interpolate
a confident-looking reading, sometimes back-translating from its own
prior English translation of the same passage. Uncertainty did not
survive the vision pass. Separating mechanical OCR from language-model
translation fixes this: the OCR step can only see pixels, not meaning,
so what it can't read becomes visibly mis-OCRd rather than invisibly
smoothed over. The earlier vision-LLM transcriptions and translations
for both books are preserved in each book's `archive/` folder as
`DEPRECATED` artifacts — they document the failure modes as well as
the shift.

## Repository layout

```
.
├── README.md                       # this file
├── ocr.sh                          # OCR wrapper: ./ocr.sh <book> [filename]
├── sanen-kinsen-hiroku/            # Book 1 — see its own README
│   ├── original-manuscript/        #   page JPGs (source of truth)
│   ├── transcription/              #   NDL OCR output (Phase 3)
│   ├── translation/                #   English translation (in progress)
│   ├── typeset/                    #   LaTeX / PDF / EPUB + covers & figures
│   └── archive/                    #   DEPRECATED Phase 2 vision-LLM work
├── sokyu-o-soba-zenshu/            # Book 2 — same shape
│   ├── original-manuscript/
│   ├── original-manuscript.zip     #   original archive as downloaded
│   ├── transcription/
│   ├── translation/
│   ├── typeset/
│   └── archive/
├── docs/                           # project-level notes (research, go-to-market)
└── reference/                      # gitignored: third-party reference PDFs
```

## OCR tool installation

The OCR wrapper expects a Python venv at
`/Users/grob/Documents/projects/japanese-ocr-tool/ndlkotenocr-lite/.venv`.
To recreate:

```bash
git clone https://github.com/ndl-lab/ndlkotenocr-lite ~/japanese-ocr-tool/ndlkotenocr-lite
cd ~/japanese-ocr-tool/ndlkotenocr-lite
python3 -m venv .venv
.venv/bin/pip install onnxruntime pillow numpy pyyaml lxml reportlab \
                     networkx dill ordered-set pyparsing tqdm pypdfium2 protobuf
```

The two ONNX model files (~80MB total) ship in the repo at
`src/model/`. No GPU required; the repo's README reports successful use
on Intel Mac, Apple Silicon, Windows, and Linux.
