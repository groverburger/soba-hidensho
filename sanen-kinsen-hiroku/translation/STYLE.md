# Translation Style Guide

This document specifies the house style for English translations in this
folder. It is derived from the Phase 2 drafts in
`../archive/translation-vision-llm/`, distilled to the patterns that
worked and should be carried forward. It is written for another LLM
agent to read and produce new translations in the same shape.

## Inputs and outputs

**Input**: `../transcription/page_XXXXX.{txt,json,xml}` — mechanical NDL
OCR output. The `.txt` is the primary source; the `.json` carries
bounding boxes + per-character confidence scores and can be consulted
to flag low-confidence regions. **Do not read the manuscript images
directly as your primary input.** Use them only to sanity-check
obvious OCR artifacts (mis-segmented characters, dropped punctuation)
and never to substitute a visual reading for what the OCR produced.

**Output**: one markdown file per page range, named
`pages_XX-YY.md`. Page ranges follow the table below, inherited from
the legacy drafts (small ranges at the start where front matter and
prefatory material warrants dedicated files, longer ranges through
the body where continuity matters):

```
pages_01-02_cover_and_title.md     # cover + inner title spread (lean)
pages_03-04.md                     # preface
pages_05-08.md
pages_09-12.md
pages_13-16.md
pages_17-20.md
pages_21-24.md
pages_25-28.md
pages_29-30.md
pages_31-33.md                     # closes with afterword + back cover
```

## File skeleton

```markdown
# Pages X–Y: <Thematic summary of what these pages cover>

## Page N — <Page-level topic>

<Optional short preamble paragraph if the page's content needs framing.>

### ◯ <Japanese section header> — *<English gloss>*

<Body prose.>

**<Japanese term>** (*<romanization>*) — <subsection label or aside>:

<More body prose.>

---

## Page N+1 — <Page-level topic>

…

---
```

Rules:

- **Top heading** is `# Pages X–Y: <summary>`, using an **en-dash** (`–`,
  U+2013) between page numbers, not a hyphen.
- **Page heading** is `## Page N — <topic>`, using an **em-dash** (`—`,
  U+2014) between the page number and the topic.
- **Section headings inside a page** are `### …`. If the manuscript
  has a red-circle marker (visible in the OCR as `◯` or as a layout
  break), begin the heading with `◯ `. If the section has a visible
  boxed label, use `□ ` instead.
- **Bilingual section headings** use the pattern
  `### ◯ <Japanese> — *<English in italics>*`. Do not romanize the
  section's Japanese inline in the heading — save that for body text.
- **Horizontal rule** (`---`) between pages. No rule after the last
  page.

## Rendering Japanese terms

On first use of any technical term, place-name, era-name, or stage marker:

```
<Japanese kanji> (*<Hepburn romanization>*)
```

Example: `old rice (*komai*)`, `favorable conditions (*junrai*)`,
`middle star (*chūboshi*)`.

On subsequent uses in the same file, the romanization alone in italics
is sufficient — the reader has already been glossed.

For **emphasized inline terms** where you want both the kanji and the
gloss prominent, bold the Japanese and italicize the romanization:

```
**風雨** (*Fūu*) — Wind and Rain:
```

This pattern is used heavily at the start of sub-sections that are
too short to warrant their own `###` heading.

### Stage markers

Preserve the manuscript's numerical stage markers in their original
Japanese numerals with the glossed reading on first use:

```
**壱** (*Ichi*) — First position: small, probing.
**弐** (*Ni*) — Second: confirmed direction.
**参** (*San*) — Third: …
**四** (*Shi*) — Fourth: …
```

For the **Fifteen Articles** / **Thirty-Eight Articles** / etc. enumerated
sections, follow the manuscript's numbering (十五ヶ条 → Fifteen
Articles, 三十八ヶ条 → Thirty-Eight Articles) and render each article
with a bolded lede when present.

### Sexagenary cycle years

When the manuscript lists sexagenary (干支) years, keep the kanji in
the translation and provide Hepburn romanization on first use:

```
- 甲子 (*Kinoe-Ne*), 丁卯 (*Hinoto-U*), 丁未 (*Hinoto-Hitsuji*)
```

Thereafter, subsequent kanji references can appear without
romanization inside the same list.

## Diagrams

When a page contains a diagram, transcribe its structure as ASCII art
inside a fenced code block. Three diagram shapes recur:

**Tree / position-building diagrams** (pages 12–13):

```
        <Top node>
        /          \
      ②            ①
     /    \
   ④      ③    <other branch>
```

Preserve the circled-digit stage markers (`①②③④`) visible in the
manuscript.

**Boxed three-level diagrams** (page 21, world-levels):

```
    ┌─────────────────────┐
    │    上 (Upper)         │
    │  35 tawara level     │
    ├─────────────────────┤
    │    中 (Middle)        │
    │  30 tawara, 1 bu     │
    ├─────────────────────┤
    │    下 (Lower)         │
    │  25 tawara level     │
    └─────────────────────┘
```

