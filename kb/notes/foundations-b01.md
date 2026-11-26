# foundations-b01 notes (map)

### 003 | 20221025 | Stock Mega-Trades (Month 11)
tags: SMT divergence (L9), quarterly shift, seasonality, higher-low failure
- RULE: Stock-selection filter: take only the buy side; wait for the index trio (Nasdaq comp / S&P cash / Dow) to diverge on a daily chart - one index holds a higher low while the other two print lower lows - then buy only stocks that also held a higher low over that same span (a stock that made a lower low is rejected) (@28:56, @31:00)
- RULE: Extra stock filters: avoid names that have already gapped away from a base (gap likely to be filled), prefer price >= ~20-25, prefer stocks sitting in a consolidation when the divergence prints (@32:18, @35:28)
- DEF: The index SMT is read on the daily TF and recurs only around quarterly shifts (every ~3-4 months, earnings-driven), not intraday (@51:40)
- CTX: Stock seasonality: low early in year, rally into spring, consolidation spring-fall, strongest buy window Sep-Nov into year end; mega-trades are 6-9+ month holds, stock-only (@02:15)
- CTX: Relative-strength funnel: bullish market -> leading sector -> leading industry group -> strongest stock; SMT is the timing trigger (@14:34)
- EX: Mar 27 -> Apr 19 2017: Dow made a lower low, Nasdaq and S&P failed to; FB held a higher low and ran ~140 -> 164 (@28:56, @44:57)
- skip: Mostly IBD/CAN SLIM fundamental screening and stock-by-stock hindsight tour; not applicable to NQ/ES intraday. Only the SMT-as-institutional-footprint idea is reusable (NQ vs ES here, plus YM).

### 004 | 20221026 | Bond Mega-Trades (Month 11)
tags: SMT divergence (L9), seasonality, discount PD array, order block, turtle soup
- RULE: Cross-market SMT recipe (generalises to NQ/ES): compare same-window swing lows across correlated instruments (5y/10y/30y notes); if at least one holds a higher low (or equal low) while another prints a lower low, treat it as accumulation footprint. Zoom to a ~1 month window on 2h bars to scan (@10:53, @11:56, @23:52)
- RULE: Swing-low definition used for SMT: lowest bar with a higher low on each side (3-bar); when no clean low pairs exist, divergence can be counted over a series (low, lower low, lower low) where one market refuses the final lower low (@27:32)
- RULE: Entry after SMT must be at an HTF PD array in discount (bullish OB or FVG in discount of the range after sell-stops were run); entry need not be the best price (@17:40, @19:11, @24:25)
- MMXM: Sequence = seasonal window -> HTF institutional order flow/discount -> SMT on the daily/intraday scan -> entry at discount array -> hold toward premium array / seasonal high (bearish OB at premium capped one run) (@05:47, @38:56)
- MMXM: Failure example: price traded above an old high, then failed as turtle soup, giving only ~5k/contract (2012) (@32:45)
- DEF: "Mega trade" for bonds = move of at least ~10k USD per contract (10 handles); smaller is just a good trade (@42:30)
- CTX: Bond seasonality: weakness early year into a May-June low, rally into Sep-Oct high; Sep-Nov short-term rallies are secondary; seasonality is a bias filter only, not guaranteed (2012, 2013 were duds) (@00:44, @34:46)
- EX: Jun 2008 30y bond: SMT at May-June low, entry ~112.5, ~12k/contract (@15:05)
- EX: Weekly chart 2008: 114 entry sat inside bullish OB after stops below a discount low were swept, then rally ~28k (@17:40, @19:11)
- skip: Year-by-year hindsight tour 2009-2017 (mostly confirms same pattern); little intraday relevance.

