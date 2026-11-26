# Series price-action-chronicles - digest (reduce of price-action-chronicles-b01)

Scope: 11 episodes, 2026-08-03 to 2026-09-01, mostly NQ 1m (one ES), live/hypothetical tape reads. Many are demo/paper trades.
Refs: `b01` = price-action-chronicles-b01, form `b01/<NNN>@mm:ss`. Episode 002 is a noisy translated transcript.
MMXM is only implicit (raid -> CISD/IFVG -> partials); this series is mostly about grading ranges and wicks.

## Core teachings
1. Every range (ORG, daily imbalance box, pre-news range, final-hour range, PM/AM range) is sliced into quadrants/octants (0.125) and even sixteenths; a PD array touching a slice line is "qualified" (b01/002@31:28, b01/008@04:05, b01/010@25:54).
2. Two independent grids landing on the same price = preferred objective (b01/001@56:33, b01/010@24:52).
3. RTH Opening Range Gap (prior 16:15 settle vs 09:30 open) is a first draw; its CE trades by ~10:00 about 70% of the time, otherwise treat as deferred (b01/001@56:33, b01/002@97:22).
4. Opening range = 09:30-10:00; the 1-hr dealing range completes 10:30 and expansion often follows it (b01/006@15:02, b01/001@42:59). PM equivalent: 13:30-14:00 (b01/011@02:50).
5. A wick is a PD array: split at its CE. Long = bodies stay in the upper half of a discount wick; short = bodies stay in the lower half of a premium wick; a body close through CE is the warning/exit (b01/004@27:17, b01/011@28:11, b01/002@58:13).
6. Wick beats an adjacent FVG as the reference array; stacked CEs (wick + FVG) = stronger (b01/011@11:01, b01/002@78:59).
7. IFVG: needs a close through the gap, a return into it, and a hold at/above its half; entries live inside the gap, stop just beyond its far edge (b01/007@11:55, b01/001@15:30, b01/004@03:39).
8. Raid long entry must fill below the targeted sell-side low; right after, the raid candle should close above its own wick CE and the next above the IFVG (b01/004@15:28, @17:30).
9. In strong order flow, pullbacks into an imbalance only tag its high/CE and leave it partly open; full closure of the gap weakens bias (b01/005@15:49, b01/007@09:54).
10. Pyramid only in the cheap half of the entry-to-target range (EQ rule); re-anchor when stops are taken (b01/004@22:08).
11. First partial funds the trade, stop then goes to BE+costs; a raised stop never goes back down (b01/001@21:53, b01/009@42:46).
12. Final-hour (MOC) short template: after an all-day trend, 15:00 premium wick with bodies stuck in its lower half, run of old highs, short in the 15:50-16:00 macro, target = -0.5 projection of the 15:00+ range (b01/011@19:22, b01/010@16:35).
13. Event-week hygiene: no live trading Thu/Fri of NFP week or Jackson Hole week; on Monday of NFP week OK (b01/002@06:35, b01/003@12:26).
14. Seek-and-destroy profile (Jackson Hole day 1): every swing extreme gets re-taken, so the first run is not a trend (b01/003@02:37, b01/004@04:40).
15. Pre-news range (07:00-08:29) is graded, SD projections (~-2.0) give the expansion target, 08:50-09:10 macro is the turn window (b01/008@01:32, @10:11).
16. Midnight open is kept on the chart as session magnet/first draw (b01/006@04:37, b01/007@10:55).
17. Buying/selling pressure is rejected as cause; turns are explained by measured ranges and time (b01/010@12:56).

## Mechanical rules
| Rule | Concept | Refs |
|---|---|---|
| ORG = settle(16:15 prior RTH) -> 09:30 open; CE is first draw; ~70% traded by 10:00 else skip | P4/L8 ORG | b01/001@56:33, b01/002@97:22 |
| FPFVG = first FVG after 09:30 (1-5m); holds while no body in its far half; carry prior day's FPFVG as level | P1 | b01/001@07:24, @42:29 |
| IFVG valid after close-through; wick-only = not inverted; bodies closing under a long's IFVG = flip | P2 | b01/001@44:46, b01/007@11:55 |
| Volume imbalance (1-tick body gap) = small support; keep unfilled in bull flow | P4 | b01/001@51:26, b01/002@117:08 |
| Raid-reversal confirm: close above wick CE, then above IFVG CE/body within 2 candles; else expect failure | S2/P2 | b01/004@16:59, b01/001@16:57 |
| Long entry only below swing/EQ low being raided | L4/L7 | b01/004@15:28 |
| Adds only below EQ (long) / above EQ (short) of entry->terminus range | S3 | b01/004@22:08, @30:51 |
| Stop under entry wick low (IFVG low -1 tick); after close above IFVG high/wick CE move to BE; trail under IFVG then under daily imbalance CE | risk | b01/005@01:36, @14:35, b01/007@02:36 |
| Partial 1 near halfway point of entry->target (a hair above it, NFP) or at first magnet; limit orders 1 tick shy of target | mgmt | b01/008@07:05, b01/004@03:07 |
| Optional stop-order partial under second wick low | mgmt | b01/007@22:42 |
| Short add while bodies stay out of upper half of premium wick; stop = wick high +1-2 ticks | mgmt | b01/011@26:09, @29:13 |
| Pre-news range 07:00-08:29 H/L, octants, SD projection ~-2.0 | T3 | b01/008@01:32, @10:11 |
| Final-hour range (15:00 to now) fib with -0.5 extension; reversal near CE of extension zone above old high | S3/T3 | b01/011@17:50, b01/010@16:04, @17:35 |
| RTH blocks: AM 09:30-11:30, lunch 11:30-13:30, PM 13:30, final hour 15:00-16:00, MOC 15:50-16:00 | T1 | b01/010@06:40 |
| Macros xx:50-xx:10, time only, no direction; if idle wait next hour | T5 | b01/002@63:14, @89:55 |
| Relative equal lows: right-hand low >= left-hand low; smooth stacks count, jagged ones do not | L4 | b01/011@08:28, @15:47 |
| Pre-market first half hour (07:00-07:30) graded and carried through first RTH hour | T1 | b01/006@06:08 |
| Month H/L/C (month ends 17:59) pinned across TFs as prep | L2 | b01/002@11:06 |

