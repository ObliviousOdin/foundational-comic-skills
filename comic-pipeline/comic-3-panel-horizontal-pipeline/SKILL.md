---
name: comic-3-panel-horizontal-pipeline
version: 1.1.0
category: comic-pipeline
description: Complete end-to-end pipeline for generating consistent 3-panel horizontal comics. Producer greenlight, Director shot plan, generation through the consistency stack, and Director final cut.
---

# Comic 3-Panel Horizontal Pipeline

**Purpose**: The canonical workflow for producing a single, high-quality 3-panel comic strip while respecting the full direction and consistency system. Also serves the `single-panel-gag` format with the panel count overridden by the contract.

## When to Use

- Default production path for most short comic work
- Testing new styles, consistency configurations, or directorial approaches
- Building larger bodies of work (this pipeline is the atomic unit)

## Pipeline Flow

1. **Input**: reference image + optional story direction
2. **Producer (pre-production)**:
   - Brief intake → project contract (default locks: `3-panel-horizontal` + `setup-reinforce-turnaround` + chosen style)
   - Greenlight gate: world bible, DNA templates, negative library, consistency config
3. **Load**:
   - `comic-core`
   - `comic-consistency` (World Bible + character + style memory)
   - Locked style skill
4. **Director (planning)**:
   - Vision check + shot plan for the strip (beat roles, shot sizes, angles, staging, eyelines, transitions, pacing weights, dialogue beats)
   - Shot plan passes the five *name* criteria before generation
5. **Process**:
   - Extract cues via World Bible
   - Resolve character state and DNA
   - Apply style rules + style memory
   - Generate with `comic-image-generation-adapter` **from the shot plan**
6. **Review**:
   - Director final cut: flow → words → everything else → Artistic Life ruling
   - Full `comic-quality-gates` run; RETAKE notes name the shot-plan field to change; two failures force a RE-PLAN
   - Human review trigger per Producer cadence
7. **Output**: final image + shot plan + structured metadata + consistency log; Producer records the strip in the production state

## Integration

This is the primary consumer of the entire lower stack and the template all other pipelines follow.

---

*The 3-panel pipeline is the fundamental production unit of the system.*
