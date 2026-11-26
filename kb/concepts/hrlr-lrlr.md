---
concept: HRLR / LRLR (High / Low Resistance Liquidity Run)
aliases: [held market, manual intervention, barcode, spotty tape, time distortion]
status: VERIFIED
confidence: medium
category: liquidity
series_seen: [2023, 2024, 2025, 2026, trade-executions, price-action-chronicles]
default_variant: regime sense - candle overlap and FVG cadence over a rolling window
---

## Definition (own words, 2-4 sentences)
Two senses coexist. Path sense (DRAFT, early 2024): a pool is a low-resistance run if no opposing unfilled arrays sit between
price and it. Regime sense (later 2024-2026, dominant): LRLR = separated, stretched candles that leave gaps open and hit
targets without re-tests; HRLR = overlapping "barcode" candles, arrays re-touched and closed through. Trade normally only in
LRLR; in HRLR stand aside or cut size, partial early, no trailing.

## Detection rule
```
regime (rolling window of hr_window bars on exec TF, default 30 x 1m):
  overlap_i = overlap(range_i, range_{i-1}) / range_{i-1}
  ov = mean(overlap_i) ; fvg_rate = FVGs created per 15 minutes ; touches = mean bars inside an active array
  HRLR if ov >= hr_overlap (0.5) or fvg_rate < hr_fvg_rate (1 per 15 min) or touches >= 3
  LRLR if ov <= 0.35 and fvg_rate >= 1 ; else NEUTRAL
day priors (flags): CPI/PPI week Mon/Tue, no-news Monday at 09:30, ORG < 75 handles, summer/holiday weeks
path sense: count unfilled opposing arrays (FVG/NDOG/NWOG/OB) between price and target pool -> path_resistance
held market: >= 3 re-entries into the FPFVG after its CE was tagged (2024-b10/033@41:12)
output: regime in {LRLR, NEUTRAL, HRLR} per bar ; path_resistance per target
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| hr_window | 30 bars | 15-90 | proxy |
| hr_overlap | 0.5 | 0.3-0.7 | 2024-b14/049@122:36 ("at least half") |
| hr_fvg_rate | 1 per 15 min | 0.5-2 | 2025-b05/065@19:29 |
| hr_touch_max | 3 | 2-5 | 2026-b05/084@33:33 (1-2 healthy, 3-5 lower odds) |
| hr_mode | regime | regime, path, both | 2024-b07/020@72:10 vs 2024-b11/036@93:23 |

## Invalidation / mitigation
- Re-evaluated every bar.

## Role in MMXM
- Gate for entries (HRLR = no new entry or reduced score); management switch (HRLR: stop to cost only, partial each new extreme, 2024-b11/036@107:07).

## Evolution across series
- DRAFT path sense; 2023 "spotty"/index disagreement; 2024 shift to regime; 2025 FVG cadence; 2026 barcode/overlap.

## Ambiguities (open questions for the user)
- Use as hard gate or score penalty.

## Refs
- `2024-b14/049@113:55`; `2025-b05/065@19:29`; `2026-b10/128@10:40`.
