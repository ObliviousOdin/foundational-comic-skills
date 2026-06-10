---
name: comic-world-bible-system
version: 1.1.0
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

### 1. visual_grammar
- `master_style_references`: 3–5 canonical style reference images
- `color_palette_anchors`: Named swatches with hex codes
- `linework_rules`: Weight, anti-aliasing, hatching conventions, pressure behavior
- `lighting_grammar`: Key light direction, shadow hardness, ambient temperature
- `typography_rules`: Lettering rules (if used)

### 2. character_compendium
One entry per character containing:
- `canonical_reference_sheet`: Front, 3/4, side, back, neutral expression
- `expression_library`: Minimum 6 core emotional states
- `costume_variants`: Per-variant color codes
- `dna_template`: Ready-to-inject prompt fragment
- `consistency_method`: Recommended LoRA path, IP-Adapter source, InstantID/PuLID settings
- `signature_marks`: Distinguishing features
- `negative_prompt_block`: Known failure modes for this character

### 3. world_register
- `location_reference_sheets`: Consistent architectural and lighting rules per location
- `recurring_props`: Visual specifications for objects
- `time_weather_lighting`: Time-of-day and weather conditions per location

### 4. negative_library
- `project_wide_negatives`
- `per_character_negatives`
- `per_style_negatives`
- `documented_artifacts_to_reject`

### 5. version_history
- Date-stamped record of all changes
- Rationale for each change (critical for long-running series)

## Expected Folder Structure

A well-organized world bible project follows this layout:

```
project-root/
├── bibles/
│   └── v1.0.0/
│       └── world-bible.yaml
├── assets/
│   ├── characters/
│   │   └── [character-name]/
│   │       ├── reference-sheet.png
│   │       └── expressions/
│   ├── locations/
│   └── style-references/
├── exports/
│   ├── dna-templates/
│   ├── model-sheets/
│   ├── consistency-config.json
│   └── style-grammar.yaml
├── artifacts/          # Generated reference packs
└── version_history.md
```

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
A valid world bible must pass these checks:

**Structural Validation**
- All top-level sections present (`visual_grammar`, `character_compendium`, `world_register`, `negative_library`, `version_history`)
- At least one character entry exists
- Every character has a `dna_template` block
- Style grammar (linework + lighting) is defined

**Content Validation**
- Canonical reference images exist for all characters (or clear placeholders)
- Negative libraries are non-empty
- Version history has at least one entry with rationale

**Consistency Validation**
- No conflicting costume or lighting rules across characters
- All referenced assets in the bible have corresponding files in the assets folder

### 4. Derive Artifacts

The world bible system is responsible for generating ready-to-use artifacts from the canonical data.

#### 4.1 DNA Template
- Automatically formatted prompt fragment
- Includes face, hair, build, costume, and signature marks
- Injected at the top of every generation prompt

#### 4.2 Model Sheet Prompts
- Generates structured prompts for front, 3/4, side, and back views
- Includes expression variations
- Optimized for InstantID / IP-Adapter workflows

#### 4.3 Negative Prompt Library
- Combines global negatives with character-specific negatives
- Includes known failure modes (e.g., "extra fingers", "deformed hands", "modern clothing")

#### 4.4 Style Memory Pack
- Extracts linework rules, screentone density, and hatching behavior
- Generates reference images for attention injection (StyleID, Consistent Self-Attention)

#### 4.5 Consistency Config
- Recommended weights for LoRA, IP-Adapter, ControlNet per character
- Optimized for long-sequence stability vs. expression freedom trade-off

Example files are available in the `/artifacts` folder.

### 5. Tooling

**Implemented** — structural/content validation runs via the repository validator:

```bash
python3 tools/validate.py --bible path/to/world-bible.yaml
```

It enforces the Validate rules above (required sections, character DNA + reference sheets, non-empty negatives, rationale-bearing version history). Example bibles under `examples/` are validated automatically in CI.

**Planned query interface**:
- `get_character_dna(name)`
- `get_style_grammar()`
- `list_characters_in_costume(costume)`
- `export_consistency_config(pipeline_type)`

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

## Versioning & Change Management

### Versioning Strategy
- **Major** (v2.0): Changes to core visual grammar, color anchors, or fundamental style rules
- **Minor** (v1.1): New characters, significant costume/location additions, or new negative library entries
- **Patch** (v1.0.1): Corrections, clarifications, or small refinements with no breaking changes
- Every version bump must be accompanied by a dated entry in `version_history` with clear rationale

### Conflict Resolution Rules
- **Character vs Character conflicts** (e.g., two characters cannot both have the same signature mark or costume color) → escalate to human review with proposed resolution
- **Panel vs Bible violations** (generated panel breaks established rules) → flag immediately, suggest corrective prompt adjustment
- **Canonical reference always wins** over any generated variation or model output
- **Style grammar overrides** individual character preferences when they conflict with the established visual language

### Export Formats for Consumers

The world bible system supports multiple export formats depending on the consuming layer:

| Consumer | Export Format | Purpose |
|----------|---------------|---------|
| `comic-character-consistency-system` | `dna-templates/*.yaml` + `model-sheets/` | Identity locking and reference generation |
| `comic-image-generation-adapter` | `consistency-config.json` | LoRA weights, IP-Adapter settings, negative blocks |
| `comic-long-sequence-orchestrator` | `world-bible.yaml` (full) | Persistent state validation across 1000+ panels |
| `comic-style-memory-system` | `style-grammar.yaml` | Linework, screentone, and hatching rules |
| Human editors / writers | `world-bible.md` (rendered) | Readable documentation with embedded references |

Example export structure is defined in `/exports/README.md`.

## Minimal Valid Example

Here is a minimal valid `world-bible.yaml` that passes all validation checks:

```yaml
visual_grammar:
  master_style_references: ["style-ref-01.png", "style-ref-02.png"]
  color_palette_anchors:
    - name: "primary-navy"
      hex: "#19294D"
  linework_rules: "clean 2px with subtle hatching"
  lighting_grammar: "soft key light from upper left, gentle shadows"

character_compendium:
  - name: "Rabot"
    canonical_reference_sheet: "rabot-ref-sheet.png"
    expression_library: ["neutral", "focused", "smirk", "surprised", "determined", "tired"]
    dna_template: "young man, short dark hair, sharp features, wearing navy jacket with white shirt"
    consistency_method: "IP-Adapter + LoRA weight 0.75"
    signature_marks: "small scar on left cheek"
    negative_prompt_block: "deformed hands, extra fingers, blurry face"

world_register:
  location_reference_sheets:
    - name: "Control Room"
      lighting: "cool fluorescent with strong overhead shadows"

negative_library:
  project_wide_negatives: ["modern clothing", "photorealistic", "text on image"]

version_history:
  - date: "2026-05-23"
    change: "Initial world bible created"
    rationale: "Establish baseline for 1000+ panel Rabot series"
```

This example satisfies structural, content, and consistency validation.



*Without a world bible, even the best technical consistency tools have nothing reliable to be consistent with.*