---
name: comic-world-bible-system
version: 1.0.0
category: comic-consistency
description: The canonical source of truth and asset registry for long-form comic production. Defines structured world bibles, character compendiums, style grammars, and generates derived consistency artifacts (DNA templates, model sheets, negative libraries).
---

# Comic World Bible System

**Core principle**: Every consistency decision in a long-running comic project must trace back to a single, versioned source of truth.

This skill implements the **World Bible** as the central nervous system for 1000+ panel arcs. It replaces ad-hoc prompt engineering and scattered reference images with a structured, queryable, and derivable knowledge base.

## When to Use
- Starting any new long-form comic project (multi-chapter, serialized, or 100+ panels)
- Establishing consistency rules before generating the first panel
- Generating or updating character DNA templates, model sheets, or style references
- Validating that new panels remain consistent with established canon
- Training or fine-tuning consistency models (LoRAs, IP-Adapter references)

## World Bible Schema (v1)

A world bible is a structured document containing the following top-level sections:

### 1. Visual Grammar
- Master style reference images (3–5 canonical examples)
- Color palette anchors (named swatches + hex codes)
- Linework rules (weight, anti-aliasing, hatching conventions, pressure behavior)
- Lighting grammar (key light direction, shadow hardness, ambient temperature)
- Typography rules (if lettering is used)

### 2. Character Compendium (one entry per character)
- Canonical reference sheet (front, 3/4, side, back, neutral expression)
- Expression library (minimum 6 core states)
- Costume variants with per-variant color codes
- DNA template block (ready-to-inject prompt fragment)
- Recommended consistency method + weights (LoRA path, IP-Adapter source, InstantID/PuLID settings)
- Signature marks and distinguishing features
- Negative prompt block (known failure modes for this character)

### 3. World / Environment Register
- Location reference sheets with consistent architectural and lighting rules
- Recurring props and objects with visual specifications
- Time-of-day and weather lighting conditions per location

### 4. Negative Library
- Project-wide negative prompts
- Per-character negative blocks
- Per-style negative blocks
- Documented artifacts to actively reject

### 5. Version History
- Date-stamped record of all changes to characters, locations, or style rules
- Rationale for each change (critical for long-running series)

## Framework

### 1. Create World Bible
- Start with a minimal valid bible (Visual Grammar + at least one Character entry)
- Use the schema above as the contract
- Store as versioned YAML or structured Markdown + assets folder

### 2. Derive Artifacts
From a valid world bible, the system can automatically generate:
- Character DNA templates (for prompt injection)
- Model sheet generation prompts
- Style memory reference packs
- Negative prompt libraries
- Consistency configuration files (LoRA weights, IP-Adapter settings)

### 3. Validate
- Check that all required sections exist
- Verify that character entries have canonical references
- Ensure style grammar is defined before any generation
- Flag missing negative libraries

### 4. Query
- Retrieve DNA template for a specific character
- Get all characters in a specific costume state
- List all locations with night lighting rules
- Export consistency configuration for a given pipeline

## Integration with Other Layers

| Layer | How it uses the World Bible |
|-------|-----------------------------|
| `comic-core` | References style grammar and structural rules |
| `comic-character-consistency-system` | Primary source for DNA templates, model sheets, and identity artifacts |
| `comic-style-memory-system` | Pulls linework, screentone, and hatching rules |
| `comic-long-sequence-orchestrator` | Maintains persistent state against the bible across 1000+ panels |
| Style skills | Load style-specific rules and negative libraries |

## Design Principles (from Research)

- **Single Source of Truth** — No consistency decision should be made without referencing the bible
- **Derivability** — The bible should be able to generate the artifacts needed by technical consistency systems
- **Versioning** — Long-running series require change tracking with rationale
- **Human + Machine Readable** — Structured enough for agents, readable enough for human artists and editors

## Related Skills (Planned)
- `comic-character-consistency-system`
- `comic-style-memory-system`
- `comic-long-sequence-orchestrator`
- `comic-image-generation-adapter`

---

*Without a world bible, even the best technical consistency tools have nothing reliable to be consistent with.*