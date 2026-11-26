---
concept: Suspension Block
aliases: []
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2025, 2026, price-action-chronicles, trade-executions]
default_variant: one candle with a volume imbalance on both sides
---

## Definition (own words, 2-4 sentences)
A displacement candle that has a volume imbalance against the prior candle AND against the next candle. The box runs from
the outer edge of one VI to the outer edge of the other (bodies, wicks excluded); its CE is a bias pivot. When traded through
by a body it flips like an IFVG.

## Detection rule
```
bullish at bar [0] for middle candle [1]:
   VI_low  between [2] and [1]: bodyLo[1] > bodyHi[2]
   VI_high between [1] and [0]: bodyLo[0] > bodyHi[1]
   (wick overlap allowed or not required; neighbours may overlap)
   box = [bodyHi[2], bodyLo[0]] ; ce = mid ; quadrants
bearish mirror
fail/flip: body close beyond far edge -> inverted (as ifvg.md)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| vi_min_ticks | 1 | 1-4 | volume-imbalance.md |

## Invalidation / mitigation
- Bearish stance invalid on a close above CE (daily use, 2026-b11/135@06:44).

## Role in MMXM
- HTF premium/discount array for SMR location (2026-b06/095@24:52 sold a suspension block); weekly context (2026-b03/058).

## Evolution across series
- trade-executions: VI at the high and low of one displacement (b01/057@25:56). 2025: one candle, box from VI edges. 2026: daily 3-candle version, CE pivot.

## Ambiguities
- "Displacement" requirement on the middle candle: not stated numerically.

## Refs
- `2025-b02/009@06:39`; `2026-b11/135@00:04`.
