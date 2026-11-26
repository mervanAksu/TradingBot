---
concept: Rejection Block (RB)
aliases: [bolo (RB body + adjacent wick CE, 2026)]
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: body edge (close/open) of the swing-extreme candle(s); zone = body edge to wick extreme
---

## Definition (own words, 2-4 sentences)
At a swing high (low) the wicks show rejection; the actionable line is the highest body edge (lowest for lows) of the candles
forming the extreme. Price may trade beyond it into the wick, but bodies failing to close beyond the body edge = rejection.
Used mostly as stop anchor, first partial or a "no-touch" defensive zone, not as a stand-alone entry.

## Detection rule
```
bearish RB at swing high (swing-points.md) at bar s:
   rb_level = max(bodyHi[s-1], bodyHi[s], bodyHi[s+1])   (default rb_span = 1)
   zone = [rb_level, high[s]] ; ce = mid (wick CE, see wick-ce.md)
   rejection confirmed when a later bar trades above rb_level but closes <= rb_level
variant "equal_lows_close" (bullish, 2023): rb_level = lowest close among the down-close candles forming equal lows
variant "ob_close" (2024): the close of the OB candle used as stop/first partial
output: zone{top,bottom,rb_level,dir}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| rb_variant | body_edge | body_edge, equal_lows_close, ob_close | trade-executions b01/057@46:25; 2023-b05/059@09:20; 2024-b03/006@72 |
| rb_span | 1 | 0-3 | not stated |

## Invalidation / mitigation
- Body close beyond rb_level = failed (2025-b04/047@16:23).

## Role in MMXM
- Stop anchor at SMR (short above RB of the up-close candle, 2025-b03/026@25:24); first rung of partial ladder (2024-b04/008@106:18).

## Evolution across series
- DRAFT wick-to-body zone retained as zone; level = body edge (2023, 2024, 2025, PAC, trade-executions agree). 2026 adds bolo (RB + wick CE, no entry).

## Ambiguities
- Number of neighbouring candles that form "the extreme".

## Refs
- `2025-b03/024@05:11` RB = closing price of swing candle.
- `price-action-chronicles b01/009@46:25` body top of highest up-close to swing high.
- `2026-b06/099@18:42` bolo, defensive zone.
