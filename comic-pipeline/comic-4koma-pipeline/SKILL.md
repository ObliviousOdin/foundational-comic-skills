---
name: comic-4koma-pipeline
version: 1.0.0
category: comic-pipeline
description: End-to-end pipeline for 4-koma (yonkoma) vertical strips and 2×2 grid pages. Pairs the 4koma-vertical format with kishōtenketsu beat structure under full direction and consistency control.
---

# Comic 4-Koma Pipeline

**Purpose**: The production workflow for four-panel vertical strips — the kishōtenketsu-native format — and its 2×2 grid variant.

## When to Use

- Gag strips, slice-of-life serials, and contemplative humor in manga-family styles
- When the story's twist is a recontextualization (*ten*), not a conflict resolution
- Serialized social formats where a tall single image outperforms a wide one

## Pipeline Flow

1. **Producer**: contract locks `4koma-vertical` (or `2x2-grid-page`) + `kishotenketsu` (or `gag-escalation`) + one manga-family style; greenlight checklist passes
2. **Load**: `comic-core`, `comic-consistency` (World Bible + character + style memory), locked style skill
3. **Director shot plan**: map *ki / shō / ten / ketsu* to the four equal panels; equal panel heights mean **pacing comes from content** — vary shot size and silence, not panel size; *ten* is often strongest as the silent panel
4. **Process**: extract cues via World Bible → resolve character DNA → apply style rules + style memory → generate via `comic-image-generation-adapter`
5. **Director final cut**: flow-first review; verify the *ketsu* reconciles rather than explains
6. **Quality gates**: full `comic-quality-gates` run against the locked format (4 panels, vertical column, top-to-bottom)
7. **Output**: final image + shot plan + consistency log; Producer records the episode in the production state

## Format-Specific Rules

- Four panels of **equal height** — the 4-koma constraint is the discipline
- Uniform horizontal gutters; reading strictly top to bottom
- 0–2 bubbles per panel; the *ten* panel earns silence more often than not
- Grid variant: obey the T-rule (no perfect "+" intersection), Z-path reading

## Integration

- Consumes `comic-format-library` (`4koma-vertical`, `2x2-grid-page`) and `comic-narrative-patterns` (`kishotenketsu`, `gag-escalation`)
- Commanded by `comic-producer`; every strip planned and cut by `comic-director`

---

*Four equal boxes, one unequal idea — that is the whole art of 4-koma.*
