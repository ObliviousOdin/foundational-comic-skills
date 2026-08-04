---
name: comic-styles
version: 2.0.0
category: comic-styles
description: Modular artistic style skills on Schema v2 — each a self-contained production spec with style locks, negative locks, story harness, direction and consistency notes, and an injectable prompt block.
---

# Comic Styles Layer

**Purpose**: This layer contains individual artistic style skills. Each style enforces its own visual rules while depending on the consistency layer for identity and world coherence.

## Design Philosophy
- One skill per distinct artistic style, on the **Style Skill Schema v2** (see `CONTRIBUTING.md`) — validator-enforced
- Strict style locks (no deviation) paired with negative locks that feed the generation negative block
- Heavy use of research from `STYLE-SPECIFIC-TECHNICAL-MASTERY.md`
- All styles must integrate with the World Bible and consistency systems
- The Producer locks **one style per project**; the Director works inside its Style Lock

## Current Skills (29)

Categories match the directory layout. "Native habitat" suggests the format/pattern pairings (from `comic-format-library` and `comic-narrative-patterns`) where the style is strongest — the default 3-panel strip works everywhere.

| Category | Skill | Native Habitat | Status |
|----------|-------|----------------|--------|
| Manga | `retro-hand-inked-manga-comic` | strip or 4-koma; RTL eligible | ✅ Schema v2 |
| Manga | `gekiga-cinematic-manga` | strip or chapter; slow-burn reveal | ✅ Schema v2 |
| Manga | `shoujo-romance-manga` | strip; RTL eligible | ✅ Schema v2 |
| Manga | `ink-wash-storybook-manga` | strip; silent strip | ✅ Schema v2 |
| Asian | `manhwa-color-webtoon` | **webtoon scroll segment** | ✅ Schema v2 |
| Asian | `chibi-kawaii-comic` | 4-koma; gag escalation | ✅ Schema v2 |
| Asian | `manhua-wuxia-comic` | chapter; parallel action | ✅ Schema v2 |
| Western | `classic-newspaper-comic` | strip; gag escalation | ✅ Schema v2 |
| Western | `golden-age-superhero-comic` | strip or chapter | ✅ Schema v2 |
| Western | `silver-age-pop-comic` | strip or chapter | ✅ Schema v2 |
| Western | `painted-prestige-comic` | chapter; slow-burn reveal | ✅ Schema v2 |
| European | `ligne-claire-franco-belge` | strip or chapter | ✅ Schema v2 |
| European | `moebius-metal-hurlant-sci-fi` | chapter; aspect-rich transitions | ✅ Schema v2 |
| Horror | `junji-ito-body-horror` | slow-burn reveal; RTL eligible | ✅ Schema v2 |
| Horror | `horror-ec-comics-style` | strip; slow-burn reveal | ✅ Schema v2 |
| Horror | `sin-city-graphic-noir` | strip or chapter | ✅ Schema v2 |
| Noir | `noir-expressionist-comic` | strip; slow-burn reveal | ✅ Schema v2 |
| Sci-Fi | `cyberpunk-sci-fi-comic` | strip or webtoon scroll | ✅ Schema v2 |
| Sci-Fi | `steampunk-victorian-comic` | strip or chapter | ✅ Schema v2 |
| Adventure | `bold-woodcut-adventure` | strip; silent strip | ✅ Schema v2 |
| Adventure | `pulp-adventure-comic` | strip or chapter | ✅ Schema v2 |
| Pop Art | `pop-art-lichtenstein-comic` | strip or single-panel | ✅ Schema v2 |
| Pop Art | `underground-zine-comix` | strip; gag escalation | ✅ Schema v2 |
| Decorative | `elegant-art-nouveau-comic` | strip or single-panel | ✅ Schema v2 |
| Decorative | `watercolor-storybook-comic` | strip; silent strip | ✅ Schema v2 |
| Literary | `autobio-indie-literary-comic` | strip or chapter | ✅ Schema v2 |
| Literary | `minimalist-line-webcomic` | strip or single-panel; gag escalation | ✅ Schema v2 |
| Literary | `reportage-comics-journalism` | chapter; parallel action | ✅ Schema v2 |
| Cartoon | `saturday-morning-cartoon-comic` | strip; gag escalation | ✅ Schema v2 |

## Integration
Every style skill must:
1. Load `comic-core`
2. Load `comic-consistency`
3. Enforce its own Style Lock
4. Use the World Bible for story and character context
5. Accept the project contract from `comic-producer` and the shot plan from `comic-director` — style answers *how it's rendered*, never *what gets framed*

---

*Style is not decoration. It is a contract.*
