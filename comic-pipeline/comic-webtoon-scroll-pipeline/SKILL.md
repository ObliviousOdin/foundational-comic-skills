---
name: comic-webtoon-scroll-pipeline
version: 1.0.0
category: comic-pipeline
description: End-to-end pipeline for vertical-scroll webtoon segments. Treats scroll distance as the timing mechanism, with full direction and consistency control for serialized episodes.
---

# Comic Webtoon Scroll Pipeline

**Purpose**: The production workflow for vertical-scroll comics — the native habitat of `manhwa-color-webtoon` and the format where gutter height literally is time.

## When to Use

- Webtoon/scroll platforms (one screen-width column, indefinite height)
- Serialized episodes with cliffhanger or slow-burn pacing
- Any style whose Style Lock declares scroll-friendly panel flow

## Pipeline Flow

1. **Producer**: contract locks `webtoon-scroll-segment` + pattern (`slow-burn-reveal`, `parallel-action`, or stretched default) + style; episode broken into scroll segments of 5–8 panels
2. **Load**: `comic-core`, `comic-consistency`, locked style skill
3. **Director shot plan** (per segment): one idea per screen-height; assign each panel a scroll-timing role — tight stacks accelerate, tall white gaps hold the breath before a reveal; eyeline vectors point **down**
4. **Process**: cues → DNA resolution → style application → generation via `comic-image-generation-adapter`, panel by panel or in consistent batches
5. **Director final cut**: scroll-through review at reading speed — does the reveal land *after* the gap, never beside it? No bubble straddles a scroll boundary
6. **Quality gates**: full run against the locked format (vertical, top-to-bottom, no side-by-side panels)
7. **Output**: stitched segment + per-panel assets + shot plan + consistency log

## Format-Specific Rules

- Working unit ~800×1280 px per screen; panels may bleed full-width
- Vertical white space is a **timing instrument**, not waste — budget it in the shot plan
- The pre-reveal gap is the webtoon equivalent of the page turn: protect it
- Long episodes re-anchor characters per the Producer's drift policy (default every 10 panels)

## Integration

- Consumes `comic-format-library` (`webtoon-scroll-segment`) and `comic-narrative-patterns`
- Pairs natively with `comic-styles/asian/manhwa-color-webtoon`; works with any scroll-compatible style
- Uses `comic-long-sequence-orchestrator` for multi-episode serials
- Commanded by `comic-producer`; planned and cut by `comic-director`

---

*In a webtoon, the reader's thumb is the metronome. Direct the thumb.*
