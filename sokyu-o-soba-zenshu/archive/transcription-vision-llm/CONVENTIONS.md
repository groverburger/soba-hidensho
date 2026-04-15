# Transcription Conventions

This folder contains a character-level transcription (翻刻, *honkoku*) of the
page images in `../宗久翁相場全集_804042_0001/`. Each file corresponds to one or
more page-images and records the Japanese text as read from the Meiji-era
woodblock print, with confidence annotations.

## Purpose

This transcription serves as the auditable intermediate step between the
scanned page images and any subsequent English translation. Any reading
of the original that informs an English text should be traceable to a specific
line here.

## Source

**宗久翁相場全集** (*Sōkyū-ō Sōba Zenshū*, "Complete Works of Old Man Sōkyū on
Markets")

- Author: 本間宗久 (Honma Sōkyū), with annotations by 早坂二菊 (Hayasaka Nikiku)
- Publisher: 信義堂書店 (Shin'gidō Shoten), Tokyo
- Date: Meiji 43 (1910)
- Source scans: 100 images from digital archive (804042_0001)

## Page numbering

"Page" numbers refer to scan file numbers (`0001_0000.jpg` = page 1, etc.).
Each image except the cover and back cover shows a two-page spread (right page
and left page of the open book). Within each file, text is presented in reading
order: right page first, then left page; within each page, columns are read
right to left, top to bottom.

## Page layout

| Pages | Content |
|-------|---------|
| 1 | Cover (表紙) |
| 2 | Preface (緒言) |
| 3 | Editorial notes (凡例) |
| 4-7 | Biography (本間宗久翁小傳) and historical context |
| 8-14 | Table of contents (目次) for 上巻 and 下巻 |
| 15 | Title page for body text + start of 上巻 chapter 1 |
| 16-62R | 上巻 body text (73 chapters). 上巻了 on page 62R |
| 62L | 下巻 title page + start of 下巻 chapter 1 |
| 63-87 | 下巻 body text (66 chapters) |
| 88 | ■ MISSING PAGE (欠) — not in source archive |
| 89-93 | Historical rice price data tables (安永 era) |
| 94R | Final data entries |
| 94L | Colophon (奥付): Meiji 43 (1910), 信義堂書店 |
| 95-96 | Publisher advertisements |
| 97-100 | Blank pages / back cover / library card |

## Confidence markup

| Markup | Meaning |
|--------|---------|
| 米 | Confident reading |
| 米(?) | Best-guess reading; character is plausible but not certain |
| [米/来] | Two or more equally plausible readings |
| □ | Illegible character (shape visible but unreadable) |
| ■ | Missing or destroyed (paper damaged, text lost) |
| (...) | Omitted passage (e.g., repeated text, standard colophon) |
| 〈note〉 | Inline editorial note about the reading |

## Confidence ratings

Each section is tagged with an overall confidence level:

- **HIGH** — Characters are clearly legible in the image; reading is
  unambiguous.
- **MEDIUM** — Most characters legible; some require contextual inference or
  are partially obscured. Reasonable readers might disagree on 1-3 characters.
- **LOW** — Significant portions are obscured, damaged, or faded.
  The transcription is a best-effort reconstruction. Multiple alternative
  readings are possible.

## Text formatting

- Section headers visible in the manuscript (often in larger characters or
  with distinct formatting) are set on their own line and prefixed with `###`.
- Chapter numbers (第一章, 第二章, etc.) are preserved as they appear.
- Running headers (柱, *hashira*) at the top of pages are noted where legible.
- Modern punctuation (、。) is added for readability; the original text
  uses traditional punctuation marks (句読点) sparingly.
- Furigana (振り仮名) readings printed alongside kanji are noted in
  parentheses where they appear in the original, e.g., 相場(そうば).

## Relationship to other folders

- `../宗久翁相場全集_804042_0001/XXXX_0000.jpg` — source image for each transcription
