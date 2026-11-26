---
concept: Wick CE (wick as gap)
aliases: [premium wick, discount wick, gray pool, obsidian, bolo]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: wick measured from body edge to extreme, graded 0/25/50/75/100
---

## Definition (own words, 2-4 sentences)
A prominent wick is treated as a gap: the span from the body edge to the wick extreme, with its CE (50%) as the key level.
On a premium (upper) wick a bearish read needs bodies to stay in its lower half; on a discount (lower) wick a bullish read
needs bodies in its upper half. A body close through the CE is the warning/exit; a close beyond the CE in the trade
direction signals follow-through. A wick adjacent to an FVG takes precedence over the FVG.

## Detection rule
```
upper wick of bar i: zone = [bodyHi[i], high[i]] ; lower wick: [low[i], bodyLo[i]]
prominent if (wick_len >= wick_min_atr * ATR(14,tf)) or bar i is a swing extreme (swing-points.md) on D/W/4H/1H
levels: q0, q25, ce=q50, q75, q100 (gradient-levels.md)
bearish respect on upper wick: no close > ce (strict) after first touch; wick pokes up to poke_ticks allowed
raid confirmation (turtle-soup.md): raiding bar closes back beyond the CE of its own wick, else wait 1 bar (trade-executions b02/062@14:25)
composites:
  gray_pool = zone between CEs of two adjacent wicks at an extreme (2026-b06/092@11:33)
  obsidian  = zone between CEs of two opposing wicks (2026-b02/027@20:49)
  bolo      = rejection-block body edge + adjacent wick CE; no-entry zone (2026-b06/099@18:42)
wick selection when several: lowest-reaching premium wick / longest wick (wick_select param)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| wick_anchor | body_edge | body_edge, full_range | 2024-b04/008@07:46; 2025-b04/041@01:07 (open question 2023-b04/028@16:03) |
| wick_min_atr | 0.5 | 0.2-1.5 | proxy for "large wick" |
| wick_select | longest | longest, lowest_reaching, most_respected | 2025-b02/006@11:04 |
| wick_tfs | D, W, 1H + exec TF | | 2023-b02/010@00:00 |

## Invalidation / mitigation
- Body close through CE = idea weakens/exit part; premium wick that price trades above flips into discount array (2025-b04/041@01:07).

## Role in MMXM
- SMR location (daily premium wick CE / quadrant as reversal zone, 2025-b04/040; 2025-b04/053@25:40).
- Partial ladder: wick CE -> wick lower quadrant -> low (2024-b04/008@106:18).

## Evolution across series
- 2023: wick CE as reaction level; 2024: wick is a gap (body edge to extreme); PAC/trade-exec: wick grading as main tool; 2025: five levels for every D/W wick; 2026: wick left of a gap overrides it; composites.

## Ambiguities
- Prominence threshold; which wick of a stack.

## Refs
- `2024-b04/008@07:46` measure from body edge.
- `price-action-chronicles b01/011@11:01` wick beats adjacent FVG.
- `2026-b01/001@17:58` wick = gap.
