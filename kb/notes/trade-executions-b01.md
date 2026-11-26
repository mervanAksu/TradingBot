# trade-executions-b01 notes (map)

### 009 | 20231207 | NQ Employment Number Live Execution (1m, 8:30 news)
tags: inversion FVG (P2), breaker (P7), volume imbalance (P4), order block (P6), Judas swing / AMD (T2), partials, standard-deviation projections (T3-like), news 8:30
- RULE: Partials: scale out one contract each time price makes a new short-term high beyond entry while long (each new high = new equity high); do this by default while learning; leave a small runner (@07:21, @15:31, @38:08)
- RULE: Profit limits are placed ~3 ticks inside the target level to allow for spread, accepting that a precise target may be missed by a tick (@13:59, @14:30)
- RULE: Stop management: after entry, stop sits below the 50% of the down-close candle (OB) that supported the move; when a big up-candle breaks higher, roll the stop to just below that candle's midpoint (@17:32, @18:03)
- DEF: Inversion FVG: an FVG that is violated and then treated as the opposite-side level - price should trade back into it, react, and leave the area between the reacting candle high and the IFVG open as a breakaway gap (no retrace into it) (@02:37, @06:20)
- DEF: Projection method "bodies": measure the swing from the highest body (open/close) to the lowest body (open/close) of the whole run, not wicks; project -1, -1.5, -2, -2.5, -3 standard deviations; wicks are only for the extreme case (@11:28, @39:10, @44:44)
- DEF: Sensitive candle for a breaker/OB entry: the last up-close (or down-close) candle; price must trade about one tick through its close to fill (spread), so a body "touch plus a little" is valid (@30:29)
- MMXM: Sell-side liquidity burned at 8:30 (low run), then a breaker formed; this is the Judas swing (fake move) -> reversal long into premium (@12:28, @29:59, @39:10)
- CTX: News days: ICT treats Wed/Thu of NFP week as imprecise (low confidence); a profitable Monday usually ends his week (@02:07, @09:23)
- EX: 2023-12-07 NQ 1m: long after 8:30 sell-side run into breaker + IFVG; targets hit at 1.5 SD, a 15,890.25 high (50% to 94% area of projection) and 2.5 SD; stopped on runner (@12:28, @22:45)
- skip: roughly 60% rant (copycats, paid mentorships, market-replay claims, personal asides).

### 010 | 20231208 | December 2023 NFP Live Execution (ES, 4H context, 15m/5m)
tags: FVG (P1), consequent encroachment (CE), 4H FVG discount, Judas swing (T2), buy-side liquidity (L4), order block mean threshold, partials, NFP
- RULE: Long entry = inside a 4H FVG while price is in the discount half of the range from the 4H low to the high; stop placed below that zone, wider than normal on NFP; 10 contracts at entry (@00:30, @01:01)
- RULE: Strength test on 5m: require a candle close above the CE (midpoint) of the prior wick/up-candle; if no second close above within a couple of candles, bank 3 of 10 contracts ("fund the position") (@13:54, @23:12, @24:14)
- RULE: Partial plan (5m): 1 off at first reaction; 3 off when a second close fails; 1 manually above the old high (buy-stops / relative equal highs); 3 more via limit above a target level, then roll stop to just under the CE of the key wick (@17:59, @26:15, @73:33, @74:04)
- RULE: After partials fund the trade, move stop to break-even + commissions + a little; stop stays below the 4H FVG high / behind the bodies (@10:14, @39:35)
- DEF: FVG explained by "efficient vs inefficient delivery": one-pass up-move leaves a zone between candle-1 high and candle-3 low that price should re-offer; quadrants = 25/50/75% levels of the gap, CE = 50% (@02:34, @06:40, @10:46)
- DEF: Invalidation uses three PD arrays: the CE of the wick, the FVG low, and the mean threshold (50%) of the down-close OB; a trade into the OB body = cancel/exit (@83:22, @84:23)
- DEF: Strong market skips the discount array: if price rallies without retracing to the discount OB/FVG, that is read as more bullish, not as failure (@15:25, @16:57)
- MMXM: Pre-8:30 raid up (did not take buy-side highs = fake resistance), drop into 4H FVG at 8:30 = Judas swing; reversal target = buy-side liquidity above old highs / relative equal highs; expects 9:30 open liquidity rush to run it (@02:04, @07:41, @53:40)
- CTX: NFP initial move is fake (like FOMC); NFP first hour is manipulated; ICT avoids pyramiding on it; minimum objective 5 handles for a scalp (@07:41, @08:42, @35:24)
- CTX: Timeframe is irrelevant to the delivery logic (same price action on 5m, 1m, 1s) (@23:43)
- EX: 2023-12-08 ES 5m: long in 4H FVG, target 4593.5 (high touched 1 tick short, 4593.25-ish), stop rolled to 4557.7, final fills at limits (@85:57, @88:05)
- skip: ~70% asides (dogs, mindset on partials, "never right", anti-DOM/level 2/Goldbach rants).

