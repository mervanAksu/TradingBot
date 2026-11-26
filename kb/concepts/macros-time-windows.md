---
concept: Macros and time windows (killzones, Silver Bullet, lunch, news)
aliases: [macro, killzone, Silver Bullet, lunch macro, MOC, time distortion]
status: VERIFIED
confidence: high
category: time
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: macro = xx:50 to xx+1:10 NY every hour; plus 15:15-15:45 and MOC 15:45-16:00
---

## Definition (own words, 2-4 sentences)
A macro is a 20-minute window from 10 minutes before an hour to 10 minutes after it, in which the delivery algorithm runs price
to a short-term high/low or an inefficiency. Macros give timing, not direction; if nothing happens, look to the next hour's
macro. Larger windows (killzones, Silver Bullet hours, lunch, last hour) frame which macros matter. News releases and FOMC
have their own two-stage timing.

## Detection rule
```
in_macro(t) = minute(t) >= 50 or minute(t) < 10   (NY), window id = hour of the :00 inside it
named (score bonus / allow-list): 02:50-03:10, 03:50-04:10, 06:50-07:10, 07:50-08:10, 08:50-09:10, 09:50-10:10, 10:50-11:10,
   11:50-12:10, 13:50-14:10, 14:50-15:10 ; extra windows: 15:15-15:45 (last-hour macro), 15:45-16:00 (MOC; hot 15:50-15:57)
08:30 = only half-hour algorithm (news print); not a macro
silver_bullet: 10:00-11:00, 14:00-15:00 (03:00-04:00 London, rarely used)
lunch: 11:30-13:30 (macro window; target = first prominent swing formed after 10:00 against the AM leg)
no_new_trades_core: 12:00-13:00 (foundations/2022) - variant filter
news gates: no position into 08:30/10:00/14:00 releases; first look 08:45 (or +15-30 min); FOMC: 14:00 fake, ~14:30 real, no entries before 14:40-14:45
rejected: xx:20/xx:40 "macros", 90-minute cycles (2024-b03/007@182:32; 2025-b05/054@74:56)
reaction point in a macro is one of {FVG, OB, short-term extreme}, at most two coexist (2024-b03/007@169:11)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| macro_filter | on (user decision 3) | on/off | kb/mmxm-spec.md user decisions |
| macro_set | all_hours | all_hours, named_only | 2024-b03/007@160:58; 2025-b04/044@12:13 |
| macro_pad_min | 0 | 0-5 | proxy |
| lunch_window | 11:30-13:30 | 11:30-13:30, 12:00-13:30, 12:00-13:00 | 2024-b05/010@31:08; 2023-b06/067@17:34; 2022-b01/005@09:58 |
| news_wait_min | 15 | 15-30 | 2024-b08/024@08:11 |
| fomc_no_entry_before | 14:40 | 14:30-14:45 | 2023-b02/021@05:39; 2026-b01/011@14:07 |

## Invalidation / mitigation
- n/a. Macro passes with no expansion -> wait next macro (trade-executions b02/064@64:19).

## Role in MMXM
- Entry timing filter (user decision 3); SMR often at a macro open (2026-b05/082 05:50 macro; 2026-b04/067 10:50-11:10).

## Evolution across series
- 2022: only 08:30, 09:30, 13:30, 14:00, 15:00-16:00. 2023: named list incl. 11:50-12:10, 15:15-15:45. 2024-2026: hourly xx:50-xx:10 rule stated explicitly; lunch 11:30-13:30.

## Ambiguities
- Overlap of 15:15-15:45 and 15:45-16:00; whether every hour's macro is tradable.

## Refs
- `2024-b03/007@178:24` 20 min xx:50-xx:10.
- `2026-b01/008@35:05` last 10 + first 10 minutes.
- `2025-b05/057@07:20` lunch macro 11:30-13:30.
