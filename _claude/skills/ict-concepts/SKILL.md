---
name: ict-concepts
description: Use whenever a task in this project mentions any ICT term (FVG, OB, breaker, MSS, CISD, OTE, MMXM, killzone, SMT, liquidity, premium/discount...). Points to the project's knowledge base so concepts are looked up, not re-derived.
---

# ICT concepts — lookup first

1. Open `kb/key-levels.md` (index + one-line definitions + status) and, for the model, `kb/mmxm-spec.md`.
2. For detail, open only the card you need: `kb/concepts/<concept>.md` (kebab-case, e.g. `fair-value-gap.md`).
3. If the card is missing, create it from `kb/concepts/_TEMPLATE.md`; do not explain the concept in chat instead.

## Status meaning
- DRAFT: from prior knowledge, not sourced. Never code a DRAFT definition without flagging it.
- SOURCED: has transcript refs. VERIFIED: synthesizer resolved conflicts. CODED: has a Pine detector in `pine/lib/`.

## Rules for writing cards
- Own words. A transcript quote is at most a short phrase and always carries `series/file@mm:ss`.
- Every definition ends in a **detection rule** precise enough to code (bar indices, comparisons, parameters with defaults).
- When series disagree, record both under "Evolution across series" — do not silently pick one.
- Anything a coder would have to guess goes under "Ambiguities".
