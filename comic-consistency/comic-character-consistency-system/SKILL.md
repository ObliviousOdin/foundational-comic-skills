---
name: comic-character-consistency-system
version: 1.0.0
category: comic-consistency
description: The core engine for maintaining character identity across long sequences. Handles DNA templates, model sheet generation, layered conditioning strategies (LoRA + IP-Adapter + ControlNet), and identity stability vs. expression variation trade-offs.
---

# Comic Character Consistency System

**Core principle**: Character identity must survive hundreds of panels, multiple scenes, costume changes, and expression shifts without becoming generic or drifting.

This skill consumes the World Bible and produces reliable identity locking for production use.

## When to Use
- Any project with recurring characters across 20+ panels
- When building model sheets or expression libraries
- When configuring layered consistency pipelines (multiple techniques at sub-max weights)
- When training or selecting LoRAs / IP-Adapter references

## Key Challenges Addressed
- Identity stability vs. natural expression variation
- Cross-panel feature drift
- Style vs. identity conflict
- Long-sequence semantic aging

## Framework

### 1. DNA Template Management
- Pull canonical DNA from World Bible
- Support per-scene overrides (costume, lighting, emotional state)
- Automatic injection into generation prompts

### 2. Model Sheet Generation
- Front / 3/4 / side / back views from canonical reference
- Expression library (minimum 6 core states)
- Use of low-denoising img2img + ControlNet for structural fidelity

### 3. Layered Conditioning Strategy (Recommended)
For production reliability, use multiple systems at moderate weights rather than one system at maximum strength:

- **FaceID / InstantID / PuLID** (0.6–0.75) → Macro facial geometry
- **ControlNet (OpenPose / Depth / Lineart)** (0.5–0.7) → Pose and expression freedom
- **Style LoRA** (0.7–0.85) → Linework and medium consistency
- **IP-Adapter-Plus** (0.4–0.6) → Skin tone and hair texture

### 4. Identity Stability Techniques
- Denoising ladders for action sequences
- Seed management across related panels
- Periodic re-anchoring to canonical reference

## Integration
- Depends on `comic-world-bible-system`
- Feeds `comic-style-memory-system` and `comic-long-sequence-orchestrator`
- Used by all style skills and generation adapters

## Planned Extensions
- Automated model sheet pipeline
- Expression variation scoring
- Drift detection between panels
- Cross-character interaction rules

---

*Good consistency is not about locking harder — it is about distributing the consistency work across multiple complementary systems.*