### 020 | 20231229 | NQ Live Execution - last trading day of 2023 (1m, demo account)
tags: inversion FVG (P2), volume imbalance (P4), CE, buy-side/sell-side liquidity, relative equal highs (L4), Judas swing, time-of-day (10:30), partials, high-probability definition
- RULE: Short entry zone = price trading into a bearish inversion FVG (drawn orange) and its CE; wanted behaviour is rejection at/near the top of the IFVG, small overshoot of the zone ("Mohawk") tolerated, stop kept above the day's initial high (@04:09, @05:40, @09:47, @13:50)
- RULE: Scaling: started ~12-14 contracts on a 100k demo with stop ~2% of account; add on each retest of the IFVG/volume imbalance; stop rolls to cost-cover after first partial at the initial low (26 handles on 3 lots) (@09:47, @21:02, @35:59, @36:31)
- RULE: Partials: 3 off at first low; 6 off below the next low; 1 more below the next; leave 1 contract with stop above the gap (@21:34, @38:03, @47:24)
- DEF: Immediate rebalance = price tags a volume imbalance on the very next candle after it forms (candle high touches the prior gap edge) (@03:07, @03:37)
- DEF: Purged buy-side pools should be extended to the right: the algorithm keeps re-referring to the same high (it does not know order size) and re-sweeps it repeatedly until the time window that allows the real move (@28:12, @30:49)
- DEF: "Smooth" equal highs get "made jagged" when retail builds a stop cluster above; rallies inside this consolidated premium zone are suspect (distribution) (@16:23, @16:55)
- DEF: High-probability trade only if it can be framed one-sided: one liquidity/inefficiency draw and no PD array giving a credible opposite case (@66:32)
- MMXM: Buy-side stacked highs cleared early (Judas up) -> next draw is sell-side below (17,100s, 17,000 round level); distribution phase: smart money sells every rally while retail buys oversold/bull-flag setups (@01:33, @02:35, @18:59)
- CTX: Last day of month/year behaves less rule-bound, wider stops; market had rallied one-way all December so ICT expects profit-taking/lower prices in the last 3 hours; target sell-side below 17,100 -> 17,000 -> 16,800s (@13:50, @39:31, @60:18)
- CTX: 10:30 = 1 hour after the 9:30 open; consolidation ("time distortion") ends there and price starts to deliver the real directional move (@47:55, @48:25)
- EX: 2023-12-29 NQ 1m: short from IFVG near 17,170s; 3 lots off at initial low then scaled down to 17,000 round-number target; "17,000" called earlier that week (@01:33, @51:31)
- skip: ~75% rants (piracy, regulators, Robbins Cup challenge, autobiographical).

### 023 | 20240110 | Funded-account / trade-copier arithmetic (ES 1m demo)
tags: risk model, buy-side liquidity (L4), HTF-to-LTF annotation
- RULE: Risk sizing illustration: 100 contracts across ten 100k accounts = 10 per account, ~750 USD risk per account (<1%, ~0.75%) per trade; compounding small fixed-fractional risk is the stated route to scale (@01:33, @02:36)
- RULE: Draw logic on 1m: first draw = minor buy-side pool above a small FVG/OB (sell-side imbalance in premium = partial area); next draw = 15m relative equal highs (@03:07, @03:37)
- DEF: Chart-annotation habit: tag LTF levels with their source TF (e.g. "REH 15m") so they remain interpretable (@05:07, @05:40)
- EX: 2024-01-10 ES 1m: long into 15m REH buy-side; a quick "lucky" FVG entry noted as a Silver-Bullet-type trade (@06:41)
- skip: Mostly motivational / Robbins Cup / prop-firm commentary; only the sizing arithmetic is codable.

