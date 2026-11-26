# MMXM v2 strategy — first backtest (2026-11-26)
Script: `ICT MMXM v2 strategy` PRIVATE `USER;ffb2118daff34a098fb073bb11bc7718` v2.0 (file pine/strategies/mmxm_v2.pine).
Indicator `ICT MMXM v2` updated to v2.0 (`USER;127678405e174280aac9152bfa074d55`), compiles.

## v1 zero-trade bug
v2 hit a runtime error on first run: `strategy.entry` reused one id ("E") for long and short. The MCP backtest returns an
empty report on some runtime errors, which is the most likely cause of v1's 0 trades (v1 also mixed order/exit sequencing).
Fix: separate ids L / S, cancel the opposite id before placing. v1 is retired.

## Defaults
OC = 07:00-09:30 session window or EQ cluster; SMR raid in HTF (4H, 20 bars) premium/discount; score >= 3.0
(C CISD 2, I IFVG 2, M MSS 1.5, S SSMT 1.5, P point SMT 1.5, H HTF quadrant 1, m macro 0.5, T SMR window 0.5);
entry = IFVG retest limit if IFVG fired else market; stop = SMR extreme + 2 ticks; 4 contracts: TP1 2 at nearest opposite
ray >= minRoom, TP2 1 at OC near edge, runner 1 at OC far edge; stop to entry after TP1; phase gate on; macro filter off;
flat 15:55 NY; commission $2.50/contract/side, 1 tick slippage. Counts below are exit legs (one trade = up to 3 legs).

| Run | Period | Legs | Win% legs | PF | Net ($) | Long PF / net | Short PF / net | Max DD ($) |
|---|---|---|---|---|---|---|---|---|
| NQ1! 15m | 2026-06-02 → 11-26 | 345 | 11.6 | 0.70 | -73,640 | 0.39 / -112,475 | **1.65 / +38,835** | 133,425 |
| NQ1! 5m | 2026-10-05 → 11-26 | 225 | 16.4 | 0.81 | -28,380 | 0.52 / -56,825 | **1.84 / +28,445** | 48,515 |
| ES1! 15m (SMT vs NQ, minRoom 4) | 2026-06-04 → 11-26 | 303 | 16.8 | 0.70 | -24,265 | 0.53 / -23,395 | 0.97 / -870 | 33,615 |

Buy & hold over the same windows: NQ -85k (15m) / -94k (5m) per 4 contracts, ES -17.5k → strongly bearish sample.

## Findings
1. Shorts (MMSM) are profitable on NQ in both TFs (PF 1.65-1.84, avg win ~10x avg loss); longs (MMBM) lose everywhere.
   In a falling market this is expected — the bot has no HTF bias / draw-on-liquidity filter yet. Direction filter is the
   first fix (DOL / daily order flow), not parameter tuning.
2. Many losses exit on the entry bar with 2-10 point risk: stop just beyond the SMR extreme + market entry is too tight
   for 5m/15m noise. Next: entry only at the IFVG/FVG retest (no market fallback), stop beyond the entry array or
   >= 0.5 x ATR, and use bar magnifier for honest intrabar fills.
3. Win rate is low but payoff is high (runner to OC far side) — the model's edge, if any, is in the runner.
4. Sample is small (≈ 40-115 trades per run, one regime). Nothing here is significant; no OOS split possible with this depth.

## Next experiments (one change at a time)
- A: HTF bias filter (trade only toward the DOL / 4H-1D structure) → expect long side to stop bleeding.
- B: limit-only entries + min stop 0.5 x ATR + bar magnifier.
- C: macro filter on; confMin 4.0; score-bucket report (needs more trades → MT5 CFD history for research).

## Round 2 (same day, script v3.0) — NQ1! 15m, 2026-06 → 11-26
New inputs: HTF bias = daily structure (close beyond last daily swing, pivot 2); counter-trend trades capped at 2R
(all exits <= entry ± 2 x risk); entry type (limit-only = IFVG retest or first FVG after SMR, no market); min stop 0.5 x ATR.

| Run | Change vs baseline | Legs | Win% | PF | Net ($) | Long PF / net | Short PF / net | Max DD |
|---|---|---|---|---|---|---|---|---|
| Baseline v2.0 | — | 345 | 11.6 | 0.70 | -73,640 | 0.39 / -112,475 | 1.65 / +38,835 | 133,425 |
| **A** | + HTF bias, CT capped at 2R (market entries allowed, no min stop) | 224 | 21.9 | **0.95** | **-9,670** | 0.59 / -59,915 | **2.11 / +50,245** | 107,685 |
| B | A + limit-only entries + min stop 0.5 ATR | 63 | 36.5 | 0.63 | -34,450 | 0.34 / -49,865 | 1.83 / +15,415 | 60,105 |
| C | B + macro filter + score >= 4.0 | — | — | — | not run (TradingView daily quota) | — | — | — |

Reading:
- A is the clear improvement: the bias filter plus the 2R cap cut the loss by ~87% and lifted shorts (with-trend in this
  sample) to PF 2.1. Longs are still the whole problem: they were mostly counter-trend in a falling market.
- B made it worse: limit-only removed ~70% of trades and the wider minimum stop doubled the average loss
  (avg loss 2,348 vs 1,085) without raising the payoff enough. Keep market entries for now; revisit the stop as
  "beyond the entry array" rather than an ATR floor.
- Next: C on top of A (not B); A with counter-trend = Skip; same on ES1! 15m and NQ1! 5m.
