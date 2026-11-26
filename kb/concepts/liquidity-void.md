---
concept: Liquidity Void
aliases: [void, vacuum block]
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2023, 2024, 2025]
default_variant: true void (no prints between two prices)
---

## Definition (own words, 2-4 sentences)
A price span with literally no trades between two consecutive prints: session/weekend opening gaps (ORG, NDOG, NWOG) and
bar-to-bar gaps where the next bar's whole range sits beyond the previous bar's range. A one-sided FVG is NOT a void (it
has prints in the middle candle). The DRAFT meaning (large one-directional multi-bar run) is kept only as a legacy variant.

## Detection rule
```
variant "true_void" (default): low[0] > high[1] (bullish) or high[0] < low[1] (bearish) on the same continuous series
   zone = [high[1], low[0]] (bullish); plus all session gaps from ndog-nwog.md and opening-range-gap.md
variant "legacy_run": >= 3 consecutive same-direction bars each forming an FVG with the bar two back, union of their gaps
output: zone{top,bottom,ce,dir,kind}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| void_variant | true_void | true_void, legacy_run | 2023-b02/019@12:31; 2025-b04/050@05:50 |

## Invalidation / mitigation
- Filled when a body trades through the whole span; CE first-touch is the usual reaction point (as for gaps).

## Role in MMXM
- Draw/target (gap magnets); delivery accelerates through voids.

## Evolution across series
- DRAFT P11 (multi-bar run) is not supported by any series; 2023/2025 define it strictly as absence of prints; 2024 separates wick-to-wick void from VI (2024-b12/038@60:24) and adds the vacuum block (2024-b09/027@68:29).

## Ambiguities
- On 24h futures, intra-session true voids are rare; mostly the session gaps. Low priority detector.

## Refs
- `2023-b01/001@13:26` void = no prints; BISI/SIBI is not a void.
- `2025-b01/002@181:37` gap with prints is only an inefficiency.
