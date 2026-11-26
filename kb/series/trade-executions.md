# Series: trade-executions (reduce of b01 + b02)

Ref key: `b01` = trade-executions-b01 (files 009-061), `b02` = trade-executions-b02 (062-070). Format `<batch>/<NNN>@mm:ss`.
Scope: live/paper NQ (some ES) executions. 2023-24 files (009-051) are short scalps on 5s-1m; 2026 files (057-070) are NQ 1m with
daily context, many with explicit prices. Roughly 40-75% of each file is non-trading talk; only the mechanics are kept here.
Caveat: 064/065 transcripts are machine-translated and noisy; wording-dependent rules from them are lower confidence.

## Core teachings
1. Every trade is framed as "draw on liquidity + a stack of PD arrays that keep the idea valid"; the idea is wrong when bodies close beyond the lowest array in the stack (b01/010@83:22, b01/061@03:43, b02/070@24:01).
2. Typical long stack (inverse for shorts): low of the IFVG/FVG, its CE, CE of the supporting wick (or mean threshold of a down-close OB). Stop goes one tick under the lowest of these (b01/061@03:43, b01/059@19:06).
3. CE (50%) of a wick or gap is the workhorse level. Bodies may not settle on the wrong side of it; wicks may probe it (b02/062@27:17, b01/059@01:03, b02/064@48:42).
4. Wick grading: split a wick at CE. Bullish: bodies stay in the upper half. Bearish: bodies stay in the lower half. First close through CE = warning, stop moves behind it (b02/062@27:17, b02/064@57:43).
5. After a raid, confirmation = the next candle closes back beyond the CE of the wick/range it pierced (or engulfs the wick). If not, wait one more candle and re-enter only with the stop tight behind the wick (b02/062@14:25, b02/065@16:57).
6. IFVG only counts after a candle closes through the gap; a wick through it leaves it supportive/resistive (b02/065@15:30, b02/065@44:46, b02/062@17:30). One lecture adds a second requirement: a retest followed by a second close (b01/059@11:25).
7. "Mohawk" tolerance: price may poke outside a zone briefly; what matters is no body close beyond the far edge (b01/058@03:04, b01/061@11:29). No tick value is ever given.
8. Strength signature: part of a gap/imbalance left unfilled after a retest means continuation; a fully filled gap is weaker (b01/057@35:05, b01/059@09:54, b01/061@15:49).
9. Volume imbalance (body-to-body gap) is the weakest, most flexible PD array: usable as entry, partial or target, and price may trade through and back (b01/046@06:18, b01/047@03:12, b01/040@06:47).
10. Suspension block = volume imbalance at both the high and the low of one displacement; the gap between them has a CE used for entry. One-sided = plain volume imbalance (b01/057@25:56, b02/062@01:02).
11. Octant grading: split any range/PDA into 0.125/0.25/0.375/0.5/0.625/0.75/0.875. Daily PDA first touched intraday tends to react at its upper octant (b02/062@07:12, b01/058@11:12, b01/060@06:08).
12. Pyramiding only in the favourable half: longs at or below EQ of the range from entry low to terminus, shorts at or above; re-measure EQ after each raid; no adds beyond EQ (b02/062@22:08, b02/065@39:26).
13. Scale-out is the default: first partial(s) at the first minor liquidity/new extreme, stop to cost cover (~10 USD/contract round-trip), bulk at the main pool, runner behind a CE-based stop. A raised stop is never lowered (b01/009@07:21, b01/057@43:16, b01/043@06:57, b02/062@41:43).
14. Exit limits sit a few ticks inside the target (1 tick in 2026 files, ~3 ticks in 2023) so spread cannot cause a miss (b01/009@13:59, b02/062@41:43, b01/061@19:30).
15. Midnight (00:00 NY) open is a magnet and first resistance on a rally; take most size just under it (b01/059@07:20, b01/060@09:22).
16. Ranges that anchor the day: 07:00-08:30 pre-news range, 07:00-07:30 premarket opening range, 09:30-10:00 RTH opening range, prior-day final RTH hour (b01/058@01:32, b01/060@00:31, b01/060@14:30).
17. RTH opening gap (prior settle to 09:30 open): the gap CE is claimed to trade by ~10:00 about 70% of the time; if not, delivery is deferred past 10:30 (b02/064@96:20, b02/065@60:54).
18. Macro windows xx:50-xx:10 give timing, not direction; if the macro passes without expansion, expect it at the next hour's macro (b02/064@64:19, b02/062@52:05).
19. News days: NFP/FOMC moves are two-stage (first run traps, reversal in a macro); NFP-week Thu/Fri are off-limits for beginners; Mon-Wed to ~11:00 acceptable (b01/058@00:30, b02/064@14:14, b02/066@03:50).
20. Seek-and-destroy day: both sides get raided before the real run; stop goes beyond the second raid only (b01/061@16:20, b02/062@17:00, b02/063@01:04).

