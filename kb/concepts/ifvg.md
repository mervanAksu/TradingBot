---
concept: Inversion Fair Value Gap (IFVG)
aliases: [inverse FVG, inverted FVG, reclaimed FVG (reverse case), reaper (IFVG+breaker)]
status: VERIFIED
confidence: high
category: pd-array
series_seen: [foundations, 2023, 2024, 2025, 2026, price-action-chronicles, trade-executions]
default_variant: one body close through the far edge
---

## Definition (own words, 2-4 sentences)
An FVG that failed: a candle body closed through its far edge, so the zone flips polarity and is used from the other side.
After inversion the bodies should stay in the half nearest the new direction (bearish IFVG: lower half). A wick-only breach
does not invert. If price later closes back through it and holds, it is "reclaimed" and resumes its original role.

## Detection rule
```
inputs: active FVG zones (fvg.md)
bearish IFVG from bullish FVG z: first bar i after creation with close[i] < z.bottom  (body close through)
bullish IFVG from bearish FVG z: close[i] > z.top
variant ifvg_mode:
   "one_close"   (default): inversion at bar i
   "retest_close": after one_close, require a return into z and a second close beyond the far edge (trade-executions b01/059@11:25)
   "liq_first"  : require that opposing liquidity was taken before the inversion (2023-b07/078@50:29)
   "used_first" : require that z was respected at least once in its original polarity (2026-b05/085@33:47)
after inversion (bearish): valid while no close > z.ce (bodies stay in lower half); wick to ce allowed
confirm (optional, 2026 sequence): a later close below z.ce after the retest
reclaimed: close > z.top after inversion -> z returns to original (bullish) role
output: zone{top,bottom,ce,dir=new_dir,inverted_at,quality}
quality ladder (bearish): A = never returns; B = returns only to near edge; C = wick to CE, bodies in lower half; D = body enters upper half w/o close above top
```

## Parameters
| name | default | range | ref |
|---|---|---|---|
| ifvg_mode | one_close | one_close, retest_close, liq_first, used_first | trade-executions b02/065@15:30; 2026-b05/082@03:34 |
| half_rule | close beyond CE = fail | ce, far_edge | 2025-b03/012@08:22; 2026-b09/119@23:19 |
| entry | near edge / CE on retest | near, ce | 2023-b07/078@50:29; 2025-b04/053@32:22 |
| stop | beyond far edge +1 tick or beyond CE | far, ce | price-action-chronicles b01/007@11:55; 2025-b04/053@32:22 |
| allow_no_retest_entry | false | bool | 2024-b13/045@39:59 (no criterion given) |

## Invalidation / mitigation
- Bearish IFVG fails on a close above its CE (strict) or top (loose); on close above top it is "reclaimed".

## Role in MMXM
- Primary confirmation component (score) of SMR: rally arrays flipping to IFVG (2026-b05/082@03:03).
- Low-risk entry: retest of the inversion gap CE (2025-b01/002@132:08 "invariant"; 2026-b04/067@19:09).
- Re-entry after a stop inside a model (2024-b07/020@10:16).

## Evolution across series
- foundations: first session FVG inverts on close-through, used as target (b02/002@30:41).
- 2023: requires opposing liquidity taken and far-edge pierce; need not be retested.
- trade-executions/PAC: one close; optional retest + second close.
- 2024/2025: half-rule after inversion; "reclaimed" named.
- 2026: body close mandatory (contrast with OB where trade-through suffices); prior utilisation; AAA ladder.

## Ambiguities (open questions for the user)
- Whether to require prior utilisation (`used_first`): changes the IFVG count a lot. Test as variant.

## Refs
- `2026-b09/116@55:36` body close needed, wick does not invert.
- `2026-b02/027@12:55` reclaimed-IFVG quality ladder.
- `2024-b10/033@43:43` inversion FVG fails on body close through far side.
- `price-action-chronicles b01/004@16:59` close above wick CE then IFVG within 2 candles.
