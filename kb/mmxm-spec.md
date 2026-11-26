# MMXM spec — v1 (VERIFIED, synthesizer 2026-11-24)

Market Maker Sell Model (MMSM) is specified in full; the Buy Model (MMBM) is its mirror (section 5). Card names refer to
`kb/concepts/<card>.md`; conventions (bars, ticks, "bodies respect") are in `kb/key-levels.md`. Items marked **[USER]** need a
choice from `kb/open-questions.md`; until then the bot runs every listed proxy as a variant and reports results per variant.

Source basis: the only geometric statement is 2025-b01/002 (buy model, raid-candle open pivot, IFVG/first-FVG low-risk entry,
stage 1 = OB+FVG to 70.5%, stage 2 = first retrace into an inefficiency). Sell-model walk-throughs: 2024-b08/024, 2024-b07/020,
2026-b04/067, 2026-b04/072, 2026-b05/082, 2026-b09/123, 2025-b03/026, 2025-b04/053. No series gives numeric stage boundaries.

## 1. Design principles (from the user decisions at the end of this file)
- **Multi-TF instances.** One state machine instance per detection TF in `detect_tfs`; each routes execution to a lower TF.
  An instance never needs another TF to exist, but it reads HTF context (arrays/draws) from TFs above it.
- **Confluence score, not one trigger.** Confirmation = weighted score >= `conf_min` (section 4). Every trade logs its score
  components so results can be bucketed.
- **Session-phase gating.** Entries only when the phase sequence allows it (section 3).
- **Macro filter** (xx:50 -> xx+1:10) is an input applied at order placement/fill.
- **Management**: partials at each re-accumulation/re-distribution level, stop to entry after the first partial, runner to the main draw.
- The model can be entered at any stage (2026-b04/072@17:34); each entry type is a separately reported variant.

## 2. Multi-TF routing
| Detection TF | Execution TF(s) | HTF context TF(s) | Notes |
|---|---|---|---|
| 1D | 15m, 5m | W, 1D box20 | daily MMXM -> trade SMR / 1st / 2nd stage on LTF |
| 4H | 5m | 1D | |
| 1H | 1m | 4H, 1D | |
| 15m | 1m | 1H, 4H | intraday models (2026: any TF) |
| 1m (optional) | 1m (or 15s if data) | 15m, 1H | "1m draw on liquidity -> trade the reaction at the key level" |
- `detect_tfs` and the routing map are inputs **[USER Q5]**. Instances on different TFs may agree; if two instances want the
  same entry (same side, entry within `dedupe_ticks`), keep one order and record both instance ids (score = max).
- Execution-TF arrays used for entries must be created after the detection-TF state that arms them (no look-back entries).

## 3. Session-phase gate (user decision 3)
Each completed window (Asia 18:00-00:00, London 02:00-05:00, 07:00-09:00, NY AM 09:30-11:30, lunch 11:30-13:30, PM 13:30-16:00)
is classified by `session-ranges.md` as CONS / EXP / RETR / REV. Gate for a new entry in the current window:
| Previous window(s) | Current behaviour | Allowed |
|---|---|---|
| CONS | expansion started (range > `exp_k` x expected, or prior window extreme taken with displacement) | yes: continuation or the reversal after the expansion's raid |
| EXP | price raids a pool and confirms (SMR) | yes: reversal entries (low-risk / stage 2) |
| EXP | pullback into an array without SMR | yes: retracement-then-continuation entries (re-accumulation/re-distribution) only in the direction of the expansion |
| CONS | still consolidating (no expansion yet) | no new entries (time distortion; 2025-b02/006@136:22) |
| EXP, EXP, EXP (3 in a row) | | reduce score (trend across three sessions is rare; 2026-b02/029@13:02) |
Regime overlay: `hrlr-lrlr.md` HRLR -> no new entries unless `allow_hrlr`; day-type flags (news, large-range-day, NFP Thu/Fri,
FOMC before 14:40) from `macros-time-windows.md` / `tgif-weekly-profile.md` gate entries (each flag is an input).
Classifier thresholds are **[USER Q6]**.

