---
name: comic-consistency
version: 1.0.0
category: comic-consistency
description: The consistency layer for long-form comic production. Provides world bible infrastructure, character identity systems, style memory, and long-sequence orchestration to maintain artistic coherence across 1000+ panels.
---

# Comic Consistency Layer

**Purpose**: This layer ensures that characters, style, world state, and artistic decisions remain coherent across long serialized comic projects. It is the bridge between the universal rules in `comic-core` and the specific artistic styles in `comic-styles`.

## Skill Inventory (Current)

| Skill | Role | Status |
|-------|------|--------|
| `comic-world-bible-system` | Canonical source of truth + asset registry | ✅ Foundation complete |
| `comic-character-consistency-system` | Identity locking, DNA templates, model sheets, layered conditioning | Planned |
| `comic-style-memory-system` | Linework, screentone, and hatching signature preservation | Planned |
| `comic-long-sequence-orchestrator` | Multi-agent pipelines, drift detection, 1000+ panel support | Planned |
| `comic-image-generation-adapter` | Unified interface for GPT Image 4, Higgsfield, ComfyUI, etc. | Planned |

## How the Consistency Layer Works

```
World Bible (single source of truth)
       ↓
comic-world-bible-system → generates DNA, model sheets, negative libraries
       ↓
comic-character-consistency-system + comic-style-memory-system
       ↓
comic-long-sequence-orchestrator (maintains state across arcs)
       ↓
comic-image-generation-adapter (executes with consistency artifacts injected)
```

## When to Load comic-consistency

- Any project expected to exceed ~50 panels
- When character identity or artistic style must survive model changes or long time gaps
- When building production pipelines that require human review gates
- When training or managing consistency models (LoRAs, IP-Adapter references)

## Design Goals for 1000+ Panel Projects

- World Bible as the single source of truth
- Layered conditioning (multiple techniques at sub-max weights)
- Persistent world state tracking
- Automated drift detection with human escalation
- Style memory decoupled from character identity

## Related Layers
- `comic-core` (required dependency)
- `comic-styles` (consumes consistency artifacts)
- `comic-pipeline` (orchestrates full workflows)

---

*Consistency at scale is not a technical trick — it is an information architecture problem.*