---
name: comic-pipeline
version: 1.0.0
category: comic-pipeline
description: End-to-end workflow skills that orchestrate comic-core, comic-consistency, and comic-styles into complete generation pipelines (3-panel, multi-page, long-arc).
---

# Comic Pipeline Layer

**Purpose**: This layer contains workflow skills that combine the lower layers into usable end-to-end processes.

## Current Skills (Planned)

| Skill | Description | Status |
|-------|-------------|--------|
| `comic-3-panel-horizontal-pipeline` | Full 3-panel comic generation with consistency | Planned |
| `comic-multi-page-chapter-pipeline` | Chapter-length comic production | Planned |
| `comic-emotional-arc-orchestrator` | Story arc planning and pacing | Planned |

## Design
Every pipeline skill should:
- Accept high-level creative input (reference image + story direction)
- Automatically load required core + consistency + style skills
- Execute generation with proper review gates
- Output structured results + assets

---

*Pipelines turn the skill library into actual production capability.*