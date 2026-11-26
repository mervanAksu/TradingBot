# MMXM v1 — first backtest attempt (2026-11-25)
Script: `ICT MMXM v1 (test)` saved PRIVATE as `USER;c36a84019d7b42ba97478a6ba589a4c6` v1.0 (compiles; 1 warning: ta.sma in conditional — fixed locally).

| Run | Symbol / TF | Range | Overrides | Trades |
|---|---|---|---|---|
| 1 | NQ1! 5m | 2026-10-04 → 2026-11-25 | defaults | 0 |
| 2 | NQ1! 15m | 2026-05-31 → 2026-11-25 | defaults | 0 |
| 3 | NQ1! 15m | same | HRLR off | 0 |
| 4 | NQ1! 15m | same | HRLR, macro, zone, flat off | 0 |
| 5 | NQ1! 15m | same | OC box 3.5xATR, HRLR off, macro off | 0 |
| 6 | NQ1! 15m | same | margin long/short 0 | 0 |

Funnel debug indicator (sell side, same core logic, NQ 15m, full history): OC box bars 14, departures 13, raids 14, confirmed 12,
limit price at confirmation 7, bars with a valid order 17, valid bars that traded through the limit 7.
=> The model logic produces setups, but the strategy places/fills none. Suspects (to check offline, not by burning quota):
strategy-only code path (order placement/cancel sequencing, exits issued before fill), or a silent runtime error.
Also: OC-A box with 2.0 x ATR is extremely rare on 15m (14 bars in ~6 months) — default must be loosened.

Data depth (MCP, user plan): 1m from 2026-11-08, 5m from 2026-10-04, 15m from 2026-05-31. Deep Backtesting (date_from) untested.
No results to report yet — nothing about edge can be concluded.
