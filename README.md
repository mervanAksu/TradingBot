# TradingBot — ICT / MMXM research bot

Rule-based research strategy built on ICT concepts with the **Market Maker Buy/Sell Model (MMXM)** at its core,
tested on **NQ** and **ES** futures (TradingView, Pine Script v6). Research and backtesting only — no live orders,
no broker integration, not financial advice.

## Layout
| Path | Content |
|---|---|
| `CLAUDE.md`, `_claude/` | project rules, skills and agent prompts used to build the project |
| `kb/` | knowledge base in our own words: series digests, concept cards, `key-levels.md`, `mmxm-spec.md` |
| `pine/lib/` | Pine v6 detector libraries (`ict_core`, `ict_time`) |
| `pine/indicators/` | `mmxm_v2` (liquidity rays, OC, SMR score, phase engine), `ict_dr_dol`, levels viewer |
| `pine/strategies/` | `mmxm_v2.pine` v3.1 — HTF bias, nested premium/discount filter, dynamic % risk sizing |
| `backtests/` | one report per backtest round |
| `scripts/` | transcript download + cleaning helpers |

Transcripts are not part of the repository (see `.gitignore`); `scripts/` shows how they were produced locally.
