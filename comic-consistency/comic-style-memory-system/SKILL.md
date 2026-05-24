---
name: comic-style-memory-system
version: 1.0.0
category: comic-consistency
description: Maintains consistent artistic mark-making and medium treatment across panels and scenes. Handles linework signature, screentone density, hatching behavior, and overall rendering language independent of character identity.
---

# Comic Style Memory System

**Core principle**: Artistic style (how marks are made) must remain coherent even when characters, scenes, and lighting change.

This skill is deliberately separated from character identity so that style rules can be shared across an entire universe while individual characters still have their own identity systems.

## When to Use
- When linework, screentone, or hatching must feel consistent across many panels
- When switching between different base models or checkpoints
- When building style LoRAs or attention-injection references
- When the project requires a recognizable "house style" across multiple artists or tools

## Key Responsibilities
- Define and enforce line weight behavior, hatching density, and edge quality
- Manage screentone rules (ruling, dot shape, moiré prevention)
- Maintain color temperature and lighting grammar consistency
- Provide style reference packs for attention-level injection (StyleID, Consistent Self-Attention)

## Integration
- Pulls style grammar from `comic-world-bible-system`
- Works alongside `comic-character-consistency-system`
- Used by `comic-long-sequence-orchestrator` for long arcs

## Planned Extensions
- Style LoRA training guidelines
- Linework signature extraction and matching
- Hatching density modulation based on emotional intensity

---

*Style memory is what makes a comic feel like it was drawn by the same hand, even across hundreds of pages.*