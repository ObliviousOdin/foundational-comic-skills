---
name: comic-core
version: 1.0.0
category: comic-core
description: The foundational operating system for authentic, human-like comic generation. Contains the universal rules, structural contracts, quality gates, and story derivation methods that every style and pipeline skill builds upon.
---

# Comic Core — Foundational Operating System

**Purpose**: This is the root layer that gives the entire comic skill system its discipline, consistency, and artistic integrity. Every higher-level skill (styles, consistency engines, pipelines) depends on these four contracts.

## Skill Inventory

| Skill | Role | Key Contribution |
|-------|------|------------------|
| `comic-universal-operating-rule` | Root contract | Input rules, four-cue story derivation, 3-panel structure, and baseline quality principles |
| `comic-structural-contract` | Narrative architecture | Precise Setup → Reinforce → Turnaround emotional arc with panel relationships and turnaround tone guidelines |
| `comic-quality-gates` | Evaluation framework | 6-layer quality system including the critical "Artistic Life" gate that separates human-like work from generic AI output |
| `comic-story-derivation` | Narrative generation method | Repeatable process for extracting emotional seeds from reference images and building coherent arcs |

## How the Core Works Together

```
Reference Image
       ↓
comic-story-derivation (extract 4 cues + build emotional arc)
       ↓
comic-structural-contract (map arc to 3-panel Setup → Reinforce → Turnaround)
       ↓
comic-universal-operating-rule (apply input contract + style translation)
       ↓
comic-quality-gates (run all 6 layers, especially Artistic Life)
       ↓
Style Skill (retro-hand-inked-manga, gekiga-cinematic, etc.)
```

## When to Load comic-core

- Before creating or modifying any style skill
- When building consistency systems or memory layers
- When designing production pipelines (Higgsfield, Remotion, etc.)
- When auditing or improving comic output quality
- As the mandatory foundation for any new comic-related skill

## Design Philosophy

This core exists to solve the biggest failure mode in AI comic generation:

> **"Technically correct but artistically lifeless."**

The four skills work together to enforce:

1. **Discipline** — No deviation from the input contract or structural rules
2. **Coherence** — Story must grow from the specific reference image
3. **Emotional Intelligence** — Every panel must serve the emotional arc
4. **Artistic Life** — Final output must pass the human-artist pride test

## Future Extensions (Planned)

- `comic-character-consistency-system` — Long-term face, hair, outfit, and linework memory
- `comic-world-memory-system` — Persistent setting, prop, and environmental continuity
- `comic-linework-style-memory` — Encoding an artist's specific mark-making decisions
- `comic-emotional-arc-tracking` — Tracking character emotional state across multiple strips

## Integration with Higher Layers

```
comic-core (this skill)
    ↓
comic-styles/ (25+ individual artistic style skills)
    ↓
comic-consistency/ (character, world, linework memory)
    ↓
comic-pipeline/ (end-to-end generation workflows)
    ↓
comic-production/ (Higgsfield, Remotion, print output, etc.)
```

## Usage Example

When building a new style skill (e.g., `comic-styles/manga/gekiga-cinematic-manga`):

1. Start by referencing `comic-universal-operating-rule`
2. Define the style-specific Story Harness using `comic-story-derivation`
3. Lock the 3-panel structure using `comic-structural-contract`
4. Add style-specific quality rules on top of `comic-quality-gates`

---

*comic-core is not optional. It is the difference between prompt engineering and a true artistic system.*