### 025 | 20240117 | Final Hour MOC Macro (NQ/ES 1m)
tags: macro (T5), MOC, consequent encroachment, swing low, order block, time window
- RULE: Entry: buy when price trades down to ~50% (CE) of a swing-low wick (in a bullish PM run), stop just below that CE; add 10 more at the same level; target = run through the prior high (@00:00, @00:32, @04:21)
- RULE: Break-even once price clears roughly +10 points; take 10 off above the next level (@09:45)
- DEF: MOC (market-on-close) algorithmic window: the hot spool period is roughly 15:50-15:57 NY; after ~15:57 expect a few minutes of retracement away from the run (@01:36, @02:07)
- MMXM: If the day sold off pre-market then drifted higher all day, shorts are trapped and the close ramps; no pullback needed (@08:37)
- CTX: PM session is usually lethargic early in the year (Jan) and in summer; clean runs are in the AM session; he waits to ~2nd week of Feb to trade a year's new-sentiment (@05:31, @07:02)
- EX: 2024-01-17 NQ 1m final hour: late entry at CE of a swing-low wick, targets above the high, last-minute order block rejection in the final minutes (@10:17, @10:47)

### 028 | 20240125 | Algorithmic High Frequency Trading (NQ 5s)
tags: macro (T5), inversion FVG (P2), relative equal highs (L4), volume imbalance (P4), scalp
- RULE: Every ~15 minutes there is a "scout" opportunity: on a 5-second chart enter at an inversion FVG with a very tight stop, add 5 more at a minor buy-side pool, target the relative equal highs and a spike above them (@00:00, @00:31, @01:03)
- DEF: Macro reference here: the 10:50-11:10 window; a volume imbalance/gap formed inside it is the key that starts the run (@00:31)
- MMXM: Algorithm reprices to equal highs and overshoots them slightly (stop-run) before reversing (@00:31)
- skip: 195 words, one micro trade; risk/costs covered by the first add.

### 029 | 20240125 | Algorithmic HFT - Opposite Direction (NQ 5s)
tags: order block mean threshold (P6), bearish FVG reclaim, scalp
- RULE: Short at a bearish order block on the 5s chart; extensions target "good enough" objective; risk 150 to make ~1500 (1:10); add when a bearish FVG is reclaimed from below / low breaks (@00:38, @01:08, @01:42)
- RULE: Take 5 contracts off on the first broken low once costs are recovered; leave the rest to run, ideally leaving a breakaway gap open (@02:14, @02:44)
- DEF: Mean threshold of the OB is the practical stop/limit reference; a reclaimed bearish FVG (price closes back below it) is a continuation entry (@00:38, @01:42)
- skip: 225 words, one trade; mirrors 028 on the sell side.

### 040 | 20240506 | Micro-Scalping Without Bias (NQ 15s)
tags: volume imbalance (P4), daily FVG, order block, inversion level, short-term liquidity, partials
- RULE: Micro-scalp without HTF bias: on a 15s chart use only the available liquidity: enter beneath a down-close candle (OB) inside a small FVG when price is at a premium to the previous settlement; stop sits below the OB; add inside nearby volume imbalances up to a max-contract cap (@00:30, @01:03, @02:06)
- RULE: Targets are the nearest short-term buy-side pools; once the target is reached limit orders are placed just below the bodies (not at the extreme) because the HTF level may not be touched again (@05:45, @03:44)
- RULE: Partial: 5 contracts off in the inefficiency between two candles; cost per contract roughly 10 USD round-trip so first partial covers fees; remaining position runs for a second attempt at the daily FVG (@07:17, @07:47)
- DEF: Volume imbalances are flexible PD arrays: price may trade through and back across them without cancelling the narrative; do not expect a sharp reversal on first touch (@06:47)
- DEF: A prior order block becomes an inversion level once violated (OB -> inversion) (@04:44)
- MMXM: Sequence: long into buy-side, then reverse short to take the sell-side liquidity under it (@10:53)
- CTX: Pure "no-bias" scalping on tiny ranges; alternative for scalpers: no partial, exit at first logical liquidity level (@09:21)
- skip: roughly 1/3 chatter about prop firms.

