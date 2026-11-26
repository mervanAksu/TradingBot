# trade-executions-b02 notes (map)

### 062 | 20260828 | NQ Trade Review & Deep Dive Into Price Delivery (Jackson Hole day 1 long)
tags: volume imbalance (P4), suspension block, FVG/IFVG (P1/P2), CE/octants, dealing range (S3), SMT-free liquidity raid, pyramiding, macros (T5), rejection block/wick halves (P9), CISD (S2), order block (P6)
- DEF: "Buyside balanced / sellside efficiency" daily PDA = range from one candle's close to another's low (volume imbalance + gap); drawn as grey box on intraday. Suspension block = a candle gap pair having volume imbalance at BOTH its high and low; single-sided is only a volume imbalance (@01:02, @03:07)
- RULE: Range sub-levels: every PDA/range is split into octants: 0.125 / 0.25 (quadrant) / 0.5 (CE) / 0.75 / 0.875. Anchor lines at the leftmost candle and project straight down to read all levels (@07:12, @24:10)
- RULE: Daily PDA first touched intraday reacts at its upper octant (0.125 from the high): price dropped to it, held, rallied (29,451 example); bodies not closing through the level = level is respected (@07:12, @19:44)
- RULE: Wick grading: split any candle wick at its CE; in a bullish context the bodies must stay in the upper half of the wick, a body closing in the lower half or below CE = weakness; wicks may probe CE but bodies may not (@27:17, @48:31)
- RULE: Buying sellside liquidity minimum criteria: price must trade below the low (stops taken); entry at/below that low is "buying the sell stops" (@15:28)
- RULE: Confirmation before holding a long after a sellside raid: the raiding candle should close above the midpoint of the wick/range it pierced; if the first candle fails to close above CE, wait one more candle then enter anyway only with stop right below the wick (@14:25, @16:29)
- RULE: IFVG confirmation: a candle that closes above the (formerly bearish) FVG's CE confirms the inversion; a later retest into it should hold. Close above wick CE + IFVG = no reason for price to revisit lower (@17:30, @18:31)
- RULE: Pyramiding: add longs only at/below equilibrium (50%) of the range from entry-region low to terminus; add shorts only at/above EQ; once price is beyond EQ of the intended run, no more adds. Range widens with every raid so recompute EQ from new low to the new target (@22:08, @23:09, @30:51)
- RULE: Stop management: stop sits just below the raid wick (1 tick buffer); if stopped, re-enter immediately with full size and a new stop below the new low. Futures: all brokers share the same low, so tight stops are viable (@19:02, @21:06)
- RULE: Stop trailing lesson (hindsight): once two consecutive up-close candles form an order block, trail stop to that OB's open instead of leaving it under the structural low (@43:19)
- RULE: Partial plan: 10 contracts built (6 + 4 pyramid); 4 off at first target just above the first high, then 5 of remaining 6 at the next high, 1 runner for the buyside/terminus. Limit exits placed 1 tick below the target level (@16:29, @41:43)
- RULE: Target = high of the volume imbalance/gap on the way up (gap CE protects higher prices); gaps left in the upper half of a run, close to the target, usually stay open until the target is hit (@46:00)
- MMXM: Seek-and-destroy day sequence: rally takes buyside, drop takes sellside (lower low), then reach for the higher high; engineered stops on both sides (megaphone-like expansion) before the real run. Bias came from daily: price returning to premium after failing to trade into the discount imbalance (@02:35, @17:00)
- MMXM: Entry model = sell-stop raid below relative equal lows / key low + wick CE reclaim, entry in discount, pyramiding in discount with stop under raid, targets = old high, buyside, daily inefficiency high (@15:28, @43:21)
- CTX: Jackson Hole day 1 = highest likelihood of seek and destroy; commentary used as smokescreen; avoid chasing; day 2 = expect unexpected (@04:40, @11:21, @60:00)
- CTX: Closing-hour macros: 14:50-15:10 and 15:15-15:45 runs, last 20 min (15:40) and final 10 min (15:50 MOC) used to drive price into a daily IFVG/PD array (@52:05, @53:07)
- CTX: Bearish daily context test: price enters key daily IFVG, bodies cannot reach its CE, respects lower half = bearish continuation; fade back to old inefficiency (@55:10)
- EX: 20260827 NQ 1m: sell-side swept below 29,451 octant zone / equal lows ~09:55-10:07, buy at ~29,50x, stop 29,501.75 (low 29,502.00 touched), 4 pyramid contracts at discount, partials at highs, stopped on runner near target (@15:28, @28:48)
- EX: 20260828 (Fri) NQ: afternoon macro run into daily IFVG at 29,662 (CE of wick) then rejection (@53:37)
- skip: large parts are rant/personal (broker rant, "my language", fasting, retail jabs).

