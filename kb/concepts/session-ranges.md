---
concept: Session ranges and HTF liquidity levels (PDH/PDL, PWH/PWL, session H/L)
aliases: [Asia range, London range, pre-market range, 07-09 range, opening range, FHDR, ONR, MOR, PM opening range]
status: VERIFIED
confidence: high
category: time
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: windows below in NY time; daily H/L on the CME 18:00-17:00 trading day
---

## Definition (own words, 2-4 sentences)
Each session leaves a high and low that are liquidity pools for later sessions, and some fixed windows form dealing ranges
that are graded and projected. Prior day/week/month highs and lows, and the 3-day high/low, are the HTF pools. A session is
classified as consolidation, expansion (trend), retracement or reversal from its range and overlap.

## Detection rule
```
windows (NY, [start, end)):
  asia_range 18:00-00:00 (killzone 19:00-21:00) | london 02:00-05:00 | pre_market 07:00-09:30 | range_07_09 07:00-09:00
  (07:00-08:30 on 08:30-news days) | pre_news 07:00-08:29 | premarket_or 07:00-07:30 | OR 09:30-10:00 | FHDR 09:30-10:30
  ny_am 09:30-12:00 (liquidity range) | lunch 11:30-13:30 | pm_or 13:30-14:00 | ny_pm 13:30-16:00 | final_hour 15:00-16:00
  MOR 00:00-00:30 | ONR 00:01-04:59 | prior RTH final hour 15:00-16:00
levels per window: high, low, EQ (+ grid), taken_at (relative-equal-hl.md run_mode)
HTF pools: PDH/PDL (trading day 18:00-17:00), 3-day HH/LL (today = day 1), last 5 daily H/L, PWH/PWL (Sun 18:00-Fri 17:00),
   prior month H/L/C (month ends 17:59 on last day), 3-month and 12-month H/L ; ignore Sunday's own H/L for daily lists
session phase classifier (input to mmxm-spec.md gating), per completed window W:
   rng = W.high - W.low ; adr = ATR(14, D) scaled by window share ; ov = mean bar overlap (hrlr-lrlr.md)
   consolidation if rng <= cons_k * expected_rng and ov >= 0.5
   expansion if rng >= exp_k * expected_rng and |close-open| >= 0.6*rng
   reversal if W took the prior window's extreme on one side and closed beyond the prior window's EQ on the other
   retracement otherwise when move is against prior expansion and stays within 50% of it
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| day_boundary | 18:00 | 18:00, 00:00 | 2024-b08/023@03:39; 2023-b01/006@22:38 |
| asia_window | 18:00-00:00 (kz 19:00-21:00) | 19:00-05:00, 20:00-00:00 | 2024-b02/005@49:39; 2026-b12/140@24:33 |
| london_window | 02:00-05:00 | 01:00-05:00 | 2024-b13/044@46:21; 2025-b03/014@03:39 |
| cons_k / exp_k | 0.6 / 1.2 | | proxy |
| range_07_09_newsday_end | 08:30 | | 2026-b01/004@03:08 |

## Invalidation / mitigation
- Levels stay until taken; taken levels kept as references (extended right).

## Role in MMXM
- Pools for SMR raids and partial targets; session-phase classifier implements user decision 3.
- 7-9 trend -> AM chop; 7-9 consolidation -> AM expansion (2026-b02/029@01:35).

## Evolution across series
- 2022 declares Asia not useful for indices; 2024/2026 give an Asia protocol (19:00 key, 19:00-21:00 work).
- Session alternation (trend then consolidation/reversal) stated in foundations and 2026.

## Ambiguities (open questions for the user)
- PDH/PDL day boundary; session classifier thresholds.

## Refs
- `2023-b06/067@17:34` session liquidity ranges.
- `2024-b03/007@160:28` daily liquidity list.
- `2026-b02/030@04:13` 07-09 classification.
