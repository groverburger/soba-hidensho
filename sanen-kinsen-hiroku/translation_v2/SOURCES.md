# External sources for translation_v2

This translation is grounded in the NDL-OCR output in `../transcription/`.
This file records the **external bibliographic sources** cited in the
edition — separated out so that every fact in the translation files that
comes from outside the OCR is traceable to a named catalogue record.

## The manuscript

The source manuscript is held at **Kyoto University Library**, Tanimura
Collection. Its RMDA record is the authoritative bibliographic witness
for this edition.

**Catalogue entry:**

- **Record ID:** RB00012360
- **URL:** https://rmda.kulib.kyoto-u.ac.jp/item/rb00012360
- **Title:** （校正）三猿金泉秘録 — *(Kōsei) Sanen Kinsen Hiroku*
- **Author:** 牛田権三郎 — *Ushida Gonsaburō*
- **Editor / proofreader:** 鳴川猛之助 — *Narukawa Takesuke*
- **Physical description:** 1 volume; 24 cm.
- **Shelfmark:** 9-64/サ/1
- **Accession number:** 91006836
- **Collection:** 谷村文庫 (Tanimura Collection / Tanimura Bunko), subset サ
- **Repository:** Kyoto University Library
- **Rights:** Open access for secondary use

**Nature of the witness.** Per the RMDA catalogue note, this is a
**manuscript copy** (写, *utsushi*) of the Kaei-4 (1851) printed edition
by 好問堂 (*Kōmondō* / *Kōmonontei*). The 1851 printed edition is the
first appearance of Narukawa's corrected recension; the Kyoto copy in
hand is a later hand-copy of that printing.

This fact resolves several readings that are ambiguous in the OCR alone:

- The cover accession stamp **`91006836`** matches the RMDA accession
  number — confirming that the NDL-OCR source images are of this
  specific Kyoto University holding.
- The seal on page 2 reading **嶋田君寄贈** (*Shimada-kun kizō*,
  "donated by Mr. Shimada") is an ownership inscription on the Kyoto
  copy; it does not belong to the author or editor.
- The library-side labels on pages 1–2 carrying **谷村文** are the
  leading characters of **谷村文庫** (Tanimura Collection).
- The publication date *Kaei 4, fifth month, third day* (1851) appearing
  in the colophon on page 32 matches the date of the printed edition
  the Kyoto manuscript copies.

## Reading of Narukawa's personal name

The RMDA record romanises 鳴川猛之助 as **Narukawa Takesuke**. The v1
draft in `../translation/` read the same characters as *Mōnosuke* or
*Takenosuke*. We follow RMDA.

The colophon on page 32 signs the editor as 鳴川繁楽 (*Narukawa
Shigeraku*) — a literary style rather than the formal name on the
printed colophon. The identification of **猛之助 = 繁楽** is treated
in the edition as probable but not proven: the RMDA entry itself only
records 猛之助.

## 好問堂 (Kōmondō)

The publisher named in the RMDA catalogue note. A Kaei-period
publisher's imprint; its location is **not** given in the RMDA record
itself. The v1 draft read the partial OCR string `五十瀬津` as the
place-name **五十嵐津** (*Igarashi-tsu*) by collation against a
"published scholarly record" that we have not been able to reconfirm
from a primary catalogue entry. Until a sourced citation for that
reading can be added here, this edition preserves the OCR `五十瀬津`
and flags the reading as uncertain.

## The transcription toolchain

The `.txt` / `.json` / `.xml` transcriptions in `../transcription/`
are the mechanical output of **NDL 古典籍OCR-Lite**
(https://github.com/ndl-lab/ndlkotenocr-lite), a toolchain published
by Japan's National Diet Library for Edo-period classical texts
(RTMDet text-region detection + PARSeq recognition). The OCR is
character-level and context-free; it does not understand meaning and
cannot interpolate from a prior English translation. This is the
property that grounds the edition's uncertainty accounting.

## What this file is NOT

This file does not reproduce content from the `../translation/` (v1)
draft. Where v1 contains a reading we have adopted, the adoption is
justified by (a) the RMDA catalogue, (b) the manuscript page image
(`../original-manuscript/page_XXXXX.jpg`), or (c) a standard reference
work cited at point-of-use in the translation file itself. A v1
reading alone is never the basis for an edition-level claim.
