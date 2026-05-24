---
name: comic-structural-contract
version: 1.0.0
category: comic-core
description: Defines the precise 3-panel horizontal narrative structure, panel relationships, and emotional arc requirements used across all comic skills.
---

# Comic Structural Contract

**Core principle**: Every comic must follow a clear, readable Setup → Reinforce → Turnaround arc within exactly three horizontal panels.

This skill codifies the structural grammar that gives short-form comics their power and readability.

## When to Use
- When designing or refining any 3-panel comic skill
- When building multi-panel pipelines
- When auditing comic output for narrative clarity
- When creating new story harnesses

## Framework

### Panel Architecture

| Panel | Name | Narrative Function | Visual Weight | Emotional Goal |
|-------|------|--------------------|---------------|----------------|
| **1** | SETUP | Establish character + situation | Medium | Introduce the emotional state from the mood cue |
| **2** | REINFORCE | Deepen the situation or emotional state | Medium-High | Use visual storytelling to intensify the mood |
| **3** | TURNAROUND | Deliver emotional payoff or reframing | High | Create surprise, warmth, irony, or satisfaction appropriate to style |

### Panel Relationship Rules

1. **Left-to-Right Flow**
   - Western reading direction assumed unless style explicitly uses right-to-left
   - Each panel must logically lead into the next

2. **Emotional Escalation**
   - Panel 1 sets the emotional baseline
   - Panel 2 heightens or complicates that emotion
   - Panel 3 delivers a meaningful shift (not random)

3. **Visual Rhythm**
   - Panel sizes can vary slightly for pacing (e.g., wider Panel 3 for impact)
   - Avoid perfectly equal panels unless the style demands uniformity

4. **Gutter Meaning**
   - The space between panels is active — it represents time, emotional transition, or withheld information
   - Do not fill gutters with text or decorative elements unless the style specifically calls for it

### Turnaround Requirements (Style-Dependent)

| Style Category | Turnaround Tone | Example |
|----------------|------------------|---------|
| Cozy / Romance / Shoujo | Warm, uplifting, quietly delightful | Character realizes they are not alone |
| Noir / Gekiga | Earned, honest, sometimes bitter | Character faces an uncomfortable truth |
| Horror | Eerie, ironic, unsettling | The thing they feared was already happening |
| Adventure / Action | Triumphant or surprising | Small victory or clever reversal |
| Literary / Indie | Poignant, ambiguous, or revelatory | Quiet emotional insight |

### Forbidden Patterns
- Random or unmotivated panel 3
- Repeating the same emotional beat across panels
- Ending on a flat statement instead of a reframing
- Using the turnaround for exposition instead of emotional payoff

## Integration Notes
- This contract is referenced by every style skill's Story Harness
- Future extensions (4+ panels, vertical formats, full chapters) will build on this base
- Consistency systems must preserve this arc across panels

## Related Skills
- `comic-universal-operating-rule`
- `comic-quality-gates`
- `comic-story-derivation`

---

*Structure is what separates comic art from illustration. Master the arc.*