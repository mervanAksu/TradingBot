---
concept: Displacement
aliases: [energetic move, speed and distance, unmistakable displacement]
status: VERIFIED
confidence: low
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026]
default_variant: proxy - large body vs ATR, closes near extreme, leaves an FVG
---

## Definition (own words, 2-4 sentences)
A fast, large-bodied move (one to a few candles) that clearly breaks away from prior prices, typically leaving an FVG and
breaking a swing. The series never give numbers ("handles, not ticks", "energetic", "unmistakable"); the proxy below is our
own and must be tested by buckets.

## Detection rule
```
displacement bar i (bullish): close>open and body[i] >= disp_body_atr * ATR(14,tf) and (close-low)/(high-low) >= disp_close_pos
displacement leg: <= disp_max_bars consecutive same-direction bars with sum(body) >= disp_leg_atr*ATR and >= 1 FVG created
optional absolute floor: body >= disp_min_ticks
output: flag per bar / leg{start,end,size_atr}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| disp_body_atr | 1.0 | 0.6-2.0 | proxy (2022-b01/005@20:09 "energetic") |
| disp_close_pos | 0.7 | 0.5-0.9 | proxy |
| disp_leg_atr | 1.5 | 1-3 | proxy |
| disp_max_bars | 3 | 1-5 | proxy |
| disp_min_ticks (NQ 1m) | 0 (off) | 0-80 | "handles not ticks": 2025-b01/003@13:17 |

## Invalidation / mitigation
- n/a (qualifier). Lethargic reaction after a raid = pass (2022-b01/005@21:12).

## Role in MMXM
- Qualifies MSS, FPFVG, SMR departure; stage-2 speed test: stage-2 leg reaches target in fewer bars than stage 1 (2026-b05/089@36:14).

## Evolution across series
- DRAFT body >= k x ATR kept as proxy; 2025 explicitly not an ATR notion but qualitative; 2026 "engulfing alone is not a shift".

## Ambiguities
- Entirely a proxy; report results by displacement bucket.

## Refs
- `2023-b01/009@10:36` speed and distance.
- `2025-b02/009@18:58` FPFVG needs unmistakable displacement.