**Radial / compass diagrams** (page 28, grand diagram): a rough ASCII
layout is acceptable; prioritize labeling each quadrant clearly over
geometric accuracy. Follow any ASCII-art diagram with a paragraph
naming each labeled element in Japanese and English.

After the ASCII block, provide an annotated key listing each label:

```
- **上 (*Ue/Jō*) — Upper:** 35 tawara — this is the ceiling range
- **中 (*Naka/Chū*) — Middle:** 30 tawara, 1 bu — the equilibrium range
```

## Prose voice and register

- **Audience**: serious readers with an interest in finance/markets
  *and* in classical Japanese texts. Write for both — don't assume
  the reader knows what Dōjima was, and don't assume they know what a
  "bale" (*tawara*) is, but also don't over-explain trading.
- **Tense**: present tense for teaching and principles ("The trader
  observes …", "When rice falls …"); past tense only when recounting
  what the manuscript records happened ("Two hundred years of records
  were consulted").
- **Voice**: sober, authorial, slightly formal. The Japanese original
  is a secret-transmission manual; the English should read as a
  considered translation of one, not as a modern trading self-help
  book.
- **Maxims**: when the manuscript presents a pithy maxim, render it
  in italics, optionally followed by an explanatory sentence:

  ```
  *"Buy once, and it returns to its original level."*
  ```

- **Do not moralize beyond what the text does.** The manuscript has
  its own ethics (patience, discipline, benevolence) — carry those
  through. Do not add modern trading advice.

## Handling uncertainty

The OCR is mechanical and will sometimes produce wrong characters. Some
pages are in dense cursive (afterword, p. 32) where even NDL OCR
struggles. Your job is **not** to paper over uncertainty — it is to
surface it explicitly.

Rules:

1. **Never invent kanji.** If the OCR output contains obvious
   mojibake or a plausibly-wrong character (e.g. the OCR says `強変`
   where context demands `強気`), flag it with `[OCR: 強変 → likely 強気]`
   rather than silently correcting. If you're confident enough to
   correct without flagging, you're overstepping.

2. **Never back-translate from prior English drafts.** The legacy
   translations in `../archive/translation-vision-llm/` are
   reference material only. Do not lift phrasings where the Japanese
   doesn't support them, and do not extend their coverage into
   passages where the underlying transcription is genuinely illegible.
   The archive's known failure mode was interpolating plausible
   English for illegible Japanese. Don't repeat it.

3. **Mark interpretive passages.** When a section is reconstructed
   from fragmentary OCR rather than confidently read, add a
   parenthetical flag at the start of the section:

   ```
   *[Interpretive. OCR for this section is fragmentary; the English
   below captures the apparent structure but specific phrasings are
   uncertain.]*
   ```

4. **Preserve the original's uncertainty markers.** If the OCR output
   contains `□` (illegible), preserve it in the translation as
   `[illegible]` or carry the `□` through.

5. **Footnote or flag low-confidence OCR regions.** The `.json`
   sidecar files have per-line confidence scores. If a critical term
   sits in a low-confidence region, say so.

## Editorial apparatus

- **Attributions** at the start of the book (牛田権三郎, 鳴川猛之助,
  the publisher 好問堂, the location 五十嵐津, the date 嘉永四年五月廿日):
  render each in kanji with romanization and a literal English gloss.
  Cross-reference the Tanimura Collection / Kyoto University RMDA
  record (RB00012360) where relevant.

- **Cross-references within the book**: use parentheticals like
  `(see page 22, Middle Star)`. Do not invent section IDs that
  aren't in the manuscript.

- **Cross-references to external concepts**: light touch — if a
  passage clearly maps to something in Dow Theory, Elliott Wave,
  or another classical framework, a brief parenthetical comparison
  is acceptable, but do not make it the primary gloss.

## What NOT to do

- Do not write new content that isn't grounded in the OCR output.
- Do not summarize pages you can't translate; mark them as
  `[Interpretive.]` or leave a `[TODO: transcription dense here —
  revisit]` stub.
- Do not recycle Phase 2 phrasings wholesale without confirming
  the Japanese supports them.
- Do not add bulleted "takeaway" sections, modern trading advice,
  or motivational framing.
- Do not translate the Japanese title into English in running text
  after the first introduction — use `*Sanen Kinsen Hiroku*` or
  `the text` thereafter.
- Do not generate files, headings, or content beyond what the
  current page range requires. Translate the range you were asked
  for; don't forward-fill.

## Working checklist for each page

Before writing a page:
1. Read `../transcription/page_XXXXX.txt` in full.
2. Spot-check `../transcription/page_XXXXX.json` for any line with
   confidence under ~0.6 — those deserve `[OCR: …]` flags.
3. Identify section breaks (red-circle markers in the OCR → `◯`
   headings; boxed labels → `□` headings).
4. Draft the page in the skeleton above.
5. On first mention of each term, add `(*romanization*)`.
6. Check: does every paragraph have a basis in the OCR? If not,
   either flag as interpretive or cut.
7. Look at the corresponding file in
   `../archive/translation-vision-llm/` for structural reference
   only — **not for phrasings to lift**.
