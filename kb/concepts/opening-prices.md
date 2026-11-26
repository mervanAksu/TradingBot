---
concept: Opening prices (data highs/lows, true day open)
aliases: [midnight open, true day open, 08:30 open, 09:30 open, 13:30 open, 18:00 open, weekly open, MOR]
status: VERIFIED
confidence: high
category: liquidity
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: 00:00 NY open is the daily premium/discount anchor; session opens fractal
---

## Definition (own words, 2-4 sentences)
Opening prints anchor intraday premium/discount: on a bullish day buy at/below the midnight open (and below the 08:30 / 09:30
open), on a bearish day sell at/above. The midnight open is also a magnet and first resistance on a rally. 2025 extends it to
a 30-minute midnight opening range with projections.

## Detection rule
```
open_at(T) = open of the 1m bar starting at T (NY) for T in {00:00, 08:30, 09:30, 13:30, 18:00}; weekly = Sun 18:00
line extends to 11:00 (midnight) or session end
governing rule (2022-b01/019@94:38): bullish -> use midnight open; if 08:30 open is below it use 08:30; below both = best location
MOR = 00:00-00:30 H/L/O; projections 0.5, 1 of its height (sd-projection.md)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| anchor_open | 00:00 | 00:00, 08:30, 09:30, 18:00 | 2023-b01/006@22:38 |
| mor_proj | 0.5, 1 | | 2025-b06/080@09:59 |

## Invalidation / mitigation
- n/a (reference lines).

## Role in MMXM
- Entry location gate (price on the correct side of the open) and first partial (just under midnight open on a long, trade-executions b01/059@07:20).

## Evolution across series
- Consistent; 2025 adds MOR.

## Ambiguities
- None material.

## Refs
- `2022-b01/019@94:38`; `2023-b04/043@15:08`; `2025-b06/080@23:18`.
