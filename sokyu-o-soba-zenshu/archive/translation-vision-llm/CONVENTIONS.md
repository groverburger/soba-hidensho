# Translation Conventions

This folder contains an English translation of the 宗久翁相場全集 (*Sōkyū-ō Sōba
Zenshū*, "Complete Works of Old Man Sōkyū on Markets"), derived from the
character-level transcription in `../宗久翁相場全集_transcription/`.

## Pipeline

```
original scans  →  transcription (翻刻)  →  translation  →  published book
../宗久翁相場全集_804042_0001/    ../宗久翁相場全集_transcription/    this folder
```

Every English sentence should be traceable back to a specific passage in the
transcription files. The translation works from the transcription only — not
directly from the manuscript images.

## Glossing conventions

- Key Japanese terms are given in romanization on first use, with the original
  characters: e.g., *tensō* (天井, market top/ceiling).
- Trading terminology is translated consistently throughout. A glossary of
  recurring terms is maintained in `glossary.md`.
- Where the transcription marks a character as uncertain (?), the translation
  notes this if it materially affects the meaning.

## Section format

Each translation file covers the same page range as its corresponding
transcription file. Sections are headed by chapter number and a translated
title.

## Uncertainty

Where the transcription is uncertain (marked with ?) and the meaning is
consequently ambiguous, the translation provides the most likely reading and
notes alternatives in square brackets: [alt: ...].

## Relationship to other folders

- `../宗久翁相場全集_transcription/pages_XX-XX.md` — source transcription
- `../宗久翁相場全集_804042_0001/XXXX_0000.jpg` — original page scans