### 043 | 20240513 | NQ Premarket Short (15m frame, 1m execution)
tags: FVG premium (P1), inversion FVG (P2), volume imbalance (P4), CE, sell-side liquidity, premium/discount (S3), partials
- RULE: Short plan on 15m: limit order in a premium 15m FVG with multiple failed attempts to break the 18,320s level (jagged highs = likely fill missed -> fallback entry); stop just above CE of the wick (@00:01, @00:31, @01:03)
- RULE: Fallback entry: sell just above the CE of the inversion FVG (orange) / above the last down-close candle; second fill added at the IFVG low; stop then moved to the volume imbalance edge left of the IFVG (@03:47, @04:17, @04:50)
- RULE: First partial at the minor sell-side (the 07:30-07:40 swing low), then stop rolled to cost cover (10 USD/contract fees) (@06:57, @08:30)
- RULE: Next partials one contract at a time at the lower edges of the old 15m imbalance (18,3x7 / 18,304.75); keep 3 for the far lower target (@09:36)
- DEF: IFVG trade shows "immediate responsiveness" when an up-close candle trades into the IFVG bottom and price drops at once; the area between becomes a breakaway gap (@05:21)
- DEF: Smooth (clean equal) lows/highs are read as draws on liquidity (@02:46)
- CTX: Premarket, no news; price in premium so he wants a pullback to a premium array; discount array expected later (@03:17)
- EX: 2024-05-13 NQ 15m/1m: short from 15m FVG/IFVG, partial at 07:30-07:40 low, 7 more lots to the lower 15m imbalance edge ~18,304 (@07:58, @09:36)

### 046 | 20240610 | NQ Lunch Macro (15s)
tags: volume imbalance (P4), inversion FVG (P2), CE, macro (T5), sell-side liquidity (L4)
- RULE: Short: enter at the CE of a sell-side volume imbalance (or its open) to ensure a fill, 6 contracts then add 4 on the next candle; stop just above the CE of the imbalance, tightened to just above the open of the candle that failed at the IFVG (@00:32, @01:07, @05:16)
- RULE: Confirmation on 5m: need price to erode below the CE of the discount wick and slice through the previous low with no respect (@03:12, @03:42)
- RULE: First partial (6 contracts) at a defined price "below 62" - a price level past the minor low, set in advance with a buy limit to cover a short (@09:24, @10:34)
- DEF: Volume imbalances are the weakest/most flexible PD arrays; occasionally "dead locked" turning points and valid as entry, partial or target depending on the narrative (@06:18, @06:49)
- DEF: Not needed: the full wick-to-wick inefficiency repriced; CE of the wick is enough (@08:22)
- MMXM: Pump all day -> liquidity under the low; reach up to CE of buy-side imbalance, reject, run below the prior low (@06:49)
- CTX: Lunch macro (title) = the late-morning/lunch hour algorithmic window; the clip does not state the window times
- EX: 2024-06-10 NQ 15s: short from CE of imbalance, targets the sell-side low, all marked in advance (@09:24, @11:05)

### 047 | 20240624 | NQ Turtle Soup Short (1m)
tags: turtle soup (L7), rejection block (P9), inversion FVG (P2), volume imbalance (P4), CE/quadrants, sell-side draw, 08:30 low, partials
- RULE: Bias plan: stay below the midpoint of the sell-side imbalance, short with stop at the high of the day; first draw = the low printed just after 08:00 (the 8:30 news low), intermediate swing target ~xx,760, final ~xx,926 (@00:33, @01:39, @09:55)
- RULE: Rejection block = last up-close (big green) candle's close/wick before the turn; add shorts when price stabs into it again; mark CE of the wick three candles back as an add level (@02:10, @04:13, @04:44)
- RULE: Inversion FVG built from a buy-side imbalance: break into quadrants (upper quadrant, CE, lower quadrant, low); wanted: price reaches at most the upper quadrant and never closes above it; after the break price should not retest above the upper quadrant (@06:18, @07:22, @08:23)
- RULE: Entry confirmation = heaviness: next candle(s) stay inside the last down-close candle's body (not above its open, not returning to its wick), then big down-close expansion; exit limit set below the target low (15 contracts below the low) (@12:00, @12:30, @10:58)
- RULE: Stop to cover costs after the first leg; ICT held (no early partial) because the target was a longer-term draw (@09:24)
- DEF: Turtle Soup: the earlier push above highs that is rejected and reverses = classic flirtation with the high; he promises a separate lecture (@14:02)
- DEF: Volume imbalance is the least rigid PD array: price may trade through it and return; used as a target or a stop reference (@03:12)
- MMXM: Sequence: sell-side draw below 8:30 low; buy-side taken in turtle-soup spike -> reversal -> gravitate to the minor sell-side then the larger target (@01:03, @14:02)
- EX: 2024-06-24 NQ 1m premarket/AM: short from rejection block + IFVG upper quadrant, 15 lots exit under the 8:30 low, then more toward the ~xx,760 level (@15:47)
- skip: first minute personal health talk; comment/Instagram scammer asides.

