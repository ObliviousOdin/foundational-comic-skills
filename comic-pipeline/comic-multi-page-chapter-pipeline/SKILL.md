---
name: comic-multi-page-chapter-pipeline
version: 1.1.0
category: comic-pipeline
description: End-to-end pipeline for chapter-length comics (multiple pages, 4–9 panels per page). Adds page grammar, scene composition across patterns, and page-turn beat management on top of the full direction and consistency stack.
---

# Comic Multi-Page Chapter Pipeline

**Purpose**: The production workflow for chapter-length work — where individual strips become scenes, pages get their own grammar, and the page turn becomes a narrative instrument.

## When to Use

- Chapters of 4–24 pages within a serialized project
- Stories that need scene changes, time shifts, or multiple narrative patterns
- Print-destined work where page parity (left/right) matters

## Pipeline Flow

1. **Producer**: contract locks `multi-page-chapter` + style; chapter broken into scenes, each scene assigned a narrative pattern; panel budget set per page (4–9)
2. **Load**: `comic-core`, `comic-consistency` (full World Bible required — no chapter without one), locked style skill
3. **Director chapter map** (before any page, template in `assets/templates/chapter-map-template.yaml`): scene order, climax placement, and **page-turn beats** — right-hand pages end on questions, left-hand pages open with consequences; never split an action-to-action pair across a turn
4. **Director shot plans**: one per page, following the five *name* criteria; shot ladder varied within and across pages
5. **Process**: page-by-page generation through `comic-image-generation-adapter`; `comic-long-sequence-orchestrator` tracks world state, costume, and lighting continuity between scenes
6. **Review gates**: Director final cut per page; Producer-scheduled human review at every scene boundary; drift re-anchoring per policy
7. **Output**: page sequence + chapter map + shot plans + consistency log + updated world bible `version_history`

## Chapter-Specific Rules

- **Scene-to-scene transitions** live between pages or at page-internal hard breaks — never mid-row
- The 180° rule holds **within a scene** across pages; re-establish the axis after every scene change
- One full-page or splash moment per chapter maximum, and it must be the climax the chapter map designated
- Dialogue budget per panel is unchanged; chapters add a **silence rhythm** — at least one wordless panel per page spread

## Integration

- Consumes `comic-format-library` (`multi-page-chapter`) and composes multiple `comic-narrative-patterns` across scenes
- Built on `comic-long-sequence-orchestrator` for state tracking and drift detection
- Commanded by `comic-producer`; mapped, planned, and cut by `comic-director`
- The atomic unit remains the planned page — this pipeline is the strip pipeline scaled with page grammar

---

*A chapter is not thirty panels. It is a sequence of page turns, each one earned.*
