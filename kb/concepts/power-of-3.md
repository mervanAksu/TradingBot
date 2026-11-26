---
concept: Power of 3 (AMD) and Judas swing
aliases: [AMD, accumulation-manipulation-distribution, Judas swing, opening range projection, seek and destroy (failure profile)]
status: VERIFIED
confidence: medium
category: time
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026]
default_variant: per session - accumulate near the open, manipulate against bias beyond the open (sweep), distribute to the far extreme
---

## Definition (own words, 2-4 sentences)
Any bar with an open (week, day, session, hour) tends to consolidate around its open, make a false move against the true
direction that takes stops (Judas swing), then expand to the far extreme. Bullish: buy at/below the open; bearish: sell at/above.
The anchoring open depends on the scale (weekly open, midnight open, 08:30, 09:30, 13:30). The first move after a window start
is presumed to be the Judas; "the first one shall be last".

## Detection rule
```
anchor open O (opening-prices.md) for window W ; bias b in {bull, bear} from context
manipulation (bull): price trades below O by >= j_min (and ideally sweeps a pool below), within judas_max_min minutes of W.start
distribution: subsequent expansion beyond the pre-manipulation high
entry band (bull): price <= O ; 2022 opening-range band: shorts only between day high and (O - judas_range) (2022-b01/010@13:38)
hourly variant (2024 b01-b03): after each hour start 07/08/09, ~30 min counter-move against the pool side, then run to untouched pool
seek_and_destroy flag: both prior-session extremes taken before 10:00 then reversal -> reduce/skip (trade-executions b01/061@16:20)
output: phase per window {accumulation, manipulation, distribution} + judas_extreme
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| judas_max_min | 30 | 15-60 | 2024-b01/002@180:00 |
| j_min_ticks | 4 | 1-40 | proxy |
| anchors | midnight, 08:30, 09:30, 13:30, weekly | | 2023-b02/010@56:42 |

## Invalidation / mitigation
- Manipulation leg continues > 1x expected range with bodies (runaway) = not Judas.

## Role in MMXM
- Session-level analogue of OC (accumulation) -> SMR (manipulation) -> distribution; Judas into premium = SMR leg (2026-b04/072@13:56).

## Evolution across series
- foundations: fractal on any bar; 2022 daily PO3 with opening-range band; 2023 weekly PO3 on Monday midnight open; 2024 hourly Judas; 2026 four-phase day.

## Ambiguities
- Overlaps with session-phase classifier; keep as labels.

## Refs
- `foundations b01/009@01:17`; `2022-b01/009@02:40`; `2024-b05/011@147:34`.
