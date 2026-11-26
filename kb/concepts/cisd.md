---
concept: Change in State of Delivery (CISD)
aliases: [OB open line, Venom close (variant)]
status: VERIFIED
confidence: high
category: structure
series_seen: [foundations, 2023, 2024, 2025, 2026, trade-executions]
default_variant: first trade through the open of the first candle of the delivering series; no close required
---

## Definition (own words, 2-4 sentences)
The run of same-direction candles that delivered price into an extreme has an opening price (the open of its first candle).
The first time price trades back through that open, delivery has changed state. It is earlier and tighter than an MSS and
is the same line as the order block's key open. Some lectures require a close through it; most do not.

## Detection rule
```
bullish CISD (after a low): series S = consecutive down-close bars ending at/just after the swing low bar
   cisd_level by cisd_anchor: "series_first_open" (default) = open of first bar of S
                              "last_candle_open" = open of the last down-close bar (foundations b02/002@10:18)
                              "wick_extreme" = if a wick of S's first bar extends above its open, use that high (2025-b01/001@15:25)
                              "venom_close" = close of the Venom candle (2025-b04/051@15:07)
   trigger: cisd_mode "trade" -> high[t] > cisd_level ; "close" -> close[t] > cisd_level
   precondition (score bonus): a pool was swept at the low (2026-b04/073@18:24)
bearish mirror with up-close series
output: event{dir, t, level, series_start, series_end}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| cisd_anchor | series_first_open | series_first_open, last_candle_open, wick_extreme, venom_close | 2024-b04/008@86:48; 2025-b05/057@16:41 |
| cisd_mode | trade | trade, close | trade: 2026-b03/051@37:09, 2025-b01/002@101:04 (one tick); close: 2024-b04/008@78:32 |
| cisd_max_bars | 30 | 5-120 | not stated |

## Invalidation / mitigation
- Offside rule: bearish bias, price takes a down-close candle's open and closes back above its CE = stop and reverse (2023-b07/085@11:29).

## Role in MMXM
- Core SMR confirmation component: the raid candle's open as pivot in the buy model (2025-b01/002@101:04); OB validation (2024-b08/024@147:53). Re-add level (trade-executions b01/051@02:10).

## Evolution across series
- DRAFT: first close through. 2023: OB confirms when its OPEN is crossed. 2024: open of whole series, close vs trade disputed. 2025: wick and Venom variants; one tick enough in the buy model. 2026: trade-through, no close.

## Ambiguities
- Series boundary when a doji interrupts the run (treat zero-body bars as continuing the series).

## Refs
- `2024-b04/008@87:18` anchored on the whole delivering series.
- `2026-b03/059@05:11` entry between candle close and wick CE, stop beyond wick.
