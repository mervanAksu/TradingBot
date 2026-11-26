# pine/ — Phase 1 detectors

Phase 1 = detectors + viewer only (no strategy, no backtest). Source of truth: `kb/key-levels.md`, `kb/concepts/*.md`.
All times America/New_York. All events are known at the close of bar [0] (no lookahead). Swings are confirmed 1 bar
after the pivot.

## Files
| File | What |
|---|---|
| `lib/ict_core.pine` | Library `ict_core`: UDTs `Zone`, `Level`; price-action detectors (below) |
| `lib/ict_time.pine` | Library `ict_time`: clock, sessions, opens, macros, NDOG/NWOG, ORG (returns tuples, no UDTs) |
| `indicators/ict_levels_viewer.src.pine` | Viewer source; `import`s both libraries (`YOUR_TV_USER/...`) |
| `indicators/ict_levels_viewer.pine` | **Generated** bundle (libraries inlined) = the script saved to TradingView |
| `../scripts/build_pine.py` | `python3 scripts/build_pine.py pine/indicators/ict_levels_viewer.src.pine` |

Why a bundle: TradingView can only `import` **published** libraries, and this project never publishes. So the viewer
saved to TradingView has the library code inlined (comments stripped). Edit `lib/*.pine` or the `.src.pine` file, then
rebuild. Never edit the bundle by hand.

## Saved TradingView scripts (PRIVATE, never published)
| Name | script_id | Version | Status |
|---|---|---|---|
| `ict_time` | `USER;72805db608184a51ab250a8b27682966` | 1.0 | saved 2026-11-24 |
| `ict_core` | — | — | **NOT SAVED**: validated clean, but the MCP daily tool quota ran out before the save call |
| `ICT Levels Viewer` | — | — | **NOT SAVED** (same reason). Bundle compiled and ran via `mcp-tv-run-pine-indicator` (15m, see below) |
To do next session: `mcp-tv-create-pine-script` with `lib/ict_core.pine` (name `ict_core`) and the bundle (name
`ICT Levels Viewer`), then add the ids here.

## Validation status (2026-11-24)
- `ict_core.pine`: `mcp-tv-validate-pine-script` 0 errors / 0 warnings.
- `ict_time.pine`: 0 errors / 0 warnings; saved (compiled by the create call).
- Viewer bundle: full compile + run OK on `CME_MINI:NQ1!` 15m (58 plots, 48 inputs).

## Data depth on the MCP (checked 2026-11-24, NQ1!)
| TF | History starts |
|---|---|
| 1m | 2026-11-08 |
| 5m | 2026-10-04 |
| 15m | 2026-05-31 |
| 30m / 1H | before 2026-05-13 |
So the KB example days cannot be checked on 1m/5m: 2026-07-08 and 2026-06-02 on 15m, 2026-05-13 only on 30m/1H/4H.
`run-pine-indicator` returns at most 1000 recent bars. For that reason the viewer has **probe plots** (`P:` prefix,
Data Window only). They hold values from the date in the `Probe date` input (`in_47`, yyyymmdd NY), so an old day can
be read from `last_values`.
ORG needs a bar that closes exactly at 16:15 (1m/5m/15m). On 30m/1H/4H, ORG is na by design, and the 08:30 open is na on 1H/4H.

## Eyeball checks
| Day / TF | Status |
|---|---|
| 2026-07-08 NQ 15m | **run** (probe values below) |
| 2026-06-02 NQ 15m | pending (quota) |
| 2026-05-13 NQ 1H/4H | pending (quota) |
| 2-3 recent days, 1m/5m (after 2026-11-08) | pending (quota) |
| OHLCV cross-check with `mcp-tv-get-ohlcv` | pending (quota) |

2026-07-08 15m probe (values from the indicator; not yet cross-checked against raw OHLCV):
- Opens: midnight 29470, 08:30 29176.75, 09:30 29202.75. PDH 29973.75 / PDL 29210. The 09:30 open is just below PDL.
- ORG: settle (16:00 15m bar close = 16:14 print) 29417.25 → open 29202.75. This is a discount gap of 214.5 handles, band 3 (>= 120, quadrant only).
- NDOG (Tue 07-07 16:59 → 18:00): 29373.75-29419.5, CE 29396.6. Asia 29266-29558.75, London 28957.25-29414.75.
- Day counts (00:00-24:00): 15 BISI, 10 SIBI, 18 IFVG, 14 bear OB, 15 bull OB, 9 breakers, 25 CISD, 6 MSS, 0 EQ pools, 40 swings.
- First RTH events: bull OB key 29212 at 09:30; BISI 29230-29287.75 at 09:45; bearish CISD at 29202.75 at 10:45;
  bearish MSS ref 29148 at 11:00.
- Consistency with the KB narrative (2026-b04/067: "09:30 up to NDOG CE, fail; short in the 10:50-11:10 macro"):
  the open is below the NDOG and the first RTH OB/BISI are bullish (rally leg). The first bearish CISD (10:45) and MSS
  (11:00) land in the 10:50-11:10 macro area. This is qualitatively consistent; the ICT example is 1m, so 15m timing
  is coarse.
