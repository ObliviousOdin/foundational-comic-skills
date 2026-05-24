---
name: comic-quality-gates
version: 1.0.0
category: comic-core
description: A rigorous, multi-layer quality evaluation system that prevents generic AI output and enforces human-like artistic standards across all comic skills.
---

# Comic Quality Gates

**Core principle**: No comic leaves the system without passing every gate. Quality is not subjective — it is measurable.

This skill defines the layered evaluation framework that separates professional-grade comic work from typical AI generation.

## When to Use
- As the final checkpoint before rendering any comic
- When building automated or semi-automated pipelines
- When training or fine-tuning models on comic output
- When creating new style skills (define style-specific gates)

## Framework

### Layer 1: Structural Gate (Non-Negotiable)
- [ ] Exactly **3 horizontal panels** in a single wide image (16:9 or 21:9)
- [ ] Clear left-to-right reading order
- [ ] No missing panels, no extra panels, no vertical stacking
- [ ] Panel borders are clean and consistent with style

### Layer 2: Character Consistency Gate
- [ ] Same face structure across all three panels
- [ ] Same hairstyle and hair volume
- [ ] Same outfit silhouette (not just color)
- [ ] Consistent line weight and rendering style for the character
- [ ] No "face drift" or sudden changes in age/expression baseline

### Layer 3: Story Integrity Gate
- [ ] Story clearly derives from the four image cues (Mood, Wardrobe, Setting, Prop/Companion)
- [ ] Setup → Reinforce → Turnaround arc is **readable at a glance**
- [ ] Panel 3 delivers a genuine emotional reframing (not random or flat)
- [ ] No exposition dumping in dialogue

### Layer 4: Style Fidelity Gate
- [ ] Every style lock rule is followed without deviation
- [ ] Line quality, texture, color (or B&W treatment), and decorative elements match the chosen style exactly
- [ ] Background treatment is appropriate to the style (screentone, floral, flat color, etc.)

### Layer 5: Text & Dialogue Gate
- [ ] Maximum 1–2 speech/thought bubbles per panel
- [ ] Each bubble ≤ ~8 words
- [ ] Dialogue matches the mood cue and emotional arc
- [ ] No captions, titles, sound effects, signs, mastheads, watermarks, or random letters (unless style explicitly permits)
- [ ] Text is legible and properly placed within bubbles

### Layer 6: Artistic Life Gate (The Human-Like Test)
This is the most important and hardest gate. Ask:
- [ ] Does the linework feel **alive** (varying pressure, intentional imperfections, breathing room) rather than mechanically perfect?
- [ ] Is there **negative space** used meaningfully?
- [ ] Does the character feel like they have **inner life** beyond the pose?
- [ ] Would a human artist be proud of this panel composition?
- [ ] Does it avoid the "AI comic" tells (overly symmetrical faces, plastic skin, repetitive eye sparkle, generic backgrounds)?

## Failure Modes to Catch
- Generic "three panel story" that could apply to any character
- Beautiful style but no emotional arc
- Consistent character but boring or random story
- Perfect technical execution but lifeless result

## Integration Notes
- This gate system should be referenced in every style skill's Quality Check section
- Future consistency engines and pipelines will include automated checks against these gates
- Human review should focus primarily on **Layer 6 (Artistic Life)**

## Related Skills
- `comic-universal-operating-rule`
- `comic-structural-contract`
- `comic-character-consistency-system` (planned)

---

*Technical correctness is table stakes. Artistic life is the goal.*