---
concept: Relative Equal Highs/Lows (EQH/EQL) and liquidity pools
aliases: [smooth highs, engineered liquidity, buy-side / sell-side liquidity (BSL/SSL), double tap]
status: VERIFIED
confidence: medium
category: liquidity
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: ordered pair (newer stops short of older) within eq_tol; smooth = no bar closed beyond between them
---

## Definition (own words, 2-4 sentences)
Two or more swing highs (lows) at nearly the same price are a resting stop pool. Quality: the older point is the anchor
and the newer point stops slightly short of it (for highs the right-hand high is lower; for lows the right-hand low is
higher); "smooth" clean pools are draws, "jagged" ones (traded through many times) are spent. A single obvious extreme or
a prior session/day high also counts as a pool. A pool is "taken" on trade-through (default) or on a body close beyond.

## Detection rule
```
candidates: swings (swing-points.md) on tf within lookback
EQH pair (a older, b newer): |H_a - H_b| <= eq_tol and (eq_order == "any" or H_b <= H_a)
   smooth: no close > max(H_a,H_b) between a and b, and touches_between <= 1
   quality A if H_b < H_a (stops short), B if equal, C if H_b > H_a (expect retrace to imbalance first, 2026-b12/140@66:19)
pool level = max(H_a, H_b) (+ optional extra low/high in cluster, foundations b02/002@03:41)
post_window: in a window study only swings formed after the window start count (2024-b01/001@103:36)
taken: run_mode "trade" -> high > level ; "body" -> close > level (2025-b02/006@48:05)
primary vs minor (2024-b13/042@13:28): primary = EQH/EQL or lone extreme beyond the opening range; minor = nearer swings
output: pool{level, side=BSL|SSL, members, quality, smooth, tf, taken_at}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| eq_tol_ticks | 4 (NQ 1m), 2 (ES) | 0-12 | 0-2 ticks: 2023-b03/026@48:54; ~2.25 handles: 2026-b12/142@25:58 |
| eq_tol_atr | off | 0.05-0.2 x ATR | proxy alternative |
| eq_order | right_shorter | any, right_shorter | 2024-b01/001@75:34; 2025-b02/006@15:11; 2026-b12/140@66:19 |
| run_mode | trade | trade, body | 2025-b02/006@48:05; 2026-b01/015@03:12 |
| pool_lookback_days | 3 (intraday) | 1-20 | 2026-b03/044@52:12 |

## Invalidation / mitigation
- Taken pool is extended right as a repeat reference (trade-executions b01/020@28:12); not a pool again unless re-formed.

## Role in MMXM
- OC base (equal lows under the original consolidation, 2024-b08/024@170:31); SMR = sweep of EQH; targets/partials at each pool.

## Evolution across series
- Tolerance never stated numerically (2024 withholds it); ordering rule consistent 2024-2026; PAC "right-hand low >= left-hand low".

## Ambiguities (open questions for the user)
- eq_tol choice (ticks vs ATR) - biggest single driver of pool counts.

## Refs
- `foundations b01/010@01:43` pools at equal/obvious extremes.
- `2024-b01/001@69:59` smooth vs jagged.
- `2026-b12/140@66:19` older point is the anchor.
