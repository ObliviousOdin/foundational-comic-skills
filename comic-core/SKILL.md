---
name: comic-core
version: 1.2.0
category: comic-core
description: The foundational operating system for authentic, human-like comic generation. Contains the universal rules, structural contracts, format and narrative-pattern libraries, lettering craft, quality gates, and story derivation methods that every style and pipeline skill builds upon.
---

# Comic Core — Foundational Operating System

**Purpose**: This is the root layer that gives the entire comic skill system its discipline, consistency, and artistic integrity. Every higher-level skill (styles, consistency engines, direction, pipelines) depends on these contracts.

## Skill Inventory

| Skill | Role | Key Contribution |
|-------|------|------------------|
| `comic-universal-operating-rule` | Root contract | Input rules, four-cue story derivation, default 3-panel structure, and baseline quality principles |
| `comic-structural-contract` | Narrative architecture | Default Setup → Reinforce → Turnaround emotional arc with panel relationships, turnaround tone guidelines, and variation governance |
| `comic-narrative-patterns` | Beat pattern library | Six sanctioned arcs: the default plus kishōtenketsu, gag escalation, slow-burn reveal, parallel action, and silent strip |
| `comic-format-library` | Format library | Six sanctioned canvases: 3-panel horizontal (default), 4-koma, webtoon scroll, single-panel, 2×2 grid, multi-page chapter |
| `comic-quality-gates` | Evaluation framework | 6-layer quality system including the critical "Artistic Life" gate that separates human-like work from generic AI output |
| `comic-lettering-and-balloons` | Lettering craft contract | Balloon taxonomy, placement law, reading-order rules, and SFX policy that every style inherits |
| `comic-story-derivation` | Narrative generation method | Repeatable process for extracting emotional seeds from reference images (incl. multi-character relationship cues) and building coherent arcs |

## How the Core Works Together

```
Reference Image
       ↓
comic-story-derivation (extract 4 cues + build emotional arc)
       ↓
comic-narrative-patterns + comic-format-library (locked per project by the Producer)
       ↓
comic-structural-contract (map arc to the locked beats and panels)
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

## Delivered Extensions

The extensions originally planned for this layer now live in their own layers:

- Character, world, and linework memory → `comic-consistency/` (`comic-character-consistency-system`, `comic-world-bible-system`, `comic-style-memory-system`)
- Decision authority and review → `comic-direction/` (`comic-producer`, `comic-director`)
- Format and pattern variation → `comic-narrative-patterns` and `comic-format-library` (this layer)

Emotional state tracking across strips → delivered as `comic-emotional-arc-orchestrator` (pipeline layer).

## Integration with Higher Layers

```
comic-core (this skill)
    ↓
comic-consistency/ (character, world, linework memory)
    ↓
comic-styles/ (28 individual artistic style skills)
    ↓
comic-direction/ (Producer + Director decision authority)
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