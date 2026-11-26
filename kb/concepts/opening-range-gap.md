---
concept: RTH Opening Range Gap (ORG)
aliases: [opening gap, RTH gap]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: prior RTH settle (close of the 16:14 1m bar) -> 09:30 open, RTH data
---

## Definition (own words, 2-4 sentences)
The gap between the previous day's RTH final print (16:14 bar close, RTH ends 16:15) and today's 09:30 opening print,
measured on RTH-only data. Open above settle = premium gap (look for shorts first), below = discount gap (longs). Its CE is
the first draw of 09:30-10:00; the claim is that CE is reached by ~10:00 about 70% of the time - a hypothesis to test.

## Detection rule
```
settle = close of the 1m bar starting 16:14 NY on the prior RTH day (= last RTH print, RTH end 16:15)
open   = open of the 1m bar starting 09:30
zone = [min, max], ce, q25, q75, octants; kind = premium if open > settle else discount; size_ticks
keep last org_keep days (carry quadrants of today + previous 3)
ce_hit_by_10 = any bar in [09:30,10:00) with low <= ce <= high  (stat, logged daily)
size band (NQ handles; ES = /4 as default scaling):
   < org_min -> ignore; org_min..75 -> expect CE; 75..120 -> no edge, wait to 10:00; >= 120 -> expect nearest quadrant only
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| org_settle_bar | 16:14 bar close | 16:14 close, 16:15 print, 16:00 close | 2024-b13/047@05:45; 2025-b03/010@04:58; trade-executions b02/064 (16:00) |
| org_keep | 5 | 3-5 | 2023-b06/069@09:22; 2026-b10/124@08:28 |
| org_min_handles (NQ) | 20 | 15-40 | 2025-b06/078@03:09; 2026-b11/133@18:49 (30-40 open-to-CE) |
| org_band_edges | 75 / 120 | | 2025-b06/078@12:29; 2024-b11/036@92:52 (>=75 trade open) |
| es_scale | 0.25 | | 2023-b05/049@04:37 (ES 5 ~ NQ 20) |

## Invalidation / mitigation
- Bias from ORG ends once CE is hit (2024-b13/047@36:38); gap never touched = gap-and-go; deferred delivery after 10:30.

## Role in MMXM
- Session context for the 09:30 Judas/SMR (premium ORG + failed run = reversal, 2026-b11/138@69:33); target ladder (CE, full closure, -0.5/-1 SD of gap height, sd-projection.md).

## Evolution across series
- 2023 defined (16:15 settle, keep 3-5). PAC/trade-exec: 70% claim, octants. 2024: morning anchor, many conflicting size gates. 2025: size bands, ORG raided at open may serve as FPFVG. 2026: premium-short/discount-long rule, grid, SD of gap height.

## Ambiguities (open questions for the user)
- Size gates conflict (20/30-40/45-50/75). Default to 2025 bands; test others.
- MCP data includes ETH bars: build the RTH settle from the 16:14 1m bar explicitly.

## Refs
- `2024-b10/029@70:02` ORG model, CE in 09:30-10:00.
- `2025-b06/078@03:09` size bands.
- `2026-b10/124@08:28` premium/discount gap.
