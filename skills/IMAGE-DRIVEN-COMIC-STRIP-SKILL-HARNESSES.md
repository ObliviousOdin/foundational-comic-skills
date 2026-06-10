# 25 Image-Driven Comic Strip Skill Harnesses

> **Canonical source note**: This document is the original, portable harness pack for external platforms and tracks the first 25 styles. The **skill tree in this repository is canonical** — where versions, names (e.g., `junji-ito-body-horror` here listed as `horror-junji-ito-manga`), or rules differ, the `comic-styles/`, `comic-core/`, and `comic-direction/` skills win. Newer styles, formats, and narrative patterns exist only in the skill tree.

A portable, versioned skill library for ChatGPT (GPT-4o/DALL-E), Gemini, and Grok Imagine. Every skill follows the same core principle: **style is rigid, story is image-derived.** The uploaded photo seeds the plot, setting, and dialogue — the skill harness supplies only the visual grammar.

***

## Universal Operating Rule

> **Applies to all 25 skills. Each SKILL.md references it as "Apply the UNIVERSAL OPERATING RULE."**

The style-agnostic foundation for every skill in this library — shared input contract, cue-extraction step, structural contract, and quality checklist.[^1][^2][^3]

### INPUT CONTRACT
Use the uploaded image **only** for visible, non-sensitive visual cues: hairstyle, face shape, outfit silhouette, posture, expression, mood palette, and any non-identifying props or environment hints. Do NOT infer identity, ethnicity, age, health, religion, personality, profession, or social class from appearance. Redraw the person completely as an original comic character in the target style.[^4]

### STORY DERIVATION (image-driven)
Before drawing, silently extract four cues from the reference:

1. **MOOD CUE** — What feeling does the pose/expression suggest? (calm, bold, curious, joyful, contemplative, intense, wry…)
2. **WARDROBE CUE** — What silhouette/era/vibe does the outfit imply? (casual, formal, athletic, outdoorsy, artistic, edgy, elegant…)
3. **SETTING CUE** — Any visible environment hint? If none, choose a setting that complements wardrobe and mood.
4. **PROP/COMPANION CUE** — Any visible object, animal, or accessory? If none, invent ONE small companion or object that fits the mood and style.[^5][^6]

The story **must feel like it grew out of this specific image**, not a template.[^7]

### STRUCTURAL CONTRACT
- Output: ONE final image, wide horizontal aspect ratio (16:9 or 21:9 preferred), containing **exactly 3 horizontal panels**, left to right.
- Narrative arc: **Panel 1 SETUP → Panel 2 REINFORCE → Panel 3 TURNAROUND**. The turnaround is style-dependent: warm/uplifting for cozy styles; earned/honest for noir/gekiga; eerie/ironic for horror styles.
- Character consistency: same face, hair, outfit silhouette, and line quality in every panel.[^8]
- Dialogue: 1–2 short bubbles per panel max (~8 words each); generated to fit the mood cue. No extra captions, titles, sound effects (unless the style calls for them), signs, mastheads, watermarks, or random letters.[^9][^10]
- Technology default: none unless the reference image or the skill's World Guardrail explicitly permits it.

### QUALITY CHECK (run silently before final render)
- [ ] 3 horizontal panels, wide format
- [ ] Style rules fully obeyed throughout
- [ ] Character matches reference cues and stays consistent across all panels
- [ ] Story clearly grew from the image's mood/wardrobe/setting cues
- [ ] Setup → Reinforce → Turnaround is readable at a glance
- [ ] Ending is tonally appropriate for the chosen style
- [ ] Only generated dialogue and permitted text appear — nothing else

***

## Skill Index

