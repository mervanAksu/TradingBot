---
concept: Gradient Levels (quadrants / octants) and tethering
aliases: [grading, quadrant grading, octants, sixteenths, tethered array, common gap (untethered)]
status: VERIFIED
confidence: medium
category: structure
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: quadrants (0/25/50/75/100) on anchor ranges; octants optional; tethered = key candle within tether_ticks of a level
---

## Definition (own words, 2-4 sentences)
Any range or array (gap, wick, OB body, session range, 20-day box, prior month range) is split into quadrants and, when
needed, octants or sixteenths. Candle bodies are judged against these lines ("levels, not zones"). A PD array is "qualified"
(tethered) only when its key candle, edge or CE touches a gradient level of a higher-order range; untethered gaps are common
gaps. Two independent grids meeting at one price mark a preferred objective.

## Detection rule
```
grid(R, n): levels R.lo + f*(R.hi-R.lo) for f in {0, 1/n, ..., 1}; n = 4 (quadrants, default) | 8 (octants) | 16
anchor ranges (grid_anchors): box20, prior_month, prior_day, ORG (today+3), NDOG/NWOG (>= 20 handles), range_07_09, OR, FHDR,
                              daily/weekly wick, daily FVG/OB body
tethered(array A) = exists level L in grids(anchors) with |L - x| <= tether_ticks for x in {A.c2 high/low, A.top, A.bottom, A.ce}
   or A is the FPFVG of its window
quad_aligned (2025 b02): A.top or A.bottom or A.ce within tether_ticks of a quadrant (not a quadrant through A's middle only)
confluence(price) = number of distinct grids with a level within conf_ticks
octant 0.125 measured from the low upward (default; open question in trade-executions)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| grid_n | 4 | 4, 8, 16 | 2026-b03/044@12:17; price-action-chronicles b01/002@31:28 |
| tether_ticks | 2 | 0-8 | proxy (2026-b03/046@16:20) |
| grid_anchors | box20, ORG, range_07_09, daily wick, daily FVG | subset | 2025-b02/004@126:02; 2026-b04/073@35:26 |
| tether_as_filter | false (score) | bool | user choice |

## Invalidation / mitigation
- Levels persist ~3 sessions for intraday ranges (2026-b03/044); box20 until daily close breach.

## Role in MMXM
- Quality score term for every entry array; stage-2 entries on 20-day quadrant levels (2025-b02/004@83:53).

## Evolution across series
- PAC/trade-exec: octants everywhere; 2025 b02: 20-day quadrant filter; 2026: tethering mandatory, 07-09 grid.

## Ambiguities
- Too many anchors make everything tethered; limit anchors and log tether hit-rate.

## Refs
- `2025-b02/006@96:16` quadrant through middle = ordinary gap.
- `2026-b11/133@30:38` untethered = common gap.
