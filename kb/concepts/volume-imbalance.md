---
concept: Volume Imbalance (VI)
aliases: [body gap, vacuum block (variant)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: body-to-body gap >= 1 tick with wick overlap
---

## Definition (own words, 2-4 sentences)
Two consecutive candles whose bodies do not overlap while their wicks do: the close of one and the open of the next leave
a price span with no body. It is the weakest and most flexible PD array (price may trade through and back) and is included
in the FVG box when adjacent. It stays open until a later candle body covers its whole span.

## Detection rule
```
bullish VI between [1] and [0]: bodyLo[0] > bodyHi[1] and low[0] <= high[1]   (wicks touch/overlap)
bearish VI:                     bodyHi[0] < bodyLo[1] and high[0] >= low[1]
size = gap between bodies >= vi_min_ticks*tick
ignore middle candles with |close-open| == 0 when scanning (2024-b10/035@22:01)
zone{top,bottom,ce,dir}; closed when a later bar has bodyLo <= bottom and bodyHi >= top
variant "vacuum": close[1] to open[0] gap with no prints at all (low[0] > high[1]) -> see liquidity-void.md
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| vi_min_ticks | 1 | 1-8 | 2024-b06/016@09:08; 2026-b04/073@34:19 |
| parent_tf_check | false | bool | judge on parent TF: 2023-b08/100@89:00 |

## Invalidation / mitigation
- Closed when one body spans it; partial body coverage = still active. Unfilled VI in strong flow = continuation sign.

## Role in MMXM
- Minor entry/partial/target levels; component of suspension block and of FVG box; "indigo" OB+VI entry (2024-b12/038@41:19).

## Evolution across series
- Consistent since 2023; 2024 ranks strength OB > FVG > VI; 2026 adds TradingView settings note (settlement-as-close) for visibility.

## Ambiguities
- Data feed: TradingView "settlement as close" toggle changes whether VIs show (2026-b10/128@17:47). Fix one setting for backtests.

## Refs
- `2023-b03/022@54:11` bodies do not overlap, wicks link; open until spanned.
- `2024-b13/046@20:41` soft array.
- `2026-b09/122@26:13` stays active until a later body covers it.
