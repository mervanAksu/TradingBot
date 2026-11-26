---
concept: Order Block (OB)
aliases: [bullish OB = down-close candle(s), bearish OB = up-close candle(s), mean threshold (MT)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: run of consecutive opposite-close candles; key price = open of the first candle of the run; validated by trade-through of that open
---

## Definition (own words, 2-4 sentences)
The run of consecutive opposite-close candles (one or more) immediately before a move in the new direction. Its key price is
the OPEN of the run (the change-in-state-of-delivery line, `cisd.md`); the OB is validated once price trades through that
open. Reactions are judged on bodies; the mean threshold (MT) is 50% of the body span; a body close beyond MT = failed.

## Detection rule
```
bearish OB (mirror for bullish):
  find a run R = bars [j..k] (k newest) with close > open for all, bar k+1 is down-close (or the run is followed by a down move)
  key_open by ob_key_open: "first" (default) = open[j]; "lowest_open" = min open in R; "largest_body" = open of largest body;
                           "last" = open[k]
  body_top = max(bodyHi in R); body_bot = key_open; MT = (body_top + body_bot)/2; high_R = max(high in R)
  validated when a later bar trades below key_open (low < key_open) -> no close required (ob_validation="trade_through")
     variant ob_validation="fvg": the down move away from R leaves an FVG (2023 v1)
     variant ob_validation="close": a later close < key_open
  optional filters: run of the down move swept liquidity first (2026-b04/073@18:24); tethered (gradient-levels.md)
output: zone{top=body_top, bottom=key_open, mt, high=high_R, dir=bearish, validated_at}
entry: between key_open and MT (work the lower half); stop = high_R + 1 tick (alt: MT + 1 tick, or body_top = rejection block)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| ob_key_open | first | first, lowest_open, largest_body, last | 2024-b04/008@89:53; 2024-b07/020@08:43; 2026-b04/073@16:16; foundations b02/002@15:23 |
| ob_validation | trade_through | trade_through, close, fvg | 2024-b08/024@147:53; 2023-b03/022@12:57; 2026-b03/051@37:09 |
| ob_max_run | 5 bars | 1-10 | not stated |
| ob_fail | close beyond MT | mt, far | 2023-b01/009@04:17; 2024-b14/048@73:50 |
| ob_stop | high_R+1 tick | high, mt, body_top | 2024-b08/024@180:21 |

## Invalidation / mitigation
- Fails on a body close beyond MT (on the entry TF; 2024 used 5m bodies). Ideal: only the near half is touched.
- After validation, the next FVG away from it is tradable at any time of day (2024-b08/024@147:23).

## Role in MMXM
- Low-risk entry anchor at the SMR ("low-risk sell" with stop above OB high, 2024-b08/024@185:00).
- Confirmation score component (OB validated by trade-through of its open).
- Stage-1 accumulation = OB+FVG pair (2025-b01/002@133:08). Trail stop to the open of a new 2-candle OB (trade-executions b02/062@43:19).

## Evolution across series
- foundations/2022: last opposite candle (or run), body, MT 50%, reaction at open/body.
- 2023: valid only if it leaves an FVG (v1), later only when price crosses its OPEN (v2).
- 2024: run counts as one OB; key open conflicts (first vs lowest); bodies only.
- 2025: whole series, open of first; strict = open of last; CE vs MT naming.
- 2026: largest-body rule (b04), last if largest/smallest, first if uniform (b06); must be tethered.

## Ambiguities (open questions for the user)
- `ob_key_open` choice materially changes entries; test first vs lowest_open vs largest_body.

## Refs
- `2024-b08/024@147:53` bearish OB open = CISD, validated by trade below it.
- `2025-b02/004@64:18` OB = series; MT = 50% of body.
- `2026-b04/073@16:16` OB open as CISD; trade-through suffices when liquidity swept.