### 005 | 20221027 | Long Term Top-Down Analysis (Month 12)
tags: premium/discount (S3), dealing range, PD array matrix, order block (P6), rejection block (P9), SMT, market profile, quarterly shift
- RULE: Top-down checklist order (run at month close, then transpose to weekly -> daily): seasonal tendency -> quarterly shift (3-4 month cycle) -> rates/fundamental driver -> market profile (consolidating? trending? retracing?) -> correlated markets -> market structure/SMT -> PD array matrix -> key levels -> bias (@06:47, @35:30)
- RULE: Framing range = the last 9-18 monthly candles; split it at 50%; list only the PD arrays that actually exist in the discount (below EQ) or premium half (@18:34, @32:26, @50:58)
- RULE: Bias-from-profile logic: if consolidating, expect expansion and look for which side's liquidity (equal highs / equal lows) is taken first; if trending, favour continuation and avoid picking tops/bottoms; if retracing, find the PD array that ends the retracement then trade the trend leg again (@29:21, @30:54)
- RULE: If the 9-18 month trend is unclear/ranging, expect the last 3-4 months' direction to retrace or reverse over the coming 1-2 months (@20:07)
- RULE: Round PD-array levels to the nearest 0/5/10 as "low-hanging" targets: premium levels above price round down, discount levels below price round up (so the level is reached before the true array) (@33:58)
- RULE: Never counter-trade when structure, SMT, seasonal and rate differential all agree, even for scalps (@26:49)
- DEF: Discount-array shopping list on a monthly range = bullish OB (open of lowest down-close candle), rejection block, old-low sell-stop pool; liquidity void/vacuum gap/breaker only when present (@47:24, @48:57)
- DEF: Failed breakout of a range above its equal highs is a stop run; once it returns through the range midpoint, expect a run down through the range low or at least through candle bodies (@45:17)
- DEF: SMT across correlated pairs: AUD held a higher low while DXY made a higher high (inverse correlation) = divergence signalling accumulation (@46:18)
- CTX: Consolidation = start of next move; ask "consolidating?" first, then "trending?", then "retracing?" (@29:21)
- MMXM: Bullish template shown: seasonal buy month + retracement into monthly OB inside discount + consolidation with buy stops above range highs = target the range high, then next rejection block / up-close above (@51:29)
- EX: AUDUSD monthly, June 2017: OB open 73.80 tagged at the June open, 3-month decline into it, then rally through June-July (@47:56, @51:29)
- skip: Interest-rate differential and inflation/deflation detail, personal remarks; not usable for NQ/ES rules.

### 006 | 20200203 | Essentials To ICT Market Structure (Primer 003)
tags: swing points (S6), MSS (S1), OTE (S4), killzones (T1), market profile, measured swing
- RULE: Three-timeframe stack per style: position = M/W/D; swing = D/4h/1h (D premise, 4h manage, 1h entry); short-term = 4h/1h/15m; day trade = 1h/15m/5m (top = bias, middle = management, bottom = entry timing) (@03:48, @05:52, @06:22)
- RULE: Structure break trigger: price reaches HTF key resistance/support, then takes out the most recent short-term swing low (high) on the HTF = market structure shift; afterward only trade retracements in the new direction, entering on pullbacks while lower swings keep being broken (@11:30, @15:37)
- RULE: Swing classification: short-term high = high with lower highs both sides; intermediate high = high with lower short-term highs on both sides; long-term high = intermediate high with lower intermediates both sides; mirror for lows (@28:31, @29:02)
- RULE: Measured-move projection (no fib): copy a completed swing's range from the break/retracement point to project the next leg; the first-leg size is reused after the retracement; exit slightly before projected target (@24:23, @26:28)
- RULE: Broken support becomes resistance on retrace, and the retrace may overshoot the level, so treat levels as zones (@25:25, @27:29)
- RULE: Execution plan: set bias from the top TF, pre-mark the key level, wait for a killzone, take the entry (OTE or other pattern) only when price reaches the level inside the window (@33:08, @35:41)
- DEF: "Bias is both directions every day" - the bias you hold must match your chosen TF/style; no bias guarantees profit (@34:10)
- CTX: Order of analysis: market profile (trend / reversal / consolidation) first, then structure on the three TFs, then killzone timing (@37:42)
- skip: Style/psychology commentary; no chart dates or instruments.

