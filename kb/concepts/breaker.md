---
concept: Breaker Block
aliases: [breaker, unicorn (breaker + FVG overlap), reaper (IFVG + breaker, 2023)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [2022, 2023, 2024, 2025, 2026]
default_variant: 3-swing sequence with sweep, zone = candle(s) at the middle swing, bodies only
---

## Definition (own words, 2-4 sentences)
A failed swing after a liquidity sweep. Bearish: swing high H1, swing low L, higher high H2 that sweeps H1, then price breaks
below L; the down-close candle(s) that formed L (before the rally to H2) become resistance. Bullish mirror: low L1, high H,
lower low L2 sweeping L1, then break above H; the up-close candle(s) at H become support. Judged on bodies.

## Detection rule
```
bearish breaker (mirror for bullish):
  swings (swing-points.md, 3-bar, tf): H1 (STH), then L (STL) after H1, then H2 > H1 + sweep_min_ticks (sweep, turtle-soup.md)
  trigger: after H2, a bar trades below L (brk_mode="trade") or closes below L (brk_mode="close")
  block = run of down-close candles ending at the bar that made L (the last down-close candles before the rally to H2)
     breaker_zone = [min bodyLo, max bodyHi] of that run (bodies) ; MT = mid ; full-range variant includes wicks (2025-b03/012@07:21)
  validity: while no close > MT (or > zone top in loose mode)
  unicorn flag: breaker_zone overlaps an FVG/IFVG formed by the break leg (2026-b04/067@12:55)
output: zone{top,bottom,mt,dir=bearish,H1,L,H2,created_at=trigger bar}
entry: lower half of zone (MT, lower octant, lowest quadrant ...); stop above H2? no -> above the candle that created the
       sell-side imbalance / above zone top + 1 tick (2026-b02/036@18:32); conservative: above H2
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| brk_mode | trade | trade, close | MSS convention, see mss.md |
| breaker_zone | bodies | bodies, full_range | 2023-b07/081@12:35; 2025-b03/012@07:21 |
| breaker_stop | zone_top+1 tick | zone_top, H2 | 2026-b02/036@18:32 |
| sd_projection | A->B leg x1 (x2 seen) | 1-2 | 2023-b06/070@36:26 |

## Invalidation / mitigation
- Body close through MT (bearish: above MT) = failed. Original breaker preferred over later ones (2023-b04/029@16:52).

## Role in MMXM
- Part of SMR confirmation (breaker forms then close through an FVG: 2026-b05/082@03:03).
- Entry E3 (breaker of the SMR swing, 2024-b07/020@08:43) and 2nd-stage re-distribution entry as unicorn (2026-b04/067@12:55).

## Evolution across series
- 2022: buy-side run then break of prior short-term low; zone = last down-close candle before the run.
- 2023: 3-swing definition with bodies; unicorn = FVG inside breaker after 09:30 sweep; breaker SD projection.
- 2024: whole run of opposite candles; most sensitive = last candle; upper half when bullish.
- 2025: full range incl. wicks, judged by bodies.
- 2026: lowest-bodied down-close candle; entries on lower-half grid levels.

## Ambiguities
- Name "unicorn": 2025 uses it for the 2nd-stage leg itself; 2023/2026 for breaker+FVG. KB uses the breaker+FVG meaning.

## Refs
- `2023-b01/007@22:33` breaker definition, bodies; unicorn.
- `2026-b02/036@12:19` bearish breaker sequence and entry ladder.
