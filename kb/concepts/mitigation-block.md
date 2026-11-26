---
concept: Mitigation Block
aliases: []
status: VERIFIED
confidence: low
category: pd-array
series_seen: [2023, 2026]
default_variant: failed swing without a liquidity sweep; used as target, not entry
---

## Definition (own words, 2-4 sentences)
Like a breaker but the failing swing did NOT take liquidity: bearish = high H1, low L, LOWER high H2 (no sweep), then a break
below L; the down-close candle(s) at L become resistance. Weaker than a breaker; the series use it as a target or reaction
area rather than an entry. 2026 also calls an OB that sat inside a run to buy-side a mitigation block after the sweep.

## Detection rule
```
bearish: STH H1, STL L after it, STH H2 with H2 < H1 (no sweep), then trade below L (brk_mode as in mss.md)
zone = bodies of the down-close run that formed L; MT = mid
output: zone{top,bottom,mt,dir=bearish,created_at}
role flag: target_only = true (default)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| mb_use_as_entry | false | bool | 2023-b07/075@21:21 |

## Invalidation / mitigation
- Body close beyond MT.

## Role in MMXM
- Target / partial level only in v1.

## Evolution across series
- 2023 defines it (high, low, higher high = bullish mirror, no grab); 2024 and 2025 never mention it; 2026 uses it as the flipped role of an OB after a buy-side sweep (2026-b06/099@17:11).

## Ambiguities
- Single defining source; low confidence. Keep as low-weight target level.

## Refs
- `2023-b06/060@59:34` mitigation block = failed swing without liquidity grab, weaker.
- `2026-b06/099@17:11` OB in a run to buy-side flips to mitigation after the sweep.
