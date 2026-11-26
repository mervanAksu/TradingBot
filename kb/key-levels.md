# Key Levels — master list

Status: **VERIFIED** by the synthesizer on 2026-11-24 from all 8 series digests (`kb/series/*.md`). Per-row status:
VERIFIED = series agree (or one definition chosen, alternatives kept as variants); VERIFIED-low = defined by a single series or
only by our own proxy (code it, but bucket results). Nothing is CODED yet.
`U` = asked for by the user, `+` = added. Full rules, params and refs live in the linked card (`kb/concepts/<card>.md`).

## Conventions (all detectors)
- Time: America/New_York. Bars: `[0]` = newest closed bar, `[1]` previous. `bodyHi = max(open,close)`, `bodyLo = min(open,close)`.
- Tick 0.25 (NQ, ES); 1 handle = 4 ticks. NQ-to-ES size scaling default 0.25 (ES 5 handles ~ NQ 20; 2023-b05/049@04:37).
- Zone object: `{top, bottom, ce|mt, q25, q75, dir, tf, created_at, state}`; CE = 50% of a gap/wick, MT = 50% of an OB/breaker body, EQ = 50% of a dealing range.
- "Bodies respect level X" (bearish) = no bar closes above X; wicks may overshoot up to `poke_ticks` (default 2, "mohawk") without invalidating.
- "Taken / traded through" default = trade-through (`high > level`); body-close variant per card (`run_mode`, `mss_mode`, `cisd_mode`).
- PD-array lookback `pda_lookback_days` = 20 trading days (variants 40/60). Every detector runs per TF in the configured TF set.

## Liquidity (targets / draws)
| # | Level | Src | Status | Operational definition (v1) | Variant/Param | Card |
|---|---|---|---|---|---|---|
| L1 | Previous Daily High/Low (PDH/PDL), 3-day HH/LL, last 5 daily H/L | U | VERIFIED | H/L of prior CME trading day (18:00-17:00); 3-day matrix with today = day 1; Sunday's own H/L ignored | `day_boundary` 18:00 \| 00:00 | session-ranges |
| L2 | Previous Weekly / Monthly H/L (+ month close) | U | VERIFIED | Week Sun 18:00 -> Fri 17:00; prior month H/L/C (month ends 17:59), 3- and 12-month H/L | monthly open ignored | session-ranges |
| L3 | Session H/L (Asia, London, pre-market, 07-09, NY AM, lunch, PM, final hour, OR, FHDR, ONR, MOR) | U | VERIFIED | H/L inside each window of the session table; taken on trade-through | windows in card; `asia_window`, `london_window` | session-ranges |
| L4 | Relative equal highs/lows (EQH/EQL), smooth pools | + | VERIFIED-low | Two swings within `eq_tol`; newer point stops short of older; smooth = no close beyond between them | `eq_tol_ticks` 4 NQ/2 ES (0-12); `eq_order`; `run_mode` trade \| body | relative-equal-hl |
| L5 | LRLR (low-resistance liquidity run) | U | VERIFIED-low | Regime: mean bar overlap <= 0.35 and >= 1 FVG per 15 min; path sense = no unfilled opposing array before the pool | `hr_mode` regime \| path \| both | hrlr-lrlr |
| L6 | HRLR (high-resistance liquidity run) | U | VERIFIED-low | Regime: overlap >= 0.5 or < 1 FVG/15 min or arrays re-touched >= 3 bars | `hr_overlap`, `hr_fvg_rate`, `hr_touch_max` | hrlr-lrlr |
| L7 | Turtle Soup (raid + reversal) | U | VERIFIED | Trade >= 1 tick beyond a marked pool, then close back inside within 3 bars (CISD optional/score) | `ts_confirm` close_back \| wick_ce \| cisd \| body_run; Venom; type B continuation | turtle-soup |
| L8 | Opening prices: 00:00, 08:30, 09:30, 13:30, 18:00, weekly open; MOR | + | VERIFIED | Opens of those 1m bars; bullish day buy at/below, bearish sell at/above; MOR 00:00-00:30 with 0.5/1 projections | `anchor_open`; `weekly_open` sun_1800 \| mon_0000 | opening-prices |
| L9 | SMT divergence NQ vs ES | + | VERIFIED | One index takes its prior swing extreme, the other does not; bodies; qualifier only; decoupling = skip | `smt_price` body \| wick; `smt_tf` | smt |
| L10 | Event Horizon | + | VERIFIED | 50% between two consecutive same-side pools; partial/add point; close beyond = next pool likely | `eh_variant` two_pools \| two_gaps \| ifvg_wick | event-horizon |
| L11 | TGIF retracement levels | + | VERIFIED | One-directional week: 20/25/30 (40)% retrace of the weekly range, Thu 13:00 -> Fri close | `tgif_levels`, `one_dir_thr` | tgif-weekly-profile |

