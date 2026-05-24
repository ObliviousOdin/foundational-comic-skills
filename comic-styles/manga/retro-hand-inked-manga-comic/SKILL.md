---
name: retro-hand-inked-manga-comic
version: 1.0.0
category: comic-styles
description: Image-driven 3-panel B&W retro hand-inked manga strip (shōnen/shōjo 1970s–80s). Style is fixed; story, setting, and dialogue are extracted from the uploaded reference image via the World Bible and consistency systems.
---

# Retro Hand-Inked Manga Comic

**Style Lock (do not deviate)**

- Retro hand-inked shōnen/shōjo manga, 1970s–80s feel
- Black and white only — no color, no gray fills beyond screentone
- Clean brush-pen outlines, expressive eyes, soft screentone shading
- Gentle cross-hatching, subtle speed/emotion lines, hand-drawn page texture
- Clean rectangular panel borders, rounded speech bubbles with hand-lettered feel

## When to Use
- When the target aesthetic is classic 1970s–80s Japanese manga
- When the reference image suggests slice-of-life, emotional, or dramatic moments
- As the default manga style for testing consistency systems

## Integration Requirements
- Must load `comic-core`
- Must load `comic-consistency` (World Bible + character + style memory)
- Uses `comic-image-generation-adapter` for final output

## Story Harness
- Derive MOOD, WARDROBE, SETTING, and COMPANION/PROP cues from the reference image
- Build a small, intimate slice-of-life moment
- Panel 1 SETUP → Panel 2 REINFORCE → Panel 3 TURNAROUND (warm/uplifting)

## Quality Gates (in addition to core)
- Screentone density appropriate to tone value
- Brush pen line variation present (not mechanically uniform)
- No modern digital artifacts

---

*This is the first modular style skill. All others will follow the same pattern.*