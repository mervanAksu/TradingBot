---
concept: TGIF and weekly profiles
aliases: [TGIF retracement, weekly profile, Thursday reversal, weekly open]
status: VERIFIED
confidence: medium
category: time
series_seen: [foundations, 2023, 2024, 2025, 2026]
default_variant: after a one-directional week, Thu 13:00 -> Fri close retraces 20-30% (max 40%) of the weekly range
---

## Definition (own words, 2-4 sentences)
In a one-directional week, from Thursday around 13:00 into Friday's close, price tends to retrace 20-30% of the week's range
(up to ~40%); if Friday does not, the next Monday often does. Weekly profiles: in a bullish week the low tends to form between
Sunday's open and Wednesday morning (best odds Tuesday London to Wednesday NY), Thursday often prints the opposite extreme,
and weekly bias is read relative to the weekly open.

## Detection rule
```
week range W = [low, high] from Sun 18:00 to Thu 13:00 (tgif_anchor)
one_directional = (close_at_thu13 - W.low)/(W.high-W.low) >= 0.75 (bullish) or <= 0.25 (bearish)
TGIF levels (bullish week): W.high - f*(W.high-W.low) for f in {0.20, 0.25, 0.30, 0.40}
active window: Thu 13:00 -> Fri 16:00 ; stand aside after 20% printed and price flat (2024-b05/010@136:42)
skip when: runaway Friday, ATH (2025-b03/020@00:31)
weekly profile: weekly_open = Sun 18:00 open (default) | Mon 00:00 (2023-b06/072@03:28)
   bullish-week invalid if new weekly low after Wed 08:30/09:30 (foundations b01/008@13:13)
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| tgif_levels | 0.20/0.25/0.30 (+0.40) | | 2024-b05/010@04:17; 2026-b02/034@41:03 |
| tgif_anchor | Thu 13:00 | Thu 13:00, Fri open | foundations b02/002@05:43 |
| weekly_open | sun_1800 | sun_1800, mon_0000 | foundations b01/008@02:20; 2023-b06/072@03:28 |
| one_dir_thr | 0.75 | 0.6-0.9 | proxy |

## Invalidation / mitigation
- Window ends Friday close; carry to Monday flag.

## Role in MMXM
- Weekly-scale target/partial; Thursday/Friday reversal context; weekly sell model examples (2026-b03/058).

## Evolution across series
- Consistent 20-30% across foundations, 2023, 2024, 2025, 2026; max 35-40% added later.

## Ambiguities
- Definition of "one-directional"; incomplete-week range at Thu 13:00.

## Refs
- `2023-b06/074@28:13`; `2024-b02/005@96:56`; `2026-b01/015@00:32`.