- Observations: on 15m NQ, EQ pools = 0 with tol 4 ticks (1 handle), so the tolerance is tight for 15m. IFVG and OB counts are high.
  OB validation by trade-through, per the card, fires on most alternations. Expected; filters belong to the strategy (score).

## Functions
`ict_core` (card → defaults):
| Function | Card (status) | Rule / defaults |
|---|---|---|
| `swingHigh/swingLow(len=1, useBody=false)` | swing-points (VERIFIED) | 3-bar, strict left, tie right; returns [ok, price, time, bar_index] of pivot at [len] |
| `nest(isNew, price, t, isHigh)` | swing-points | STH stream → ITH; ITH stream → LTH |
| `eqPool(isNew, price, t, isHigh, tol, rightShorter=true, maxSwings=10)` | relative-equal-hl (VERIFIED-low) | tol 4 ticks NQ / 2 ES (viewer); quality A/B/C; flag = smooth |
| `displacementBar(1.0, 0.7, 14, 0)` | displacement (VERIFIED-low, proxy) | body >= 1xATR14, close in outer 30% |
| `displacementLeg(fvgBull, fvgBear, 1.5, 3, 14)` | displacement | <= 3 bars, sum body >= 1.5xATR, >= 1 FVG |
| `volumeImbalance(minSize)` / `viUpdate(z)` | volume-imbalance (VERIFIED) | 1 tick; skips zero-body middle bar; closed when one body spans it |
| `fvg(minSize, withVI=true, c2Disp)` / `fvgUpdate(z)` | fvg (VERIFIED) | 4 ticks NQ / 2 ES; box incl. adjacent VI; CE, q25, q75; tested / weak (close beyond CE) / failed (close beyond far edge) |
| `ifvgFrom(z)` / `ifvgUpdate(z)` | ifvg (VERIFIED) | one_close inversion; fails on close beyond CE, "reclaimed" on close beyond original far side |
| `orderBlock(maxRun=5)` / `blockUpdate(z)` | order-block (VERIFIED) | key = open of first candle of the run; validated on trade-through; MT = ce; fails on close beyond MT |
| `breaker(isSH, shP, shI, isSL, slP, slI, sweepMin=0, closeMode=false, maxRun=5)` | breaker (VERIFIED) | H1-L-H2 sweep, trade-through of L (Q8); zone = bodies; fails on close beyond MT |
| `cisd(isSH, isSL, maxSeries=10, maxBars=30, closeMode=false)` | cisd (VERIFIED) | series_first_open, trade-through (Q8) |
| `mss(isSH, shP, isSL, slP, dispDir, extRaidUp, extRaidDn, maxBars=20, closeMode=false, needDisp=true)` | mss (VERIFIED) | raid → displacement → trade through last opposite swing (Q8) |
| `wickZone(upper, off=0, minAtr=0.5, force=false)` / `wickUpdate(z)` | wick-ce (VERIFIED) | body edge → extreme; CE; fails on close beyond CE |
| `newZone`, `overlaps` (unicorn), `grid(lo, hi, n=4)` | gradient-levels | quadrants / octants |

`ict_time`:
| Function | Card | Rule / defaults |
|---|---|---|
| `nyMin`, `nyDate`, `startsAt(hh, mm)`, `inWindow(sess)` | — | NY clock helpers |
| `openAt(hh, mm)` | opening-prices (VERIFIED) | open of the bar starting at hh:mm (viewer: 00:00, 08:30, 09:30) |
| `sessionRange(sess)` | session-ranges (VERIFIED) | running H/L/O; viewer: Asia 1800-0000, London 0200-0500, NY AM 0700-1000, lunch 1130-1330, PM 1330-1600 |
| `prevDayHL()` | session-ranges L1 | PDH/PDL on the 18:00 CME day |
| `macro(padMin=0)` | macros-time-windows (VERIFIED) | xx:50-xx:10 hourly + 15:15-16:00 extra |
| `openingGap(quarterMin)` | ndog-nwog (VERIFIED) | 16:59 close → 18:00 open; NDOG Mon-Thu, NWOG Sunday; quarters if >= 20 handles (NQ) |
| `org(min=20, mid=75, high=120)` / `orgCeTouch(ce)` | opening-range-gap (VERIFIED) | 16:14 close → 09:30 open; bands; ES sizes x0.25 in the viewer |

## Decisions the cards left open (all are inputs or documented defaults)
1. Swing `body` variant: pivots are still detected on wicks; only the reported price is the body extreme.
2. EQ pools: compare against the last 10 untaken swings, newest first. A swing is dropped once traded through, so quality C
   (newer beyond older) cannot occur. "touches_between <= 1" is not implemented. Smoothness is checked with closes up to the confirmation bar.
