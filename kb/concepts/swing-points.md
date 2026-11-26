---
concept: Swing Points (STH/STL, ITH/ITL, LTH/LTL)
aliases: [short-term high, intermediate-term high, long-term high, ring high]
status: VERIFIED
confidence: high
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026]
default_variant: 3-bar fractal on wicks; nesting for ITH/LTH; body-anchored variant
---

## Definition (own words, 2-4 sentences)
A short-term high is a candle whose high exceeds the highs of the candle before and after it (3-bar pattern; no 5-bar
fractal). An intermediate-term high is a short-term high with a lower short-term high on each side; a long-term high is an
intermediate high with lower intermediate highs on each side. Lows mirror. 2026 prefers body extremes for anchoring.

## Detection rule
```
STH at bar [1] (confirmed at close of [0]): high[1] > high[2] and high[1] >= high[0]   (tie on the right allowed)
STL: low[1] < low[2] and low[1] <= low[0]
ITH: STH s_k with STH s_(k-1) < s_k and next STH s_(k+1) < s_k (confirmed when s_(k+1) prints)
LTH: ITH with lower ITH on both sides
swing_price = "wick" (default) | "body" (max(bodyHi) of the pivot bar, 2026-b08/114@90:06)
optional ITH tag "has_fvg" = an FVG inside the leg into/away from it (2022-b01/017@14:29; 2025-b03/017@04:46)
output: swing{price, time, kind (STH/ITH/LTH), confirmed_at}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| swing_len | 1 (3-bar) | 1-2 | 2022-b01/002@43:26 |
| swing_price | wick | wick, body | 2026-b03/049@04:34 |

## Invalidation / mitigation
- Swing is "taken" on trade-through (default) or body close beyond (variant, see relative-equal-hl.md `run_mode`).

## Role in MMXM
- Basis for MSS, breaker, pools, stage-swing lows (2025-b01/002 stop trailing under 3-bar swing low).

## Evolution across series
- foundations/2022/2023/2025: consistent nesting; 2022 "intermediate = swing carrying an FVG" kept as a tag; 2026 body anchors.

## Ambiguities
- Strict vs non-strict ties.

## Refs
- `2022-b01/010@18:16`; `2023-b02/014@00:04`; `2025-b03/017@04:46`; `2026-b10/131@15:10`.