## PD arrays (entries / reaction zones)
| # | Level | Src | Status | Operational definition (v1) | Variant/Param | Card |
|---|---|---|---|---|---|---|
| P1 | Fair Value Gap (FVG, BISI/SIBI) | U | VERIFIED | Bullish `low[0] > high[2]`, zone [high[2], low[0]] incl. adjacent VI; respected while bodies stay in near half; body close beyond far edge = failed | `fvg_min_ticks` 4; `fvg_box`; `entry_price` near_edge \| ce; `respect_test` | fvg |
| P2 | Inversion FVG (IFVG), reclaimed FVG | U | VERIFIED | FVG whose far edge is closed through by one body; then bodies stay in the half nearest the new direction | `ifvg_mode` one_close \| retest_close \| liq_first \| used_first | ifvg |
| P3 | Balanced Price Range (BPR), shadow | U | VERIFIED | Overlap of a bullish and a bearish FVG within 10 bars; zone = overlap | `bpr_variant` fvg_overlap \| outer \| two_way_vi \| range_two_way | bpr |
| P4 | Volume imbalance (VI) | + | VERIFIED | Body-to-body gap >= 1 tick with wick overlap; open until a later body spans it; weakest array | `vi_min_ticks` | volume-imbalance |
| P5 | NDOG / NWOG | + | VERIFIED | NDOG 16:59 close -> 18:00 open (Mon-Thu, labelled next day, keep 5); NWOG Fri 16:59 -> Sun 18:00 (keep 5 weeks); CE key | `nwog_anchor` fri_1659 \| fri_rth_1615 \| body_close \| rth; quarters if >= 20 handles | ndog-nwog |
| P5b | RTH Opening Range Gap (ORG) | + | VERIFIED | Prior 16:14-bar close (RTH settle) -> 09:30 open on RTH data; CE draw in 09:30-10:00 (70% = hypothesis) | `org_min_handles` 20; bands 75/120; `org_keep` 5 | opening-range-gap |
| P5c | First Presented FVG (FPFVG) | + | VERIFIED | First displacement 1m FVG with candle 1 at 09:31+ (and per window: 07:00, 10:00, 13:30, Asia, London); not inside BPR | `fpfvg_min_ticks` 40 NQ; `fpfvg_mode` plain \| displacement \| reflection | first-presented-fvg |
| P6 | Order Block (OB) | U | VERIFIED | Run of consecutive opposite-close candles before the move; key = open of first candle; validated by trade-through of that open; MT = 50% of bodies; close beyond MT = failed | `ob_key_open` first \| lowest_open \| largest_body \| last; `ob_validation` | order-block |
| P7 | Breaker Block (+ unicorn) | U | VERIFIED | H1, L, H2 > H1 (sweep), break below L; zone = bodies of the down-close run at L; fails on close beyond MT; unicorn = overlaps FVG | `brk_mode` trade \| close; `breaker_zone` bodies \| full_range | breaker |
| P8 | Mitigation Block | U | VERIFIED-low | As breaker but H2 < H1 (no sweep); target-only in v1 | `mb_use_as_entry` false | mitigation-block |
| P9 | Rejection Block (+ bolo) | + | VERIFIED | Body edge of the swing-extreme candles; zone body edge -> wick extreme; stop anchor / first partial | `rb_variant` body_edge \| equal_lows_close \| ob_close | rejection-block |
| P9b | Wick CE (wick as gap; gray pool, obsidian) | + | VERIFIED | Wick from body edge to extreme, graded 0/25/50/75/100; bodies on the correct side of CE | `wick_anchor` body_edge \| full_range; `wick_min_atr` 0.5 | wick-ce |
| P10 | Propulsion Block | + | VERIFIED | OB-direction candle that dips into an older OB without body close beyond its MT, then launches | `prop_bars` 3; `require_parent_tethered` | propulsion-block |
| P11 | Liquidity Void | + | VERIFIED-low | No prints between two consecutive bars (`low[0] > high[1]`) + session gaps; DRAFT multi-bar run kept as legacy variant | `void_variant` true_void \| legacy_run | liquidity-void |
| P12 | Suspension Block | + | VERIFIED | One candle with a VI on both sides; box = outer VI edges; CE = bias pivot | `vi_min_ticks` | suspension-block |
| P13 | Immediate Rebalance | + | VERIFIED-low | Candle 3 refills exactly to candle 1's extreme (no FVG), price continues | `ir_variant` refill_to_c1 \| body_retrace \| daily_wick_ce | immediate-rebalance |

