---
concept: First Presented FVG (FPFVG)
aliases: [first presented fair value gap, reflection FVG (first opposite one)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [foundations, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: AM - first 1m FVG with candle 1 at 09:31 or later, displacement-sized, within 09:31-10:00
---

## Definition (own words, 2-4 sentences)
The first fair value gap that forms on displacement after a session/window opens; the 09:30 bar is excluded as candle 1.
It is the day's reference array (price above = bullish, below = bearish) and the beginner model's entry array, and it is
carried forward for several days. Tiny gaps without displacement, gaps inside a balanced range, and gaps counter to the
draw do not qualify.

## Detection rule
```
window W (default AM: candle-1 start in [09:31, 10:00)); tf = 1m
scan FVGs (fvg.md) in time order with c1_time >= W.start; first one with
   size >= fpfvg_min_ticks and displaced flag and not in_bpr  -> FPFVG(W)
fpfvg_mode: "plain" = first FVG regardless of size/displacement; "displacement" (default) = as above;
            "reflection" = first opposite-direction FVG after the FPFVG
families: AM (09:31), PM (13:30-14:00, prefer one containing a VI), pre-market (07:00), London (01:30/02:00), Asia (18:00/19:00),
          silver bullet (10:00), weekly-first (Monday 09:31), post-turtle-soup
carry: keep fpfvg_keep_days; overlay Mon/Fri FPFVGs of this and last week (2026-b01/015@14:00)
re-label: trade above it -> bullish (only CE and above matter); below -> bearish (2025-b03/013@05:09)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| fpfvg_min_ticks (NQ) | 40 (10 handles) | 4-60 | 2026-b12/140@52:03; 2025-b02/009@18:58 |
| fpfvg_mode | displacement | plain, displacement, reflection | 2026-b01/013@00:33 |
| fpfvg_keep_days | 3 | 3-20 | 2024-b08/021@06:30; 2026-b11/139@16:24 (20 days) |
| org_exception | false | bool | ORG raided at open may act as FPFVG: 2025-b04/034@12:28 |

## Invalidation / mitigation
- Holds while no body in its far half (PAC b01/001@07:24); repeated re-entry after CE tag = held market (2024-b10/033@41:12).

## Role in MMXM
- Low-risk entry array on intraday models; stage-2 legs slide through it (2025-b04/040@02:36); bias toggle.

## Evolution across series
- foundations: first session FVG inverts and becomes target. 2024: 09:31 rule, 3 days. 2025: displacement-sized, BPR exclusion, families. 2026: window starts 07:00/09:30/10:00/after turtle soup; ~10-handle floor; reflection FVG.

## Ambiguities
- Size floor 10 handles may be too strict on quiet days; test 2/5/10.

## Refs
- `2024-b06/016@20:29` first 1m FVG, candle 1 at 09:31+.
- `2025-b04/049@08:14` displacement, not inside BPR.
- `2026-b10/128@36:09` 09:31 bar, not long if equal lows untouched nearby.
