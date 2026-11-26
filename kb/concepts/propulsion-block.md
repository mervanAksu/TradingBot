---
concept: Propulsion Block
aliases: []
status: VERIFIED
confidence: medium
category: pd-array
series_seen: [2023, 2024, 2025, 2026]
default_variant: same-direction candle that trades into an older OB up to its MT without a body close beyond, then price departs
---

## Definition (own words, 2-4 sentences)
A newer candle in the OB direction that dips into an existing order block, respects its mean threshold on a body basis,
and launches price away. It becomes a tighter, higher-priority block than the parent OB. 2026 adds that the parent OB must
itself sit on a gradient level.

## Detection rule
```
bullish (mirror bearish): parent OB P (bullish, validated). bar k with close < open (down-close, i.e. OB-type candle) such that
   low[k] <= P.top and close[k] >= P.mt (no body below parent MT)
   and within prop_bars after k a bar closes above high[k]  (launch)
propulsion zone = [bodyLo[k], bodyHi[k]] ; mt = mid ; activated when price trades through open[k] (2026)
optional: P tethered (gradient-levels.md)
fails: close below mt of the propulsion candle
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| prop_bars | 3 | 1-10 | not stated |
| require_parent_tethered | false | bool | 2026-b09/122@30:18 |

## Invalidation / mitigation
- Close beyond its 50% (2023-b07/075@27:32).

## Role in MMXM
- Re-accumulation / re-distribution entry refinement; trail anchor.

## Evolution across series
- 2023: candle trading into older OB, valid until close beyond 50%. 2024: no trade through MT, then launch. 2025: same. 2026: second OB candle inside parent; parent on gradient level; retrace bodies stay in upper half of enclosing FVG.

## Ambiguities
- DRAFT "propels price" replaced by the MT-respect test.

## Refs
- `2023-b02/019@10:00`; `2025-b03/019@09:49`; `2026-b10/125@26:31`.
