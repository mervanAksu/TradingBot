---
concept: NDOG / NWOG (New Day / New Week Opening Gap)
aliases: [opening gap, event horizon (between gaps, 2024 variant)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [foundations, 2023, 2024, 2025, 2026, trade-executions]
default_variant: 16:59 close -> 18:00 open (NDOG Mon-Thu); Fri 16:59 close -> Sun 18:00 open (NWOG)
---

## Definition (own words, 2-4 sentences)
The price gap across the CME maintenance break: last print before 17:00 vs first print at 18:00 (NDOG), and Friday's last
print vs Sunday's 18:00 open (NWOG). Each is a zone with high, low and CE (quadrants when large), labelled for the NEXT
trading day, kept for several days/weeks and used as magnets, entry zones and bias references.

## Detection rule
```
NDOG(d): a = close of the last bar ending at 17:00 NY on day d (the 16:59 1m bar); b = open of the first bar at 18:00
   Mon-Thu only; zone = [min(a,b), max(a,b)], ce = mid; if a == b -> single line at b (2024-b04/008@09:29)
   label = next trading day; keep last ndog_keep
NWOG(w): a = close of Friday's 16:59 bar ; b = Sunday 18:00 open ; same zone logic; keep last nwog_keep weeks
quadrants q25/q75 only if size >= gap_quarter_min_ticks
cluster: >= 2 overlapping unfilled gaps on one side of price = draw side (2024-b02/004@51:21)
output: zone{top,bottom,ce,q25,q75,kind,label_date}
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| nwog_anchor | fri_1659_close | fri_1659_close, fri_rth_1615, fri_body_close_to_mon_open, rth (Fri close -> Mon 09:30) | 2023-b04/039@05:51; 2024-b05/011@07:16; foundations b02/002@02:06; 2023-b04/039@14:36 |
| ndog_keep | 5 | 3-5 | 2024-b02/003@23:54 |
| nwog_keep | 5 | 4-12 (<=60 days) | 2023-b04/039@04:17; 2026-b01/019@32:23 |
| gap_quarter_min_ticks | 80 (20 NQ handles) | 0-200 | 2024-b02/004@15:56 |
| skip_holiday_week_nwog | true | bool | 2023-b05/046@16:05 |

## Invalidation / mitigation
- One touch does not retire it (2026-b02/029@07:49); stays a level until expiry; CE is the main target.

## Role in MMXM
- HTF draw/target (NWOG CE, gap clusters); premium array for SMR (2026-b04/060).
- Dense gap layers near price = HRLR "speed bumps" (2024-b08/021@25:08).

## Evolution across series
- foundations: NWOG from Friday BODY close to Monday open. 2023: 16:59/18:00, RTH variant, keep 4-5. 2024: 5 days / 5 weeks, next-day labelling, quarter only > 20 handles; NWOG anchor inconsistent (16:59 vs 16:15 vs 17:00). 2025: settle 17:00 or 16:00 quoted; one file says Sunday 17:00. 2026: 16:59 -> 18:00, Monday 18:00 NDOG is the week's key.

## Ambiguities (open questions for the user)
- NWOG Friday anchor (16:59 ETH close vs 16:15 RTH settle). Default 16:59 (3 series agree). On TradingView NQ1! check whether the 18:00 Sunday bar exists in MCP data.

## Refs
- `2024-b02/003@17:42` NDOG 16:59 -> 18:00, next-day label.
- `2023-b04/039@12:01` price orbiting NWOG = consolidating week.
- `2026-b01/001@31:07` NDOG belongs to next day.
