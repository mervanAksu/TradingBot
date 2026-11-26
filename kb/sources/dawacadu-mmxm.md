# MMXM as read from Dawacadu (@Dawacadu_SMC) — study notes (2026-11-25)

Source: public X posts of @Dawacadu_SMC (self-described ICT mentee), ~136 posts scanned (Jul 2024 – Jul 2026), ~10 NQ/ES
MMXM charts studied in detail. Own-words operational summary; no images or long quotes copied.

## Cases studied (instrument, date, labels on the chart)
| Post | Setup | OC | Left-side stage(s) | SMR | Right-side stage(s) | Draw |
|---|---|---|---|---|---|---|
| NQ 2026-07-31 "Pre-session MMSM" | sell | 08:30–09:00 box (between overnight high and Asian-range low) | 09:00–09:30 rally | 09:30–09:35 run above overnight high (buy-side liquidity) | fast leg down | Asian-range low (sell-side) |
| NQ 2026-05-13 "2nd stage MMBM of HTF MMBM" (2m) | buy | premarket 04:30–07:30 range ("Original Cons.") | 08:00–09:15 drop = "First Stage of Acc." | 09:30–10:00 opening range = "Smart Money Reversal" | 10:00–11:00 AM Silver Bullet = "2nd Stage" rally | OC high and beyond |
| same, 30m view | buy | prior-day range | "First Stage of Acc." | "Smart Money Reversal" | "First Stage of Dist.", "Second Stage of Dist." — 2nd-stage low shows **stage divergence (SMT) with ES** | — |
| ES 2026-06-09 "MMSM Daily Expansion" (1m) | sell | Asian range = "Original Cons." | Overnight session = "First Stage of Acc." | NY open / opening range = SMR | AM Silver Bullet = "Dist." | daily FVG lower quadrant / CE |
| NQ 2026-07-29 "Noon Reversal MMBM" (2m) | buy | 05:30–09:30 premarket "Origin" | 09:45–11:15 drop = "First stage of acc." | 11:30–12:15 noon = SMR | 12:30–15:00 = "Dist." | origin high |
| NQ 2025-11-10 "MMSM, Turtle Soup entry" (1m) | sell | 07:00–09:25 pre-session range | 09:30–10:00 expansion up | 10:15–10:40 turtle soup above relative equal highs + **SMT with ES** at the high | entry at bearish OB/FVG (~10:45), drop | pre-session range low = "Sellside liquidity / pre-session liquidity pool" (hit ~11:00) |

## The model as he uses it (generalised)
1. **Draw first.** A setup exists only if there is an area to distribute into: fractal equal / near-equal highs or lows,
   usually built in accumulation-profile windows (Asia, lunch, CBDR, pre-session). (2025-03-22 thread)
2. **Time-anchored phases.** The four MMXM legs map onto the clock (Quarterly/AMD logic):
   - OC = a completed consolidation window: Asian range, overnight/premarket range, pre-session 07:00–09:30, or the prior PM.
   - 1st stage (left side of the curve) = the next window (overnight/London, premarket 08:00–09:15, AM session for a noon model).
   - SMR = an execution window: NY open / 09:30–10:00 opening range, 08:30–09:30 pre-session, noon 11:30–12:30.
   - Right side ("Dist.", 2nd stage) = 10:00–11:00 AM Silver Bullet, or 12:30–15:00 after a noon reversal.
3. **Naming convention (important, differs from our spec):** consolidations on the curve **before** the SMR are
   "stages of accumulation", those **after** the SMR are "stages of distribution" — for both buy and sell models
   (time-sequence naming, like AMD), not "re-accumulation / re-distribution by direction".
4. **SMR = liquidity raid at a PDA + SMT.** Execution model (his words paraphrased): around a PDA, the swing that made the new
   high/low (an intermediate-term high/low, which must sit inside an FVG) gets broken; the reversal extreme must show
   **SMT divergence with the correlated index** (NQ vs ES). Turtle soup above relative-equal highs is the typical raid.
5. **Stage divergence:** the 2nd-stage pullback low (buy model) / high (sell model) also shows SMT vs ES — a second,
   lower-risk entry.
6. **Fractality:** an LTF full MMXM often forms inside the HTF model's 2nd stage ("2nd stage MMBM of HTF MMBM").
   Best markets = where an HTF (weekly/daily) model is in its 2nd stage.
7. **Fade the first move** in the direction of the bias near the opening price; it becomes the future breaker. The first
   expansion from a PDA usually fills an HTF FVG and marks an ITH/ITL.
8. **RTH gap narrative:** if the prior PM session was consolidation / range / first curve of an MMXM, use purge-and-revert
   (session high/low purge → target the opposite session high/low). NQ gap ideal 50–150 handles, ignore >250; read body
   closes / wick rejections at gap quadrants.
9. **Opening gaps create false narratives** for retail (chasing the gap); the engineered low-resistance liquidity left in
   the gap move is where smart money pairs orders later.

## What changes in our bot (v2.1)
- OC source: add **session-window OC** (default pre-session 07:00–09:30 NY; presets Asia, premarket, prior PM) besides
  the EQ-cluster OC; EQH/EQL inside the window raise quality.
- Stage labels: before SMR → "Acc. 1/2…", after SMR → "Dist. 1/2…".
- SMR score: add point **SMT vs ES at the raid** and an **SMR time-window** bonus (08:30–10:00, 11:30–12:30).
- Stage divergence: SMT at the 2nd-stage swing → mark as second entry.
- Draw: OC far side / session liquidity pool (unchanged default).