### 051 | 20240827 | Premarket NQ - OB to Discount / NDOG (1m)
tags: order block (P6), rejection block (P9), CE, CISD (S2), NDOG (P5), partials
- RULE: Short at a bearish order block; stop above the rejection block; first partial at a minor sell-side; stop moved above CE of the key wick and later above the open of the sequence (@00:02, @01:37)
- RULE: Pyramid: add 5 more contracts only if price retraces to the open of the candle (series) that delivered the drop - the open is the CISD level; then stop rolls to commissions cost (@02:10, @02:41, @04:18)
- DEF: CISD (state-of-delivery change) = return to the opening price of the up-candle series; used as a re-entry/pyramid level (@02:10, @03:12)
- DEF: Premium array: price traded away from it on the downside becomes resistance on retest (@05:16 in 047 analog; here @00:33 "deep premium inside the OB body")
- CTX: "No bear flags or trendline breaks" - the model sells into strength (up moves) at algorithmic PD arrays and buys weakness (@03:43)
- skip: 401 words; title mentions NDOG but the transcript does not explain it.

### 057 | 20260806 | Price Action Chronicles - The Science of Anticipation (NQ 1m, daily context)
tags: inversion FVG (P2, daily), suspension block, volume imbalance (P4), rejection block (P9), CE, relative equal highs (L4), partials, NFP week, 07:00-09:00 window
- RULE: Setup: price falls quickly into a daily inversion FVG during 07:00-09:00 NY; go long at the CE of a 1m gap/suspension block right after the first reaction; stop starts at the CE of the daily wick (top of IFVG) and below (@03:41, @04:46, @06:53)
- RULE: Long confirmation ladder: want price to lay bodies above the midpoint of the vertical decline's inefficiency (high of the gap to the low of the volume imbalance); a close above halfway -> roll stop to just below the lows of that decline (@07:56, @09:31)
- RULE: Partial plan: sell 1 contract with a limit just above the first level (pop); roll stop to cover commissions; then take 2 of 3 off at the old high; once the stop is raised into profit never lower it again (@08:31, @12:06, @39:09, @43:16)
- RULE: If-then framework for the retest: price may return to the upper half of the buy-side imbalance; it must stay reactive (the CE of the wick and old high) - three PD arrays stacked: old high, upper portion of the imbalance, CE of wick; below the lowest = the idea is wrong (@34:04, @34:34)
- DEF: Suspension block = a volume imbalance at the high and another at the low of the same inefficiency (bodies of two candles do not touch/overlap at each end of the displacement); the CE of the gap in between is an entry (@25:56, @26:26)
- DEF: Rejection block = highest up-close (body top) of a swing high; price reacting to it after a failed run is the sign to take a partial (@46:25)
- DEF: A small portion of a gap staying open (upper half unfilled) after a retest = unwillingness to trade lower = strongest buy (@35:05)
- DEF: Volume imbalance tested with exact price match (open 29,390.75 = candle low) - treat as algorithmic precision; imbalance colours may sit outside the IFVG box (@29:27, @25:56)
- CTX: NFP week: cleanest price action is Mon-Wed up to ~11:00 for beginners; 07:00-09:00 NY premarket window for daily-PD-array reactions (@03:11, @47:59)
- CTX: Last of the sellers: after a big drop, a quick bounce from a daily IFVG shows shorts caught; "relative equal highs" above are next targets (@10:32, @30:29)
- EX: 2026-08-06 NQ 1m 07:00-09:00: long at CE of suspension-block gap after drop into daily IFVG; target RE highs ~30,6xx-30,74x; 2 of 3 off, stop under CE of the wick (@04:46, @39:09)
- skip: ~40% on fundamentals (NFP data unreliable; supply/demand only valid for commodities), mindset.