### 007 | 20171209 | The ICT New York Killzone (Primer 006)
tags: killzones (T1), power of 3 (T2), OTE (S4), EQL liquidity, London low/high
- RULE: Early NY killzone window in this lecture = 07:00-09:00 NY (classic form); expected output on dollar-crosses is a 20-30 pip OTE scalp (@00:39, @01:10)
- RULE: Continuation model: daily bias bullish + London formed the low of day and rallied -> expect a retracement down into 07:00-09:00, run sell stops (equal lows / prior low) and take an OTE long; mirror for bearish (@09:55, @13:29)
- RULE: Prefer trades only in the daily-bias direction; reversals against HTF are not systematized here (@11:26)
- DEF: NY session = 07:00 to 14:00 NY (wider than the killzone); economic news inside it can reverse or amplify the move (@07:23)
- MMXM: Fractal PO3 inside the session: open -> a counter move creates the session low -> expansion to session high -> pullback into close (bullish version) (@07:54)
- CTX: NY behaviour is either continuation of London's direction or full daily reversal; London agreeing with daily bias makes the setup "loaded" (@09:25, @14:32)
- EX: USDCAD (bullish day): London low, rally, NY-open retracement sweeping equal lows, then expansion to relative equal highs (@13:29, @14:01)
- EX: EURUSD short day: Asia swing high, London high, NY retracement high then expansion down (@05:53)

