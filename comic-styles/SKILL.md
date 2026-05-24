---
name: comic-styles
version: 1.0.0
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

## Current Skills

| Category | Skill | Status |
|----------|-------|--------|
| Japanese Manga | `retro-hand-inked-manga-comic` | ✅ Foundation |
| Japanese Manga | `gekiga-cinematic-manga` | ✅ Foundation |
| Japanese Manga | `shoujo-romance-manga` | ✅ Foundation |
| Japanese Manga | `manhwa-color-webtoon` | ✅ Foundation |
| Japanese Manga | `chibi-kawaii-comic` | ✅ Foundation |
| Japanese Manga | `manhua-wuxia-comic` | ✅ Foundation |
| Horror | `junji-ito-body-horror` | ✅ Foundation |
| Horror | `horror-ec-comics-style` | ✅ Foundation |
| Noir | `noir-expressionist-comic` | ✅ Foundation |
| European | `moebius-metal-hurlant-sci-fi` | ✅ Foundation |
| European | `ligne-claire-franco-belge` | ✅ Foundation |
| Sci-Fi | `cyberpunk-sci-fi-comic` | ✅ Foundation |
| Sci-Fi | `steampunk-victorian-comic` | ✅ Foundation |
| Adventure | `bold-woodcut-adventure` | ✅ Foundation |
| Adventure | `pulp-adventure-comic` | ✅ Foundation |
| Decorative | `elegant-art-nouveau-comic` | ✅ Foundation |
| Literary | `autobio-indie-literary-comic` | ✅ Foundation |
| Pop Art | `pop-art-lichtenstein-comic` | ✅ Foundation |
| Pop Art | `underground-zine-comix` | ✅ Foundation |
| Western | `classic-newspaper-comic` | ✅ Foundation |
| Western | `golden-age-superhero-comic` | ✅ Foundation |
| Western | `silver-age-pop-comic` | ✅ Foundation |
| ... | (0 more styles) | Complete |

## Integration
Every style skill must:
1. Load `comic-core`
2. Load `comic-consistency`
3. Enforce its own Style Lock
4. Use the World Bible for story and character context

---

*Style is not decoration. It is a contract.*