## 4. State machine — Sell model (MMSM)
Variables per instance: `OC{hi,lo,base_pool}`, `R[]` (re-accumulation levels on the buy side of the curve, ordered high -> low),
`SMR{high,bar,pool}`, `score`, `LRS` (low-risk sell array), `stage`, `RD` (re-distribution array), `draw` (main target).

| # | State | Enter when (transition condition) | Leave / invalidate | Cards |
|---|---|---|---|---|
| 0 | `IDLE` | default; reset target of all invalidations | -> 1 when an OC is detected | — |
| 1 | `OC` | OC detector fires (proxy **[USER Q1]**, section 6.1); store OC.hi/lo and the sell-side pool at/below OC.lo (EQL if present) | -> 2 on departure up: close > OC.hi (`oc_break` close) ; -> 0 if price closes < OC.lo - `oc_pad` first (that raid may seed a buy-model instance, section 5) ; -> 0 after `oc_timeout` bars | relative-equal-hl, swing-points, session-ranges |
| 2 | `BUY_CURVE` | departure from OC upward | each pullback that forms a 3-bar STL and resumes above the prior high appends a level to R[] (the STL low and any bullish FVG/OB left under it); stage labels on this side use the same proxy as Q3 ; -> 3 when price is in the SMR zone (below) ; -> 0 on close < OC.lo | swing-points, fvg, order-block |
| 3 | `SMR_ZONE` | (a) price trades into an HTF premium array (FVG/IFVG/OB/wick q50-q100/NWOG/NDOG/ORG premium quadrant/suspension block on a context TF) or above EQ of the context range (`premium-discount.md`), and (b) a buy-side pool is raided (`turtle-soup.md` raid: high >= pool + `ts_min_poke_ticks`) | SMR.high = max high since entering; -> 4 when score >= `conf_min` within `smr_window` bars of the raid; -> 2 if no confirmation and a close > SMR.high + `poke_ticks` (run, not raid: re-enter BUY_CURVE with new high) | turtle-soup, wick-ce, ndog-nwog, opening-range-gap, premium-discount |
| 4 | `SMR_CONFIRMED` | confirmation score >= `conf_min` (section 4.1) and lock rule **[USER Q2]** (section 6.2) | arms entries; `draw` set (section 7); -> 0 on body close > SMR.high | cisd, ifvg, mss, order-block, breaker, smt |
| 5 | `LOW_RISK_SELL` | an entry array exists: E1 IFVG formed in the reversal (retest of near edge/CE), E2 first bearish FVG after confirmation, E3 bearish OB validated (key open -> MT), E4 breaker/unicorn of the SMR swing, E5 OTE 62-79% (variant) | order placed if gates pass (section 3, macro, price >= EQ of the SMR leg, room to first target >= `min_room`); fill -> 6 ; no fill before price reaches the first partial level -> skip to 6 without position (later entries still allowed) ; -> 0 on close > SMR.high | fvg, ifvg, order-block, breaker, ote, macros-time-windows |
| 6 | `DIST_1` | first leg down after SMR (with or without a position) | partial ladder runs (section 7); stage-1 end by proxy **[USER Q3]** (section 6.3) -> 7 ; -> 0 / stop on close > SMR.high | event-horizon, sd-projection |
| 7 | `REDIST` | stage-1 end detected: retracement up begins | RD = first premium array of the stage-1 leg that price retraces into (bearish FVG/IFVG/breaker/OB/BPR/premium wick), must be at or above EQ of the stage-1 leg; stage-2 entry allowed while bodies respect RD (no close above RD.ce or RD.mt) ; -> 8 on departure: close below RD.bottom then new low below stage-1 low (or below the RD swing low) ; -> 0 / exit on close above the stage-2 swing high or SMR.high (2025-b01/002@141:55 mirror) | fvg, ifvg, breaker, bpr, wick-ce |
| 8 | `DIST_2` | departure from RD | runner managed to `draw`; speed check (optional): stage 2 reaches the stage-1 distance in fewer bars than stage 1 (2026-b05/089@36:14) | displacement |
| 9 | `COMPLETE` | `draw` hit, or `model_timeout` bars, or exit at end of day for intraday instances (`flat_by` 16:50; no weekend holds) | log stages, score, levels; -> 0 | — |

