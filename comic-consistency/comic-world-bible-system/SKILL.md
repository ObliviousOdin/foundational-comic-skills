---
name: comic-world-bible-system
version: 1.4.0
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

**The four buckets say where a negative lives, not what it is for.** Negatives accumulate as reflexes — a panel goes wrong, a phrase gets added, and nobody can later say which failure any given line prevents. That matters because negatives compete for prompt budget, and a bloated block dilutes the entries doing real work.

Every negative belongs to one of four **bleed classes**, and naming the class is what makes a negative reviewable:

| Class | The failure it prevents | Where it lives | Example |
|-------|------------------------|----------------|---------|
| **Identity bleed** | One character acquiring another's signature marks | `per_character_negatives` — each entry carries the *others'* marks | Echo's block negates "facial scar" because Rabot has one |
| **Style bleed** | A registered variant leaking into another | `per_style_negatives`, per variant | Chibi mode negates "realistic proportions"; the main series negates "chibi proportions" |
| **Era bleed** | Period-locked worlds acquiring modern or wrong-era content | `project_wide_negatives` | A 1930 strip negates "smartphone, plastic, LED" |
| **Anatomy bleed** | Generic generation failures unrelated to this project | `project_wide_negatives` | "deformed hands, extra fingers" |

Two rules follow from the table:

1. **Identity and style bleed are bidirectional.** A negative added to one side without its opposite protects one character or variant and leaves the other exposed. Add both or neither.
2. **Anatomy-bleed entries are the only ones safe to copy between projects.** The other three are all statements about *this* world, and a project-wide negative inherited from another project is how a lock stops matching the thing it was written for.

When the prompt budget forces cuts, drop from anatomy bleed first: backends have improved most there, and it is the class whose entries say the least about the project.

### 5. version_history
- Date-stamped record of all changes
- Rationale for each change (critical for long-running series)

### 6. source_register (nonfiction projects only)

Fiction invents its world; nonfiction owes its world to something outside itself. A bible declaring `production_mode: nonfiction` carries a source register, and every depicted fact traces to an entry in it.

- `production_mode`: `fiction` (default, omit freely) or `nonfiction`
- `source_register`: one entry per sourced fact, each containing:
  - `claim`: the depicted fact, stated plainly ("the depot roof is corrugated steel")
  - `source`: where it came from — photograph, interview, document, site visit
  - `depicted_in`: the panels or assets that render the claim
  - `confidence`: `verified` (direct evidence) or `reported` (single-source testimony)
  - `register`: `observed` (the artist was present), `reconstructed` (documented but not witnessed), or `represented` (deliberately non-literal — a metaphor, diagram, or mental state)
- Character entries additionally carry, when the subject is a real person:
  - `source_note`: where the depiction comes from, and the consent position
  - `identifiability`: `exact`, `reduced`, or `anonymised` — the recognisability the artist *chose*
  - `composite`: `true` when the figure merges several real people, with `composite_disclosure` stating how the reader is told

**Why `register` is separate from `confidence`.** They answer different questions. Confidence grades the *evidence* — verified or single-source. Register grades the artist's *relationship to the scene*, and `COMICS-JOURNALISM-AND-DEPICTION-ETHICS.md` identifies collapsing the two as the field's commonest failure: a reconstructed scene rendered with the same confident specificity as a witnessed one is not a lie, it is an unmarked claim. A well-sourced reconstruction is still a reconstruction, and the panel should say so.

**Why identifiability is recorded rather than assumed.** An artist controls how recognisable a face is on a continuous gradient, which is a capability prose does not have and therefore a decision prose never has to log. Recording it makes the choice reviewable instead of implicit.

**Why this is a schema section and not a style note.** `reportage-comics-journalism` locks out fabricated documentary detail — invented insignia, made-up signage, plausible-looking evidence. That lock is only checkable if the project holds a register of what *is* sourced; otherwise "no fabrication" is a sentiment. A style can state the rule, but only the bible can hold the evidence, and the bible outlives any single panel.

**What the register does not do.** It records provenance, not permission. Whether a real person or place may be depicted at all is a Producer decision recorded in the contract; the register only answers whether what was drawn traces to something observed.

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

**Provenance Validation** (when `production_mode: nonfiction`)
- `source_register` is present and holds at least one entry
- Every entry carries `claim`, `source`, and `depicted_in`
- Every entry carries a `register` from the sanctioned set — an unmarked reconstruction is the failure this catches
- Every character in the compendium carries a `source_note` and an `identifiability` level
- Any character marked `composite: true` carries a `composite_disclosure`

Fiction bibles skip this block entirely — omitting `production_mode` means `fiction`, and nothing changes for existing projects.

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

### Nonfiction Delta

A reportage project adds two things to the shape above — the mode flag and the register — and a `source_note` on any real subject:

```yaml
production_mode: nonfiction

character_compendium:
  - name: "Yard Foreman"
    canonical_reference_sheet: "foreman-ref-sheet.png"
    dna_template: "man in his fifties, weathered face, hi-vis vest over flannel"
    source_note: "site visit 2026-03-11; photographed with consent, name withheld at request"
    identifiability: reduced        # face softened at the subject's request

source_register:
  - claim: "the depot roof is corrugated steel with three patched sections"
    source: "site photograph DSC_0142"
    depicted_in: ["panel-01", "panel-03"]
    confidence: verified
    register: observed              # the artist stood there
  - claim: "night shifts run four crews since the January change"
    source: "interview, yard foreman, 2026-03-11"
    depicted_in: ["panel-02"]
    confidence: reported
    register: reconstructed         # documented, not witnessed - and the panel says so
```

Anything drawn that no entry supports is fabrication, and the style's negative locks reject it.



*Without a world bible, even the best technical consistency tools have nothing reliable to be consistent with.*