### 058 | 20260807 | NFP Case Study with NQ (1m/5m, 07:00-09:00 range)
tags: pre-8:30 dealing range, macro 08:50-09:10 (T5), octants/quadrants of range, BISI/SIBI (P1), balanced price range (P3), standard deviation projection (T3), Judas-style two-stage NFP, mohawk tolerance
- RULE: Before an 08:30 release define the dealing range = highest high to lowest low from 07:00 to 08:30 NY; do this before the news (@01:32, @02:03, @02:33)
- RULE: Qualify each FVG by where it sits in that range: bullish FVG just under the range CE/lower octant (0.625 etc.) = institutional order flow entry drill; FVG in the upper quadrant/octant selling off = bearish entry (@11:12, @11:44, @12:14)
- RULE: Mohawk tolerance: price may poke slightly outside the imbalance zone; what counts is that bodies do not close beyond its far edge (@03:04, @03:34)
- RULE: Project SD from the 07:00-08:30 range (high/low, check tick-level extremes); the move to the macro window 08:50 reached -2.05 SD, a likely reversal zone; macro = 08:50-09:10 (@08:37, @10:11, @05:05)
- RULE: Partial rule used: take 1 of 3 contracts only above halfway between entry and the draw; never below the midpoint (@07:37, @08:07)
- DEF: Balanced price range here = a BISI and a SIBI sharing one range; use highest high and lowest low of the two as zone (@06:05)
- DEF: A bullish suspension block that is traded through (close below) becomes a bearish inversion FVG; failure to touch its CE = sell (@05:35, @06:05)
- MMXM: NFP is a two-stage delivery like FOMC: first run up (traps longs, stops below), then reversal inside range in the macro window; the key level 29,780 was pre-flagged as a weekly/daily PD reference (@00:30, @10:42)
- CTX: Pre-news consolidation the day before is typical; do not trade Thu/Fri of NFP week if inexperienced (@00:00, @01:01)
- EX: 2026-08-07 NQ: long (3 demo contracts) from ~29,6xx 8:29 sell-side clear, to 29,780; 1 off above halfway; reversal at 8:50-9:10 macro, then sell-side swept lower (@07:05, @08:07)

### 059 | 20260810 | Navigating High Resistance Liquidity Run Conditions (NQ 1m, Monday premarket)
tags: inversion FVG (P2) qualification, midnight opening price (L8), HRLR (L6), relative equal highs (L4), CE of wick, partials, anticipation
- RULE: Long entry: 4 contracts into a bullish inversion FVG, stop just under the low of the entry candle (+/- 1-2 ticks); add 2 on the retest of the IFVG high, add more in its deep end; average = about the IFVG high; then stop to the IFVG low minus a tick (@00:03, @00:33, @02:36)
- RULE: "No bodies buried" rule: bodies must not close below the CE of the supporting wick(s) (two such wicks tracked); if one does, the next candle must close back above - otherwise reduce (@01:03, @03:40, @05:18)
- RULE: Partial #1: 5 of 7 just under the midnight open (29,878.25) once price closes above the pivot; roll stop to cost cover; remaining runner uses a stop at the wick low (@07:20, @07:52, @20:07)
- RULE: Partial #2 variant: resting stop-sell on 2 of 7 below the wick low = "partial on a retracement" so a stop-out still pays; extra benefit: second close below gives info the move will fail (@22:42, @25:46)
- RULE: Next target set: minor buy-side at ~29,920 (2 off just above), then overnight / Monday London relative equal highs (@15:32, @16:05, @07:20)
- DEF: IFVG qualification: an FVG counts as an inversion only after it has been (1) closed through and (2) retested with a second close beyond it; two qualifications before using it for entries (@11:25, @11:55, @12:29)
- DEF: Midnight opening price (New York 00:00) acts as a magnet and as initial resistance; it is a draw / session bias anchor, not necessarily daily bias (@10:55)
- DEF: Leaving a small slice of a bullish FVG open (price does not fill it fully) is the strongest signature of continued strength; same for volume imbalances: leave a portion open or do not trade into it (breakaway/measuring gap) (@09:54, @14:00)
- DEF: Mean "PD array number two" = the CE of the wick; last defence = the swing low under it (@19:06)
- MMXM: Open 9:30 near IFVG high; sell stops below a low swept (smart money buys them), reclaims -> bullish; heavy news Wed/Thu (CPI/PPI) made price messy; "high-resistance" here = midnight open + several unfilled gaps above (@11:25, @15:32)
- CTX: He insists on anticipating (not reacting): predicts targets and tethers entries to the order-flow direction (@19:06)
- EX: 2026-08-10 NQ 1m: long at IFVG formed 7:29, 7 contracts, 5 off at 29,87x midnight open; extra 2 on stop; stopped out runner (@07:52, @25:16)

