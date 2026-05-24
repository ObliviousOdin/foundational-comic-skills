---
name: comic-3-panel-horizontal-pipeline
version: 1.0.0
category: comic-pipeline
description: Complete end-to-end pipeline for generating consistent 3-panel horizontal comics. Loads core + consistency + chosen style, executes generation with review gates.
---

# Comic 3-Panel Horizontal Pipeline

**Purpose**: The canonical workflow for producing a single, high-quality 3-panel comic strip while respecting the full consistency system.

## When to Use
- Default production path for most short comic work
- Testing new styles or consistency configurations
- Building larger chapters (this pipeline is the atomic unit)

## Pipeline Flow

1. **Input**: Reference image + chosen style + optional story direction
2. **Load**:
   - `comic-core`
   - `comic-consistency` (World Bible + character + style memory)
   - Target style skill
3. **Process**:
   - Extract cues via World Bible
   - Resolve character state and DNA
   - Apply style rules + style memory
   - Generate with `comic-image-generation-adapter`
4. **Quality Gates**:
   - Run full `comic-quality-gates`
   - Human review trigger (optional)
5. **Output**: Final image + structured metadata + consistency log

## Integration
This is the primary consumer of the entire lower stack.

---

*The 3-panel pipeline is the fundamental production unit of the system.*