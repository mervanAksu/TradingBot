---
concept: Optimal Trade Entry (OTE)
aliases: [62-79, 70.5 sweet spot]
status: VERIFIED
confidence: medium
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026]
default_variant: 0.62-0.79 retracement of the displacement leg, sweet spot 0.705, body anchors
---

## Definition (own words, 2-4 sentences)
After a shift, the retracement zone 62%-79% of the leg that caused it (measured from its origin to its extreme) is the
preferred entry band, with 70.5% as the sweet spot. Anchors are bodies in the earliest teaching and in 2026's anchoring
rule. If price does not retrace into the band, there is no OTE trade. 2025 also uses 70.5% of the dealing range as the
buy model's first "low-hanging" target.

## Detection rule
```
leg L from swing origin O to extreme X (after MSS/CISD); size = X - O (signed)
ote_hi = X - ote_lo_pct*size ; ote_lo = X - ote_hi_pct*size ; sweet = X - 0.705*size
anchor = body (default: O = bodyLo of origin bar, X = bodyHi of extreme bar) or wick
entry valid if price trades into [ote_lo, ote_hi] before taking X again ; skip if not reached
rounding (optional): levels rounded to 0/5 (foundations b01/005@33:58)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| ote_band | 0.62-0.79 | 0.62-0.70 (2022), 0.62-0.72 (2024), 0.62-0.79 | foundations b01/011@10:45; 2022-b02/041@18:10; 2024-b01/002@96:38 |
| ote_sweet | 0.705 | | 2024; 2025-b01/002@77:21 |
| ote_anchor | body | body, wick | foundations b01/011@13:48 |

## Invalidation / mitigation
- Leg extreme taken before entry, or close beyond 100% (origin).

## Role in MMXM
- Optional entry E2; 70.5% of dealing range = first target of buy model (2025-b01/002@98:02).

## Evolution across series
- 2026 does not use 62-79; replaced by quadrant/octant ladder (2026-b11/138@38:52). 2023 rarely uses OTE (SD projections instead).

## Ambiguities
- Keep as variant entry, not default.

## Refs
- `foundations b01/011@13:48` body-anchored.
- `2025-b01/002@98:02` 70.5 of the range = low-hanging draw.
