# Translation Style Guide

This document specifies the house style for English translations of
*Sōkyū-ō Soba Zenshū* (宗久翁相場全集, "Complete Collected Works on
Markets by Master Sōkyū"). It is adapted from the style guide used
for *Sanen Kinsen Hiroku* and tailored to the distinctive structure of
this text — a Meiji 43 (1910) annotated edition of Honma Sōkyū's
rice-trading writings, edited and annotated by Hayasaka Nikiku
(早阪二菊, also written 早坂豊藏). It is written for an LLM agent to
read and produce translations in a consistent shape.

## About the source text

The *Sōkyū-ō Soba Zenshū* is not a single manuscript but a
**compiled edition**. Hayasaka collated Sōkyū's autograph manuscript
(preserved by the Honma family) against circulating hand-copies,
added several dozen chapters from variant texts, and supplied
extensive commentary (marked 釋). The result is a two-volume work
(Upper and Lower) totalling 158 numbered chapters, preceded by
front matter (preface, annotator's notes, biography, Sakata
exchange customs) and followed by historical price tables and
calendar apparatus.

The OCR source is from the NDL (National Diet Library) 古典籍OCR-Lite
pipeline applied to the Meiji printed edition.

## Inputs and outputs

**Input**: `../transcription/XXXX_0000.{txt,json,xml}` — mechanical NDL
OCR output. The `.txt` is the primary source; the `.json` carries
bounding boxes and per-character confidence scores. **Do not read
manuscript images directly as your primary input.** Use them only to
sanity-check obvious OCR artifacts.

**Output**: one markdown file per page range, named `pages_XX-YY.md`.
Page ranges follow this table:

```
pages_01-03.md          # cover, title, preface (緒言), notes (凡例)
pages_04-07.md          # biography (小傳), Sakata exchange customs
pages_08-14.md          # table of contents (Upper and Lower volumes)
pages_15-18.md          # Upper Volume: Ch. 1–2
pages_19-22.md          # Upper Volume: Ch. 3–7
pages_23-26.md          # Upper Volume: Ch. 8–9
pages_27-30.md          # Upper Volume: Ch. 10–15
pages_31-34.md          # Upper Volume: Ch. 16–22
pages_35-38.md          # Upper Volume: Ch. 23–29
pages_39-42.md          # Upper Volume: Ch. 30–42
pages_43-46.md          # Upper Volume: Ch. 43–46
pages_47-50.md          # Upper Volume: Ch. 47–51
pages_51-54.md          # Upper Volume: Ch. 52–56
pages_55-58.md          # Upper Volume: Ch. 57–66
pages_59-62.md          # Upper Vol. end / Lower Vol. begins
pages_63-66.md          # Lower Volume: Ch. 1–6
pages_67-70.md          # Lower Volume: Ch. 7–14
pages_71-74.md          # Lower Volume: Ch. 15–27
pages_75-78.md          # Lower Volume: Ch. 28–40
pages_79-82.md          # Lower Volume: Ch. 41–50
pages_83-86.md          # Lower Volume: Ch. 51–61
pages_87-90.md          # Lower Volume: Ch. 62–85 / price records
pages_91-94.md          # price records / historical tables
pages_95-100.md         # publisher advertisements, colophon
```

Chapter-to-page boundaries are approximate and will shift as
translation proceeds. Adjust ranges if a chapter straddles a file
boundary — prefer keeping a chapter whole over keeping page counts
even.

## File skeleton

```markdown
# Pages X–Y: <Thematic summary>

## Page N — <Page-level topic>

<Optional preamble paragraph.>

### Chapter NN: <Japanese chapter title> — *<English gloss>*

> <Sōkyū's original text, in Japanese, as a blockquote.>

<English translation of Sōkyū's text.>

**Commentary** (*Shaku*):

<English translation of Hayasaka's 釋 annotation.>

---

## Page N+1 — <Page-level topic>

…
```

Rules:

- **Top heading** is `# Pages X–Y: <summary>`, using an **en-dash**
  (`–`, U+2013) between page numbers.
- **Page heading** is `## Page N — <topic>`, using an **em-dash**
  (`—`, U+2014).
- **Chapter headings** are `### Chapter NN: <Japanese> — *<English>*`.
  Use Arabic numerals for the chapter number. When the source has
  第一章, render as `Chapter 1`; 第卅八章 → `Chapter 38`.
- **Horizontal rule** (`---`) between pages. No rule after the last
  page.

## Two-layer text: Sōkyū vs. Hayasaka

The body text has a distinctive two-layer structure that must be
preserved:

1. **Sōkyū's original text** — introduced by `一` at the start of
   each chapter. This is Edo-period trading instruction in a
   semi-classical register. Render it in a blockquote (`> …`),
   followed immediately by the English translation in regular prose.
   Keep the translation sober, close to the original's terse,
   didactic voice.

2. **Hayasaka's commentary** — marked `(釋)` in the source. This
   is Meiji-era explanatory prose, often two to four times longer
   than Sōkyū's text. Render under a `**Commentary** (*Shaku*):` label
   in regular prose. Hayasaka's voice is more discursive and
   analytical; the translation may be slightly freer, but should not
   editorialize beyond what Hayasaka himself says.

When Hayasaka adds a second or third passage of commentary within the
same chapter (sometimes marked by further `(釋)`, sometimes not),
continue under the same commentary label with a paragraph break.

When a chapter has no `(釋)` section, omit the Commentary label.

## Rendering Japanese terms

On first use of any technical term, place-name, era-name, or
personal name within a file:

```
<English gloss> (<Japanese kanji>, *<Hepburn romanization>*)
```

Example: `ceiling price (天井直段, *tenjō nedan*)`,
`margin call (落引, *ochibiqi*)`,
`range-bound market (通相場, *kayoi sōba*)`.

On subsequent uses in the same file, the English gloss alone or the
romanization in italics is sufficient.

For **emphasized inline terms**, bold the Japanese and italicize the
romanization:

```
**天井** (*tenjō*) — ceiling:
```

### Key recurring terms

Maintain consistent glosses for these terms across all files:

| Japanese | Romanization | English gloss |
|----------|-------------|---------------|
| 天井 / 天井直段 | *tenjō* / *tenjō nedan* | ceiling / ceiling price |
| 底 / 底直段 | *soko* / *soko nedan* | floor / floor price |
| 通相塲 | *kayoi sōba* | range-bound market |
| 伸相塲 | *nobi sōba* | trending market |
| 保合 | *mochai* | holding pattern / consolidation |
| 落引 | *ochibiki* | margin call |
| 繋ぎ | *tsunagi* | carrying (a position) |
| 利喰 | *rigui* | profit-taking |
| 踏出し | *fumidashi* | initial entry (into a trade) |
| 三位の傳 | *sanmi no den* | the Three-Position Tradition |
| 二ツ仕廻 三ツ十分 四ツ轉じ | — | "At two, close out; at three, fully ripe; at four, it turns" |
| 駈引 | *kakehiki* | maneuvering / tactical play |
| 商内 | *akinai* | trade / position |
| 俵 | *tawara* | bale (unit of rice quantity) |
| 乘米 | *nosei-mai* | arbitrage rice / carry rice |
| 限月 | *gengetu* | contract month |
| 霜月限 | *shimotsuki-giri* | November contract |
| 發會 | *hakkai* | opening (of a contract period) |
| 月節 | *tsukibushi* | monthly high/low mark |
| 人氣 | *ninki* | market sentiment |
| 强氣 / 弱氣 | *tsuyoki* / *yowaki* | bullish / bearish |
| 甲月 | *kinoe-tsuki* | "first-stem month" (see calendar system) |
| 年塞 | *toshifusagari* | year-block (directional taboo year) |

### The Three-Position Tradition (三位の傳)

This is Sōkyū's central doctrine, referenced throughout both volumes.
On first introduction (Chapter 1), give the full formula with
romanization:

> *"At two, close out; at three, fully ripe; at four, it turns"*
> (二ツ仕廻、三ツ十分、四ツ轉じ, *futatsu shimai, mittsu jūbun,
> yottsu tenji*) — the Three-Position Tradition (三位の傳, *sanmi no
> den*).

Thereafter, use "the Three-Position Tradition" or "the *sanmi* rule."

### Sexagenary cycle and calendar terms

The text uses the 十干 (Heavenly Stems) system to predict monthly
price movements. On first use, explain:

```
甲 (*kinoe*), 乙 (*kinoto*), 丙 (*hinoe*), 丁 (*hinoto*) — the
first four Heavenly Stems, which Sōkyū associates with rising
markets.
```

For 年塞 (year-blocks) and directional terms (西へ廻る, etc.),
preserve the Japanese and provide a brief gloss on first use.

### Personal names and attributions

- **本間宗久** — Honma Sōkyū (also 本間古作, Honma Kosaku). Use
  "Sōkyū" in running text after first introduction.
- **早阪二菊** / **早坂豊藏** — Hayasaka Nikiku / Hayasaka Toyozō.
  Same person. Use "Hayasaka" in running text.
- **慈雲齋** — Jiunsai. A different author (Ushida Gonzaburō, of
  *Sanen Kinsen Hiroku*); Hayasaka quotes him several times.

## Prose voice and register

- **Audience**: serious readers interested in both historical
  Japanese finance and classical Japanese texts. Don't assume the
  reader knows what Dōjima or Sakata was, but don't over-explain
  trading mechanics either.
- **Sōkyū's text**: terse, imperative, oracular. Translate in
  present tense for principles: "The trader should …", "When rice
  falls …". Preserve the didactic cadence.
- **Hayasaka's commentary**: analytical, discursive, Meiji-era
  pedagogical. Slightly more relaxed register than Sōkyū, but still
  sober. He explains Sōkyū's teachings for a Meiji audience.
- **Kanbun passages** (biography, pp. 4–6): these are classical
  Chinese prose. Translate into formal English that reflects the
  biographical gravitas without being stilted.
- **Maxims**: when Sōkyū presents a pithy maxim, render it in
  italics:

  ```
  *"What seems too late is still early; what seems still early is
  already too late."*
  ```

- **Do not moralize beyond what the text does.** Sōkyū's ethics
  (patience, discipline, detachment, Zen composure) and Hayasaka's
  analytical framework speak for themselves.
- **Do not add modern trading analogies** unless Hayasaka himself
  draws them (he occasionally references Western traders like
  "David Ricardo" — 「タビツト、リカード」).

## Handling OCR noise

The NDL OCR of this Meiji printed edition produces characteristic
noise patterns:

1. **Scattered running headers**: the vertical running header
   (宗久翁相場全集上卷, etc.) appears as isolated characters on
   separate lines. Ignore these entirely — do not translate or
   reproduce them.

2. **Dot-fill lines**: rows of `…` or `、` from ruled lines and
   decorative borders. Ignore.

3. **Scattered page numbers**: numbers like `一四`, `二三` that
   appear as isolated lines. These are page numbers — ignore in body
   text but use them for page-boundary tracking.

4. **Brace/bracket artifacts**: `}`, `{`, and similar characters
   from column boundaries. Ignore.

5. **Zero/circle runs**: sequences like `〇〇〇〇、、、、` from
   tabular content or decoration. Ignore unless they appear within
   meaningful content (e.g., price tables).

6. **Duplicated chapter titles**: the OCR sometimes captures both
   the TOC entry and the body heading for the same chapter. Use
   the body text version.

## Handling uncertainty

1. **Never invent kanji.** If the OCR contains obvious errors
   (e.g., `盆々` where context demands `益々`, or `塲` for `場`),
   flag with `[OCR: X → likely Y]` rather than silently correcting.
   Exception: obvious period-variant characters (塲/場, 處/所) that
   are interchangeable in this text need not be flagged.

2. **Mark interpretive passages.** When reconstructing from
   fragmentary OCR:

   ```
   *[Interpretive. OCR for this section is fragmentary; the English
   below captures the apparent structure but specific phrasings are
   uncertain.]*
   ```

3. **Preserve illegibility markers.** If the OCR shows `□`, carry
   through as `[illegible]`.

4. **Note low-confidence regions.** The `.json` sidecar has
   per-line confidence scores. Flag critical terms in low-confidence
   regions.

## Table of contents (pages 8–14)

Render as a numbered list with Japanese chapter titles and English
glosses:

```markdown
1. 第一章 米商は踏出大切の事 — *The Initial Entry into Trading Is
   of the Utmost Importance*
2. 第二章 下相塲月頭強く月末弱き事 — *In a Falling Market, the
   Month Opens Strong and Closes Weak*
…
```

Preserve the Upper Volume / Lower Volume division with `##` headings.

## Price tables (pages 90–94)

Render historical price records in a structured format:

```markdown
### 安永七年 戌年 (*An'ei 7, Year of the Dog*, 1778)

- **Opening**: 46 tawara
- **November (甲)**: 30 tawara, 9 bu — ceiling, 151-tawara rise
  [on a 不成就日]
- **Following year (亥)**: 35 tawara, 5 bu — 46-tawara decline
```

Preserve all calendar annotations (甲, 不成就日, 天上, etc.) with
glosses on first use.

## What NOT to do

- Do not write content that isn't grounded in the OCR output.
- Do not summarize pages you can't translate; mark them as
  `[Interpretive.]` or leave a `[TODO]` stub.
- Do not add bulleted "takeaway" sections, modern trading advice,
  or motivational framing.
- Do not translate the Japanese title into English in running text
  after the first introduction — use *Sōkyū-ō Soba Zenshū* or
  "the text" thereafter.
- Do not generate content beyond the current page range.
- Do not conflate Sōkyū's voice with Hayasaka's. Keep the two
  layers distinct.

## Working checklist for each page

Before writing a page:
1. Read `../transcription/XXXX_0000.txt` in full.
2. Spot-check `../transcription/XXXX_0000.json` for lines with
   confidence under ~0.6 — those deserve `[OCR: …]` flags.
3. Filter out OCR noise (running headers, dot-fills, scattered
   numbers, brace artifacts).
4. Identify chapter boundaries (`第N章` headings) and
   commentary boundaries (`(釋)`).
5. Draft the page in the skeleton above.
6. On first mention of each term, add the gloss.
7. Check: does every paragraph have a basis in the OCR? If not,
   flag as interpretive or cut.