## Mechanical rules
| Rule | Concept | Refs |
|---|---|---|
| Long into a bullish IFVG/FVG in discount; stop 1-2 ticks under entry candle low, or under lowest of the 3-array stack | P1/P2 entry | b01/059@00:03, b01/061@03:43 |
| Short mirror: enter at/just above CE of a bearish imbalance or wick, or a bearish OB; stop above wick high / CE of the up candle | P1/P4/P6 entry | b01/046@00:32, b01/051@00:02, b02/068@01:11 |
| IFVG valid only after a candle closes through the gap; wick-only does not invert; after inversion bodies stay out of its far half | P2 | b02/065@15:30, b02/062@17:30, b02/066@06:21 |
| Optional stricter IFVG: close through, then retest, then a second close | P2 | b01/059@11:25 |
| Instant rebalance: next candle revisits the gap with no new imbalance = strongest IFVG; short at that candle's high, stop 1 tick over CE of the big up candle | P2 | b02/064@116:37, b01/020@03:07, b01/043@05:21 |
| Stack two PDAs (gap CE overlapping wick CE) for higher quality | confluence | b02/064@78:59, b02/067@08:22 |
| Sell-side raid long: price must trade below the low; entry at/below it, stop 1 tick under the raid wick; if stopped, re-enter full size with a new stop under the new low | liquidity raid | b02/062@15:28, b02/062@19:02 |
| Raid confirmation: raiding candle closes above midpoint of the pierced wick/range, else wait one candle | raid | b02/062@14:25, b02/062@16:29 |
| Pyramid longs only at/below EQ of (entry low -> terminus); shorts at/above; recompute EQ per new raid | pyramiding | b02/062@22:08, b02/062@30:51 |
| Pyramid at a retest of the IFVG pivot/low; in consolidation add in the lower half only | pyramiding | b01/059@02:36, b02/070@04:45, b02/065@39:26 |
| CISD re-add: add only if price retraces to the open of the candle series that delivered the move; then stop to cost | S2 | b01/051@02:10 |
| Pre-news range = high/low 07:00-08:30; qualify FVGs by their octant in it; project SD of bodies (-1 to -3) from it | T3 | b01/058@01:32, b01/009@11:28 |
| Dealing range for 09:30 session = first 30 min (07:00-07:30 premarket, 09:30-10:00 RTH), graded 0.375/0.625/0.75 | S3 | b01/060@14:30, b01/060@06:08 |
| Frame Monday from Friday's final RTH hour high/low | L3 | b01/060@00:31 |
| First partial just under the midnight open on a long; 5 of 7 contracts | L8 | b01/059@07:20 |
| Partial at each new extreme (new low for shorts) when none taken yet ("running down equity"); first partial funds costs | scale-out | b02/068@10:22, b02/064@68:37 |
| Event horizon: take profit just shy of the midpoint between two pools, remainder at the next | scale-out | b02/070@15:16, b02/064@68:37 |
| Partial only if price is beyond halfway between entry and draw (1 of 3) | scale-out | b01/058@07:37 |
| Stop ratchet: to cost after first partial/15-20 pts; trail under prior candle low or last pullback low; if a range redelivers the same distance as the last pullback, trail under the pullback low | stop mgmt | b02/065@06:46, b02/065@68:55 |
| Two consecutive same-colour candles forming an OB: trail the stop to that OB's open | stop mgmt | b02/062@43:19 |
| Stop to the 50% of the last opposite-close candle after close through the IFVG/octant (short) | stop mgmt | b02/066@07:53, b01/009@17:32 |
| Resting stop-sell below the wick low for part of the runner = "partial on retracement" | stop mgmt | b01/059@22:42 |
| Raise stop / flatten before scheduled 10:00 news; wait for the first 30 min of RTH after a 10:00 release | news | b02/063@06:41, b02/064@18:35, b02/065@99:33 |
| RTH gap: discount gap if 09:30 opens below prior settle; first target CE, then full fill; where daily BISI/SIBI octant equals gap octant, use it as primary draw | P5 | b02/064@96:20, b02/065@56:03 |
| NWOG short: sell at NWOG low after the 08:30 spike prints an intraday high; stop above NWOG high; add only on a higher pass | P5 | b02/066@00:02 |
| Sell at the high of the 09:30 opening gap when it coincides with the top of the daily imbalance box; outer target 25-30% retracement of the week range | P5 | b02/067@05:27, b02/067@09:55 |
| Half-gap target for a ~100-pt premium opening gap; premium sensitivity: no body above CE of the SIBI | gap | b02/068@01:00, b02/068@08:52 |
| Asia long: IFVG tied to the CE/octant of the prior RTH gap; targets are nearest equal highs, then prior gap CE/low | Asia | b02/070@00:08 |
| Entry in the middle of a 09:50-10:10 macro after the intraday low is raided; target intraday-high buy stops, 1 tick short | T5 | b01/061@01:04 |
| MOC window: hot period ~15:50-15:57; retrace after ~15:57; entry at CE of swing-low wick, stop under CE | T5 | b01/025@01:36, b01/025@00:32 |
| 5s/15s scalps: enter at IFVG or OB with a tiny stop, add at minor pools, first partial pays fees, runner for the HTF level | scalp | b01/028@00:31, b01/029@00:38, b01/040@00:30 |
| Weekly prep: mark prior month H/L/C (no monthly open), octant-grade the prior month range | L1/L2 | b02/064@15:58, b02/064@22:40 |
| Calendar: only USD red/orange events matter; NFP Thu/Fri no-go; post-holiday first day = 1 contract | filter | b02/064@14:14, b02/068@03:41 |

