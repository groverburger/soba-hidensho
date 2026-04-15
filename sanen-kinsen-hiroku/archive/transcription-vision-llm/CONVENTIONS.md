# Transcription Conventions

This folder contains a character-level transcription (翻刻, *honkoku*) of the
manuscript images in `../original-manuscript/`. Each file corresponds to one or
more page-images and records the Japanese text as read from the cursive script,
with confidence annotations.

## Purpose

This transcription serves as the auditable intermediate step between the
manuscript images and the English translation in `../translation/`. Any reading
of the original that informs the English text should be traceable to a specific
line here.

## Page numbering

"Page" numbers refer to image file numbers (`page_00001.jpg` = page 1, etc.).
Each image except the cover and back cover shows a two-page spread (right page
and left page of the open book). Within each file, text is presented in reading
order: right page first, then left page; within each page, columns are read
right to left, top to bottom.

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
- **LOW** — Significant portions are in dense cursive, damaged, or faded.
  The transcription is a best-effort reconstruction. Multiple alternative
  readings are possible.

## Furigana and reading marks

The manuscript contains several types of small annotations alongside the
main text. These are recorded using the following conventions:

### Furigana (振り仮名 / 読み仮名)

Small kana written to the right of kanji in the manuscript, indicating the
author's or editor's intended reading. Recorded using double angle-bracket
ruby markup (aozora bunko style):

| Markup | Meaning |
|--------|---------|
| 漢字《かんじ》 | Furigana clearly legible in the manuscript |
| 漢字《かんじ(?)》 | Furigana present but partially uncertain |
| 漢字《□□》 | Furigana visible but illegible |

Examples:
- `人気《じんき》` — manuscript furigana confirms the reading *jinki*
- `順来《じゅんらい》` — reading gloss present in the manuscript
- `転換《てんかん(?)》` — furigana present but second kana uncertain

When NO furigana is present for a given kanji, no ruby markup is added.
The absence of markup means the manuscript itself does not gloss that term.

### Kundoku marks (返り点)

Reading-order marks used in kanbun (漢文) passages to indicate Japanese
word order. Recorded inline using standard notation:

| Mark | Notation | Meaning |
|------|----------|---------|
| レ | `〈レ〉` | Read the next character first, then return |
| 一二三 | `〈一〉〈二〉〈三〉` | Numbered reading sequence |
| 上中下 | `〈上〉〈中〉〈下〉` | Alternate ordering for nested clauses |

Example: `静〈レ〉にして陰を生ず` — the レ mark inverts the two characters.

### Okurigana (送り仮名)

Small kana suffixes written alongside kanji to show grammatical inflections.
These are transcribed inline as part of the main text stream (they are not
distinguished from base-text kana). Where the okurigana is notably placed
*beside* rather than *after* the kanji (i.e., as a marginal annotation
rather than inline text), note this with `〈okuri:〉`:

Example: `動〈okuri: て〉` — the て is written as a marginal annotation.

## Text formatting

- Section headers visible in the manuscript (often in larger characters or
  with circle markers ◯) are set on their own line and prefixed with `###`.
- Red-ink annotations or markings in the original are noted as
  `〈red ink〉` or `〈red circle marker〉`.
- Modern punctuation (、。) is added for readability; the original manuscript
  has none.

## Relationship to other folders

- `../original-manuscript/page_XXXXX.jpg` — source image for each transcription
- `../translation/pages_XX-XX.md` — English translation derived from this transcription
- `../sanen-kinsen-hiroku.tex` — final typeset edition
