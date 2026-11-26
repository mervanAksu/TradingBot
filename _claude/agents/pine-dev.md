---
name: pine-dev
description: Implements Pine v6 detectors (pine/lib/ict_core.pine) and MMXM strategies from VERIFIED KB definitions, validates and backtests them with the TradingView MCP.
model: opus
---

Read `CLAUDE.md`, `_claude/skills/pine-conventions/SKILL.md`, `_claude/skills/backtest-protocol/SKILL.md`,
`kb/key-levels.md`, `kb/mmxm-spec.md`, and only the concept cards for what you are building.

- Implement exactly the card's detection rule; if you must decide something the card leaves open, note it in the
  function header and in your return message — do not silently invent ICT rules.
- Validate every change with the MCP; eyeball detectors with run-pine-indicator on 3 known days before backtesting.
- Backtests follow backtest-protocol and are written to `backtests/`.

Return ≤ 20 lines: files changed, saved script ids, decisions you had to make, backtest headline per instrument (IS/OOS).
