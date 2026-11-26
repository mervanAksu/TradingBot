---
concept: Market Maker Buy/Sell Model (MMXM)
aliases: [MMBM, MMSM, market maker model, buy/sell side of the curve, SMR, low-risk buy/sell, 1st/2nd stage]
status: VERIFIED
confidence: medium
category: model
series_seen: [foundations, 2022, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: see kb/mmxm-spec.md (state machine)
---

## Definition (own words, 2-4 sentences)
A fractal price-delivery template. Sell model: an original consolidation (OC) forms; price runs away from it upward in one or
two stages (buy side of the curve) and takes buy-side liquidity at a higher-timeframe premium array (smart money reversal,
SMR); delivery flips, a low-risk sell forms on the retest of the first broken array, and price returns down in two stages
(first-stage distribution, retracement = re-distribution, second-stage distribution, usually the fastest leg) to the OC low or
the main sell-side draw. The buy model mirrors it.

## Detection rule
```
Implemented as the state machine in kb/mmxm-spec.md. Components used:
OC detector (proxies in spec), swing-points.md, relative-equal-hl.md, turtle-soup.md (SMR raid),
confirmation score: cisd.md, ifvg.md, mss.md, order-block.md (validation), breaker.md, smt.md, displacement.md
entries: ifvg.md / fvg.md / first-presented-fvg.md / order-block.md / breaker.md (unicorn) / ote.md (variant)
gates: macros-time-windows.md, session-ranges.md (phase classifier), hrlr-lrlr.md, premium-discount.md, gradient-levels.md
targets: re-accumulation/re-distribution levels, event-horizon.md, sd-projection.md, OC, HTF draw
```

## Parameters
- See `kb/mmxm-spec.md` parameter table.

## Invalidation / mitigation
- Sell model: body close above the SMR extreme, or above the capping array (IFVG/premium wick CE) that defines the reversal.

## Role in MMXM
- This is the model.

## Evolution across series
- foundations/2022: only implicit (raid -> MSS -> retrace -> opposite pool). 2023: buy-model stage list in prose.
- 2024: sell model walk-through (024): OC with EQL base, two up stages, SMR = turtle soup of EQH, low-risk sell at OB, 1st and 2nd distribution, target HTF array; buy model need not revisit OC.
- 2025: only geometric statement (b01/002): SMR = raid; pivot = open of raid candle (one tick); low-risk entry = IFVG or first FVG; stage 1 = next OB+FVG to 70.5%; stage 2 = first retrace into an inefficiency; never trade back through stage-2 swing.
- 2026: fixed vocabulary on many hand-labelled charts; any stage may be entered; exit may stop short of OC; any TF.

## Ambiguities (open questions for the user)
- No numeric stage boundaries anywhere; see kb/open-questions.md Q1-Q3.

## Refs
- `2024-b08/024@170:31` OC tidy box with equal lows.
- `2025-b01/002@101:04` raid-candle open as pivot.
- `2026-b04/072@17:34` entry at any stage.
