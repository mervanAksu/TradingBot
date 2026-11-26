---
name: pine-conventions
description: Use when writing or changing Pine Script in pine/ for this project, and before validating, saving or backtesting it with the TradingView MCP.
---

# Pine conventions

- Pine **v6**. Detectors live in one library `pine/lib/ict_core.pine` (exported functions + UDTs); strategies import it.
  Mirror every saved TradingView script into the repo file of the same name — the repo is the source of truth.
- One detector per concept, named after its card: `fvg()`, `orderBlock()`, `breaker()`, `mss()`, `cisd()`, `sessionHL()`...
  Each returns a UDT `Zone {top, bottom, ce, dir, t_created, t_end, mitigated}` or `Level {price, kind, t}`.
  Header comment of each function: card path + status + parameter defaults.
- **No lookahead / repaint**: `request.security(..., lookahead = barmerge.lookahead_off)` on confirmed HTF bars only
  (`[1]` offset pattern); act on `barstate.isconfirmed`; swing points are known only `right` bars after the pivot — account for it.
- Times via `time(timeframe.period, "0200-0500", "America/New_York")`; never hard-code UTC offsets.
- Strategy settings explicit in code: `commission_type=strategy.commission.cash_per_contract`, `commission_value`,
  `slippage` (ticks), `process_orders_on_close=false`, `calc_on_every_tick=false`, `pyramiding=0`.
- Inputs grouped: `Context`, `Levels`, `Entry`, `Risk`, `Time`. Every magic number is an input.
- Workflow with the MCP: validate (`mcp-tv-validate-pine-script`) → fix → save → `mcp-tv-run-pine-indicator` to eyeball
  detector output on a few known days → only then `mcp-tv-run-pine-backtest`.
- Keep files under ~400 lines; split helpers into the library.