### 4.1 Confluence score (user decision 2)
| Component | Default weight | Fires when (within `smr_window` bars after the raid, before body close > SMR.high) | Card |
|---|---|---|---|
| CISD of the raid series | 2.0 | trade (or close, per `cisd_mode`) below the open of the up-close series that made SMR.high | cisd |
| IFVG close | 2.0 | a bullish FVG of the last up-leg is closed through by a body | ifvg |
| MSS | 1.5 | trade/close below the nearest STL with displacement | mss |
| Bearish OB validated | 1.0 | trade below the key open of the up-close run at SMR.high | order-block |
| Breaker formed | 1.0 | H1-L-H2 sweep pattern + break below L | breaker |
| SMT NQ/ES | 1.0 | bearish SMT at SMR.high | smt |
| HTF array confluence | 1.0 | SMR.high inside a context-TF premium array or on its quadrant | gradient-levels, wick-ce |
| Raid in a macro / killzone | 0.5 | raid bar inside a macro window | macros-time-windows |
| Displacement on the break | 0.5 | break leg passes displacement test | displacement |
| Tethered entry array | 0.5 | entry array tethered | gradient-levels |
- Default `conf_min` = 3.0 (= two of the strong components, or one strong + two weak). Weights and threshold are inputs
  **[USER Q2]**; results are reported by score bucket (3-4, 4-5, 5-6, >= 6) and by component.

## 5. Buy model (MMBM) — mirror
Swap highs/lows, premium/discount, BSL/SSL, up/down-close. States: `OC` -> `SELL_CURVE` (re-distribution levels R[] ordered
low -> high) -> `SMR_ZONE` (sell-side raid inside an HTF discount array) -> `SMR_CONFIRMED` -> `LOW_RISK_BUY` -> `ACC_1` ->
`REACC` -> `ACC_2` -> `COMPLETE`. Buy-model specifics from 2025-b01/002:
- Pivot = open of the raid candle (series); one tick above it counts (CISD, `cisd_mode=trade`).
- Low-risk buy = IFVG at the turn if one exists, else the first bullish FVG after SMR (E1 then E2 priority).
- Stage 1 = next FVG anchored to an OB (OB+FVG pair) carrying price to 70.5% of the dealing range (OC.hi -> SMR.low).
- Stage 2 = first retrace into an inefficiency after stage 1; price may never trade back through the stage-2 swing low (exit if it does).
- 2024-b13/045@69:54: the buy model need not revisit the OC; the draw decides (section 7 `draw_mode`).
A sell-side raid of OC.lo while an MMSM instance sits in state 1-2 spawns an MMBM candidate with SMR_ZONE = that raid.

## 6. Stage-boundary proxies [USER] — the transcripts give no numbers
### 6.1 Original consolidation (Q1)
| Proxy | Rule (detection TF) | Basis |
|---|---|---|
| OC-A box | last `oc_min_bars` (20) bars with (max high - min low) <= `oc_k` (2.0) x ATR(14) and mean bar overlap >= 0.5; OC = that box; extends while the condition holds | "tidy box-like range", 2024-b08/024@170:31 |
| OC-B session | the most recent completed session window classified CONS (Asia, London, 07-09, lunch) on the execution day; OC = its H/L | sessions as consolidation, 2023 daily skeleton (2023-b01/009@03:44); London EQL as OC, 2026-b05/082@01:01 |
| OC-C swing base | the last pair of relative equal lows (EQL, `relative-equal-hl.md`) with a swing high between them, before a departure that breaks that swing high with displacement; OC = [EQL level, intervening swing high] | "box with equal lows at its base", 2024-b08/024@171:02; 2026 EQL OC |
| OC-D dealing-range (2025) | no box: OC.hi (sell model: OC.lo) = the last ITL (ITH for buy model) before the curve; used only as target anchor | 2025-b01/002@27:33, @65:14 |

