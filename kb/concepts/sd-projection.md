---
concept: Standard Deviation (SD) / Fib Projections
aliases: [measured move, -0.5/-1/-2 extension, 1.25 projection, fulcrum, opening-range extension]
status: VERIFIED
confidence: medium
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: project a reference range beyond its broken extreme by multiples of its height; target only when it converges with a real level
---

## Definition (own words, 2-4 sentences)
Take a reference range (a leg, a session range, an opening range, a gap) and project multiples of its height beyond the
extreme that breaks: -0.5, -1, -1.5, -2, -2.5 (and beyond). Projections are measurement tools, not targets on their own;
they become targets when they converge with a pool, gap CE or array, or with a second projection.

## Detection rule
```
ref range R (hi, lo) by sd_ref; direction d = side that was broken
levels_down = lo - k*(hi-lo) for k in sd_levels ; levels_up mirror
anchors: bodies (default for leg/range, trade-executions b01/009@11:28) or wicks
converged(level) = exists pool/gap-CE/array edge or another projection within sd_conv_ticks
sd_ref options: leg (swing low->high, ITL/LTL anchored), pre_news 07:00-08:29, range_07_09, OR 09:30-10:00, FHDR,
                ORG (unit = gap height), MOR 00:00-00:30, final_hour 15:00+, breaker A->B leg, displacement leg (open c2 -> extreme, 1.25)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| sd_levels | 0.5, 1, 1.5, 2, 2.5 | up to 4, 8 | 2023-b04/029@36:33; 2025-b04/044@05:34 |
| sd_anchor | body | body, wick | trade-executions b01/009@11:28; 2026-b04/074@19:34 |
| sd_conv_ticks | 8 | 0-20 | 2024-b10/031@54:08 (only with real level) |
| sd_ref | leg | see list | per model |

## Invalidation / mitigation
- n/a (levels). Do not rest orders exactly on published round projections (2026-b02/032@31:46).

## Role in MMXM
- Partial/target levels in distribution stages; -0.5 of 07-09 range = projected session extreme; 1.25 = max-run.

## Evolution across series
- foundations: 1/1.5/2.5/3/3.5x FX, 0.5/1x ES. 2023: SD replaces fib retracement. 2024: only with a real level. 2025: OR/MOR extensions. 2026: ORG-height SD, 1.25, fulcrum.

## Ambiguities
- Which reference range per model; body vs wick.

## Refs
- `price-action-chronicles b01/008@10:11` pre-news range -2 SD.
- `2026-b01/008@25:18` ORG -0.5/-1/-2 SD with pool convergence.