## Definitions vs DRAFT / other series
- P2 IFVG: DRAFT says "closes fully through". Here the trigger is a single candle close through the gap (CE-based in 062/065), and bodies must then respect it; one lecture adds a retest plus a second close (b01/059@11:25). A wick-only breach does not invert (b02/065@44:46). Tolerance is the Mohawk poke.
- P4 volume imbalance: DRAFT body-to-body gap confirmed; added that it is a weak, flexible array and that price can leave part of it open as a continuation sign (b01/046@06:18, b01/040@06:47). Suspension block (imbalance at both ends) is new (b01/057@25:56).
- P9 rejection block: the series uses the body top (highest up-close) of a swing high, not the whole wick zone (b01/057@46:25). Plus a separate "wick CE" tool (halves of a wick) which DRAFT lacks.
- S2 CISD: matches DRAFT (open of the delivering series), used here as pyramid/re-entry level (b01/051@02:10); 062 describes a consecutive same-colour series as an order block (b02/062@49:49).
- L8 midnight open confirmed as magnet/bias anchor (b01/059@10:55). NDOG/NWOG (P5) confirmed and used as entry zones (b02/066@00:02), plus a new family: the RTH opening range gap (settle to 09:30 open) with CE and octants (b02/064@96:20, b02/065@56:03). Settle time stated as 16:14/16:15 in 065, 16:00 close in 064.
- L1/L2/L3: DRAFT has no monthly levels; here prior month H/L/C are marked, monthly open ignored (b02/064@15:58). Opening range is 30 min, not 5 or 15 (b01/060@14:30). Purged pools are extended rightward as repeat references (b01/020@28:12).
- L4 equal highs/lows: "smooth" ones are draws; ones made jagged are suspect/trap zones (b01/043@02:46, b01/020@16:23).
- L5/L6 HRLR: used as a day label (midnight open + stacked unfilled gaps above, CPI/PPI week) rather than a coded run test (b01/059@11:25, b01/060@02:03).
- S3 premium/discount: also applied inside a single wick or gap (upper half = bullish defence) and to the prior month range (b01/061@06:52, b02/064@22:40).
- T3: SD projections here use bodies, not wicks, from the range extremes (b01/009@11:28), and the 07:00-08:30 range for news days (b01/058@08:37).
- T5 macros seen: 07:50-08:10, 08:50-09:10, 09:50-10:10, 10:50-11:10, 14:50-15:10, 15:15-15:45, 15:40, 15:50 MOC (b01/060@09:22, b01/058@05:05, b01/061@00:01, b01/028@00:31, b02/062@52:05, b01/025@01:36). Matches the xx:50-xx:10 spec decision.
- Not in DRAFT: first presented FVG (first FVG after 09:30), BISI/SIBI daily box (close of one candle to low of another incl. imbalance), event horizon, double tap, cork, institutional order flow entry drill, 1-hour dealing range at 10:30.

