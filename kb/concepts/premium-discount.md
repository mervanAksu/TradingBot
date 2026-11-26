---
concept: Premium / Discount and Dealing Range
aliases: [equilibrium (EQ), dealing range, implied dealing range, inception-to-terminus, 20-day box, IPDA lookback]
status: VERIFIED
confidence: medium
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: leg range (swing extreme to swing extreme, bodies) for entries; 20-day box for context
---

## Definition (own words, 2-4 sentences)
Split a dealing range at 50% (equilibrium): above = premium (sell area), below = discount (buy area). Longs and adds only
at/below EQ, shorts at/above. Which range is a parameter: the latest swing leg, the entry-to-draw range, a session/opening
range, or a fixed 20-day box. The same half-rule is applied inside a single array (gap, wick, OB).

## Detection rule
```
range R by pd_range:
  "leg" (default for entry): from the swing that started the current leg to its extreme (body anchors, 2026-b03/051@27:26)
  "entry_to_draw": from entry low (raid low) to the targeted pool (2025-b03/027@14:38)
  "box20": high/low of last 20 completed daily candles (40/60 if parabolic) (2025-b02/004@11:48)
  "session": ORG, 07:00-09:00, opening range 09:30-10:00, FHDR 09:30-10:30, ONR 00:01-04:59
eq = (R.hi + R.lo)/2 ; zone(price) = premium if price > eq else discount ; grade via gradient-levels.md
entry gate: long only if entry_price <= eq (or <= q25 strict) ; short if >= eq (>= q75 strict)
pyramid gate: adds only while price on the favourable side of EQ of (entry -> terminus) range; recompute after each raid
box20 gate: ignore arrays outside box until a daily close breaches it
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| pd_range | leg | leg, entry_to_draw, box20, session | 2024-b14/048@67:05; 2025-b02/004@13:58 |
| pd_strict | eq | eq, quadrant | 2024-b14/048@71:44 |
| box_days | 20 | 20/40/60 | 2025-b02/004@11:48 |
| anchor | body | body, wick | foundations b01/011@13:48; 2026-b09/121@36:20 |

## Invalidation / mitigation
- Range re-anchors after a new extreme (2026-b09/119@36:41).

## Role in MMXM
- SMR location: sell model only from premium of the context range; entries for low-risk and stage-2 only on the favourable side of EQ.

## Evolution across series
- foundations/2022: daily swing 50%; 2023 quarters of implied range; 2024 several ranges; 2025 20-day box; 2026 applied to every array and range.

## Ambiguities (open questions for the user)
- Context range for "HTF premium/discount": 20-day box vs dealing range of the model (OC to extreme).

## Refs
- `2023-b03/025@43:29` shorts at/above EQ, pyramid only in favourable half.
- `2025-b02/004@17:06` 20-day box quadrants.
