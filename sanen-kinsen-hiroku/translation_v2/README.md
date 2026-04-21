# *Sanen Kinsen Hiroku* — translation_v2

An English translation of **三猿金泉秘録** (*Sanen Kinsen Hiroku*),
Ushida Gonsaburō's 1755 secret-transmission manual on the rice-market
trade, in Narukawa Takesuke's corrected recension of Kaei 4 (1851),
as held at Kyoto University Library (Tanimura Collection, shelfmark
9-64/サ/1, RMDA record RB00012360).

This is a **second independent translation**, built from scratch on
the mechanical NDL OCR transcription in `../transcription/`. A prior
translation is preserved in `../translation/` (v1).

## What this edition is for

The edition is aimed at professional traders, historians of Japanese
commercial literature, and serious readers of classical Japanese
texts who care about **honest accounting of what the manuscript says
and where the uncertainty lies.** It is not a smoothed or literary
translation. Where the OCR is fragmentary, the translation says so,
in line; where a reading has been emended, the emendation is
attributed to its source at point of use.

## Edition principles

1. **OCR-grounded**. Every line of English is tied to a recoverable
   line of Japanese in `../transcription/page_XXXXX.txt`. The
   translation does not interpolate prose into passages the OCR
   cannot read.

2. **External apparatus only from named sources**. Bibliographic
   claims (author, editor, publisher, date, collection, shelfmark)
   are sourced to the Kyoto RMDA catalogue entry **RB00012360**. See
   `SOURCES.md`.

3. **Emendations justified by image**. Where a reading differs from
   the OCR output, the translation records both, with the
   justification attributed to a verification pass against the
   manuscript images in `../original-manuscript/page_XXXXX.jpg`.
   Corrections adopted wholesale from the v1 translation without
   independent verification are flagged as such.

4. **Uncertainty surfaced, not smoothed**. Every page-range file
   closes with a **Confidence** section identifying what is
   high-confidence, what is medium, and what is interpretive. The
   afterword (p. 32), the limit-extremity diagram (p. 28), and the
   era-year chronology on p. 22 are the three lowest-confidence
   passages in the book; each is flagged in place.

5. **Independent of v1**. This translation was initially drafted
   without consulting `../translation/`. The subsequent integration
   pass (see `CHANGES.md`, below) imported only those v1 emendations
   that could be independently verified against the manuscript
   image or against a named external source.

## File layout

- `STYLE.md` — the style guide the initial drafts were written to.
- `SOURCES.md` — external bibliographic metadata, with citations.
- `pages_01-02.md` — covers and library markings.
- `pages_03-04.md` — the preface; the three-monkey doctrine.
- `pages_05-09.md` — seasonal verses; the 38-verse song; the 15
  prohibitions.
- `pages_10-13.md` — trading ladders (pp. 10–11) and the four-stage
  method-cycle diagrams (pp. 12–13: *hanban*, *anraku*, *tenpen*).
- `pages_14-16.md` — the *banzai unki hōkyō-roku* almanac; tides;
  winds.
- `pages_17-20.md` — the nine essentials; the three virtues
  (智仁勇).
- `pages_21-22.md` — rice-and-field totals; the three-tier world
  estimation; opening of the five bullish secrets.
- `pages_23-26.md` — five bullish / five bearish secrets; *seven
  fortunes* (七福即生); reverse-accumulation trade.
- `pages_27-29.md` — the six-part limit trade; standby; hidden-color;
  the radial **三割上下割之圖** diagram.
- `pages_30-31.md` — function of the bull / function of the bear;
  the three first-tier secrets; closing maxims.
- `pages_32-33.md` — the editor's afterword (Narukawa, 1851) and
  final leaf.

## Page groupings

The files follow the manuscript's natural section breaks, not a
fixed grid. Short prefatory material and single-topic sections get
their own small files; longer continuous body sections are grouped.
The v1 translation's fixed 4-page files occasionally split a section
across files (e.g. the three virtues run across v1's 17-20 and 21-24
files); the present grouping keeps each section intact wherever
possible.

## How to read the apparatus

- `[OCR: X → Y]` — the OCR produced *X*; the translation adopts *Y*.
  The entry is always followed by a short justification.
- `*[Interpretive. …]*` — opens a passage where the OCR is
  fragmentary and the English captures apparent sense rather than
  line-for-line meaning. Not citable without image audit.
- `[illegible]` / `□` — preserves the OCR's illegibility markers.
- `(*romanisation*)` — on first use of a technical term,
  place-name, or stage marker.

## How v2 relates to v1

v1 is a longer, more scholarly-apparatus-heavy draft that assumes
access to external bibliographic records and reconstructs readings
in places where the OCR is weak. v2 is a tighter, OCR-first reading
that flags rather than reconstructs. The two complement each other:
v1 is more generous with scholarly context; v2 is more honest about
what the transmitted witness actually says. For publication as a
scholarly edition with a clear accounting of evidence, v2 is the
correct base; v1 is referred to at points of use where its
emendations have been independently verified.
