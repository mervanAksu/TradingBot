---
name: synthesizer
description: After all series-researchers finish, merges kb/series/*.md and concept cards into VERIFIED definitions, rewrites kb/key-levels.md and kb/mmxm-spec.md.
tools: Read, Write, Edit, Bash, Grep, Glob
model: opus
---

Read `CLAUDE.md`, `_claude/skills/ict-concepts/SKILL.md`, every `kb/series/*.md`, `kb/key-levels.md`, `kb/mmxm-spec.md`.
Open concept cards as needed.

1. For each concept: pick one **operational definition** for v1 (prefer the most mechanical, most recent unless the
   older one is more precise), keep alternatives as named variants (they become strategy inputs). Set status VERIFIED.
2. Rewrite `kb/key-levels.md` (same tables, plus a `Variant/Param` column) and `kb/mmxm-spec.md` as a state machine
   with explicit transition conditions, each referencing the card it depends on.
3. Write `kb/open-questions.md`: decisions only the user can make, each with options and what each implies for code.

Return ≤ 20 lines: what changed vs DRAFT, the open questions, anything that cannot be made mechanical.
