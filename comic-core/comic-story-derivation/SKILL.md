---
name: comic-story-derivation
version: 1.0.0
category: comic-core
description: A systematic method for extracting narrative seeds from a single reference image and transforming them into emotionally coherent 3-panel stories.
---

# Comic Story Derivation

**Core principle**: The best stories feel like they were already hiding inside the reference image.

This skill provides the repeatable process for turning visual cues into narrative without falling back on generic templates.

## When to Use
- As the story generation step inside any style skill
- When building new image-driven comic skills
- When auditing why a generated comic feels generic or disconnected from the reference
- When training consistency or memory systems

## Framework

### Step 1: Silent Cue Extraction (Never Skip)
Before writing any story, extract these four cues from the reference image:

| Cue | Extraction Focus | Example from a tired person in a raincoat |
|-----|------------------|-------------------------------------------|
| **MOOD CUE** | Dominant emotional tone | Weary, contemplative, quietly resilient |
| **WARDROBE CUE** | Silhouette + implied lifestyle | Practical, slightly worn, urban professional or traveler |
| **SETTING CUE** | Environment or logical extension | Misty street at dusk, or a quiet train platform |
| **PROP/COMPANION CUE** | One small storytelling anchor | A folded newspaper, a small umbrella, or a stray cat |

**Rule**: If the image gives you nothing for a cue, **invent one small, specific detail** that feels like it belongs to this person — never a generic default.

### Step 2: Emotional Arc Construction
Map the four cues to the three-panel structure:

- **Panel 1 (SETUP)**: Place the character in a situation that externalizes the **mood cue** + **wardrobe cue**. Introduce the **prop/companion cue** as a small inciting detail.
- **Panel 2 (REINFORCE)**: Have the character **engage** with that detail. Deepen the emotional state using visual storytelling appropriate to the style.
- **Panel 3 (TURNAROUND)**: Deliver an emotional reframing that feels earned. The turnaround should feel like a natural (but surprising) extension of the mood cue.

### Step 3: Style Translation
Once the emotional arc exists, translate it into the visual language of the chosen style:

- Retro hand-inked manga → speed lines, sweat drops, expressive eyes
- Gekiga → cinematic angles, rain, heavy shadows
- Shoujo → floral backgrounds, sparkling effects, flowing hair
- Noir → chiaroscuro, cigarette smoke, wet streets

### Step 4: Dialogue Seeding
- Generate 1–2 short lines per panel that **match the mood cue**
- Keep each line under ~8 words
- Dialogue should advance the emotional arc, not explain it

### Anti-Patterns to Avoid
- Using the same three-panel structure regardless of the reference image
- Making the story about the prop instead of the character's emotional state
- Choosing a turnaround that contradicts the mood cue
- Writing dialogue that sounds like it came from a template

## Example Flow (Conceptual)

**Reference**: A young woman in an oversized sweater, looking out a window with a soft, distant expression. Holding a small potted plant.

- **Mood**: Quiet longing, gentle melancholy
- **Wardrobe**: Cozy, introspective, artistic
- **Setting**: Small apartment at golden hour
- **Prop**: The plant (suggests care, patience, hope)

**Resulting Arc**:
- Panel 1: Character watering the plant while looking out at the city
- Panel 2: A small smile forms as she notices something outside
- Panel 3: The turnaround — she places the plant on the windowsill so it can "see" the city too

## Integration Notes
- This derivation method feeds directly into every style skill's Story Harness
- Future memory systems will track recurring emotional patterns across multiple images of the same character
- Quality gates will check whether the final story truly grew from these cues

## Related Skills
- `comic-universal-operating-rule`
- `comic-structural-contract`
- `comic-quality-gates`

---

*The image already contains the story. Our job is to listen.*