### 6.2 SMR confirmation / lock (Q2)
| Proxy | Rule | Basis |
|---|---|---|
| SMR-A CISD pivot | SMR locked at the first trade through the open of the up-close series that made SMR.high | 2025-b01/002@101:04; 2024-b08/024@147:53 |
| SMR-B breaker + IFVG close | locked when a breaker (H1-L-H2) exists and a body closes below a bullish FVG of the last leg | 2026-b05/082@03:03 |
| SMR-C MSS (Model 2022) | locked on trade/close through the nearest STL with displacement leaving an FVG | 2022-b01/002@16:14; 2026-b12/142@07:45 |
| SMR-D score only (default) | locked when score >= `conf_min` regardless of which components fired | user decision 2 |

### 6.3 First vs second stage (Q3) — applies to distribution (sell) and accumulation (buy), and to the left-side labels
| Proxy | Stage-1 end / re-distribution start | Basis |
|---|---|---|
| ST-A swing | first 3-bar STL after SMR followed by a retracement >= `st_retr_min` (0.25) of the leg SMR.high -> that STL | "first leg, then retracement", 2024-b08/024@187:35 |
| ST-B target | stage 1 ends when price reaches the first target level (highest R[] level, OC.hi, or 70.5% of OC->SMR range for the buy model), then the first retrace into an inefficiency starts re-distribution | 2025-b01/002@133:40, @134:41 |
| ST-C time | stage boundary at the next window boundary where the phase classifier says CONS/RETR (e.g. lunch after an AM leg); stage 2 = the next EXP window | time-first teaching; 2026-b09/123 two-day chain |

## 7. Entries, stops, management (user decision 4)
- **Stop**: default above SMR.high + `stop_pad` (2 ticks) for E1-E4; variants: entry-array far edge + 1 tick (OB high +1,
  2024-b08/024@180:21), or the first-stage-distribution high once it exists (trade-executions b02/066@19:52). **[USER Q11]**
- **Partial ladder** (sell model, nearest first): R[] levels below entry (re-accumulation lows and their FVG/OB edges from the
  buy side of the curve), OC.hi, event horizons between consecutive pools (`event-horizon.md`), session/day pools, OC.lo. Exit
  limits sit `exit_inside_ticks` (1) before each level. Skip levels closer than `p1_min_handles` (NQ 10) to entry.
- After the first partial: stop -> entry (+ costs). Never lowered/widened afterwards. Optional trail (off by default): above the
  most recent 3-bar swing high or the open of a new 2-candle bearish OB (trade-executions b02/062@43:19).
- Size split: `partial_plan` default = 50% at P1, then equal parts at each later level, `runner_pct` 25% held to `draw`.
- **Main draw** (`draw_mode`, **[USER Q10]**): `oc_far` = OC.lo (sell) / OC.hi (buy) (default) | `htf_draw` = nearest
  unfilled context-TF array or pool beyond OC | `705` = 70.5% of the dealing range (2025 low-hanging) | `nearest_of` (first reached).
  If OC.lo was already swept before SMR, use the next pool beyond it (2026-b04/067@08:46).
- **HRLR switch**: no trailing, stop to cost only, partial at each new extreme (2024-b11/036@107:07).
- **Re-entry**: after a stop-out inside an armed model, re-entry allowed once at the next IFVG/VI retest if state is still 5-7
  (2024-b07/020@10:16); none after `DIST_2` started (2026-b05/089@95:34).
