---
name: comic-long-sequence-orchestrator
version: 1.0.0
category: comic-consistency
description: Orchestrates generation across long comic arcs (100–1000+ panels). Manages world state tracking, multi-agent pipelines, drift detection, denoising ladders, and human review gates for serialized production.
---

# Comic Long Sequence Orchestrator

**Core principle**: Long-form comics require persistent state, coordinated agents, and controlled variation — not just better single-panel consistency.

This skill is responsible for scaling consistency from individual panels to full arcs and series.

## When to Use
- Any project exceeding 50–100 panels
- Serialized or episodic comic production
- When maintaining continuity across time jumps, costume changes, or location shifts
- When implementing human-in-the-loop quality gates

## Key Responsibilities

### 1. World State Tracking
- Maintain persistent state across panels (costume, emotional state, prop locations, lighting conditions)
- Detect and resolve conflicts with the World Bible

### 2. Multi-Agent Pipeline
- Director agent — implemented by `comic-direction/comic-director` (vision, shot plans, camera grammar, final cut)
- Producer agent — implemented by `comic-direction/comic-producer` (contract, schedule, review cadence, escalation)
- Character agent (DNA + state resolution per panel)
- Prompt engineering agent (injects bible + consistency artifacts + the shot plan)
- Render agent (generation + review gate)

### 3. Drift Management
- Periodic re-anchoring to canonical references
- Automated detection of identity or style drift
- Escalation to human review when drift exceeds thresholds

### 4. Generation Strategies for Long Sequences
- Denoising ladders for action continuity
- Batched generation with Consistent Self-Attention where supported
- Controlled re-seeding patterns

## Integration
- Consumes `comic-world-bible-system`, `comic-character-consistency-system`, and `comic-style-memory-system`
- Feeds `comic-image-generation-adapter`

## Design Goals for 1000+ Panel Projects
- Minimal manual intervention per panel
- Clear human review points at key narrative beats
- Full traceability back to the World Bible

---

*Long-sequence consistency is an orchestration and state management problem, not just an image generation problem.*