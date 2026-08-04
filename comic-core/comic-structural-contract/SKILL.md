---
name: comic-structural-contract
version: 1.2.0
category: comic-core
description: Defines the default 3-panel horizontal narrative structure, panel relationships, and emotional arc requirements — and governs how sanctioned format and pattern variations extend it.
---

# Comic Structural Contract

**Core principle**: Every comic must follow a clear, readable beat arc within a locked structure. The default is Setup → Reinforce → Turnaround in exactly three horizontal panels; variations exist, but only as locked contracts — never as improvisation.

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
   - Western reading direction assumed by default; manga-family styles may lock right-to-left via the project contract's `reading_direction` (see `comic-format-library`) — once locked, all eyelines and gutter logic must obey it
   - Each panel must logically lead into the next

2. **Emotional Escalation**
   - Panel 1 sets the emotional baseline
   - Panel 2 heightens or complicates that emotion
   - Panel 3 delivers a meaningful shift (not random)

3. **Visual Rhythm**
   - In variable-geometry formats, panel sizes can vary for pacing (e.g., wider Panel 3 for impact), and perfectly equal panels should be avoided
   - **Uniformity is mandated by the format, not chosen by the style**: `4koma-vertical` and `2x2-grid-page` fix panel geometry outright, and varying it there breaks the format contract rather than improving the rhythm
   - When geometry is locked, rhythm comes from content density instead — see the pacing instruments in `comic-director`

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

### Sanctioned Variations

This contract defines the **default** structure. Two extension libraries provide disciplined alternatives:

| Library | Provides | Examples |
|---------|----------|----------|
| `comic-format-library` | Alternative canvases and panel counts | 4-koma vertical, webtoon scroll segment, single-panel gag, 2×2 grid, multi-page chapter |
| `comic-narrative-patterns` | Alternative beat arcs | kishōtenketsu, gag escalation, slow-burn reveal, parallel action, silent strip |

Rules of variation:
1. A variation is only valid when **locked in the project contract** by `comic-producer` — defaults apply otherwise
2. Format and pattern must be compatible (a 4-beat pattern needs a 4+ panel format)
3. All other rules in this contract — emotional escalation, gutter meaning, forbidden patterns, turnaround tone — apply to every variation

## Integration Notes
- This contract is referenced by every style skill's Story Harness
- Extended by `comic-format-library` (canvases) and `comic-narrative-patterns` (beat arcs)
- The `comic-direction` layer selects and enforces the locked structure per project
- Consistency systems must preserve the locked arc across panels

## Related Skills
- `comic-universal-operating-rule`
- `comic-quality-gates`
- `comic-story-derivation`
- `comic-format-library`
- `comic-narrative-patterns`

---

*Structure is what separates comic art from illustration. Master the arc.*