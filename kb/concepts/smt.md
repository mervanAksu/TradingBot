---
concept: SMT Divergence (NQ vs ES)
aliases: [smart money technique, Sick Sister, decoupling]
status: VERIFIED
confidence: medium
category: liquidity
series_seen: [foundations, 2023, 2024, 2025, 2026]
default_variant: NQ vs ES on the TF above execution, swing extremes compared by bodies, qualifier only
---

## Definition (own words, 2-4 sentences)
At a liquidity raid one index takes its prior swing extreme while the correlated index fails to: the failing index shows
where accumulation/distribution happened. It is a qualifier (score term), never a trigger. When the indices move in
opposite directions overall (decoupling) the series stand aside.

## Detection rule
```
pairs: (NQ, ES); time-aligned bars on smt_tf
for a swing window: A_prev = prior swing low of A, B_prev of B (same anchor time +- smt_align_bars)
bullish SMT at time t: A makes low < A_prev (sweep) and B's low >= B_prev (higher low)  [price = body or wick per smt_price]
bearish mirror with highs
decoupled(t) = sign(return over N bars NQ) != sign(ES) with both |ret| > dec_min_atr * ATR
output: event{dir, leader (swept), laggard (held), t}
trade side: Sick Sister - trade the laggard in consolidation (2023-b05/053@04:17); 2026: weakest index is the short
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| smt_tf | one TF above execution | | 2024-b13/045@07:15 |
| smt_price | body | body, wick | 2024-b10/029@39:09 |
| smt_align_bars | 2 | 0-5 | foundations b01/004@27:32 (series divergence allowed) |
| decoupling_filter | on | bool | 2024-b09/026; 2026-b07/105@33:27 |

## Invalidation / mitigation
- Qualifier only; ignore Dow (2024).

## Role in MMXM
- Optional SMR confirmation score term (2024-b08/024: qualifier); unresolved SMT before reversal (2025-b04/049@06:40).

## Evolution across series
- foundations/2023 used it as accumulation footprint and Sick Sister; 2024-2026 demote it to qualifier, NQ-ES only, bodies.

## Ambiguities
- Which instrument to trade when SMT fires (leader vs laggard).

## Refs
- `foundations b01/004@10:53`; `2023-b03/022@24:21`; `2026-b10/127@02:28`.