## Definitions vs DRAFT / other series
- ORG is new (not NDOG); NDOG is the 18:00 gap, ORG is the 16:15->09:30 gap (b01/001@64:12).
- Opening range is 30 min, not 5/15 (b01/006@15:02).
- P/D graded in octants/sixteenths, not just 50%; month PD uses prior-month 50% (b01/002@22:40).
- SIBI/BISI = daily FVG/imbalance box, gridded; suspension block = imbalance with volume imbalance at both ends (b01/004@01:34, b01/009@25:56). BPR = BISI and SIBI sharing one span, zone = outer H/L (b01/008@06:05).
- OB (here) = run of opposite-close candles before a CISD; stop at its open, confirmed by a close above their opens (b01/004@43:51). DRAFT P6 says last candle only.
- Rejection block here = body top of highest up-close to the swing high (b01/009@46:25); differs from DRAFT P9 (wick-to-body zone is similar, details differ).
- Wick as PD array with precedence over FVG: not in DRAFT.
- "Event horizon" = midpoint between IFVG high and wick CE; "cork" = sloppy upsloping consolidation under target, bullish; "mohawk" = few-tick excursion tolerated if bodies don't close beyond (b01/004@28:17, @44:52, b01/008@03:04).
- Buy-side liquidity = any prior high, no special marking (b01/002@24:14).
- Overnight prints count less than RTH prints (b01/001@78:16).

## MMXM material
- Raid long (20260827): two-sided 09:30 raid, drop into daily BISI octant, sweep below equal lows, buy below that low in the 09:50-10:10 macro, 10 contracts incl. pyramid, partial at first inefficiency high, rest at buy-side (b01/004@09:15, @41:43; b01/005@01:04).
- Short (20260831): gap-down open fills half gap, exceeds ORG high, IFVG from the failed up-close, short on CE retest, scale 50-65% below swing low, rest to sell-side low (b01/002@112:57, @117:38).
- CISD after sweep: reclaiming a bearish gap is the trigger (b01/003@08:17); confluence of IFVG + wick CE + OB (b01/005@03:43).
- Final-hour SMR/distribution: all-day rally, premium wick, equal highs run, sell leg in 15:50 macro to minor pools then projection (b01/011@13:41, @31:17).
- Partials at minor pools in order (not clustered), consistent with spec decision 4; first partial then stop to BE (b01/010@22:50).
- NFP two-stage delivery: stop run, then reversal into pre-news range during the macro (b01/008@01:01).

## Session-phase logic
- After a trend/selloff day expect AM consolidation; big gap = bias toward fill but chop (b01/001@29:42).
- Open serves the nearer gap first, then re-tests opposite liquidity (b01/002@95:20).
- CPI/PPI-week Mon/Tue = HRLR chop; trends mostly in London/pre-market; one RTH session may trend briefly (b01/006@02:03).
- After 10:30 range expansion likelier (b01/001@61:24).
- NFP week: Mon-Wed clean until ~11:00 (b01/009@03:11). On 10:00 news wait ~30 min after open (b01/002@08:35).
- All-day trend + final-hour pullback to discount = expect turtle-soup run of highs then reversal at MOC (b01/010@11:48).

## Discretionary items needing a proxy
- "Smooth" vs "jagged" equal highs/lows (tolerance in ticks).
- Strength of order flow ("IOFED poke only"): proxy = depth of gap fill as % of gap.
- "Large wick" qualifying as PD array; "massive decline candle" (use ATR multiple).
- Seek-and-destroy day identification (event calendar flag).
- Daily bias statements ("bearish until daily reaches zone") - needs HTF draw rule.
- Instant rebalancing rating of an array (reaction at next candle) (b01/002@116:37).
- Anticipation before candle close (b01/007@19:06) cannot be coded; use closed-bar versions.

## Open questions
- Direction/instrument dependence of ORG 70% claim; ES vs NQ.
- -0.5 extension: of range size beyond the extreme, and which CE is used for reversal.
- Octant anchoring: wick extremes vs bodies; tolerance for mohawk and equal-level tests.
- FPFVG timeframe (1m only?).
- Many trades are hypothetical/demo; fills may not be achievable.
- BISI/SIBI orientation unreliable in auto-subs; episode 002 translation noisy.
