---
name: comic-pipeline
version: 1.1.0
category: comic-pipeline
description: End-to-end workflow skills that orchestrate comic-core, comic-consistency, comic-styles, and comic-direction into complete generation pipelines (3-panel strip, 4-koma, webtoon scroll, multi-page chapter).
---

# Comic Pipeline Layer

**Purpose**: This layer contains workflow skills that combine the lower layers into usable end-to-end processes. Every pipeline runs under the authority of the `comic-direction` layer.

## Current Skills

| Skill | Format Served | Status |
|-------|---------------|--------|
| `comic-3-panel-horizontal-pipeline` | `3-panel-horizontal` (default), `single-panel-gag` | ✅ Active |
| `comic-4koma-pipeline` | `4koma-vertical`, `2x2-grid-page` | ✅ Active |
| `comic-webtoon-scroll-pipeline` | `webtoon-scroll-segment` | ✅ Active |
| `comic-multi-page-chapter-pipeline` | `multi-page-chapter` | ✅ Active |
| `comic-emotional-arc-orchestrator` | Series-level emotional continuity above all pipelines | ✅ Active |

## The Universal Pipeline Shape

Every pipeline follows the same five stages — only the format rules differ:

```
1. PRE-PRODUCTION   Producer locks the contract (format + pattern + style + scope)
                    and runs the greenlight gate
2. PLANNING         Director writes the vision statement and per-strip/page shot plans
3. GENERATION       Consistency stack resolves DNA + style memory;
                    comic-image-generation-adapter executes the shot plan
4. REVIEW           Director final cut (flow → words → everything → Artistic Life);
                    full comic-quality-gates run; failures follow Producer policy
5. DELIVERY         Producer sign-off, exports, production state + bible updated
```

## Design Rules

Every pipeline skill must:
- Refuse to run without a locked project contract from `comic-producer`
- Generate **only** from a Director shot plan — never directly from a prompt
- Run the full quality-gate suite against the locked format and pattern
- Output structured results: assets + shot plan + consistency log

---

*Pipelines turn the skill library into actual production capability — and direction turns pipelines into authorship.*