## MMXM material
- Sell model labelling in live trades: original consolidation, smart money reversal (SMR), low-risk sell/add, first-stage distribution (first leg, first partial), second-stage redistribution (longest, most animated leg) (b02/066@16:14, b02/067@23:11). Preferred phase to trade is the 2nd stage (sell) / 2nd-stage reaccumulation (buy) (b02/067@24:14).
- Stop anchoring: in the sell model keep the stop at the first-stage distribution high, not close behind price (b02/066@19:52).
- SMR on news: sell-side run at 08:30 then breaker/IFVG = Judas, reversal to premium (b01/009@12:28); pre-8:30 fake high then drop into a 4H FVG = Judas, target the buy-side above (b01/010@02:04).
- Spec mapping: entries here correspond to E1 (first gap after the shift: IFVG/FVG CE), with confirmation by CISD/IFVG close. Partials at each pool and stop-to-cost after the first match decision 4 of the spec (b01/043@06:57, b02/070@15:16). Targets are the next pool, the opposing day-range extreme, or a gap CE.
- Two-sided sweeps before the real move (megaphone): rally takes buy-side, drop takes sell-side, then the run (b02/062@02:35, b02/063@01:04). Buy-side clears early then sell draw below with rallies sold (b01/020@01:33).
- Algorithm overshoots equal highs slightly then reverses (b01/028@00:31); after a sweep a pullback should not retest the old pool (b02/070@21:59).
- Flush-aligned equal lows are likely engineered support expected to fail (b02/066@17:16).

## Session-phase logic
- Asia: slow unless news-driven; only trade easy pools, simple accumulation-type long into obvious liquidity (b02/070@07:32).
- Premarket 07:00-09:00: window for daily PDA reactions (b01/057@47:59); first 30 min 07:00-07:30 sets its range (b01/060@06:08); ETH tends to trend, RTH to range, and either AM or PM gets one trending leg (b01/060@05:08).
- 09:30-10:00: opening range; RTH gap CE expected by ~10:00; if consolidation persists, expansion after 10:30 (b02/064@96:20, b01/020@47:55, b02/065@60:54).
- Consolidation days (big overnight trend then flat morning): prefer longs/shorts toward the gap and pools, tape-trade the other side only (b02/065@27:02).
- PM: lethargic in January/summer; clean runs in AM; closing macros 14:50-15:10, 15:15-15:45, 15:50 MOC can drive price into a daily PDA (b01/025@05:31, b02/062@52:05).
- Event days: NFP first hour manipulative (b01/010@07:41); Jackson Hole day 1 = highest seek-and-destroy odds, day 2 unpredictable (b02/062@04:40); CPI/PPI weeks suppress Mon/Tue RTH (b01/060@02:03); month/year end less rule-bound (b01/020@13:50).
- Reversal vs retracement test: bodies unable to reach the CE of a daily IFVG and respecting its lower half = continuation of the prior trend (b02/062@55:10); a quick bounce from a daily IFVG after a drop = shorts trapped, equal highs next (b01/057@10:32).

## Discretionary items needing a proxy
- "Heaviness"/"willingness"/"respect": proxy = bodies stay inside/outside a defined half; count of body closes in the wrong half (b01/047@12:00, b01/057@35:05).
- Mohawk tolerance: tick value never given; make `poke_ticks` a parameter, test by bucket.
- Seek-and-destroy detection: no trigger given; proxy = both prior-session extremes taken before 10:00 followed by reversal (b01/061@16:20).
- Gradient/octant levels: code as range fractions on a chosen anchor; which range (daily box, session range, prior month) is a parameter.
- Cork pattern, "hot knife through butter", premium/discount "sensitivity": need price-action proxies (small-overlap candle cluster below target; low overlap with the gap).
- "Low-hanging fruit"/"easy pools": nearest equal highs/lows or session extreme.
- Anticipation of CE hit (70% at 10:00) is a stat to test, not assume.
- Hindsight stop rules (trail to OB open) are not rules until a trigger is fixed.

## Open questions
- Exact settle time/candle for the RTH gap (16:00 vs 16:14/16:15), and whether octant 0.125 is measured from the high or the low of a box (b02/064@46:11, b02/065@56:03).
- Whether the IFVG needs one close or close plus retest-close; default to one-close with an optional strict flag.
- First presented FVG: which timeframe and which FVG counts (b02/065@07:24).
- Wick CE: high-low midpoint or body-based (b02/064@48:42).
- Lunch macro (b01/046) times not stated; 10:50-11:10 is the nearest listed window.
- 2026 prices: 29,xxx in Aug-Sep and 30,7xx after the December contract roll (b02/070); check continuous-contract data for backtests. 067 first 4 min missing; file 069 absent.
- Risk sizing: only illustrations (about 0.75% per account b01/023@01:33; 2% stop on demo b01/020@09:47); no firm rule.