### 060 | 20260810 | How to Frame Sessions in High-Resistance Liquidity Run Conditions (NQ review)
tags: HRLR (L6), dealing range (S7), octants/quadrants, premarket first-30-min range, final-hour RTH range, midnight open (L8), NWOG (P5), macro 07:50-08:10, session highs/lows (L3), IFVG qualification
- RULE: Frame Monday from Friday: take the final regular-trading-hour range (about 15:00-16:00 NY; lowest low to highest high) and grade it with a fib: 0.75 lower quadrant etc.; those two extremes are liquidity references for the next session (@00:31, @01:33)
- RULE: Premarket range = first 30 minutes after 07:00 (07:00-07:30) high/low; grade it with quadrant/octant levels (0.375, 0.625, 0.75) and carry the levels forward through the premarket/first hour; a FVG is valid if it sits on those graded levels (@06:08, @06:46, @07:19, @07:49)
- RULE: Entry logic: short when price rises into the CE/mid of a wick or into a bullish FVG that will invert (price below it); partial below relative equal lows; stop trails behind; midnight open + octant 0.375 as the short level (@13:29, @15:02)
- DEF: Opening-range definition: RTH opening range = first 30 minutes (09:30-10:00) - not 5 or 15 minutes - and the same 30 minutes after 07:00 for the premarket (@14:30, @15:02)
- DEF: Why a given low is a target: it is a session low/high (final RTH hour, London lunch range, premarket), daily or weekly high/low, or a 3-day extreme (@09:54)
- DEF: Macro 07:50-08:10 is the window in which price reached the midnight open + IFVG before selling off (@09:22)
- CTX: Week with CPI (Wed) and PPI (Thu): Mon/Tue likely suppressed (HRLR) in RTH; ETH (London, premarket) tends to trend, RTH tends to range; either AM or PM gets one trending session (@02:03, @03:05, @05:08)
- CTX: Midnight opening price must be on the chart; price gravitates to it before the session low is made (@09:22)
- EX: 2026-08-10 NQ 1m: premarket low into NWOG sell-side/green box, rally to midnight open 29,878.25 and IFVG at 08:10 macro, sell-off to Friday's final-hour low; later short at wick mid with partial under equal lows (@07:49, @13:29)
- skip: ~20% asides about students asking questions.

### 061 | 20260827 | NQ Seek & Destroy Profile - Jackson Hole Day 1 (1m)
tags: seek and destroy profile (T4), macro 09:50-10:10 (T5), inversion FVG (P2), SIBI/BISI, CE of wick, institutional order flow entry drill, intraday high buy-side (L3), partials
- RULE: Entry: during the middle of the 09:50-10:10 macro, buy after the intraday low is taken (candle before price returns into a SIBI that should invert); stop one tick under the wick; target = intraday high (buy-stops) ~1 tick below it (@00:01, @01:04, @05:45)
- RULE: Three-PD-array support for the long: low of the IFVG, CE of the IFVG, CE of the wick (plus a down-close OB) - stop under the lowest; bring stop to positive once price closes above the IFVG high (@03:43, @04:13, @07:25)
- RULE: Bodies stay in the upper half of the wick / FVG ("discount array" = upper half of the wick); a close below the CE -> wait for the upper-half defence; a Mohawk below the IFVG is tolerated (@06:52, @09:27, @11:29)
- RULE: Scale: 6 contracts; limit 5 at the intraday high buy side, leaving 1; stop under CE of the BISI-SIBI gap (@19:30, @20:32)
- DEF: Seek and destroy = a day of alternating up and down sweeps of both sides with a quick final move to the other side; usually day 1 of Jackson Hole; ICT does not recommend executing it (@16:20, @26:15)
- DEF: Institutional order flow entry drill = after a BISI forms, price returns into it and pokes only slightly below the high/upper part while leaving the rest of the gap unfilled; unfilled remainder = continuation (@15:49, @31:00)
- DEF: "Cork": a small sloppy block of overlapping candles just under the target buy-side, not a bull flag; resolves up (slow bleed, then last 2-3 candles deliver); read as a fake high (@20:01, @23:05, @27:16)
- MMXM: Why bullish: price failed to trade down to the prior day (4 Aug 2026) BISI/SIBI volume-imbalance high; the day-1 intraday low sweep + macro hit = reversal to take intraday-high buy stops (@22:05)
- CTX: Grade the first range of the morning on seek-and-destroy days; the move is slow and tedious; keep stop where it is after raising it; expect a stop-out of the remaining after most is paid (@25:13, @31:59)
- EX: 2026-08-27 NQ 1m: long ~29,44x under 29,443 low, mid macro 09:50-10:10; 5 of 6 off near 29,640 high; remaining stopped (@01:04, @19:30, @33:31)
- skip: political asides and mindset anecdotes.