## Structure & context
| # | Concept | Src | Status | Operational definition (v1) | Variant/Param | Card |
|---|---|---|---|---|---|---|
| S1 | Market Structure Shift (MSS) | U | VERIFIED | After a raid, displacement trades through the nearest opposing 3-bar swing | `mss_mode` trade \| close; `mss_need_fvg` | mss |
| S2 | Change in State of Delivery (CISD) | U | VERIFIED | First trade through the open of the first candle of the delivering series (no close) | `cisd_anchor` series_first_open \| last_candle_open \| wick_extreme \| venom_close; `cisd_mode` | cisd |
| S3 | Premium / Discount, dealing range | U | VERIFIED | EQ = 50% of the chosen range; longs/adds at/below EQ, shorts at/above | `pd_range` leg \| entry_to_draw \| box20 \| session | premium-discount |
| S4 | Optimal Trade Entry (OTE) | U | VERIFIED | 62-79% retrace of the shift leg, 70.5 sweet spot, body anchors; variant entry only | `ote_band` 62-79 \| 62-70 \| 62-72 | ote |
| S5 | Displacement | + | VERIFIED-low | Proxy: body >= 1.0 x ATR(14), close in outer 30%, leg <= 3 bars leaving an FVG | `disp_body_atr`, `disp_close_pos`, `disp_leg_atr` | displacement |
| S6 | Swing points (STH/ITH/LTH) | + | VERIFIED | 3-bar fractal; ITH/LTH by nesting | `swing_price` wick \| body | swing-points |
| S7 | Dealing range / IPDA lookbacks; 20-day box | + | VERIFIED | Last 20 completed daily candles graded in quadrants; PD arrays expire after 20 (40/60) days | `box_days` | premium-discount |
| S8 | SD / fib projections | + | VERIFIED | Multiples -0.5/-1/-1.5/-2/-2.5 of a reference range beyond its broken extreme; target only with convergence | `sd_ref`, `sd_anchor`, `sd_conv_ticks` | sd-projection |
| S9 | Gradient levels / tethering | + | VERIFIED | Quadrants (octants) on anchor ranges; array tethered if its key candle/edge/CE is within 2 ticks of a level | `grid_n`, `tether_ticks`, `grid_anchors`, `tether_as_filter` | gradient-levels |

## Time & bias
| # | Concept | Src | Status | Operational definition (v1) | Variant/Param | Card |
|---|---|---|---|---|---|---|
| T1 | Killzones, Silver Bullet, lunch, news gates | + | VERIFIED | London 02:00-05:00; NY AM 07:00-11:00 (setup window 07:00-10:00); SB 10:00-11:00 / 14:00-15:00; lunch 11:30-13:30; no entries into 08:30/10:00/14:00 prints | `lunch_window`; `news_wait_min` 15; `fomc_no_entry_before` 14:40 | macros-time-windows |
| T2 | Power of 3 / AMD / Judas | + | VERIFIED | Accumulate near the open, manipulate against bias beyond it within ~30 min, distribute to the far extreme | `judas_max_min`; anchors | power-of-3 |
| T3 | Range SD projections (pre-news, 07-09, OR, ORG, MOR) | + | VERIFIED | See S8; CBDR is not taught in any series (dropped) | `sd_ref` | sd-projection |
| T4 | Weekly profiles / TGIF / day-type gates | + | VERIFIED | Bullish week low Sun-Wed AM; Thursday opposite extreme; TGIF 20-30%; large-range-day next AM skip; NFP-week Thu/Fri skip | `weekly_open`; day-type flags | tgif-weekly-profile |
| T5 | Macros | + | VERIFIED | xx:50 -> xx+1:10 every hour; plus 15:15-15:45 and MOC 15:45-16:00; 08:30 half-hour algo | `macro_filter` on/off; `macro_set` all_hours \| named_only | macros-time-windows |
| T6 | Session phase (consolidation / expansion / retracement / reversal) | U | VERIFIED-low | Per window: range vs expected range and overlap; see classifier in card | `cons_k`, `exp_k` | session-ranges |

## MMXM link
The model lives in `kb/mmxm-spec.md`; every card above has a "Role in MMXM" section. Decisions only the user can make are in
`kb/open-questions.md`.
