---
name: comic-image-generation-adapter
version: 1.1.0
category: comic-consistency
description: Unified interface for image generation calls (GPT Image, Higgsfield, ComfyUI, FLUX, etc.). Defines the canonical prompt assembly contract that injects World Bible context, character DNA, shot-plan directives, style memory, and negatives — in a fixed order.
---

# Comic Image Generation Adapter

**Core principle**: Generation calls should be simple for the caller while automatically carrying all consistency context — assembled in one canonical order, so two panels never differ because their prompts were *organized* differently.

This skill is the execution layer connecting the consistency stack to actual image models.

## When to Use

- Any time a skill needs to generate images while respecting the full consistency system
- When switching between generation backends
- When debugging "same inputs, different look" — the first suspect is assembly-order drift

## The Prompt Assembly Contract (Canonical Order)

Every generation prompt is assembled in exactly this order. Sections come from their owning artifacts — the adapter composes, it never authors:

| # | Block | Source | Notes |
|---|-------|--------|-------|
| 1 | **STYLE LOCK** | Style skill `Prompt Block` | Verbatim; never paraphrased |
| 2 | **FORMAT DIRECTIVE** | Project contract | Canvas, aspect, panel count, reading direction (e.g., "one wide 21:9 image, three panels, left to right") |
| 3 | **CHARACTER DNA** | World bible `dna_template` per character | Stacked in screen-position order (see multi-character rules); per-scene overrides applied |
| 4 | **PANEL DIRECTIVES** | Director shot plan | Per panel: beat, shot size, camera angle, staging, eyeline, dialogue text + placement zone |
| 5 | **SCENE CONTEXT** | World bible `world_register` | Location rules, lighting grammar, time/weather |
| 6 | **CONSISTENCY ANCHORS** | Consistency config | Seed policy, reference-image handles, LoRA/IP-Adapter weights (backend-dialect section) |
| 7 | **NEGATIVE BLOCK** | World bible `negative_library` | Project + per-character + per-style negatives, merged and deduplicated; never hand-edited |

**Budget rule**: when the backend's prompt budget forces cuts, cut from the bottom of block 5 upward — style lock, format, and DNA are never truncated.

## Worked Mini-Example (Blocks 1–4, Abbreviated)

```text
[STYLE] 1970s-80s retro hand-inked Japanese manga style, black and white,
G-pen brush outlines, soft screentone shading, hand-lettered bubbles…
[FORMAT] One wide 21:9 image, exactly three panels, read left to right.
[CHARACTER: Rabot] young man, short dark hair, sharp features, navy
jacket over white shirt, small scar on left cheek.
[PANEL 1 — SETUP] medium shot, eye level; Rabot at a control-room
console, fg hands on console, bg monitors; gaze toward panel right;
speech balloon upper-left dead zone: "Quiet shift tonight."
[PANEL 2 — REINFORCE] close-up, slight low angle; …
```

## Backend Dialects

| Backend | Dialect Notes |
|---------|---------------|
| GPT-Image-class (single-call multi-panel) | Whole strip in one call; format directive is load-bearing; consistency anchors live in the text + attached references |
| ComfyUI / SD-class | Panel-by-panel + stitch; blocks 6–7 become node parameters (LoRA weights, IP-Adapter refs, negative field); seed policy per `comic-character-consistency-system` |
| FLUX Kontext-class | Reference-image conditioning carries DNA; text DNA block is shortened to signature marks only |
| Higgsfield | Per its adapter (see `comic-production`); assembly order unchanged |

The assembly **order is invariant across backends** — only the delivery mechanism of each block changes.

## Key Responsibilities

- Accept high-level requests (character + scene + style + shot plan)
- Resolve and inject all seven blocks automatically from their owning artifacts
- Support single-panel and batched long-sequence generation (Consistent Self-Attention where available)
- Emit a **generation log**: blocks used, artifact versions (bible version, shot-plan id), backend, seed — so any panel can be reproduced or audited
- Provide hooks for the Director's final cut and Producer review gates

## Failure Modes to Catch

- Paraphrased style locks ("retro manga style" instead of the verbatim block) — the top cause of style drift between sessions
- Negatives pasted manually instead of merged from the bible
- Shot-plan fields silently dropped when budgets are tight (cut scene context first, never directives)
- Generating without a shot plan at all — the adapter must refuse

## Integration

- Depends on all consistency-layer skills; consumes `comic-director` shot plans and the Producer's contract
- Used by every `comic-pipeline` skill and all style skills

---

*Generation should be the easy part. The hard part is making sure every call carries the right context — in the right order, every time.*
