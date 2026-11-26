---
concept: Turtle Soup (liquidity raid reversal)
aliases: [sweep, raid, stop run, Judas (session version), Venom (2025 model), purge and revert]
status: VERIFIED
confidence: medium
category: liquidity
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: type A - trade beyond a marked pool then close back inside within n bars, confirmed by a CISD
---

## Definition (own words, 2-4 sentences)
A raid beyond a marked high/low (prior day/session/equal levels) that fails: price returns inside and reverses. ICT's sense is
not the 20-day Turtle fade but any raid inside a narrative, entered either at the raid (aggressive), on the close back
inside, or deferred into a rejection block / IFVG. A "sweep" returns; a "run" goes through and continues (type B
continuation). A shallow 1-handle poke or a lethargic reaction is not a signal.

## Detection rule
```
pool P (relative-equal-hl.md, session-ranges.md) on side BSL (mirror SSL)
raid bar r: high[r] >= P.level + ts_min_poke_ticks*tick
confirm (ts_confirm):
  "close_back" (default): some bar c in [r, r+ts_n] with close[c] < P.level
  "wick_ce": raid bar closes below its own upper-wick CE, else next bar does (trade-executions b02/062@14:25)
  "cisd": CISD (cisd.md) bearish within ts_n bars of r
  "body_run" (2024 type A): a BODY closed above P.level (run by bodies) then CISD
fail: a later close above max(high[r..c]) before target = run (type B continuation)
quality: + SMT divergence (smt.md), + inside HTF premium array, + inside macro window, + staged raid (two pools)
output: event{dir, P, raid_high, raid_bar, confirm_bar, mode}
type B (continuation, 2024-b04/008@143:51): any FVG entry beyond an old extreme in the direction of the program
Venom (2025-b04/051@08:48): short case needs a raid candle CLOSING above EQH, then two imbalances in <= 3 bars; CISD = its close
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| ts_min_poke_ticks | 1 | 1-8 | 2022-b01/005@20:09; 2026-b01/015@03:12 (1-handle poke no signal) |
| ts_confirm | close_back | close_back, wick_ce, cisd, body_run | 2026-b03/056@09:27; 2024-b04/008@141:48 |
| ts_n | 3 | 1-10 | proxy |
| ts_need_smt | false (score) | bool | 2023-b03/022@167:52 |

## Invalidation / mitigation
- New extreme beyond the raid high after confirmation (bodies) = idea wrong (2025-b01/002 stop under SMR low).

## Role in MMXM
- SMR = turtle soup of the buy-side (sell model) at the end of the buy-side curve (2024-b08/024@185:00; 2025-b01/002@100:34).
- 09:30 Judas into premium read as SMR leg (2026-b04/067@09:18).

## Evolution across series
- 2022: sweep vs run; sweep of EQL not automatically a reversal. 2023: sweep + SMT + PD array, no MSS needed. 2024: types A/B, bodies. 2025: any TF, deferred entry, Venom. 2026: close back below; staged raids; inside macro.

## Ambiguities
- Whether a body close beyond the pool is required (2024/2025) or a wick poke suffices (2022/2026).

## Refs
- `2023-b06/067@17:34` turtle soup with HTF bias.
- `2024-b08/024@295:34` not the Turtle-trader fade.
- `2026-b07/104@15:34` turtle soup inside a macro.
