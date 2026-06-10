---
name: comic-format-library
version: 1.0.0
category: comic-core
description: The sanctioned library of output formats — 3-panel horizontal (default), 4-koma vertical, webtoon scroll segment, single-panel gag, 2×2 grid page, and multi-page chapter — with aspect ratios, gutter rules, reading direction, and dialogue budgets.
---

# Comic Format Library

**Core principle**: One project, one format, locked in the contract. The 3-panel horizontal strip is the default — not the only option.

This library generalizes the structural contract so that vertical, gridded, single-panel, and multi-page work are first-class formats with the same discipline as the original strip — and so that scroll-native styles like `manhwa-color-webtoon` finally have a format that matches their Style Lock.

## When to Use

- During Producer brief intake, to match format to platform, style, and narrative pattern
- During Director shot planning, to apply the format's gutter, sizing, and flow rules
- When a style's native habitat conflicts with the default strip (webtoon → scroll; 4-koma gag → vertical column)

## The Format Library

### 1. `3-panel-horizontal` (Default)
- **Canvas**: one wide image, 16:9 or 21:9
- **Panels**: exactly 3, left to right (right to left if the contract sets RTL)
- **Gutters**: clean vertical gutters; width modulates pacing (wide before the payoff)
- **Native patterns**: `setup-reinforce-turnaround`, `gag-escalation`, `silent-strip`
- **Dialogue budget**: 1–2 bubbles per panel, ≤ ~8 words each
- **Pipeline**: `comic-3-panel-horizontal-pipeline`

### 2. `4koma-vertical` (Yonkoma)
- **Canvas**: one tall image, ~9:16 to 1:3; single column
- **Panels**: exactly 4, equal height, top to bottom
- **Gutters**: uniform horizontal gutters — pacing comes from content, not panel size (the 4-koma constraint)
- **Native patterns**: `kishotenketsu` (the historically correct pairing), `gag-escalation` (+1 reaction beat)
- **Dialogue budget**: 0–2 bubbles per panel, ≤ ~8 words; panel 3 (*ten*) is often strongest silent
- **Pipeline**: `comic-4koma-pipeline`

### 3. `webtoon-scroll-segment`
- **Canvas**: vertical scroll unit, 9:16 or taller (800×1280 px per screen as the working unit)
- **Panels**: 5–8 per segment, variable height, full-bleed width permitted
- **Gutters**: generous vertical white space **is** the timing mechanism — tall gaps before reveals, tight stacks for rapid beats; one idea per screen-height
- **Reading direction**: strictly top to bottom; never side-by-side panels
- **Native patterns**: `slow-burn-reveal`, `parallel-action`, `setup-reinforce-turnaround` (stretched)
- **Dialogue budget**: 1 bubble per panel preferred; bubbles never straddle a scroll boundary
- **Pipeline**: `comic-webtoon-scroll-pipeline`

### 4. `single-panel-gag`
- **Canvas**: 1:1 or 4:5
- **Panels**: exactly 1 — the entire arc lives inside one frame plus its caption
- **Special allowance**: one caption line below the panel is permitted (this format's only exception to the no-caption rule)
- **Native patterns**: `gag-escalation` (compressed: the panel is the BREAK; context implies the pattern)
- **Dialogue budget**: 1 bubble **or** 1 caption, not both
- **Pipeline**: runs through `comic-3-panel-horizontal-pipeline` with panel count overridden by the contract

### 5. `2x2-grid-page`
- **Canvas**: square or 4:5 portrait
- **Panels**: 4 in a 2×2 grid, Z-path reading (RTL mirror allowed)
- **Gutters**: obey the T-rule — avoid a perfect "+" intersection; stagger one gutter slightly
- **Native patterns**: `kishotenketsu`, `parallel-action` (threads on the diagonal)
- **Dialogue budget**: 1–2 bubbles per panel, ≤ ~8 words
- **Pipeline**: `comic-4koma-pipeline` with grid layout flag

### 6. `multi-page-chapter`
- **Canvas**: sequence of pages (typically 2:3 portrait), 4–9 panels per page
- **Page grammar**: page-turn beats are sacred — end right-hand pages on questions, open left-hand pages with consequences; never split an action-to-action pair across a turn
- **Native patterns**: all; chapters compose multiple patterns across scenes
- **Dialogue budget**: per-panel budget unchanged; chapter adds scene-level silence rhythm
- **Pipeline**: `comic-multi-page-chapter-pipeline`

## Reading Direction Rule (Resolves the LTR/RTL Conflict)

- Default: **left-to-right** for Western and European styles
- Manga-family styles (`retro-hand-inked-manga-comic`, `gekiga-cinematic-manga`, `shoujo-romance-manga`, `ink-wash-storybook-manga`, `junji-ito-body-horror`) **may** lock right-to-left for authenticity — the Producer sets `reading_direction` once in the contract, and every shot plan's eyeline vectors must obey it
- Vertical formats read strictly top-to-bottom regardless of style

## Selection Rules

1. **One format per project**, locked in the Producer's contract
2. Format must be **pattern-compatible** (a 4-beat pattern cannot run in a 3-panel format)
3. Format must be **style-compatible**: scroll-native styles pair with `webtoon-scroll-segment`; print-era styles pair with strip, grid, or chapter
4. `comic-quality-gates` Layer 1 validates against the **locked format**, not against a hardcoded panel count

## Integration

- Extends `comic-structural-contract` (which remains the default-format contract)
- Consumed by `comic-producer` (selection), `comic-director` (per-format flow rules), and all `comic-pipeline` skills
- Resolves the format conflict for `manhwa-color-webtoon` and gives 4-koma and chapter work a sanctioned home

---

*The strip was never the point. The discipline was — and the discipline now travels across formats.*
