# Translation Style Guide (v2)

This document specifies the house style for English translations of
*Sanen Kinsen Hiroku* (三猿金泉秘録) in this folder. It is written for
an LLM agent producing fresh translations from the OCR transcription.

## Inputs and outputs

**Input**: `../transcription/page_XXXXX.{txt,json,xml}` — mechanical
NDL OCR output of the manuscript. The `.txt` is the primary source;
the `.json` carries bounding boxes + per-character confidence scores
and can be consulted to flag low-confidence regions. **Do not read the
manuscript images directly as your primary input.** Use them only to
sanity-check obvious OCR artifacts (mis-segmented characters, dropped
punctuation) and never to substitute a visual reading for what the OCR
produced.

**Do not consult `../translation/` for any reason.** That folder holds
an earlier translation produced by a different model. This v2 effort
is intended as an independent reading of the same OCR. Do not open
those files even for "structural reference" — chunking, chapter
divisions, glosses, and editorial framing should all be developed
fresh from the transcription.

**Output**: one markdown file per page range, named `pages_XX-YY.md`
(or `pages_NN.md` for a single page). Choose page ranges that follow
the manuscript's natural section breaks — don't force a uniform
stride. Front matter and short prefatory pages can warrant their own
small files; longer continuous body sections can be grouped.

## File skeleton

```markdown
# Pages X–Y: <Thematic summary of what these pages cover>

## Page N — <Page-level topic>

<Optional short preamble paragraph if framing helps.>

### ◯ <Japanese section header> — *<English gloss>*

<Body prose.>

**<Japanese term>** (*<romanization>*) — <subsection label or aside>:

<More body prose.>

---

## Page N+1 — <Page-level topic>

…
```

Conventions:

- **Top heading**: `# Pages X–Y: <summary>`, **en-dash** (U+2013)
  between page numbers.
- **Page heading**: `## Page N — <topic>`, **em-dash** (U+2014)
  between page number and topic.
- **Section headings inside a page**: `### …`. If the manuscript
  shows a red-circle marker (visible in the OCR as `◯` or as a layout
  break), begin the heading with `◯ `. If it shows a boxed label, use
  `□ ` instead.
- **Bilingual section headings**: `### ◯ <Japanese> — *<English in
  italics>*`. Don't romanize inline in the heading — save the
  romanization for body text.
- **Horizontal rule** (`---`) between pages. No rule after the last
  page.

## Rendering Japanese terms

On first use of any technical term, place-name, era-name, person-name,
or stage marker:

```
<Japanese kanji> (*<Hepburn romanization>*)
```

On subsequent uses in the same file, romanization alone in italics is
fine — the reader has been glossed.

For **emphasized inline terms** at the start of a short subsection too
small to warrant its own `###` heading, bold the kanji and italicize
the romanization:

```
**<kanji term>** (*<romanization>*) — <English label or gloss>:
```

### Stage and enumeration markers

When the manuscript uses Japanese numerals (壱/弐/参/四/五, 一/二/三,
or counters like 十五ヶ条 / 三十八ヶ条), preserve them on first use
with romanization, and follow the manuscript's enumeration faithfully —
don't renumber, don't reorganize, don't merge or split items.

### Sexagenary cycle years (干支)

Keep kanji in the translation; provide Hepburn romanization on first
use within a list:

```
- 甲子 (*Kinoe-Ne*), 丁卯 (*Hinoto-U*), …
```

Subsequent kanji references in the same list can drop the romanization.

## Diagrams

When a page contains a diagram, render its structure as ASCII art
inside a fenced code block. Prioritize labeling each visible element
clearly over geometric accuracy. After the ASCII, provide an annotated
key:

```
- **<kanji label>** (*<romanization>*) — <English gloss>: <what it represents>
```

Do not invent labels that aren't visible in the diagram. If
surrounding prose explains or names the diagram (e.g. compass
directions, hexagram names, philosophical categories), describe what
the prose says *separately* from what the diagram itself shows. A
prose label is not a diagram label.

## Prose voice and register

- **Audience**: serious readers with an interest in finance/markets
  *and* in classical Japanese texts. Don't assume the reader knows
  what Dōjima was or what a *tawara* is, but don't over-explain
  trading either.
- **Tense**: present tense for teaching and principles; past tense
  only when recounting what the manuscript records as having
  happened.
- **Voice**: sober, authorial, slightly formal — a considered
  translation of a secret-transmission manual, not a modern trading
  self-help book.
- **Maxims**: render in italics, optionally followed by an
  explanatory sentence:

  ```
  *"<Maxim translation here.>"*
  ```

- **Do not moralize beyond what the text does.** Carry through the
  manuscript's own ethics; do not add modern trading advice.
- **Do not translate the title** in running English text. Use
  *Sanen Kinsen Hiroku* or "the text" after first introduction.

## Handling uncertainty

The OCR is mechanical and sometimes wrong. Some pages are dense
cursive that even NDL OCR struggles with. Your job is **not** to paper
over uncertainty — it is to surface it explicitly.

1. **Never invent kanji.** If the OCR contains obvious mojibake or a
   plausibly-wrong character (e.g. context demands one character but
   OCR produced a visually similar but semantically wrong one), flag
   it inline:

   ```
   [OCR: <what OCR produced> → likely <what context suggests>]
   ```

   If you're confident enough to silently correct, you're overstepping.

2. **Mark interpretive passages.** When a section is reconstructed
   from fragmentary OCR rather than confidently read:

   ```
   *[Interpretive. OCR for this section is fragmentary; the English
   below captures the apparent structure but specific phrasings are
   uncertain.]*
   ```

3. **Preserve illegibility markers.** If the OCR contains `□` or
   another illegibility marker, carry it through as `[illegible]` or
   keep the `□`.

4. **Spot-check confidence scores.** The `.json` sidecar carries
   per-line confidence. If a critical term sits in a low-confidence
   region, say so in a footnote-style aside.

5. **Never back-translate from English.** The English gloss of a
   passage must be supported by the Japanese in the OCR. Don't extend
   coverage into passages where the underlying transcription is
   genuinely illegible — leave them flagged.

## Editorial apparatus

- **Cross-references within the book**: parentheticals like
  `(see page N)`. Do not invent section IDs the manuscript doesn't
  use.
- **Cross-references to external frameworks**: light touch. A brief
  parenthetical noting an obvious parallel to a Western
  technical-analysis concept is acceptable, but it should never
  become the primary gloss for an indigenous concept. The Japanese
  name and meaning come first; the parallel is supplementary.

## What NOT to do

- Do not write content that isn't grounded in the OCR.
- Do not summarize pages you can't translate; mark them interpretive
  or leave a `[TODO: transcription dense here — revisit]` stub.
- Do not add bulleted "takeaway" sections, modern trading advice, or
  motivational framing.
- Do not translate the Japanese title in running text.
- Do not generate files, headings, or content beyond the page range
  you were asked for.
- Do not consult `../translation/` (v1) at any point, for any reason.

## Working checklist for each page

1. Read `../transcription/page_XXXXX.txt` in full.
2. Spot-check `../transcription/page_XXXXX.json` for any line with
   confidence under ~0.6 — those deserve OCR flags.
3. Identify section breaks (◯ / □ markers, layout shifts).
4. Draft the page in the skeleton above.
5. On first mention of each term, add `(*romanization*)`.
6. Confirm every paragraph has a basis in the OCR. If not, flag as
   interpretive or cut.
