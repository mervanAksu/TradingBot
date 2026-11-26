---
concept: Balanced Price Range (BPR)
aliases: [shadow (2026), balanced range]
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles]
default_variant: overlap of opposite FVGs
---

## Definition (own words, 2-4 sentences)
A span that has been delivered both ways: a bullish and a bearish gap overlap, or a range is traded up and down and then left.
Used as an entry zone after the two-way delivery and as a disqualifier (an FPFVG formed inside a BPR is not valid). Its CE is
a hard line in the Venom long model.

## Detection rule
```
variant "fvg_overlap" (default): bullish FVG A and bearish FVG B (either order) with |created_at(A)-created_at(B)| <= bpr_max_bars
   overlap_top = min(A.top,B.top); overlap_bot = max(A.bottom,B.bottom); require overlap_top > overlap_bot
   zone = [overlap_bot, overlap_top]; dir = direction of the later gap; ce = mid
variant "outer": same pair, zone = [min(A.bottom,B.bottom), max(A.top,B.top)]  (price-action-chronicles b01/008@06:05)
variant "two_way_vi": a volume imbalance later covered by both an up body and a down body = balanced (2024-b13/046@36:11)
variant "range_two_way": bars [i..j] with mean overlap >= 0.6 that are left with displacement (2024-b06/016@15:17)
output: zone{top,bottom,ce,dir,created_at}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| bpr_variant | fvg_overlap | fvg_overlap, outer, two_way_vi, range_two_way | 2024-b03 / 2024-b06/016@15:17 |
| bpr_max_bars | 10 | 2-60 | not stated; proxy |

## Invalidation / mitigation
- Directional BPR fails on a body close beyond its CE (Venom: CE revisit voids the model, 2025-b04/039@10:57).

## Role in MMXM
- Re-distribution zone in premium (a "wall" of overlapping wicks/BPR overhead) before 2nd-stage distribution (2024-b08/024@187:35).
- Filter: arrays inside BPR are not first-presented FVGs (2025-b04/049@08:14).

## Evolution across series
- 2023: a gap traded both ways and left = BPR (2023-b05/050@30:16). 2024: three uses (overlap / range / VI both colours).
- 2025: BPR in Venom; disqualifies FPFVG; balanced half of a HTF FVG will not fill (2025-b05/065@15:58).
- 2026: "shadow" = overlap graded with its own quadrants/octants (2026-b04/073@35:56).

## Ambiguities
- Which variant to code first; overlap vs outer zone. Default overlap (most mechanical).

## Refs
- `2025-b04/039@05:17` Venom long: SIBI then BISI, overlap = BPR, CE must hold.
- `2026-b04/073@35:56` shadow = overlap of two imbalances, graded.