- Min room: entry to first partial >= `min_room` (NQ 15 handles, ES 4) (2026-b10/129@55:06; 2023-b03/024@24:22).

## 8. Parameters (defaults)
| Name | Default | Range | Note |
|---|---|---|---|
| detect_tfs | 1D, 4H, 1H, 15m | + 1m | [USER Q5] |
| exec_map | 1D->15m/5m, 4H->5m, 1H->1m, 15m->1m | | [USER Q5] |
| oc_proxy | all (variants) | OC-A, OC-B, OC-C, OC-D | [USER Q1] |
| oc_min_bars / oc_k | 20 / 2.0 | 10-60 / 1-4 | OC-A |
| oc_timeout | 200 bars | | |
| smr_window | 20 bars | 5-60 | raid -> confirmation |
| conf_min | 3.0 | 1.5-6 | [USER Q2] |
| smr_lock | SMR-D | A-D | [USER Q2] |
| stage_proxy | all (variants) | ST-A, ST-B, ST-C | [USER Q3] |
| st_retr_min | 0.25 | 0.15-0.5 | ST-A |
| entry_types | E1, E2, E3, E4 | + E0 aggressive at raid, E5 OTE, stage-2 entry | [USER Q4] |
| macro_filter | on | on/off | decision 3 |
| allow_hrlr | false | bool | [USER Q12] |
| stop_mode | smr_extreme | smr_extreme, array, dist1_high | [USER Q11] |
| draw_mode | oc_far | oc_far, htf_draw, 705, nearest_of | [USER Q10] |
| partial_plan / runner_pct | 50% P1 / 25% | | |
| exit_inside_ticks | 1 | 0-4 | |
| min_room | NQ 15 h, ES 4 h | | |
| model_timeout | 3 x (bars from OC break to SMR) | | proxy |
| flat_by | 16:50 for instances on TF <= 1H | | no weekend holds |

## 9. Cannot be made fully mechanical (logged, not guessed)
- "Tidy" consolidation, "unmistakable" displacement, "respect" by bodies: only proxies (OC-A..C, displacement.md, poke_ticks).
- Narrative/bias (which draw is "the" draw): approximated by `draw_mode` and context-TF arrays; the instructor's after-the-fact
  stage labels are inconsistent (2024-b12/038@88:15; 2026-b03/044@12:49), so labels are leg counts, not separate detectors.
- Model completion is unknowable in real time (2026-b11/138@59:17): hence partials, runner and timeout.

## User decisions (2026-11-24)
1. **No fixed TF pair.** The model is traded on whatever timeframe it forms (daily MMXM → trade SMR / 1st / 2nd
   distribution on lower TFs; a 1m draw on liquidity → trade the reaction at the key level). v1 must therefore detect
   MMXM on several TFs (e.g. 1D, 4H, 1H, 15m) and route execution to a lower TF. Execution TF set is a parameter.
2. **Confluence score, not a single confirmation.** Confirmations: CISD, IFVG, MSS, OB, breaker (+ others from the KB).
   1-2 is enough to trade; more = higher score. Implement as a weighted score with a minimum threshold (input),
   and report results by score bucket so we learn which confirmations matter.
3. **All sessions allowed, gated by market phase.** Classify each session as consolidation / expansion /
   retracement / reversal. After a consolidation (e.g. Asia), wait for expansion, then decide reversal vs
   retracement-then-continuation. Entries preferably inside **macros: xx:50 → xx+1:10 NY** (last 10 min of the hour
   to first 10 min of the next); macro filter on/off is an input.
4. **Partial take-profits at each re-distribution / re-accumulation level; after the first partial the stop moves
   to entry; the runner targets the main draw (original consolidation / opposing liquidity).**
