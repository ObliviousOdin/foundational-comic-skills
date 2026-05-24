---
name: comic-universal-operating-rule
version: 1.0.0
category: comic-core
description: The foundational input contract, story derivation method, and quality principles that apply to every comic generation skill in the system.
---

# Comic Universal Operating Rule

**Core principle**: Style is rigid. Story is image-derived. Quality is non-negotiable.

This skill defines the shared foundation that **every** comic skill in this system must follow.

## When to Use
- As the mandatory first step before applying any style-specific skill
- When creating new comic generation skills
- When auditing or improving existing comic output
- When building consistency layers or pipelines

## Framework

### 1. INPUT CONTRACT
- Accept **one reference image** of a person (or clear subject)
- Extract **only visible, non-sensitive visual cues**:
  - Hairstyle, face shape, outfit silhouette, posture, expression
  - Mood palette, visible props, environment hints
- **Never** infer identity, ethnicity, age, health, religion, personality, profession, or social class
- Redraw the subject as a **completely original comic character** in the target style

### 2. STORY DERIVATION (Image-Driven)
Silently extract four cues from the reference before generating:

| Cue | Purpose | Example Questions |
|-----|---------|-------------------|
| **MOOD CUE** | Emotional tone of the moment | What feeling does the pose/expression suggest? (calm, bold, curious, weary, joyful, contemplative, determined…) |
| **WARDROBE CUE** | Character archetype & era/vibe | What silhouette/era/vibe does the outfit imply? (casual, formal, athletic, cozy, edgy, elegant…) |
| **SETTING CUE** | Environment that supports the mood | Any visible environment hint? If none, choose one that naturally complements wardrobe + mood |
| **PROP/COMPANION CUE** | Small storytelling anchor | Any visible object, animal, or accessory? If none, invent **one** small companion or object that fits the mood and style |

**Rule**: The story must feel like it **grew out of this specific image**, not a fixed template.

### 3. STRUCTURAL CONTRACT (3-Panel Horizontal)
- Output: **One** wide horizontal image (16:9 or 21:9 preferred)
- **Exactly 3 horizontal panels**, left to right
- Narrative arc: **Panel 1 SETUP → Panel 2 REINFORCE → Panel 3 TURNAROUND**
  - Turnaround must be emotionally satisfying and tonally appropriate to the style
- Character consistency across all panels (face, hair, outfit silhouette, line quality)
- Dialogue: 1–2 short bubbles per panel max (~8 words each)
- No extra captions, titles, sound effects (unless style explicitly permits), signs, mastheads, watermarks, or random letters

### 4. QUALITY CHECK (Run Silently Before Final Render)
- [ ] Exactly 3 horizontal panels in wide format
- [ ] Style rules fully obeyed throughout
- [ ] Character remains consistent across panels
- [ ] Story clearly grew from the image's four cues
- [ ] Setup → Reinforce → Turnaround is readable at a glance
- [ ] Ending is tonally appropriate for the chosen style
- [ ] Only permitted text appears — nothing else

## Integration Notes
- Every style skill (`retro-hand-inked-manga-comic`, `gekiga-cinematic-manga`, etc.) must explicitly reference this rule
- Consistency engines and pipeline skills should build on top of this contract
- Future skills (multi-page, vertical webtoon, full chapter) will extend this base

## Related Skills (Planned)
- `comic-structural-contract`
- `comic-quality-gates`
- `comic-story-derivation`
- `comic-character-consistency-system`

---

*This is the root contract. All artistic ability in the system rests on disciplined adherence to these rules.*