---
concept: Immediate Rebalance (IR)
aliases: [instant rebalance]
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2023, 2024, 2025, 2026, trade-executions]
default_variant: 3-bar pattern where candle 3 refills exactly to candle 1's extreme (no FVG left), then price continues
---

## Definition (own words, 2-4 sentences)
A strong candle whose follow-up candle immediately retraces only to the prior candle's extreme (so no gap is left), after
which price continues in the original direction. It signals fast delivery to the nearest pool and works on any TF, including
daily. Variants: an oversized candle whose next candle retraces its whole body; a candle that tags the CE of the prior day's
wick and leaves.

## Detection rule
```
bullish IR at bar [0] (pattern [2],[1],[0]):
   [1] displacement up (displacement.md) ; low[0] <= high[2] + ir_tol_ticks*tick and low[0] >= high[2] - ir_tol_ticks*tick
   (i.e. what would have been an FVG is exactly refilled, no deeper) ; confirm: within ir_n bars a close > high[1]
variant "body_retrace" (2024-b06/017@28:36): range[1] >= ir_k * mean(range, 20) and close[1] in top 25% ; [0] retraces >= 100% of body[1]; continuation only if on the very next bar
variant "daily_wick_ce" (2026-b09/121@02:41): bar trades to CE of the prior day's wick/high then leaves; delivery same or next day
output: event{dir, level=high[2], t}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| ir_variant | refill_to_c1 | refill_to_c1, body_retrace, daily_wick_ce | 2025-b05/055@36:34 |
| ir_tol_ticks | 1 | 0-4 | proxy |
| ir_k | 1.5 | 1.2-3 | proxy |
| ir_n | 3 | 1-5 | proxy |

## Invalidation / mitigation
- Close back below high[2] (bullish) voids it; day-2 trade through the IR = complex reversal (2026-b09/121@13:27).

## Role in MMXM
- Continuation signal inside distribution/accumulation stages; short entry at that candle's high (trade-executions b02/064@116:37).

## Evolution across series
- 2023 run with no FVG; 2024 oversized candle + full body retrace; 2025 refill to prior extreme; 2026 daily wick CE version.

## Ambiguities
- Several incompatible definitions; default = 2025 (most mechanical).

## Refs
- `2023-b06/072@06:00`; `2024-b06/017@32:09`; `2025-b05/057@14:38`.
