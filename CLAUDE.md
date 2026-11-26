# ICT-Bot — Project Rules

Goal: a rule-based trading strategy built on ICT concepts with the **MMXM (Market Maker Buy/Sell Model)** at its core,
tested only on **NQ** and **ES** futures via the TradingView MCP. Discretionary ideas must become explicit,
testable rules before they reach code.

## Language
- The user writes Turkish: talk to them in Turkish. Files, code, comments and KB cards are in English (ICT terms stay as-is).

## Layout
```
_claude/skills/, _claude/agents/   skills + agent prompts (remote tools cannot write .claude/; rename to .claude to auto-load in Claude Code)
transcripts/<series>/*.vtt   raw subtitles (user-downloaded, local only, never published or quoted at length)
transcripts/_clean/<series>/*.txt   output of scripts/clean_vtt.py (what agents actually read)
kb/series/<series>.md        per-series digest (what that series teaches, how it changed definitions)
kb/concepts/<concept>.md     one card per concept, from kb/concepts/_TEMPLATE.md
kb/key-levels.md             master list of key levels + status (DRAFT / VERIFIED / CODED)
kb/mmxm-spec.md              the MMXM state machine that the strategy implements
pine/lib/                    Pine v6 library (detectors), pine/strategies/ (strategies)
research/                    Python notebooks/scripts on OHLCV pulled from the MCP
backtests/<date>-<name>.md   one report per backtest run (protocol: backtest-protocol skill)
```

## Token discipline
- Agents read `transcripts/_clean/`, never raw `.vtt` (auto-subs repeat every line 2-3x).
- Read a KB card before re-deriving a concept; update the card instead of explaining it again in chat.
- Read `kb/key-levels.md` and `kb/mmxm-spec.md` first in any strategy/coding task; they are the source of truth.
- Pull OHLCV with `format="columns"`; use `summary=true` when only stats are needed. Save pulled data to `research/data/` and reuse it.

## Copyright
- KB content is written in our own words as operational definitions. Quote a transcript at most a short phrase,
  always with a `file@mm:ss` reference. Never paste transcript passages into the KB, code or artifacts.

## Instruments (TradingView)
| | Symbol | Tick | $/point | Micro |
|---|---|---|---|---|
| NQ | `CME_MINI:NQ1!` | 0.25 | 20 | MNQ $2/pt |
| ES | `CME_MINI:ES1!` | 0.25 | 50 | MES $5/pt |
- MCP OHLCV includes overnight (ETH) bars despite the "regular session only" notice (checked 2026-11-24 on 1h). 1m history ≈ 5000 bars/page; page back with `date_to=next_date_to`.
- CME daily maintenance break 17:00-18:00 New York.

## Time (always America/New_York)
| Window | Time (NY) |
|---|---|
| Asia session (range) / Asia killzone | 18:00-00:00 / 19:00-21:00 (VERIFIED 2024, 2026) |
| Midnight open | 00:00 |
| London session / killzone | 02:00-05:00 |
| NY AM killzone | 07:00-10:00 (later content: 08:30-11:00) |
| 8:30 open (news) | 08:30 |
| RTH open | 09:30 |
| NY lunch (lunch macro) | 11:30-13:30 (VERIFIED 2024-2026; no-new-trades core 12:00-13:00) |
| NY PM session | 13:30-16:00 |
| Macros (user's preferred entry windows) | xx:50-xx+1:10, every hour (VERIFIED); plus 15:15-15:45 and MOC 15:45-16:00 |
| ORG settle (RTH last print) | close of the 16:14 1m bar (RTH ends 16:15) → 09:30 open (VERIFIED) |
| Silver Bullet | 03:00-04:00, 10:00-11:00, 14:00-15:00 |
These are working defaults; the series digests may refine them (record the change in the concept card).

## Workflow (orchestrator = main session)
1. `scripts/clean_vtt.py` → `transcripts/_clean/`.
2. One `series-researcher` agent per series → `kb/series/<series>.md` + concept-card updates.
3. `synthesizer` agent → resolves cross-series conflicts, writes `kb/key-levels.md`, `kb/mmxm-spec.md`.
4. `pine-dev` agent → detectors + strategy, validated with the MCP.
5. `verifier` agent (has NOT seen the build) → checks code against spec and backtest numbers against raw data.

## Hard limits
- No live orders, no broker/API keys handled by Claude. Output is signals, alerts, backtests.
- No "buy/sell this" advice to the user; report results and trade-offs.