| # | Skill Name | Category | Color | B&W | Key Style Anchor |
|---|-----------|----------|-------|-----|-----------------|
| 01 | `retro-hand-inked-manga-comic` | Japanese Manga | — | ✓ | Brush pen, screentone, 1970s–80s |
| 02 | `shoujo-romance-manga` | Japanese Manga | — | ✓ | Sparkle eyes, floral backgrounds, emotional |
| 03 | `ink-wash-storybook-manga` | Japanese Manga | — | ✓ | Gray washes, handmade paper, quiet |
| 04 | `gekiga-cinematic-manga` | Japanese Manga | — | ✓ | Realistic, noir-like, cinematic panels |
| 05 | `classic-newspaper-comic` | Western Newspaper | — | ✓ | Bold ink, gag strip, wholesome twist |
| 06 | `golden-age-superhero-comic` | Western Superhero | ✓ | — | Primary colors, Ben-Day, 1938–55 |
| 07 | `silver-age-pop-comic` | Western Superhero | ✓ | — | Dynamic anatomy, Kirby energy, 1956–70 |
| 08 | `ligne-claire-franco-belge` | European Comics | ✓ | — | Uniform line weight, flat color, Hergé |
| 09 | `moebius-metal-hurlant-sci-fi` | European Comics | ✓ | — | Intricate linework, cosmic surrealism |
| 10 | `noir-expressionist-comic` | Noir & Crime | — | ✓ | Chiaroscuro, rain, film noir angles |
| 11 | `sin-city-graphic-noir` | Noir & Crime | Spot | ✓ | Pure B&W + ONE spot color, extreme contrast |
| 12 | `pop-art-lichtenstein-comic` | Pop Art & Experimental | ✓ | — | Ben-Day dots, primary fills, drama |
| 13 | `underground-zine-comix` | Pop Art & Experimental | — | ✓ | Scratchy DIY, irregular, punk energy |
| 14 | `horror-ec-comics-style` | Horror & Dark | ✓ | — | Gothic atmosphere, vintage 1950s dread |
| 15 | `horror-junji-ito-manga` | Horror & Dark | — | ✓ | Obsessive detail, distortion, body horror |
| 16 | `bold-woodcut-adventure` | Adventure & Action | — | ✓ | Carved ink, folkoric, strong silhouettes |
| 17 | `pulp-adventure-comic` | Adventure & Action | ✓ | — | Warm saturated, 1930s–40s, bold staging |
| 18 | `cyberpunk-sci-fi-comic` | Sci-Fi & Speculative | ✓ | — | Neon accents, digital, rain and chrome |
| 19 | `steampunk-victorian-comic` | Sci-Fi & Speculative | ✓ | — | Brass palette, clockwork, Victorian |
| 20 | `elegant-art-nouveau-comic` | Decorative & Fine Art | — | ✓ | Flowing curves, ornamental borders |
| 21 | `watercolor-storybook-comic` | Decorative & Fine Art | ✓ | — | Soft washes, bleeding edges, whimsy |
| 22 | `manhwa-color-webtoon` | Asian Webtoon/Digital | ✓ | — | Clean digital, cinematic lighting, K-drama feel |
| 23 | `chibi-kawaii-comic` | Asian Webtoon/Digital | ✓ | — | 2-head proportion, pastel, emoji expressions |
| 24 | `manhua-wuxia-comic` | Asian Webtoon/Digital | ✓ | — | Calligraphic, jewel tones, martial arts |
| 25 | `autobio-indie-literary-comic` | Literary & Indie | — | ✓ | Personal linework, memoir register, caption-driven |

***

# Japanese Manga Skills (1–4)

## Skill 01 — Retro Hand-Inked Manga Comic

```yaml
---
name: retro-hand-inked-manga-comic
version: 2.0.0
category: Japanese Manga
description: >
  Image-driven 3-panel B&W retro hand-inked manga strip (shōnen/shōjo 1970s–80s).
  Style is fixed; story, setting, and dialogue are extracted from the uploaded
  reference image's mood, wardrobe, setting, and prop/companion cues.
---
```

Apply the UNIVERSAL OPERATING RULE.[^11][^12]

