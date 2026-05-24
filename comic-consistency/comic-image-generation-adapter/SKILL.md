---
name: comic-image-generation-adapter
version: 1.0.0
category: comic-consistency
description: Unified interface for direct image generation calls (GPT Image 4, Higgsfield, ComfyUI, etc.). Injects World Bible context, character DNA, style memory, and consistency artifacts automatically.
---

# Comic Image Generation Adapter

**Core principle**: Generation calls should be simple for the user while automatically carrying all consistency context from the lower layers.

This skill acts as the execution layer that connects the consistency stack to actual image models.

## When to Use
- Any time a skill needs to generate images while respecting the full consistency system
- When switching between different generation backends (GPT Image 4, Higgsfield, local ComfyUI, etc.)
- When building end-to-end pipelines

## Key Responsibilities
- Accept high-level requests (character + scene + style)
- Automatically resolve and inject:
  - World Bible rules
  - Character DNA
  - Style memory references
  - Layered conditioning parameters
- Support both single-panel and batched long-sequence generation
- Provide hooks for human review gates

## Supported Backends (Planned)
- GPT Image 4
- Higgsfield
- ComfyUI (Qwen/Kontext + ControlNets)
- FLUX.1 Kontext
- Other providers via unified interface

## Integration
- Depends on all consistency layer skills
- Used by `comic-pipeline` and style skills

---

*Generation should be the easy part. The hard part is making sure every call carries the right context.*