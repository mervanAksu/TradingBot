---
name: backtest-protocol
description: Use before running or reporting any backtest of a strategy in this project (NQ/ES), so every run is comparable and honest.
---

# Backtest protocol

## Fixed assumptions (change only with the user's OK, and note it in the report)
- Instruments: `CME_MINI:NQ1!`, `CME_MINI:ES1!`, both always — a result on one only is not a result.
- Costs per side: commission $2.50/contract; slippage 1 tick on NQ and ES (2 ticks for stop orders in news minutes).
- Size: 1 contract; report in points and $ (NQ $20/pt, ES $50/pt).
- Continuous contract `1!`: be aware of roll gaps; note any trade spanning a roll date.

## Data split
- In-sample (IS): oldest ~70% of the available history at the execution TF. Out-of-sample (OOS): newest ~30%, touched
  **once** per strategy version. Parameter tuning happens on IS only.
- Prefer few parameters; any parameter tuned must be listed with the grid tried.

## Report: `backtests/<YYYY-MM-DD>-<strategy>-<version>.md`
- Config (TFs, sessions, entry/stop/target rules, params, Pine file + saved script id).
- Per instrument, IS and OOS: trades, win rate, avg R, profit factor, expectancy ($ and R), max drawdown, longest losing
  streak, trades/week, % of trades per session window.
- 5 sample trades with timestamps (NY) so the user can check them on the chart.
- Verdict section: what is robust, what is likely overfit, next experiment. No buy/sell advice.

## Red flags (stop and report instead of "improving" the number)
- < 30 OOS trades; IS→OOS profit factor drop > 40%; results driven by < 5 trades; any lookahead suspicion.
