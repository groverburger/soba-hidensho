# Sanen Kinsen Hiroku (三猿金泉秘録)

**The First English Translation of the Three Monkeys Gold Spring Secret Record**

An Edo-period Japanese manuscript on the art of rice market speculation, attributed to Ushida Gonzaburō (牛田権三郎), revised by Narukawa Takenosuke (鳴川猛之助). Translated directly from the 1851 manuscript held at Kyoto University (Record ID: [RB00012360](https://rmda.kulib.kyoto-u.ac.jp/item/rb00012360)).

Edited and produced by Zach Booth. Translated with AI assistance (Claude Opus 4.6, Anthropic).

## Why This Translation Exists

For thirty-five years, English-language traders have searched for this text under the wrong name, attributed to the wrong author. The *Sanen Kinsen Hiroku* has been consistently misattributed to Honma Munehisa of Sakata in Western trading literature, beginning with Steve Nison's *Japanese Candlestick Charting Techniques* (1991). Two English books have been published under variations of this text's title. Neither translates it — both render a separate body of trading maxims from the Honma/Sakata tradition while putting Ushida's title on the cover.

In Japanese scholarship, the authorship is unambiguous: the National Diet Library, CiNii, Kyoto University's digital archive, and sources from Honma's own hometown all attribute the *Sanen Kinsen Hiroku* to Ushida Gonzaburō. The confusion exists almost exclusively in English.

This project produces the first English translation of the actual text, from an identified manuscript with real provenance.

## How the Translation Was Produced

### Methodology

The translation was produced using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI agent) powered by **Claude Opus 4.6**, which has strong multimodal capabilities for reading historical Japanese cursive script (草書/kuzushiji).

The workflow evolved through three phases:

**Phase 1: Direct translation.** Claude Opus 4.6 read each manuscript page image and produced English translations directly. This yielded usable drafts but conflated two distinct tasks — character recognition and meaning interpretation — making errors difficult to trace and audit.

**Phase 2: Vision-LLM transcription, then translation.** We separated the process into two stages: Claude Opus 4.6 produced a character-level transcription of each page, then a second pass translated from the transcription. This was more auditable than Phase 1 but revealed a systemic failure mode: when the LLM could not read a cursive character, it often interpolated a confident-looking reading — sometimes back-translated from its own prior translation output — rather than admitting uncertainty. The Phase 2 artifacts are preserved in `./archive/transcription-vision-llm/` and `./archive/translation-vision-llm/` for audit.

**Phase 3 (current): NDL OCR transcription, then LLM translation.** The transcription step is now performed by [NDL 古典籍OCR-Lite](https://github.com/ndl-lab/ndlkotenocr-lite), a specialist OCR toolchain released by Japan's National Diet Library for Edo-period and earlier classical texts (RTMDet text-region detection + PARSeq recognition, both as ONNX; CPU-only, no GPU required). This is a purely mechanical step — the model does not interpret meaning, does not know the English translation exists, and cannot interpolate from context it doesn't have. The `.txt` / `.json` / `.xml` / TEI output in `./transcription/` is the authoritative source for translation. LLMs are now used only for the translation step that reads the mechanical OCR output. Run with `./ocr.sh sanen-kinsen-hiroku` from the project root.

1. **Transcription** (`./transcription/`): Mechanical OCR output from NDL 古典籍OCR-Lite, one set of files per manuscript page.
2. **Translation** (`./translation/`): Working from the transcription (not directly from the images), Claude produces English translations. This keeps every editorial decision traceable — a reader can check the transcription against the original image, then check the translation against the transcription, with no opaque vision-to-prose step in between.

The three-phase history is preserved here intentionally: the `./archive/` folder shows what went wrong in Phase 2, so that readers can see both the method and the reasons it was revised.

### Adversarial Grading (GAN-Inspired Iteration)

To improve quality iteratively, we used a technique inspired by Generative Adversarial Networks (GANs) from the 2010s deep learning era: a separate, context-free Claude Opus 4.6 instance grades the work using the prompt:

> "Grade ./sanen-kinsen-hiroku.pdf (and the LaTeX source document) as a standalone document"

This external reviewer has no knowledge of our process, goals, or prior conversations — it evaluates the output cold, as a reader would. Its feedback is then incorporated by the production instance (Claude Code), creating an iterative improvement loop:

1. **Generator** (Claude Code): produces the translation and LaTeX document
2. **Discriminator** (independent Claude instance): grades the output, identifies weaknesses
3. **Iteration**: the generator incorporates the feedback and resubmits

This cycle was repeated multiple times, catching fabricated content, arithmetic errors, misattributions, bibliography inaccuracies, layout problems, and omitted source material that the production instance had missed. The technique proved remarkably effective at surfacing blind spots.

<details>
<summary>Example grader output (click to expand)</summary>

```
Grade: A-

Category Grades:

| Category                       | Grade |
|--------------------------------|-------|
| Scholarly rigor & attribution  | A+    |
| Translation quality & voice    | A     |
| Editorial transparency         | A     |
| Typography & design            | A-    |
| Front/back matter completeness | A-    |
| Internal structure & pacing    | B     |
| Calculation tables clarity     | C+    |
| Overall                        | A-    |

Strengths:
1. The attribution argument is the document's standout contribution.
   The Translator's Introduction makes a careful, well-sourced case
   that English-language sources have systematically misattributed
   this text to Honma Munehisa...

2. Transparency of method is exemplary. The document is consistently
   honest about what it is and isn't...

Weaknesses:
1. Chapter 7 calculation tables are the weakest section (C+).
   Sections 7.3.2 through 7.3.6 are repetitive and hard to follow...

2. Excessive white space / short chapters (B-). Multiple chapters
   end with over half a page blank...

Summary: The document is publishable as-is. The weaknesses are real
but none are disqualifying — they're the kind of refinements that
separate a strong first edition from a polished second edition.
```

This feedback led directly to restructuring Chapter 7.3 (summary table + appendix), fixing orphaned headings, and multiple rounds of content restoration.

</details>

### What Claude Opus 4.6 Does Well

- **Reading kuzushiji**: Claude Opus 4.6 can read Edo-period cursive Japanese script directly from manuscript images with reasonable accuracy, identifying kanji, kana, and structural elements (section markers, diagram labels, numerical tables).
- **Bilingual apparatus**: Consistent inline glossing of Japanese terms with kanji, romanization, and English throughout.
- **Scholarly footnotes**: Contextualizing Edo-period concepts for modern readers (e.g., connecting the three-phase decline pattern to Dow Theory, identifying the Zhou Dunyi cosmological framework).
- **LaTeX typesetting**: Professional book production with XeLaTeX, including CJK font handling, figure placement, and cross-references.

### What Required Human Judgment

- **Editorial decisions**: What to include, what to summarize, how to structure chapters, when to admit uncertainty.
- **Accuracy verification**: Checking AI-generated translations against the manuscript images, catching fabricated content and arithmetic that didn't add up.
- **Attribution research**: The misattribution story required independent research into Nison's books, Japanese library catalogs, and the Honma/Ushida distinction.
- **Source identification**: Finding the manuscript in Kyoto University's digital archive and recognizing its significance.

### Confidence Assessment: What We Know and What We Don't

A page-by-page audit of the manuscript images against the transcription and translation revealed a systemic issue: the original translation pipeline converted uncertain transcriptions into confident English prose, with zero of the transcription's 342 uncertainty markers propagating into the published text. This has been corrected. The translation now marks interpretive passages explicitly.

#### What is reliably translated (high confidence)

- **Section headers and boxed labels** throughout the manuscript: 十五ヶ条, 三十八ヶ条, 穂足の録, 萬光商内之圖, 七福即宝秘密, 随金商内, 強氣立の秘傳, 世の中三段之圖, 上割三下割之圖, 強氣の初, 弱氣の初, 大壱落修の事, etc.
- **The kanbun preface** (page 3): written in clear semi-cursive, faithfully translated.
- **Publication details and attribution**: 牛田権三郎, 鳴川猛之助, 嘉永四年五月廿日, 好問堂蔵版, 五十嵐津 — all clearly legible.
- **Diagram labels and structures** (pages 12, 21, 28): stage markers (壱–四 in red ink), tawara levels, ryo figures, and the Three Levels / Grand Diagram structures are clearly legible.
- **Sexagenary year lists** (pages 14–15): formulaic characters in systematic lists, reliably read.
- **The Six Observations list** (page 20): all six Japanese terms (二割, 三割, 高の内, 横の平, 人の気, 大勢) confirmed with furigana.
- **Key standalone lines**: e.g., 壱買段せ、其まゝ本へもどる (page 19).
- **Harvest quality grades**: 上作/中作/下作 with furigana.

#### What is partially legible (moderate confidence)

- **Seasonal trading rules** (pages 5–7): month references (四月, 六月, 七月) and key terms (古米, 順来, 逢来) are partially legible; the connecting instructions are reconstructed from these anchors.
- **Position calculation tables** (pages 22–24): stage markers (壱–四/五) and round figures (百両, 八百両, 二拾俵) are legible; intermediate calculations carry uncertainty.
- **The turnover method ratio** (page 13): 転換の法 and the 1,000/2,000 ratio are supported by partially legible text.
- **The Middle Star concept** (page 22): 中星 and 三十年 are legible; the buy/sell framework around them is interpretive.

#### What is largely illegible (low confidence — marked `[Interpretive.]`)

- **The 禁判 entries** (pages 6–9): the red-ink 禁判 markers are legible, but the six paragraphs of trading maxims between them are reconstructed from genre conventions and fragmentary readings.
- **The afterword** (pages 31–32): dense flowing cursive with water damage. Only the attribution (鳴川猛之助) and date are confirmed. The philosophical prose is an interpretive reconstruction of the afterword's apparent themes.
- **The Wisdom section** (page 18): the header 智 十首 is legible; the body text cannot be reliably translated.
- **Courage section** (page 19): the header 勇 is legible; body text too brief and cursive to confirm.
- **Wind and Rain** (page 29): header and month markers legible; agricultural details between them were fabricated in earlier versions and have been removed.
- **Strong Qi / Weak Qi / Great First Decline** (pages 29–30): headers legible; the prose descriptions are interpretive reconstructions from fragments.
- **The Seven Fortunes conditions** (page 25): the header 七福即宝秘密 is legible; a numbered list of seven specific conditions that appeared in earlier versions was fabricated and has been removed.

#### What was corrected in this audit

- **六秘見** → **六初覚**: a fabricated Japanese compound was replaced with the transcription's actual reading.
- **Turnover diagram labels**: the caption claimed 千両買/二千両売; the manuscript shows 百両買/百両賣.
- **Page 12 attribution**: 転換商内之圖 was attributed to the left page; the visible boxed label is 萬光商内之圖.
- **天明古写本** → **天明古米**: a misreading in the Grand Diagram caption.
- **天明 era reference** → **天之商内**: "in the Tenmei era" was a misreading of "within heaven's trading."
- **大名 (daimyō)**: likely a misreading of 男の方 (men's side) — removed.
- **大潮/小潮 furigana**: claimed readings おおしお/こしお could not be confirmed and were removed.
- **Fabricated prose removed**: "The market is not a place of chance but of pattern," the four-virtue afterword list, "Gold and rice are like flowing water," monthly agricultural details (frost, plum rains, typhoon), "A rule without understanding is dangerous," the military-general analogy, and others.

### Research Context: Why This Is Novel

As of early 2026, this project represents a genuinely novel workflow in the field of AI-assisted classical Japanese translation. Here's why:

**No published end-to-end pipeline exists for this task.** The academic literature on AI translation of classical Japanese focuses on either (a) OCR/kuzushiji recognition (CODH's KuroNet/Miwo) or (b) LLM translation of already-transcribed classical text (the CODH Tsukushi Project, the MITRA Buddhist text project). Nobody has published an end-to-end pipeline that goes directly from Edo-period cursive manuscript images to a publication-ready English translation with a full audit trail.

**The current generation of models is untested on classical Japanese.** The formal academic benchmarks that exist (the Genji ambiguity test, the Kanbun-LM evaluation, the PoetMT benchmark) all tested models from 2023-2024 — GPT-4 era. Claude Opus 4.6, GPT-5.x, and Gemini 3.x have not been rigorously evaluated on classical Japanese. The CODH Tsukushi Project rated Claude Sonnet 4.5 highest among all tested models for classical Japanese text interaction, but did not test Opus 4.6. Our project is, as far as we can determine, one of the first to apply Opus 4.6's multimodal capabilities directly to Edo-period kuzushiji manuscripts.

**Claude Opus 4.6 reads the manuscript images directly.** Most existing workflows use a dedicated OCR tool (KuroNet, Miwo) for character recognition, then feed the recognized text to an LLM for translation. Our workflow skips the OCR step — Claude reads the cursive script directly from the IIIF page images. This is possible because of Opus 4.6's multimodal capabilities, which combine visual character recognition with contextual language understanding in a single pass. The tradeoff is lower character-level accuracy than dedicated OCR tools on clean printed text, but potentially better performance on damaged or ambiguous manuscript pages where context helps.

**The transcription-then-translation separation is methodologically significant.** Our initial approach (Phase 1) had Claude translate directly from images, conflating character recognition and meaning interpretation. When we separated these into explicit stages — transcription with confidence levels, then translation from transcription — the results became more consistent and, critically, auditable. A reader can check the transcription against the original image, then check the translation against the transcription. This separation has been discussed in the literature (e.g., the CODH Tsukushi pipeline) but not, to our knowledge, implemented as an open-source audit trail for a complete book-length translation.

**The adversarial grading loop has no direct precedent in translation work.** Using an independent, context-free LLM instance to grade the output — inspired by GANs — proved remarkably effective at catching failure modes that the production instance couldn't self-detect: fabricated content, arithmetic errors, misattributed sources, and editorial paraphrase presented as translation. This technique is applicable to any AI-assisted translation project and, to our knowledge, has not been formally described in the translation studies literature.

**Key references for the research context:**
- Clanuwat et al., "Deep Learning for Classical Japanese Literature" (2018) — KuroNet, Kuzushiji-MNIST
- Kitamoto et al., CODH Tsukushi Project — LLM interaction with classical Japanese texts
- Wang et al., "Kanbun-LM" (ACL 2023) — Classical Chinese to kanbun parallel dataset
- Nehrdich, "MITRA: A Parallel Corpus for Buddhist Chinese" (2025) — LLM evaluation for Buddhist texts
- De Wolf, "Can ChatGPT Translate Literary Japanese?" (2023) — The Genji ambiguity test
- Miwo app (CODH) — Kuzushiji OCR, 3.4M+ images processed

## Repository Structure

```
sanen-kinsen-hiroku/
├── README.md                      # this file
├── original-manuscript/           # 33 page scans from Kyoto University RMDA
│   ├── page_00001.jpg             #   (RB00012360, Tanimura Collection)
│   └── …
├── transcription/                 # NDL 古典籍OCR-Lite mechanical output
│   ├── page_00001.txt             #   plain text
│   ├── page_00001.json            #   bboxes + confidence scores
│   ├── page_00001.xml             #   layout XML
│   └── page_00001_tei.xml         #   TEI-P5 (batch)
├── translation/                   # English translation (from transcription)
├── typeset/
│   ├── sanen-kinsen-hiroku.tex    # LaTeX source (compile with XeLaTeX)
│   ├── sanen-kinsen-hiroku.pdf
│   ├── sanen-kinsen-hiroku.epub
│   ├── epub-style.css
│   ├── covers/                    # cover artwork variants
│   └── diagrams/                  # cleaned-up crops of manuscript figures
└── archive/
    ├── transcription-vision-llm/  # Phase 2 artifact (DEPRECATED)
    └── translation-vision-llm/    # Phase 2 artifact (DEPRECATED)
```

## Building the PDF

Requires XeLaTeX with the following fonts installed:
- Noto Serif / Noto Serif Bold / Noto Serif Italic / Noto Serif Bold Italic
- Noto Serif JP
- Noto Sans JP (used as Japanese bold fallback)

```bash
cd typeset
xelatex sanen-kinsen-hiroku.tex
xelatex sanen-kinsen-hiroku.tex  # twice for cross-references
```

## Source Manuscript

**Record**: 校正三猿金泉秘録 (Kōsei Sanen Kinsen Hiroku)
**Record ID**: RB00012360
**Collection**: Tanimura Collection (谷村文庫), Main Library, Kyoto University
**Date**: Kaei 4 (嘉永四年五月廿日; 1851)
**Publisher**: Kōmondō (好問堂蔵版), Igarashi-tsu (五十嵐津)
**Digital Archive**: https://rmda.kulib.kyoto-u.ac.jp/item/rb00012360
**License**: Free with Attribution (二次利用自由・所蔵表示)

All manuscript images courtesy of the Main Library, Kyoto University.
所蔵：京都大学附属図書館

## License

Copyright (c) 2026 Zach Booth. All rights reserved.

**Translation, transcription, and LaTeX source** (this repository): Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International). You may read, study, fork, and build on this work for non-commercial purposes, provided you credit the original and share derivatives under the same terms.

**The compiled book** (PDF / printed editions): All rights reserved. Commercial distribution of the finished book is exclusively authorized by the copyright holder.

**Source manuscript images**: Provided under Kyoto University's free-with-attribution license (二次利用自由・所蔵表示). See [reuse policy](https://rmda.kulib.kyoto-u.ac.jp/reuse). All manuscript images courtesy of the Main Library, Kyoto University (所蔵：京都大学附属図書館).