### 008 | 20171220 | Weekly Bias - Short Term Trading (Primer 008)
tags: weekly open (L8), power of 3 (T2), Judas swing, weekly profiles (T4), OTE (S4), turtle soup (L7), premium/discount
- RULE: Weekly open = Sunday opening price (first trade of the week), drawn as a horizontal line to Friday close; it is the weekly equilibrium/"fair value" for premium vs discount (@02:20, @09:07)
- RULE: Bullish week (HTF bias up): buy BELOW the weekly open; the weekly low forms between Sunday open and Wednesday 07:00 NY open, highest odds Tuesday London to Wednesday NY open (@00:45, @10:38)
- RULE: Bearish week (mirror): weekly high forms between Sunday open and Wednesday 07:00 NY, highest odds Tue London to Wed NY open; sell ABOVE the weekly open (@26:07)
- RULE: Invalidation: bullish week and price makes a new low after Wednesday NY open (below the low printed by then) = trade is wrong, stand aside, even if price later rallies (@13:13)
- RULE: Wednesday line in the sand: once price trades above (bullish) the weekly open by Wednesday it should not return to it; a return after Wednesday means reversal or a flat week (@19:30, @22:33)
- RULE: Entry via OTE: after the weekly low prints, wait for price to break the short-term high preceding it, then fib from the lowest close/open of the swing low to the top body of the run; buy the 62-79% retracement (@14:15, @15:19)
- RULE: Monday ignored for the weekly extreme (he skips Mondays and watches Monday's range); if Monday is the low and price reclaims the weekly open, distrust it; if taking it, take profit at the open and trail (@18:26, @21:02)
- RULE: Simple version: bullish -> buy ~30 pips below weekly open with 150 pip stop, target 150-300; bearish mirrored at +30 pips above (@24:34, @31:45)
- RULE: Partial profit protocol: take something off every +100 pips; day trader banks ~80%, short-term trader >= half, then stop to breakeven (@32:46, @35:50)
- RULE: Better short entry: sell limit just above Monday's high / equal highs (resting buy stops) before Tuesday London (@37:24)
- MMXM: Weekly PO3: open -> Judas swing against bias (above open for bearish, below for bullish) sweeping orders -> expansion away from open through Friday (@09:37, @28:40)
- DEF: Overbought/oversold = price relative to the weekly open in the direction of HTF bias, not an indicator (@04:59)
- EX: Nov 21-22 2017, 30m: USDCAD bearish week, double-top Monday/Tue highs swept above open then dropped from ~2695 level area through the open (@28:40, @30:42)
- EX: Nov 21-22 2017, 30m: bullish example, low made Tue/Wed, OTE long from swing low to prior short-term high (@15:50)

### 009 | 20171209 | Accumulation - Manipulation - Distribution (Primer 010)
tags: power of 3 (T2), AMD, open price (L8), liquidity (L4), Judas swing
- RULE: PO3 on any bar of any TF using only O/H/L/C: accumulation = consolidation around the open; manipulation = a quick move away from the open on the side opposite the real direction; distribution = the expansion to the extreme where smart money exits (@01:17, @06:32)
- RULE: Bullish bar: manipulation takes price BELOW the open, running sell stops under the old/consolidation low (a break of ~10-20 pips below equal lows shown) - knocks out early longs and recruits breakout shorts; buy at or below the open; close above open (@07:03, @18:54)
- RULE: Bearish bar mirrored: manipulation above the open running buy stops above old highs/double tops; sell at or above the open; close below the open (@12:44, @16:48)
- RULE: Distribution exit targets: bullish = the buy stops above an old/intraday high (about 20 pips above the old high); bearish = sell stops below the old low (about 20 pips under original consolidation) (@10:42, @14:48)
- DEF: Opening price = reference value before the imbalance; range expansion = the open-to-close move (dynamic imbalance). "Equal highs/double tops" are where retail buy stops rest (@05:27, @17:19)
- DEF: Manipulation does two jobs at once: engineers new counterparties (breakout traders on the wrong side) and neutralizes existing positions (stops of the earlier right-side traders) (@08:35, @13:14)
- CTX: Model is fractal, applies to daily, weekly, session, any interval with a defined open (@01:48)
- skip: Mentor-origin anecdote (buying below the open/selling above the close).

### 010 | 20171218 | Higher Time Frame Concepts (Primer 023)
tags: PDH/PDL, PWH/PWL (L1, L2), EQH/EQL (L4), turtle soup (L7), dealing range (S7), liquidity
- DEF: Key-level set for daily-chart trading = last-week H/L, last-month (previous ~30 days) H/L, last-3-month (quarterly) H/L, and rolling 12-month high/low (not calendar year) (@00:41, @01:13)
- RULE: Liquidity run pattern: equal highs (double top) get driven through, reject, and trade lower; equal lows mirrored; a single old high/low behaves the same when it is the nearest clean pool (@01:43, @25:51)
- RULE: Rejection = price takes the level then closes back across it (e.g. below an old low then back above); after a low-side run + rejection, the next target is the nearest opposing old/equal high, and vice versa; ping-pong between pools (@20:45, @22:18)
- RULE: Do not trade inside the middle of a range (about 50% of the defined high-low range); wait for price to reach a key level (@19:44)
- RULE: Measured move projection: low-to-high range of the last leg added to the retracement low (@11:00)
- RULE: Cross-market filter for dollar pairs: align with DXY - DXY up favours EURUSD down, USDCAD/USDJPY up (@15:37, @17:09)
- CTX: Check profile first: trending vs ranging vs reversal; late December is typically consolidation; seasonal consolidation windows (spring trending down from March to Aug/Sep, etc.) (@07:57)
- CTX: Large-fund liquidity pools sit at equal highs/lows and obvious highs/lows, not at retail stops (@24:51)
- EX: Dec 2017 daily DXY: range after year-long decline, equal highs above as draw; EURUSD equal lows being run (@04:14, @09:28)
- skip: Rest is a pair-by-pair walkthrough (GBPUSD, AUD, NZD, USDCAD, CHF, JPY) with low reuse.

### 011 | 20171219 | Secrets To Swing Trading (Primer 024)
tags: OTE (S4), swing points (S6), displacement (S5), partials, EMA filter, consolidation breakout
- RULE: Daily bias filter (retail crutch): EMA10 and EMA20 on close, DAILY chart only. Bullish regime starts when price leaves a consolidation by breaking a swing high and EMA10 crosses above EMA20; ends the bar EMA10 crosses back below EMA20 (bear regime mirrored) (@05:24, @06:28)
- RULE: "Stacking" = EMA10 and EMA20 both pointing the same way with EMA10 fanning away from EMA20; the ideal regime state (@08:04)
- RULE: Hourly execution inside a daily bull regime: only look for longs while price is above the 1h EMA20; after an impulse leg up (new swing high), buy the OTE retrace (62-79% fib, from lowest body/open of the swing low to the highest body of the swing high). Price may wick through EMA20 on the 1h retrace only if EMA10 has not crossed below EMA20 (@09:05, @10:45)
- RULE: Skip if the retrace does not reach OTE depth (no trade) (@14:19)
- RULE: Targets: T1 and T2 = symmetrical swing (leg repeated, ~100% extension) and the 200% extension; hold a small runner (@11:46, @24:11)
- RULE: Stop: below/above the swing; do NOT trail aggressively; trail only after price leaves a consolidation, behind swing lows/highs (@12:16, @12:47)
- RULE: Partials: swing trade take ~50% at T1; day trade take 75-80% at T1 (@26:19)
- RULE: Counter-regime day trades allowed only to a nearby pool (e.g. equal highs + ~20 pips) with a small runner (@25:12)
- DEF: Fib anchors use bodies (open/close), not wicks, on 1h (@13:48, @20:02)
- CTX: Reasoning: daily chart is most watched by banks, so momentum on it gives swing bias; no need for a bias every day, only when conditions are loaded (@02:20, @04:21)
- EX: AUDUSD 1h long: ~0.7570 entry to ~0.7610, one-day hold, after daily 10/20 EMA bull cross (Dec 2017) (@11:46)

### 012 | 20200508 | OTE Pattern Recognition Vol. 02 (USDJPY)
tags: OTE (S4), PDH/PDL (L1), partials, killzone (T1)
- RULE: Daily-TF OTE: fib a swing low to swing high; a daily close/entry into the 62% zone plus price taking the previous day's high signals potential expansion; the target is the previous day's high level (@00:42, @01:42)
- RULE: Intraday entry on 5m: fib the swing inside the NY window 08:30-11:00; entry = 62% level rounded to the nearest 5 pips, stop 10 pips below the swing low (@03:14, @03:47)
- RULE: Scaling: partial 1 at >=15 pips (minimum range criterion), partial 2 ~25 pips, partial 3 ~40 pips at a round 10-level above prior-day high (@04:19)
- DEF: NY window used here for pattern study = 08:30 to 11:00 NY (matches later content) (@03:14)
- EX: USDJPY Thu daily high 106.657 above Wed high 106.629; 5m OTE entry 106.315 stop 106.215 (May 2020) (@01:42, @04:19)

### 013 | 20200513 | OTE Pattern Recognition Vol. 05 (ES)
tags: OTE (S4), order block (P6), PDL (L1), liquidity, partials, SD projection
- RULE: Short setup: HTF structure bearish, target = previous day's low (sell stops below it); in NY session wait for retrace up into the bearish OB (last up-close candle) then sell; stop above the retracement high (@01:13, @01:43)
- RULE: ES scaling is in handles: partial 1 at +30, partial 2 at +50 (half of the range projected), partial 3 at +75 (1.0 projected range / one full SD of the range) (@02:14)
- DEF: "Standard deviation" projection here = the OTE fib range (swing high to low) projected down from the low: 0.5x and 1.0x (@02:14)
- DEF: The fib is not the reason for the move; liquidity below the prior day's low is; price may take several passes to reach it (@02:45)
- EX: ES Jun 2020 contract, 13 May 2020, 5m: target PDL of 12 May, entry 2865 from bearish OB, partial near 2788.75 (@01:43, @02:14)

### 014 | 20220901 | Emini S&P500 AM & PM Session Review 09/01/22
tags: FVG (P1), order block (P6), dealing range (S3/S7), liquidity (L1/L4), MSS (S1), lunch (T1), displacement (S5)
- RULE: Order-block precision: for an up-close candle OB with a wick, use the BODY (open) as the reaction level, not the wick extreme; the 15m bearish OB was hit to the tick (@03:39, @14:25)
- RULE: Intraday draw logic: when price has traded down through a daily FVG and below a daily old low (sell-side taken), then closes in and shifts structure, the draw reverses to the opposite side (back to the intraday swing high / FVG high) (@06:43)
- RULE: Daily FVG high (3922.25) acted as support in the PM: price trades down into it, displaces and breaks a swing high; long with stop below the low, partials as it rallies (@12:54, @13:24)
- RULE: A swing high with an imbalance (FVG) left on the drop after news counts as an intermediate-term high; return into its FVG high was tapped exactly (@07:15)
- RULE: Short-term MSS definition in use: a short-term swing low is broken after a run up into the zone; then entries are taken as price retraces into the FVG/OB; shorts were taken below the highest high (@04:39, @05:42)
- RULE: Avoid resting limit orders into the 12:00-13:00 NY lunch hour: price can fill prematurely before the real move; author's early limit fill was an error (@09:18)
- MMXM: Daily range logic: sell-side below the previous week/quarter low (3913.25) as draw; run lower, take it, then reversal day with run on the buy side (@02:08)
- CTX: PM structure: 13:00 push to buyside level (3938), 14:00 drop into daily FVG high, 15:00 hour setup, ~15:45 window where the market-on-close algorithm runs, ending at a 15m bearish OB (@12:54, @14:25)
- CTX: Marks 10:00 news as a possible disruption to an 09:30 setup (@05:10)
- EX: ES Sep 2022 contract, 1 Sep 2022 daily/15m/5m: objective 4080 stated publicly earlier; today's sell-side low 3913.25 cleared, closed in daily FVG, reversed; PM long off 3922.25 FVG high (@00:37, @12:54)
- skip: Second half is commentary on format (plans for 5-min reviews) and a self-critique of a premature fill.

### 015 | 20220903 | Emini S&P500 AM & PM Session Review 09/02/22 (NFP day)
tags: PO3 / AMD (T2), buy-side liquidity (L4), FVG (P1), order block (P6), rejection block (P9), false bull flag, NFP
- RULE: Do not trade the 08:30 NFP print itself (slippage, bad fills); levels are pre-marked the night before and used after the news (@01:39, @02:40)
- RULE: Premarked draw: relative equal highs / old swing high (ES 4017.75) as buy-side target after the 08:30 spike from a bullish OB; reaching it with a bull-flag-like consolidation that then breaks lower = failed continuation (false bull flag) and sell-side is the new draw (@03:10, @04:10, @06:47)
- RULE: After a sweep of the premarked high, price that stays below it and breaks lower targets the next sell-side pools in sequence, ending at the daily FVG; each lower pool run is a continuation signal (@07:17)
- RULE: Counter-trend leg unfinished business: with buy-side above untouched, early drops (10:00 hour) are expected to rally (OB / FVG at 10:00) toward it; lunch hour then tends to retrace, so the lows get attacked into ~13:15 (@07:49, @08:20)
- MMXM: Intraday PO3 read: open at 09:30 -> run up into a premium PD array (the premarked high) = manipulation/accumulation of shorts -> expansion down to a discount draw -> distribution/cover at the low (daily FVG / sell side) (@09:21, @10:54)
- DEF: Buy-side liquidity = resting buy stops above single or relative equal highs; large funds also leave stops there, so the market is drawn to them (@03:10)
- DEF: Execution meat of the move = the middle of the expansion (FVG re-entries on the way), not the extremes (@10:54, @11:24)
- EX: ES Fri 2 Sep 2022 (NFP): up to 4019.25 vs 4017.75 level at ~10:23, bull-flag fail, drop to daily FVG ~3919 (@06:16, @07:17)
- skip: Tweets/commentary about social media.

### 016 | 20220331 | Real Money Real Results - First Year Expectations (Part 1)
tags: risk/psychology, overtrading
- RULE: Overtrading correction: after a loss streak or a revenge-trade tailspin, cut frequency to one winning trade, then stop for the day (@08:44, @09:14)
- DEF: Account facts for expectation-setting: 25,000 USD funded, one e-mini contract at a time (two contracts only for a reversal), January return reported +22% (@04:34, @09:44)
- skip: Mostly broker-statement walkthrough to rebut critics; no price mechanics.

### 017 | 20220331 | Real Money Real Results - First Year Expectations (Part 2 of 3)
tags: risk/psychology, overtrading
- RULE: Daily cap suggestion: 1-2 trades per day; going past 3 is a warning sign; if you cannot trust yourself, observe only (tape read) for the rest of the period (@12:12, @12:42)
- RULE: Fear-of-execution drill (demo-to-live gap): put on a minimal live trade, exit it, then study what followed; repeat to desensitise, without blowing the account (@08:14, @09:15)
- DEF: February reported +31% (return = (end balance - prior end balance) / prior end balance) (@13:20)
- skip: Statement scrolling; psychology only. Nothing codable except a trades-per-day cap as a risk parameter.

### 018 | 20230110 | ICT Forex Review January 09, 2023 (DXY, EURUSD)
tags: FVG/SIBI (P1), consequent encroachment (CE), EQL liquidity (L4), midnight open (L8), killzones (T1), displacement, SD projection
- RULE: Short setup inside NY open killzone (07:00-09:00 NY): bearish bias, price rallies into a buy-side imbalance / sell-side inefficiency FVG (or takes buy-side), reaches the FVG's CE (midpoint) but fails to retrace to the old daily lows/equal lows; then a short-term MSS (break of a swing low) = entry; stop above the high; target equal lows then the daily FVG (@01:37, @02:07, @02:38)
- RULE: Midnight open (00:00 NY) price extended across the day acts as a premium/discount reference for the day (@01:06, @04:09)
- RULE: Range-extreme timing for trend days: London KZ (02:00-05:00) forms the low (bullish) or high (bearish) of day; the opposite extreme forms in the 10:00-12:00 NY window (London close killzone) (@05:09, @05:39)
- RULE: SD projection recipe: fib anchored from the London low (closing price) to the high of the leg after buy-side is taken, set extension levels 1 / 1.5 / 2.5 / 3 / 3.5 (standard-deviation multiples of the leg); the high of day aligns with the time window ~10:00-12:00 (@06:10, @07:13)
- DEF: SIBI/BISI naming: sell-side imbalance buy-side inefficiency (SIBI) = bearish FVG; equal highs/lows are the preferred liquidity marks he highlights by eye (@01:37, @04:39)
- DEF: Killzone times given here: London open 02:00-05:00 (earlier note said 2-5), NY open 07:00-09:00, London close ~10:00-12:00 (@01:06, @04:39)
- MMXM: Bearish DXY day -> bullish EURUSD day: low of day in London, run buy side, NY continuation entry on bullish OB / FVG retrace, high of day in London close window (@05:39)
- EX: DXY daily 9 Jan 2023: traded down to the sell-side pool and into a daily FVG, closed at the low of day at ~noon (@00:04, @02:38)
- EX: EURUSD 9 Jan 2023, 15m/5m: London low, bullish OB retrace, buy-side run, high ~10:00-12:00 (@04:39)

### 019 | 20250208 | Shotgun Saturday February 08, 2025
tags: dealing range (S7), NDOG/NWOG (P5), PDH/PDL (L1), session H/L (L3), FVG (P1), IFVG (P2), partials, regime filter
- RULE: Level list for trading inside a range: previous day high/low, previous session high/low (e.g. AM high/low and its 50% equilibrium for PM-session trades), NDOGs of the last 5 days, NWOGs of the last 5 weeks (@07:27)
- RULE: Choppy-range playbook: look pre-market or in the opening range for the first FVG, trade it with the bias, take only part of the move (@21:47, @22:17)
- RULE: Plan exits before entry: partial at an opposing FVG once its level fills, or at an inverted old bearish FVG / next short-term high (buy-side) when long; take a realistic stop, not a minimal one (@23:18, @24:51)
- RULE: Define a "best case" target (limit order) but do not require it; scale out at logical levels (@22:48)
- RULE: In a tight, violent range reduce size to one contract and one trade per day until the range resolves (@21:17)
- DEF: Regime filter (discretionary): ranging, whipsaw days with fast, unsustained runs = low-quality; he avoids live January trading and starts around the second week of Feb (@04:55, @05:25)
- CTX: Seasonal volatility windows: clean volatility roughly mid-April through June/July, then late Aug / Sep-Nov / first two weeks of December (@12:35, @13:06)
- CTX: Relative equal highs on the daily chart as buy-side pool; the open daily gap is still being worked, so highs are expected to be run (@26:25)
- EX: NQ daily, Feb 2025: stuck inside a defined range after a late-Dec run down, equal highs above, with gaps being revisited (@02:48, @26:25)
- skip: Mostly psychology/macro commentary and risk warnings; note the NDOG/NWOG list and exit planning only.

## Batch summary
- Top mechanical rules (<=10)
  1. PO3 on any bar/session: bullish = sweep below the open's consolidation low then expand above; bearish mirrored; buy at/below open, sell at/above (009, 012 refs @07:03/@12:44)
  2. Weekly profile: bullish week low forms Sunday open through Wed 07:00 NY, best Tue London to Wed NY open; buy below weekly open; invalidate on new low after Wed NY open; Wed line-in-the-sand (008)
  3. NY continuation model: daily bias + London extreme formed -> 07:00-09:00 retrace sweeping equal lows/prior low -> OTE/FVG entry (007, 018)
  4. OTE: 62-79% fib from lowest body of swing low to top body of swing high; round entry to 5 pips; scale at +15/25/40 pips (FX) or +30/50/75 handles (ES) (012, 013)
  5. Daily bias filter via EMA10/EMA20 daily regime plus 1h EMA20 side filter; only OTE longs when above EMAs (011)
  6. Previous-day high/low as the raid target, sell/buy stops resting beyond; fib is not the cause (012, 013, 015)
  7. Swing hierarchy: short-term = 3-bar, intermediate = swing with lower short-term swings both sides, long-term likewise; MSS = break of last short-term swing after sweep at HTF key level (006)
  8. Entry zones: OB entry on the body not wick; FVG CE (50%) retest; do not rest limits in the 12:00-13:00 lunch hour (014, 018)
  9. Do not trade the 08:30 high-impact print; premark levels, trade after (015)
  10. Partial profits: day trade 75-80% at first target, swing ~50%; take something off every fixed distance; move stop to BE; do not trail aggressively (008, 011)
- Definition changes vs DRAFT
  - Weekly open = Sunday opening price of the week (not 18:00 close-based NWOG) and used as premium/discount pivot (L8/T4)
  - Yearly/quarterly/monthly levels = rolling 12 months / last 3 months / previous month / previous week highs and lows (L2, S7)
  - NY killzone here = 07:00-09:00 (classic), 08:30-11:00 for study window; London KZ 02:00-05:00; London close ~10:00-12:00 (T1; CLAUDE.md says 07:00-10:00)
  - OTE sweet spot 62-79% is anchored to bodies (open/close of extremes), not wicks (S4)
  - Day-range timing: London forms one extreme, 10:00-12:00 NY forms the other on trend days (T2)
  - Swing hierarchy defined by nesting short/intermediate/long (S6) - matches DRAFT
  - Standard-deviation targets: leg projected 1x, 1.5x, 2.5x, 3x, 3.5x (also 0.5x/1.0x in ES example) (T3-like)
  - Bearish OB uses the last up-close candle's body for precision (P6)
- New concepts not in key-levels.md
  - Weekly open / Judas swing / weekly profile timing (Tue-Wed low/high)
  - Cross-market SMT recipe (daily trio of indices; bond 5/10/30) plus quarterly shift and seasonality
  - EMA10/20 regime filter (retail crutch, daily only)
  - 08:30 news avoidance; ~15:45 market-on-close algorithm window
  - Failed continuation pattern ("false bull flag") at a premarked pool
  - Consequent encroachment (CE) of an FVG, SIBI/BISI naming
- Open questions
  - Exact day/session boundary for PDH/PDL and for "weekly open" on futures (Sunday 18:00 NY vs Monday 00:00)
  - Whether the 07:00-09:00 vs 08:30-11:00 NY window should be the entry window for NQ/ES
  - Codable definition of "short-term MSS" at the 5m level and of displacement (not given numerically)
  - How to proxy "bias/HTF order flow" without discretion (only the EMA10/20 regime and weekly open logic are explicit)
  - Quarterly shift/seasonality inputs are only usable for macro filters, not intraday rules
