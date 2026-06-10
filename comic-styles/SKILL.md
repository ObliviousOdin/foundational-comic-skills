---
name: comic-styles
version: 1.1.0
category: comic-styles
description: Modular artistic style skills. Each style is a self-contained skill that loads comic-core and comic-consistency, then applies strict visual grammar rules derived from traditional comic art techniques.
---

# Comic Styles Layer

**Purpose**: This layer contains individual artistic style skills. Each style enforces its own visual rules while depending on the consistency layer for identity and world coherence.

## Design Philosophy
- One skill per distinct artistic style
- Strict style locks (no deviation)
- Heavy use of research from `STYLE-SPECIFIC-TECHNICAL-MASTERY.md`
- All styles must integrate with the World Bible and consistency systems
- The Producer locks **one style per project**; the Director works inside its Style Lock

## Current Skills (28)

Categories match the directory layout. "Native habitat" suggests the format/pattern pairings (from `comic-format-library` and `comic-narrative-patterns`) where the style is strongest — the default 3-panel strip works everywhere.

| Category | Skill | Native Habitat | Status |
|----------|-------|----------------|--------|
| Manga | `retro-hand-inked-manga-comic` | strip or 4-koma; RTL eligible | ✅ Foundation |
| Manga | `gekiga-cinematic-manga` | strip or chapter; slow-burn reveal | ✅ Foundation |
| Manga | `shoujo-romance-manga` | strip; RTL eligible | ✅ Foundation |
| Manga | `ink-wash-storybook-manga` | strip; silent strip | ✅ Foundation |
| Asian | `manhwa-color-webtoon` | **webtoon scroll segment** | ✅ Foundation |
| Asian | `chibi-kawaii-comic` | 4-koma; gag escalation | ✅ Foundation |
| Asian | `manhua-wuxia-comic` | chapter; parallel action | ✅ Foundation |
| Western | `classic-newspaper-comic` | strip; gag escalation | ✅ Foundation |
| Western | `golden-age-superhero-comic` | strip or chapter | ✅ Foundation |
| Western | `silver-age-pop-comic` | strip or chapter | ✅ Foundation |
| Western | `painted-prestige-comic` | chapter; slow-burn reveal | ✅ Foundation |
| European | `ligne-claire-franco-belge` | strip or chapter | ✅ Foundation |
| European | `moebius-metal-hurlant-sci-fi` | chapter; aspect-rich transitions | ✅ Foundation |
| Horror | `junji-ito-body-horror` | slow-burn reveal; RTL eligible | ✅ Foundation |
| Horror | `horror-ec-comics-style` | strip; slow-burn reveal | ✅ Foundation |
| Horror | `sin-city-graphic-noir` | strip or chapter | ✅ Foundation |
| Noir | `noir-expressionist-comic` | strip; slow-burn reveal | ✅ Foundation |
| Sci-Fi | `cyberpunk-sci-fi-comic` | strip or webtoon scroll | ✅ Foundation |
| Sci-Fi | `steampunk-victorian-comic` | strip or chapter | ✅ Foundation |
| Adventure | `bold-woodcut-adventure` | strip; silent strip | ✅ Foundation |
| Adventure | `pulp-adventure-comic` | strip or chapter | ✅ Foundation |
| Pop Art | `pop-art-lichtenstein-comic` | strip or single-panel | ✅ Foundation |
| Pop Art | `underground-zine-comix` | strip; gag escalation | ✅ Foundation |
| Decorative | `elegant-art-nouveau-comic` | strip or single-panel | ✅ Foundation |
| Decorative | `watercolor-storybook-comic` | strip; silent strip | ✅ Foundation |
| Literary | `autobio-indie-literary-comic` | strip or chapter | ✅ Foundation |
| Literary | `minimalist-line-webcomic` | strip or single-panel; gag escalation | ✅ Foundation |
| Cartoon | `saturday-morning-cartoon-comic` | strip; gag escalation | ✅ Foundation |

## Integration
Every style skill must:
1. Load `comic-core`
2. Load `comic-consistency`
3. Enforce its own Style Lock
4. Use the World Bible for story and character context
5. Accept the project contract from `comic-producer` and the shot plan from `comic-director` — style answers *how it's rendered*, never *what gets framed*

---

*Style is not decoration. It is a contract.*