### 063 | 20260828 | NQ Trade Review, Jackson Hole Day 2 (short wrap)
tags: seek and destroy, IFVG (P2), wick CE (P9), liquidity raid, fib projection, order block, news (10:00)
- MMXM: Seek-and-destroy profile as a repeatable sequence: low -> higher high -> lower low -> higher high (each side's liquidity taken, then back) over a range measured from the 07:00 start to the day's extremes (29,597.5-29,665) (@01:04, @11:20)
- RULE: Entry pattern day 2: displacement down at 09:30 leaves an inefficiency that is graded as a potential IFVG (not as "first presented FVG"); wait for price to trade into a fib low projection (1-2 ticks beyond OK), then back above the FVG to qualify the inversion; entries sit inside the IFVG; bodies must hold above its half (CE) (@04:38, @05:10, @06:10)
- RULE: Prior-day wick reused: Thursday 09:55 discount wick, upper half respected by bodies again (price traded into the wick's lower half but no body close there) (@02:37, @07:12)
- RULE: Exit/stop: take partial on way out into old inefficiency; before scheduled 10:00 news raise stop; if price fails at the midpoint again, roll stop to just below CE of the longest wick (hindsight fix) (@06:41, @22:08)
- CTX: Price run draws: 29,757.25 as next upside draw, then 29,83x region (@03:37)
- CTX: Avoid/size down on Jackson Hole week and on 10:00 chair speech; "can trade every day" for advanced, but not-new students should tape-read only (@12:56, @13:57)
- skip: Mostly commentary (Camtasia rendering, discipline, Friday off, learning path: log observations, backtest, 2-3 months demo before live).

### 064 | 20260831 | How New Students Should Start Part 1 (weekly prep + live NQ tape-read, Aug 31)
tags: HTF levels (L1/L2), premium/discount (S3), octants, volume imbalance/suspension block (P4), IFVG (P2), RTH opening gap (P5), macros (T5), wick CE (P9), economic calendar, partial profit
- RULE: Weekly prep (Sat/Sun): mark previous month high, low and close as horizontal lines (label right-aligned, visible on ALL timeframes incl. seconds); do same for weekly; monthly OPEN is not needed because new-week/new-day gaps already contain it. Do NOT label buyside/sellside on these: monthly high = buyside above it, low = sellside below (@11:06, @15:58, @26:19)
- RULE: Anchor a fib/range on previous month low->high; price above 50% = premium of that month, below = discount. Show 0, 0.5 and quadrant/octant lines only (hide mid-line clutter on LTF) (@22:40, @28:21)
- RULE: Daily "buyside imbalance / sellside inefficiency" (BISI/SIBI) box = zone from a candle's close down to another's low incl. volume imbalance; if volume imbalance exists on BOTH ends it is a suspension block. Grade octant levels: 0.125 = 29,451, CE 29,211.25 in this example (@31:28, @46:11)
- RULE: Daily PDA reaction: price entering the upper part of the box first targets its upper octant (0.125) then the quadrant (29,371 example); lower half of the box = no candle bodies yet, so if bodies close below CE expect the whole lower half to be explored (@47:41, @53:51, @104:00)
- RULE: Wick/CE tracking: for every big wick, split in half and watch whether bodies close in the upper half (premium wick). Bearish bias: bodies must stay below the midpoint; first close above CE of the wick = reason for concern, move stop to just above the level; short stop = above wick/high (@48:42, @57:43, @59:15)
- RULE: Partial profit on shorts: take some (e.g. 1 of 3 micro contracts / 50-65% of position) when price reaches a point about halfway between the new low and the next quadrant-level ("event horizon" = midpoint between two measured levels), then move stop above the last swing high; this finances the trade so a stop-out costs nothing (@68:37, @113:27, @132:09)
- RULE: Macro: last 10 min of each hour and first 10 min of the next (xx:50-xx:10); gives timing only, not direction; if price consolidates through it, the expected move should fire at the next hour's macro; the consolidation itself weakens the directional thesis (@64:19, @82:34, @89:55)
- RULE: RTH opening gap: mark prior-day 16:00 close (violet line). If 09:30 opens below it = discount gap, above = premium gap. Gap fill odds claimed: half-gap (CE of the gap) trades by ~10:00 in about 70% of cases; target gap CE first, full close second (@96:20, @97:22)
- RULE: Buyside/sellside "minor" levels: small equal lows/highs and wick-lows are tracked as minor liquidity; a raid beyond them followed by quick return above a bearish FVG's CE => the FVG becomes an IFVG and the low is (at least) an intermediate low (@76:35, @80:59)
- RULE: Instant rebalancing: candle that closes and next candle immediately revisits the gap without leaving a volume imbalance = strongest IFVG; short entry on the next candle's retrace to the candle's high, stop one tick above CE of the big up candle (@116:37, @117:38)
- RULE: Stacking: choose FVG whose CE overlaps wick CE (two PDAs nested) for higher quality (@78:59)
- DEF: Economic calendar filter: only USD, orange/red folder events matter; NFP week Thursday and Friday = no trading for beginners; safe window is Monday to Wednesday ~11:00; NFP-week Monday always tradable; other Mondays are experience dependent (@05:05, @14:14)
- DEF: Low-impact/grey items ignored; 10:00 releases: wait for first 30 min of RTH to build liquidity/inefficiency, then trade what remains after the news (@18:35)
- CTX: Monthly opening: new month (Sep) is a seasonal volatile period; price in upper half of July range, lower half of August range (@22:40)
- CTX: Pre-open expectation: price drifting toward the gap target then, after 09:30, rallies through gap and takes the buyside; the early up-run leaves sellside (low under the opening) unprotected so a return down to sweep that low is expected (@106:31, @187:57)
- EX: 20260831 NQ 1m 08:30-09:35: sell below 29,4xx session low, partial at ~55-60 pts, stop 29,412; open below Friday close 29,487.5 -> gap up filled within 5 minutes of 09:30 (@93:00, @103:29)
- skip: Heavy chart-formatting tutorial (TradingView colors/alignments/layouts), personal anecdotes; transcript is a machine-translated, noisy Russian-English mix, wording uncertain.

### 065 | 20260901 | How New Students Should Start Part 2 (hypothetical tape-read, Tue Sep 1 morning, NQ)
tags: opening range gap (RTH gap), first presented FVG (FPFVG), daily BISI/SIBI octants, IFVG, order block (P6), consolidation profile, partials, pyramiding, wick halves (P9), macro/10:30, NFP week
- RULE: Level confluence target: grade the daily imbalance box with octants, project the RTH opening-range-gap (prior 16:14/16:15 settle -> 09:30 open) CE and octants from the candle open; when a daily octant price equals an opening-gap octant (here 29,212 = lowest octant/lower quadrant of both) use it as the primary draw, ahead of the plain gap midpoint (@56:03, @57:03, @82:03)
- RULE: Gap midpoint stat repeated: the opening-gap CE is expected to trade by ~10:00 (about 70%); if it hasn't, deferred delivery after 10:30 (1-hour dealing range established, algos "start firing") (@56:33, @60:54)
- RULE: Entry pattern on a large discount gap in consolidation: first presented FVG (first FVG after 09:30) of the prior day/week (e.g. Aug 24 FPFVG) used as foothold; long when bodies stay out of the lower half of that FPFVG; wicks may poke in; stop under the FPFVG low/candle low (@07:24, @17:31, @41:14)
- RULE: IFVG qualification: a down-close FVG becomes an IFVG only after a candle CLOSES through it; wicking below without closing means it is still supportive (not an inversion); a close below after a high was taken converts it to a sell signal (@15:30, @44:46, @73:30)
- RULE: Wick confirmation: after a drop into a wick, next candle must close above that wick's CE (dash line) or completely engulf the wick; otherwise setup is unconfirmed; bodies should remain in upper half of the wick (@16:57, @19:12, @23:16)
- RULE: Stop management: move stop to entry/break-even+commission after first ~15-20 point move (e.g. stop to 29,170/92 "covers cost"); partial at first buyside, trail stop under the previous candle low, or under the low of the last pullback when a range redelivers (@06:46, @16:16, @69:30)
- RULE: Trail by range redelivery: measure last retracement range; if price re-trades that same range distance above, bring stop under the pullback low; otherwise leave stop (@68:55, @70:01)
- RULE: Add-on (pyramid): in consolidation add at lower half only (long) -- add into the daily imbalance box top ("institutional order flow entry drill") and leave the volume-imbalance portion unfilled; unfilled tick-gap between candle close and next open = bullish evidence (@39:26, @51:26, @88:00)
- RULE: Shorts in same session: fill at wick CE / premium; add more (2 -> 4 minis); exit if price retakes the first presented gap (@34:00, @60:00)
- RULE: Sizing in hypothetical drill: 2 minis, risk ~20-30 points, partial 1 contract at each liquidity pool (e.g. 29,172 -> +49 handles on one partial), then last contract trails; micro = $2/pt, mini $20/pt, 4 ticks per point (@22:34, @73:59)
- MMXM: Day profile: overnight "serious trend" lower (~500 handles) -> morning expected consolidation, then a run into the opening-range gap/buyside pools; first the stop run of lows, then rally to FPFVG and buyside (@29:09, @41:14, @58:34)
- CTX: NFP-week Tuesday after big consolidation + huge discount gap: prefer longs toward gap while in consolidation; shorts allowed only as quick tape trades; news 10:00 (ISM) -> be flat/small before it (@27:02, @41:14, @99:33)
- CTX: Overnight (ETH) behavior counts only if confirmed in RTH; RTH booking at same price more significant (@78:16)
- CTX: Seasonal tendency note: lower prices into Sep; low-resistance objective chosen on consolidation days (@12:17, @99:33)
- EX: 20260901 NQ 1m: long ~29,189 (stop 29,161), partial 29,172 (+33.5), then +49 on second partial, stopped out around 10:00 news, re-long 29,132 (2 minis), partials 29,153.5/29,193/29,213; octant 29,212 hit; net ~125-130 handles (hypothetical) (@05:53, @22:34, @62:37)
- skip: much commentary on teaching, commenter rants, family chatter.

### 066 | 20260903 | Trading NFP Thursday: High Resistance Liquidity Runs (live NQ short, real account)
tags: NWOG (P5), opening range gap, market maker sell model, smart money reversal, 1st/2nd stage distribution, IFVG (P2), FPFVG, octants, HRLR (L6), NFP
- RULE: Short entry at the New Week Opening Gap: sell at/into the NWOG low after the 08:30 news spike printed an intraday high; stop just above the NWOG high; add only if price makes another higher pass (@00:02, @03:20)
- RULE: IFVG validation for shorts: a small gap above price validates as IFVG only when a candle closes below its low (here below 29,292.25 = high of an up candle); until then retracements may wick to a quadrant/octant line but bodies must not sit in its upper half (@06:21, @08:53, @09:53)
- RULE: Stop ratchet: after close below the IFVG (and below an octant level, e.g. 29,291.25), move stop to the mean threshold (50%) of the last up-close candle (29,340), later to just above the prior-day FPFVG CE; worst case becomes a locked profit (@07:53, @10:24, @18:17)
- RULE: Partial/scale plan on 3 contracts: first contract off at a clearly resting equal-low pool (low-hanging fruit), buy back 2 / keep 1 runner; do not require the far target (@03:20, @11:59)
- RULE: Reaction checks: price spikes to a quadrant line then reacts sharply; bodies respecting the lower half of a FPFVG (Wed Aug 26) and failing to tag the high of a candle that defines an IFVG = bearish respect (@18:49, @19:20)
- RULE: Add on retracement: add a short when a deep retrace reaches the high of Tuesday FPFVG but bodies stay out of the upper half of the inefficiency; risk accepted via original stop (@25:18, @25:52)
- RULE: Opening-range-gap read: price should "go through" the RTH gap (29,249.5-29,194.25) without discount sensitivity (no bodies bouncing) toward 29,110 (Aug 24 FPFVG); take out the gap low then drop stop (@14:32, @18:17)
- MMXM: Sell model labelling: entry at smart money reversal (SMR) after NWOG raid; low-risk add; first-stage distribution = initial leg where first partial is taken; "second stage redistribution" = longest, most animated leg; stop anchored to the first-stage distribution high, not close behind price (@16:14, @17:16, @19:52)
- MMXM: Perfectly aligned bodies at one level below (flush equal lows) are likely engineered support, expected to fail later (draw = relative equal lows / sellside) (@17:16, @03:20)
- CTX: NFP Thursday: heavy manipulation / manual intervention; ICT trades it only with reduced size, taught to students to avoid; drawing the 08:30 news spike up into NWOG is "selling the story" (@03:50, @07:22)
- EX: 20260903 NQ 1m ~09:50-10:30: short at NWOG low, three contracts total, stop 29,340, targets 29,178 min, FPFVG Aug 24 ~29,110 (@01:35, @11:28, @26:22)
- skip: Half is commentary (market replay proof, critics, being away for dogs).

### 067 | 20260904 | My Model On NQ NFP Friday (live NQ short, holiday week)
tags: market maker sell model (MMXM), smart money reversal, first/second stage distribution, original consolidation, NWOG (P5), NDOG (P5), opening range gap, daily BISI/SIBI high, retracement % of weekly range, partial/stop ratchet
- MMXM: Day recognised as MM sell model: original consolidation -> smart money reversal (SMR) -> low-risk sell (add) -> first stage distribution -> second stage redistribution (longest leg); preferred phase to trade = 2nd-stage redistribution of a sell model / 2nd-stage reaccumulation of a buy model (@23:11, @24:14)
- RULE: Short location: sell when price has rallied to the HIGH of the RTH opening range gap (9:30 open) that coincides with the top of the daily volume imbalance / BISI-SIBI box; stop above that high, then pull stop down in steps as lows are taken (@05:27, @05:58, @15:15)
- RULE: Targets: sellside under yesterday's NFP price-run low (~29,500) and yesterday's NDOG/NWOG low; retracement benchmark of the weekly range: 25-30% retracement (e.g. 29,471.25) as outer target; actual exit placed ~6 pts above ("limit just below") (@09:55, @13:03, @18:07)
- RULE: Stop trail: take stop to lock profit only after the low (29,502) is taken; wait for an expected pop before dropping stop; closed rest at stop-out +64.7 pts when lost interest (@12:32, @21:33)
- RULE: Nested PD arrays: IFVG/NWOG/volume imbalance overlapping at one level = discount sensitivity expected (bounce) but preferred behaviour is "hot knife through butter" (@08:22, @08:52)
- CTX: NFP Friday: wait first hour before engaging; relative equal highs left untouched above reduced confidence in early short ("felt uncomfortable"); holiday weekend: expect slower, demand more (@24:45, @30:31)
- CTX: Market-maker logic argument: stop-hunt below 29,500 after NWOG tag is expected to be completed (longs stops resting there are the draw) (@13:03, @13:34)
- EX: 20260904 NQ 1m 09:30-11:06: short at the 09:30 opening-gap high / daily BISI-SIBI high, stop first risking ~$480 then ratcheted down, closed manually for about +$6,470 total (multi-contract) before the limit target at the Thursday FPFVG high (@05:58, @21:33)
- skip: banter about "my concepts only work some days", market replay denial, Deadpool joke.

### 068 | 20260908 | How To Engage Price After Holiday Volume Days (paper trade, Tue Sep 8)
tags: premium gap, opening range gap, FPFVG, suspension block (P4), NWOG (P5), partial profits ("running down equity"), premium sensitivity, holiday volume
- RULE: Holiday re-entry: first session after a holiday (low-volume Monday), trade one contract/paper only to "get in alignment with price"; no size until price confirms expectation (@03:41, @07:26, @29:46)
- RULE: ~100-handle premium opening gap: first target = half gap (CE of gap 9:30 vs prior settle); then past the CE the sellside liquidity pool inside a suspension block; full gap closure beyond (@01:00, @06:26, @16:41)
- RULE: Short at half of a wick (CE) with stop above the wick high; target the volume-imbalance/suspension block high-low area (@01:11, @02:40)
- RULE: Premium sensitivity check: bodies must stay in the lower half of the suspension block/SIBI; no body closing above its CE means price likely trades back to 9:30 open in "heavy" manner and then lower; keep top half un-tested (@08:52, @15:08, @16:41)
- RULE: Partial rule: every time price prints a new low (clearing sellside) and no partial yet, take one; "running down equity" = build realized equity along the leg instead of requiring terminus (@10:22, @10:54)
- RULE: Stop placement: after the move down, stop above the new week opening gap high / above the last high (@09:52)
- MMXM: Price ran buyside first (premium), then reversal into the premium gap CE -> sellside / NWOG high; prior Asia entry used Friday's FPFVG as the entry zone (long ~29,595.25, max heat ~20 handles on 3 lots) and took out highs ~00:46 sell-off (@12:01, @13:03)
- CTX: Post-holiday: market participants avoid moving price; light size, observe reaction (@07:56)
- EX: 20260908 NQ 1m: gap down from Fri 28-Aug FPFVG zone after Labor Day, suspension block above ~29,1xx-29,2xx; half-gap fill within minutes (@06:26, @16:41)
- skip: 4-minute chat with son, paper-trading disclosure.

### 070 | 20260930 | NQ December Asian Session Execution (09/29 evening, long)
tags: IFVG (P2), opening range gap, FPFVG, volume imbalance (P4), buyside liquidity, partials, "event horizon", Asia session (T), defensive PD array framing
- RULE: Long entry in Asia (ETH): buy at a bullish IFVG anchored to the optimum (octant/CE) of Tuesday's RTH opening range gap; target = nearest easy buyside pool (equal highs ~30,709), then next pool ~30,725, then the low/CE of Monday's RTH opening range gap and today's 09:30 open as higher draws (@00:08, @07:32, @09:32)
- RULE: Volume imbalance rule: ideal that the imbalance beneath stays open; if price drops into it, it must react immediately; bodies stay in or above it (@03:21, @04:09)
- RULE: Scale-in ladder: add 3 contracts when price retests the inversion pivot/IFVG low; risk 525 USD on ~12 contracts; stop below the second (gap) candle of the FVG, ideally under the gap candle low (@04:45, @11:09, @12:43)
- RULE: "Double tap" exits: half of position at the near target (body shot), runner for the far target (head shot); staggered exits fund the trade (@05:16, @15:46)
- RULE: Event horizon exit: midpoint between two liquidity pools; take 5 of 9 contracts just shy of it, then 6 off at the next level, leave 3-4 as runner; roll stop to remove all risk once first partial and a small run are done (@15:16, @19:43, @26:34)
- RULE: Defensive framing: three PD arrays that keep the long valid = (1) midpoint (CE) of the last wick, (2) Monday RTH opening-range-gap low, (3) lower part of the daily BISI/SIBI box; a body below them invalidates and stops are placed just under (@24:01, @24:32, @30:49)
- RULE: After sweeping a liquidity pool, a pullback should not retest the old pool (support/resistance traders expect it); not retesting it = stronger (@21:59)
- MMXM: Asia accumulation-type trade: slow session, simple low-risk 'bread and butter' trade into obvious liquidity; no distribution phase mapping (@07:32, @08:02)
- CTX: Asia is slow unless event-driven; trade only easy pools; RTH gap levels (Monday/Tuesday) are still draws overnight (@07:32, @08:32)
- EX: 20260929 NQ Dec 1m ~Asia: long IFVG entry, partials at ~30,709 pool, adds on retests, stopped on runner after ~30,742 test, net ~+1,000 locked then stop-out (@17:34, @31:24)
- skip: Video-mechanics, replies to critics.

## Batch summary
- Top mechanical rules:
  1. Pyramid longs only at/below 50% of the (re-measured) range to terminus; shorts only at/above it; no adds past EQ (062@22:08).
  2. IFVG confirmed only by a candle close through the gap (CE-based); wick-only violations do not invert; after close, bodies must stay outside its far half (062@17:30, 065@44:46, 066@06:52).
  3. Wick grading: in a bullish setup bodies stay in the upper half of the reference wick, bearish setup bodies stay in the lower half; first close through wick CE = warning, stop moves behind it (062@27:17, 064@57:43).
  4. Level confluence for targets: daily BISI/SIBI octant levels (0.125, 0.25, 0.5...) aligning with RTH opening range gap octants/CE = primary draw (065@56:03, 064@46:11).
  5. RTH opening gap: CE traded by ~10:00 about 70% of the time; 10:30 dealing-range onset speeds up delivery (064@96:20, 065@60:54).
  6. Scale-out scheme: partial at each new low/high pool, stop to cost after first partial, trail below previous candle low or pullback low; "event horizon" = midpoint between two pools (064@68:37, 068@10:22, 070@15:16).
  7. NFP week: Thursday/Friday off-limits for beginners, trade only after the first hour, expect manipulation; Mon-Wed until 11:00 OK (064@14:14, 067@30:31).
  8. Macro: xx:50-xx:10 window gives timing not direction; if no expansion within the macro, expect it at the next hour macro (064@64:19, 062@52:05).
  9. NWOG/NDOG lows/highs as entry zones: sell NWOG low after news spike; stop beyond NWOG high (066@00:02, 067@12:32).
  10. Seek-and-destroy day = both sides raided once before the real run; trade with stop beyond the second raid only (062@17:00, 063@11:20).
- Definition changes vs DRAFT:
  * Gap is measured with RTH settle (16:14/16:15 prior) to 09:30 open; RTH opening range gap CE/octants are a key-level family not in DRAFT (064@42:03).
  * "BISI/SIBI" daily box (candle close to candle low incl. volume imbalance); suspension block = volume imbalance at both ends (062@03:07).
  * Octant levels (1/8 steps) next to CE and quadrants for PD grading.
  * IFVG validated by CLOSE through CE-based gap; CISD described as "series of consecutive down-close candles = order block" (062@49:49, 062@96:20).
  * Monthly H/L/C marked, monthly open ignored (064@15:58).
- New concepts not in key-levels.md: RTH opening range gap (settle->09:30 open) + octants; daily BISI/SIBI box; suspension block; first presented FVG (FPFVG) of 09:30; wick halves/CE; event horizon (midpoint between two levels); double tap/headshot exit; running down equity; pyramiding-at-EQ rule; 1-hour dealing range at 10:30; seek-and-destroy profile; MM sell model stage names (SMR, low-risk sell, 1st stage distribution, 2nd stage redistribution); holiday/NFP engagement rules; Jackson Hole week.
- Open questions: exact timing of settle (16:14 vs 16:15) and candle for RTH gap; how wick CE is codified (high-low or body-high); definition of first presented FVG (first FVG after 09:30 on which TF); whether octant 0.125 is measured from high or low of the box; 070 spoken "Dec contract" prices differ (30,7xx) from earlier 29,xxx (contract roll); 067 first 4 min absent; file 069 not in batch.