3. FVG `fvg_min_ticks` is tested on the wick gap before the VI extension. `t_created` = time of candle 1.
4. VI: a zero-body middle bar is skipped (compare with bar [2]).
5. OB: run capped at the newest `maxRun` (5) bars; dojis continue a run but are not used as the first candle. One pending
   candidate per side: a newer run replaces an older unvalidated one. No expiry.
6. Breaker: H1 = the STH immediately before H2. L = lowest STL between them. A higher STH with no new STL extends H2.
   The block = down-close run found within 5 bars at or before L. Unicorn = overlap with any active same-direction FVG (viewer).
7. CISD: series = up-close run ending at the pivot bar, or at bar [0] if the run continues, or at bar [2] if the pivot is
   down-close. Max 10 bars. Re-armed by every new pivot. Expires after 30 bars.
8. MSS: default raided pool = latest confirmed opposite swing (session pools can be passed via `extRaidUp/Dn`).
   Ref = last opposite swing confirmed before the raid. Displacement = `displacementBar` proxy, counted from the raid bar.
9. ORG: settle = close of the bar closing at 16:15. TF must be <= 15m. An early-close day keeps the previous settle.
10. NDOG/NWOG: needs a real break (`time_close[1] < time`). The holiday-week NWOG skip is not implemented.
11. Session ranges use the bar start time; opens are na if no bar starts exactly at the time.
12. Macro shading is shown only on TFs <= 15m.
Gaps (not built in phase 1): ITH "has_fvg" tag, wick composites (gray pool / obsidian / bolo), FVG expiry by
`pda_lookback_days`, `max_touches`, tethering/quad-alignment flags, IFVG modes other than one_close, session phase classifier.
Realtime: drawings are updated on every tick of the forming bar. The library logic is bar-close based, so use confirmed bars for alerts.

## strategies/mmxm_v1.pine (2026-11-25, NOT yet validated on TradingView — quota)
MMXM sell + buy model on the chart TF, HTF dealing range for premium/discount.
- OC-A box (ocLen bars, height <= ocK x ATR) -> departure (close beyond box) -> curve; swing lows/highs on the curve = R[] levels.
- SMR: raid of a swing pool in HTF premium/discount, then confirmation score within smrWin bars
  (C CISD trade-through, I IFVG body close, M MSS trade-through, O OB body close beyond key open, S SMT vs ES/NQ,
  H SMR in HTF outer quadrant, m raid in macro, D displacement candle). Score + letters go into the order comment.
- Entry: IFVG retest or first FVG after confirmation (limit). Stop = SMR extreme + pad. TP1 = nearest R level >= minRoom away
  (fallback OC near edge), TP2 = next level (fallback event horizon), runner = OC far side. Stop -> entry after TP1.
- Filters: macro windows (order active only in xx:50-xx:10), HRLR overlap filter, flat by 15:55 NY.
- Not in v1: multi-TF instances (run it on several chart TFs instead), stage-2 (re-distribution) entries, session-phase classifier, OC-B/C, ST-A/B variants.

## indicators/mmxm_v2.pine (2026-11-25) — saved PRIVATE `USER;127678405e174280aac9152bfa074d55` v1.0, compiles with 0 warnings
- Liquidity levels as horizontal rays (extend right) from each swing; a ray stops (dotted) at the bar that sweeps it.
- OC v2 = cluster of relative-equal highs and/or lows (tolerance max(0.25 x ATR14, 4 ticks), 5-150 bars apart, height <= 4 x ATR).
  Mode "EQH or EQL" / "EQH and EQL" (★). Departure = displacement close beyond the box -> arms the sell (up) / buy (down) model.
- Phase engine: day 18:00-18:00 NY in four 6h quarters, each 6h in four 90-min quarters with clock roles A/M/D/X;
  each completed quarter is classified from price (CONS / MANIP / EXP / REV / RETR) vs the previous quarter and a range baseline;
  table shows the expected next phase by clock and by price.
- SSMT: current quarter vs previous completed quarter against ES1!/NQ1! (one takes the prior quarter extreme, the other does not).
- SMR after departure: raid of a ray beyond the OC in HTF premium/discount + score (C CISD, I IFVG, M MSS, S SSMT, H HTF quadrant, m macro).

## mmxm_v2 strategy v3.1 (2026-11-26)
- Nested premium/discount: dealing range (last swing low -> swing high, pivot 3) on D / 4H / 1H / chart TF.
  <50% = discount (votes long), >50% = premium (votes short), ±5% = EQ. Default gate: net agreement >= 2.
  HTF bias for the counter-trend rule = D zone (CT: capped at 2R, risk x0.5).
- Dynamic sizing: base 5% of equity; ±10% equity vs start -> x(1+0.15) / x(1-0.35); 10% DD from peak -> x0.75;
  last 10 trades net +/- -> x1.15 / x0.85; clamp 1%..8%; contracts = risk$ / (stop pts x point value + fees); TP1 50%, TP2 25%, runner rest.
- New inputs appended (in_42..in_64) so earlier ids stay valid. Backup of v3.0: ~/mmxm_v2_v30_backup.pine (VM) + TradingView version history.
