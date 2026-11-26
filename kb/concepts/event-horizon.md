---
concept: Event Horizon
aliases: []
status: VERIFIED
confidence: medium
category: liquidity
series_seen: [2024, 2026, price-action-chronicles, trade-executions]
default_variant: midpoint between two consecutive same-side pools in the trade direction
---

## Definition (own words, 2-4 sentences)
The 50% line between two liquidity references on the same side of price (two lows, two highs, or a swept low and the next
low). It is a partial point, an add point and a strength gauge: a close beyond it raises the odds that the next pool is
taken. Older variants define it between two opening gaps or between an IFVG high and a wick CE.

## Detection rule
```
variant "two_pools" (default): pools P1 (nearer), P2 (farther) on the target side, ordered by distance
   eh = (P1.level + P2.level)/2 ; after P1 is taken: close beyond eh -> flag next_pool_likely
variant "two_gaps" (2024-b06/016@29:47): gap above price G_a and gap below G_b (both within 60 days): eh zone = between their CEs, mid + quadrants
variant "ifvg_wick" (price-action-chronicles b01/004@28:17): mid of IFVG high and wick CE
variant "news" (2026-b01/004@07:50): fib from post-news extreme to next daily draw, 0.5
output: level{eh, kind, members}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| eh_variant | two_pools | two_pools, two_gaps, ifvg_wick, news | 2026-b05/075@06:46 |
| eh_need_convergence | false | bool | 2026-b01/004@14:59 |

## Invalidation / mitigation
- Level; retired when P2 is taken.

## Role in MMXM
- Partial between redistribution pools (take profit just shy of EH, remainder at next pool: trade-executions b02/070@15:16).

## Evolution across series
- PAC (IFVG/wick mid) -> 2024 (between gaps) -> trade-exec/2026 (between pools, most used). v1 = 2026.

## Ambiguities
- Body vs wick anchors for pools.

## Refs
- `2026-b09/119@27:24`; `2024-b06/016@28:46`; `trade-executions b02/064@68:37`.