## Batch summary
- Top mechanical rules:
  1. Partial ladder tied to levels: first 1-3 contracts at the first minor liquidity/new high, roll stop to cost cover (~10 USD/contract round trip); then bulk at the buy-side/old high; runner behind a stop under the CE of the key wick; never lower a raised stop (009, 010, 057, 059, 061).
  2. Stop placement = beneath the CE (50%) of the supporting wick or the low of the entry candle; "no bodies buried" below the CE; for gaps, the three-array stack (IFVG low, CE, wick CE/OB mean threshold) defines invalidation (010, 059, 061).
  3. IFVG qualification: an FVG counts as inverted only after one close through it and a second close beyond after a retest; price may poke outside by a Mohawk, bodies must not close beyond the far edge (058, 059, 060).
  4. Pre-news range: 07:00-08:30 high/low is the dealing range; project -1 to -2.5 SD of bodies; NFP-type events are two-stage (first run traps, then reversal in the 08:50-09:10 macro) (009, 058).
  5. Premarket 07:00-09:00 and the first 30 minutes (07:00-07:30, 09:30-10:00) are the dealing ranges; grade with 0.375/0.625/0.75 octants and require FVGs to sit on graded levels (060, 058).
  6. Midnight New York open is a magnet/first resistance; take most contracts just under it on a long (059, 060).
  7. Gap strength: leaving part of the BISI/SIBI unfilled after the retest (small poke only) = continuation; fully filled = weaker (059, 061).
  8. Macro windows seen: 07:50-08:10, 08:50-09:10, 09:50-10:10, 10:50-11:10, 15:50-15:57 (MOC) (028, 025, 058, 060, 061).
  9. Entry fills use limit just inside the zone; target limits 3 ticks short of the level for spread (009).
  10. Seek & destroy days: first day of Jackson Hole, CPI/PPI weeks (Mon/Tue suppressed): trade only what is graded, expect HRLR/chop in RTH (060, 061).
- Definition changes vs DRAFT:
  - IFVG (P2): requires retest + second close (059); drawn orange, bearish IFVG = prior bullish gap closed through (020, 043).
  - Volume imbalance (P4) is a body-to-body gap and the weakest/most flexible PD array; used for entries/targets, may be traded through (040, 046, 047).
  - Rejection block (P9): highest up-close (body top) of a swing high, not the wick zone only (057).
  - CISD (S2): return to the open of the series of candles that delivered the move = pyramid/re-entry level (051).
  - NDOG/NWOG usage: NWOG sell-side gap used as a target/low reference (060); midnight open L8 confirmed.
  - Opening range = first 30 minutes (09:30-10:00; also 07:00-07:30 premarket) (060).
  - Premium/discount applied inside a single wick/gap: upper half of the wick or gap = bullish defence zone (057, 061).
  - Liquidity pools purged are extended forward (rewritten as references) (020).
- New concepts not in key-levels.md: suspension block (057); BISI/SIBI shorthand; consequent encroachment (CE) of wicks and gaps; octant/quadrant grading of ranges (058, 060); institutional order flow entry drill (058, 061); Mohawk tolerance; immediate rebalance (020); breakaway/measuring gap (009, 043); cork pattern (061); seek-and-destroy profile (061); MOC macro (025); three-PD-array invalidation; 2-qualification IFVG; final-hour RTH range (060).
- Open questions:
  - What is the exact numerical Mohawk tolerance (ticks)? Never given.
  - Which timeframe defines a "valid" FVG for the IFVG (1m vs 5m vs daily) when stacked? Mixed in lectures.
  - Day/time macro definitions: only some windows explicit (09:50-10:10 etc.); lunch macro (046) times unstated.
  - How to proxy "heaviness"/"willingness" and "gradient levels" (0.375/0.625/0.75) as codable rules; discretionary.
  - Seek-and-destroy detection: no objective trigger given; need a proxy (e.g. two-sided sweeps before 10:00).
  - Prior ICT filename years: 2026 videos use NQ ~29-30k; check data availability for backtest range.