**STYLE LOCK (do not deviate)**
- Retro hand-inked shōnen/shōjo manga, 1970s–80s feel[^13]
- Black and white only — no color, no gray fills beyond screentone
- Clean brush-pen outlines, expressive eyes, soft screentone shading
- Gentle cross-hatching, subtle speed/emotion lines, hand-drawn page texture
- Clean rectangular panel borders, rounded speech bubbles with hand-lettered feel

**STORY HARNESS (image-driven)**
- Derive MOOD, WARDROBE, SETTING, and COMPANION/PROP cues from the reference image
- Build a small, intimate slice-of-life moment that fits those cues
- **Panel 1 SETUP:** introduce character in a setting that matches wardrobe/mood, with a small inciting detail (sound, stranger, object, animal — whatever the image suggests)
- **Panel 2 REINFORCE:** character engages with that detail, deepening the mood; use manga visual tropes (speed lines for action, sparkles for wonder, sweat drops for stress)[^14]
- **Panel 3 TURNAROUND:** an unexpected, warm reframing that leaves the character touched, surprised, or quietly delighted — never sad, ironic, or mean

**WORLD GUARDRAIL:** Default to timeless, pre-digital setting unless reference clearly points elsewhere (sporty outfit → quiet park; cozy sweater → café courtyard; raincoat → misty lantern street). Props natural or handmade unless reference dictates otherwise.

**DIALOGUE RULE:** 1–2 short speech or thought bubbles per panel, max ~8 words each, matching mood cue. No captions, titles, extra sound effects, labels, or random letters.

***

## Skill 02 — Shōjo Romance Manga

```yaml
---
name: shoujo-romance-manga
version: 1.0.0
category: Japanese Manga
description: >
  Image-driven 3-panel shōjo romance manga with flowing hair, floral
  backgrounds, sparkling eyes, and delicate emotional storytelling
  derived from the uploaded reference.
---
```

Apply the UNIVERSAL OPERATING RULE.[^15][^16]

**STYLE LOCK**
- Classic shōjo manga aesthetic (1970s–90s influenced)[^15]
- Large, multi-highlight sparkling eyes; delicate, varied line weight[^16]
- Floral and bubble decorative backgrounds expressing emotion
- Soft, layered hair rendering; elegant costume silhouettes
- Panel borders can be flowery or organic; speech bubbles rounded and gentle
- Black and white with optional selective screentone for flowers and sparkles

**STORY HARNESS (image-driven)**
- Read the reference for emotional cues — shyness, warmth, quiet longing, joy, gentle determination
- Translate wardrobe silhouette into a character archetype (school uniform → quiet everyday romance; flowing outfit → storybook encounter)
- **Panel 1 SETUP:** character in a moment of quiet emotion — a glance, a hesitation, a soft smile — in a setting that echoes their visible mood
- **Panel 2 REINFORCE:** a small meaningful exchange or gesture; use classic shōjo visual language (roses, petals, sparkles, soft close-ups)[^17]
- **Panel 3 TURNAROUND:** a warm emotional resolution — a moment of connection, recognition, or gentle surprise

**WORLD GUARDRAIL:** Schools, gardens, rooftops, quiet cafés, or dreamlike nature settings. No harsh or violent imagery. Technology only if reference insists.

**DIALOGUE RULE:** Sparse, emotionally resonant, soft-toned. 1 bubble per panel preferred. Silence in panel 2 is often the strongest choice.

***

## Skill 03 — Ink-Wash Storybook Manga

```yaml
---
name: ink-wash-storybook-manga
version: 2.0.0
category: Japanese Manga
description: >
  Image-driven 3-panel soft ink-wash storybook manga. Style is fixed; the
  quiet emotional beat, setting, and dialogue are pulled from the uploaded
  reference's mood and cues.
---
```

Apply the UNIVERSAL OPERATING RULE.[^18]

**STYLE LOCK**
- Soft ink-wash storybook manga: delicate brush lines, layered gray ink washes[^18]
- Pale handmade-paper texture, subtle stippling
- Gentle manga facial expressions, generous negative space, atmospheric quiet
- Black, white, and gray only
- Calm panel spacing, thin elegant borders or borderless wash edges