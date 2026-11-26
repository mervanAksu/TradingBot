---
concept: Fair Value Gap (FVG)
aliases: [BISI (bullish), SIBI (bearish), imbalance, common gap, breakaway gap, measuring gap]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: wick-gap + VI, near-edge entry, body-close-beyond-far-edge = failed
---

## Definition (own words, 2-4 sentences)
A three-candle pattern where the wicks of candle 1 and candle 3 do not overlap, leaving a price span that was traded in
only one direction during the middle (displacement) candle. Bullish = BISI, bearish = SIBI. The gap is graded with three
prices (near edge, CE = 50%, far edge) plus optional quadrants; it is respected when bodies stay in the half nearest the
departure and failed when a body closes beyond the far edge (it then becomes an IFVG, see `ifvg.md`).

## Detection rule
```
inputs: OHLC per TF; conventions from kb/key-levels.md (bar [0] = newest closed, bodyHi/bodyLo, tick)
bullish at bar [0]:  low[0] > high[2]            -> zone bottom = high[2], top = low[0]
bearish at bar [0]:  high[0] < low[2]            -> zone top = low[2], bottom = high[0]
size = top - bottom;  require size >= fvg_min_ticks*tick
optional box extension (fvg_box = "wick+VI"): if a volume imbalance (volume-imbalance.md) touches the gap edge
   between candles 1-2 or 2-3, extend the zone to include it (one entity; CE from the outer range)
quality flags (stored, not filters, unless enabled):
   displaced   = candle[1] is a displacement bar (displacement.md)
   tethered    = candle[1] (or the VI candle) touches a gradient level / key-level / HTF array within tether_ticks (gradient-levels.md)
   quad_aligned= top, bottom or ce within tether_ticks of a quadrant of the active frame range (2025 b02 filter)
   in_bpr      = formed inside a balanced price range (bpr.md) -> not tradable as FPFVG
output: zone{top, bottom, ce=(top+bottom)/2, q25, q75, dir, tf, created_at=time[0], c1_extreme, c2_extreme, flags}
state machine per zone: active -> tested (first wick into zone) -> {respected | weak (CE touched by body) | failed}
   failed (bullish) when close < bottom - 0 ticks  -> spawn IFVG(bearish) from this zone
   expired after pda_lookback_days trading days
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| fvg_min_ticks | 4 (NQ), 2 (ES) | 1-40 | floor for "common gap" ~10 NQ handles: 2026-b12/140@52:03 |
| fvg_box | wick+VI | wick, wick+VI | 2024-b10/032@12:38; 2025-b03/023@09:23; 2026-b01/001@06:40 |
| entry_price | near_edge | near_edge, ce, q25 | near edge: 2024-b09/028@19:57; CE: 2023-b03/024@23:19 |
| entry_offset_ticks | 1 (inside near edge) | -1..2 | conflicting: 2024-b05/010@197:54 vs 2024-b05/011@83:08 |
| stop_anchor | c1_extreme+1 tick | c1, c2, ce+2 ticks | 2024-b09/028@29:21; 2026-b11/139@19:02 |
| respect_test | close_beyond_far_edge | close_beyond_ce (strict), close_beyond_far_edge | 2023-b03/022@09:22; 2024-b09/028@43:17 |
| require_displacement | true for entries | bool | 2022-b01/020@12:21; 2025-b02/009@18:58 |
| pda_lookback_days | 20 | 20/40/60 | 2023-b02/015@04:17; 2024-b07/018@86:42 |
| max_touches | 2 (skip on 3rd) | 1-5 | 2024-b01/002@106:00; 2026-b05/084@33:33 |

## Invalidation / mitigation
- Failed: body close beyond the far edge (wicks/pokes up to `poke_ticks` tolerated) -> becomes IFVG.
- Weak: body close beyond CE (strict variant treats this as failed).
- Spent: 3rd touch, or fully filled and price left (filled gap levels stay usable as reference: 2025-b03/010@34:37).
- Strength signature: part of the gap left unfilled after the retest = continuation (trade-executions b01/057@35:05; 2023-b01/001@41:16).

## Role in MMXM
- Entry array for low-risk entry (first FVG after SMR) and for re-distribution/re-accumulation entries; stage-1 leg = OB+FVG pair (2025-b01/002@133:08).
- Target/partial levels: opposing HTF FVG edges/CE. Context: HTF premium/discount FVG for SMR location.

## Evolution across series
- foundations/2022: plain 3-candle gap; usable only with displacement through a swing; drop TF until an FVG appears (2022-b01/010@37:52).
- 2023: three prices + quarters; CE fill most likely, near edge guaranteed fill (IOFED).
- 2024: VI included in the box; near-edge entry preferred; half-rule; 3rd-touch skip.
- 2025: quadrant-aligned filter (b02); breakaway (~20-30% of IDR) vs measuring gap (~50%).
- 2026: tethering to gradient levels mandatory for quality; ~10-handle NQ floor for "real" gaps.

## Ambiguities (open questions for the user)
- Use tethering / quadrant alignment as a hard filter or as a score term? (default: score term).
- fvg_min_ticks per TF (1m vs 15m) - suggest ATR-relative variant `fvg_min_atr = 0.1`.

## Refs
- `2022-b01/002@16:14` raid -> displacement -> retrace into FVG.
- `2023-b03/022@09:22` three prices and quarters; CE close = failure.
- `2024-b09/028@43:17` near-half respect, CE = weak, far-edge close = failed.
- `2025-b02/004@126:02` quadrant-aligned FVG = high probability.
- `2026-b03/046@16:20` tethering rule.
