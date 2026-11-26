---
name: transcript-digest
description: Use when processing ICT transcripts in transcripts/_clean/ into the knowledge base. Defines the map (batch notes) → reduce (series digest) → synthesize (cards, key-levels, MMXM spec) pipeline and the note format.
---

# Pipeline
Batches are listed in `_work/batches.json` (≈75k words each, playlist order).

| Stage | Agent | Reads | Writes (only this) |
|---|---|---|---|
| map | series-researcher (1 per batch) | the batch's files | `kb/notes/<batch-id>.md` |
| reduce | series-researcher in reduce mode (1 per series) | `kb/notes/<series>-b*.md` | `kb/series/<series>.md` |
| synthesize | synthesizer | `kb/series/*.md` (+ notes on demand) | `kb/concepts/*.md`, `kb/key-levels.md`, `kb/mmxm-spec.md`, `kb/open-questions.md` |

Map agents run in parallel, so they never edit shared files.

# Map: note format (`kb/notes/<batch-id>.md`)
Read each file fully, in order. After each file append its entry immediately (keeps the working set small):
```
### <NNN> | <yyyymmdd> | <short title>
tags: <concepts touched, canonical names from kb/key-levels.md>
- RULE: <mechanical rule in own words: candle conditions, times, %, TF> (@mm:ss)
- DEF: <definition that differs from key-levels.md DRAFT or from earlier series> (@mm:ss)
- MMXM: <phases, entries, targets, invalidation, examples with date+instrument+TF> (@mm:ss)
- CTX: <bias / time / session-phase logic: consolidation→expansion→retracement/reversal> (@mm:ss)
- EX: <worked chart example: date, instrument, TF, what happened> (@mm:ss)   (max 3 per file)
- skip: <if mostly commentary/Q&A/personal, say so in one line>
```
Only lines with content; 5-25 lines per file. Refs use the file's [mm:ss] markers.

End the batch file with:
```
## Batch summary
- Top mechanical rules (≤10)
- Definition changes vs DRAFT (≤10)
- New concepts not in key-levels.md
- Open questions
```

# Reduce: `kb/series/<series>.md`
Merge the batch notes of one series: Core teachings (10-25 bullets) · Mechanical rules table (rule | concept | refs) ·
Definitions vs DRAFT / other series · MMXM material · Session-phase logic · Discretionary items needing a proxy · Open questions.
Refs as `<batch-id>/<NNN>@mm:ss`.

# Constraints (all stages)
- Own words, always. The KB is a set of operational definitions, not a record of the lectures:
  no transcript sentences, no close paraphrase of a passage; a quote is at most a short phrase with a ref.
- Auto-subs mishear terms ("fair value cap", "order lock"): normalise to canonical names.
- Prefer precision over coverage: one exact rule beats five vague paraphrases.
