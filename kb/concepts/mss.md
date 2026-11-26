---
concept: Market Structure Shift (MSS)
aliases: [structure break, shift]
status: VERIFIED
confidence: medium
category: structure
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026]
default_variant: after a sweep, displacement trades through the nearest opposing 3-bar swing
---

## Definition (own words, 2-4 sentences)
After a liquidity pool is raided, price moves with displacement through the most recent opposing short-term swing
(short: the nearest STL; long: the nearest STH), usually leaving an FVG. Order is fixed: raid, then break, then imbalance.
A plain engulfing candle is not a shift; the break only counts if it happens after the intended pool was raided.

## Detection rule
```
bearish MSS (mirror bullish):
  precondition: pool P (BSL) taken at bar r (relative-equal-hl.md / session level)
  ref = most recent STL formed before the break and at/after... default: last confirmed STL before r (mss_ref="pre_raid")
  trigger bar t > r, t - r <= mss_max_bars:
     mss_mode "trade" (default): low[t] < ref ;  "close": close[t] < ref
  and displacement within the break leg (displacement.md) ; mss_need_fvg: an FVG created between r and t+1
output: event{dir, t, ref_price, raid_bar r, fvg_id}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| mss_mode | trade | trade, close | trade: 2023-b02/012@30:08, 2025-b05/057@14:38; close: 2025-b03/020@03:10 |
| mss_need_displacement | true | bool | 2023-b03/022@42:30; 2026-b11/139@18:31 |
| mss_need_fvg | false (score bonus) | bool | 2022-b01/002@43:26 |
| mss_max_bars | 20 | 5-60 | not stated |

## Invalidation / mitigation
- Event, not a zone; the FVG/OB it leaves are the trade arrays.

## Role in MMXM
- Optional confirmation component (score) of SMR; 2024 says no separate MSS is needed for the first short (2024-b08/024@188:37).

## Evolution across series
- DRAFT required a close; 2023 accepts a one-tick pierce; 2025 conflicting (trade vs body close, wick-break inside opposing array invalid); 2026 rarely uses MSS, prefers CISD/IFVG.

## Ambiguities (open questions for the user)
- trade vs close default (shared with CISD/breaker convention).

## Refs
- `2022-b01/002@27:32` order raid -> break -> imbalance.
- `2023-b02/010@41:52` break counts only after the intended high was raided.
