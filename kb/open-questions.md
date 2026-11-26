# Open questions — decisions only the user can make

## ANSWERED by the user (2026-11-24)
- **Q1 → OC-A box** (N bars, range <= k x ATR).
- **Q2 → SMR-D confirmation score** (weighted score >= `conf_min`, default 3.0; no single required event).
- **Q3 → run ST-A (swing + >=25% retracement) and ST-B (target-based) as variants** and compare in backtests.
- **Q8 → trade-through** (1 tick beyond the level) for MSS / CISD / breaker break / pool taken. IFVG still needs a body close.
Q4-Q7, Q9-Q14: defaults apply until the user decides.

Priority order (highest impact on the code first). Each item: options, default the bot uses until you decide, and what each
option implies for code. Until answered, the default runs and the alternatives are run as backtest variants where cheap.
Q numbers are referenced from `kb/mmxm-spec.md`.

## Q1. Original consolidation (OC) detector — mmxm-spec 6.1
The series only say "tidy, box-like range, equal lows at its base" (2024-b08/024@170:31).
- **OC-A box** (default variant 1): N bars with range <= k x ATR. Code: rolling window, cheap; finds many small boxes on 1m, few on 1D.
- **OC-B session**: last session window classified as consolidation. Code: reuses session classifier; ties MMXM to the clock (intraday only; does not work on 4H/1D).
- **OC-C swing base**: equal lows + intervening swing high, broken with displacement. Code: depends on `eq_tol`; fewest, most "textbook" OCs.
- **OC-D dealing range** (2025): no box, OC = last intermediate swing before the curve; used as target only. Code: simplest; removes state 1 gating.
Implication: OC choice sets the main target (`draw_mode=oc_far`) and how many models are found. Pick one, or keep two as variants.

## Q2. SMR confirmation: score weights, threshold, lock rule — mmxm-spec 4.1 / 6.2
- Threshold `conf_min`: 3.0 (default; two strong components) vs 2.0 (any one strong + one weak; "1-2 is enough") vs 4.0+.
- Lock rule: SMR-D score only (default) / SMR-A CISD pivot / SMR-B breaker + IFVG close / SMR-C MSS.
Implication: lower threshold = more trades, earlier entries, more stop-outs at the SMR high; requiring MSS (SMR-C) delays entry and raises stop distance.

## Q3. First vs second stage boundary — mmxm-spec 6.3
- **ST-A swing**: first swing after SMR + retracement >= 25% of the leg. Code: purely structural, works on any TF.
- **ST-B target**: stage 1 ends at first target (top R level / OC.hi / 70.5%). Code: needs R[] and OC; matches the only geometric source (2025-b01/002).
- **ST-C time**: boundary at the next consolidation/retracement window. Code: intraday only.
Implication: defines where the stage-2 entry and partials happen. Default: run ST-A and ST-B as variants.

## Q4. Which entry types are live
Options: E0 aggressive at the raid (stop just above the wick; 2024 "low-risk sell" above the old high), E1 IFVG retest, E2 first FVG after confirmation, E3 OB, E4 breaker/unicorn, E5 OTE, stage-2 (re-distribution) entry. Default: E1-E4 + stage-2; E0/E5 off.
Implication: each enabled type is one report column. trade-executions prefers stage 2 (b02/067@24:14); 2026 says any stage.

## Q5. Detection TF set and execution routing — mmxm-spec 2
Default: detect 1D/4H/1H/15m, execute 1D->15m/5m, 4H->5m, 1H->1m, 15m->1m. Options: add 1m detection; execute one step lower only; 15s execution (needs data the MCP may not provide).
Implication: more TFs = more instances and overlapping signals (dedupe rule), more OHLCV paging (1m ~5000 bars/page).

## Q6. Session-phase classifier thresholds — session-ranges card
Default: consolidation if range <= 0.6 x expected and overlap >= 0.5; expansion if range >= 1.2 x expected and body >= 60% of range.
Options: ATR-based (default) vs fixed handles vs 07-09 rule only (2026: trending 7-9 -> choppy AM).
Implication: this is the gate for every entry (decision 3); too strict = almost no trades.

## Q7. Day boundary for PDH/PDL and daily candles
Options: CME day 18:00-17:00 (default; TradingView daily bar) vs midnight-to-midnight ("true day", 2024-b02/003@17:11) vs RTH only.
Implication: changes PDH/PDL, 3-day H/L, daily wick CEs and daily FVGs. Midnight open as intraday anchor is kept either way.

## Q8. Trade-through vs body close; wick tolerance (global convention)
Options for MSS / CISD / breaker break / pool taken: trade-through (default; 2023, 2025-b01/002, 2026) vs body close (DRAFT, some 2024/2025 files). IFVG always needs a body close.
Wick tolerance `poke_ticks`: 2 ticks (default) vs 0 vs gap-width-relative (2024-b08/024@163:48).
Implication: trade-through confirms earlier, more false shifts; body close is later and safer. Affects every detector.

## Q9. Relative-equal tolerance
Options: 4 ticks NQ / 2 ES (default) vs 0-2 ticks (2023) vs ~9 ticks (2026 example) vs 0.1 x ATR.
Implication: biggest driver of pool count (targets, SMR raids, OC-C).

## Q10. Main draw / runner target and completion — mmxm-spec 7
Options: OC far side (default) / HTF draw beyond OC / 70.5% of the dealing range / first of these reached. Timeout rule.
Implication: runner holding time and R-multiple; 2026 says exits often stop short of OC.

## Q11. Stop placement
Options: above SMR extreme (default) / beyond entry array (OB high +1 tick, FVG candle-1 extreme) / above first-stage-distribution high for stage-2 entries.
Implication: array stops = smaller risk, more stop-outs inside the model (2024-b07/020 warns against tightening inside the model).

## Q12. Hard filters vs score penalties
HRLR regime, news days (08:30 CPI/NFP/PPI, FOMC before 14:40), NFP-week Thu/Fri, day after a large-range day (AM), Mondays without news, holiday weeks, NQ/ES decoupling, lunch 12:00-13:00.
Options: hard block (default for news releases and FOMC) / score penalty / off.
Implication: hard blocks cut sample size; penalties keep data for learning.

## Q13. Gap anchors and size gates
- NWOG Friday anchor: 16:59 ETH close (default) vs 16:15 RTH settle vs RTH variant (Fri close -> Mon 09:30).
- ORG size gates: 2025 bands (<20 ignore, 20-75 expect CE, 75-120 no edge, >=120 nearest quadrant; default) vs 2026 (open-to-CE >= 30-40 handles) vs 2024 (>= 75 trade the open).
Implication: which gaps become context arrays/targets; whether the 09:30-10:00 window trades at all.

## Q14. Risk regime of the student rules
Options: bot-level caps (1 trade/day per instrument, a loss ends the day, 0.25-0.5% risk) vs none (research mode, every signal logged).
Implication: caps make backtests match the taught routine but hide signal quality; default = no caps in research, caps in the "live-like" report.
