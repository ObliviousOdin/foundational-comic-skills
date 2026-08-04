---
name: comic-styles
version: 2.1.0
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

## Current Skills (30)

Categories match the directory layout. **Native habitat** names the canonical format and pattern (from `comic-format-library` and `comic-narrative-patterns`) where the style is strongest — its *primary* pairing, not its only one. Each style's own `Integration` line carries the full set, and the validator checks this column against it. RTL eligibility is noted where the reading-direction rule permits it.

| Category | Skill | Native Habitat | Status |
|----------|-------|----------------|--------|
| Manga | `retro-hand-inked-manga-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` · RTL eligible | ✅ Schema v2 |
| Manga | `gekiga-cinematic-manga` | `3-panel-horizontal` · `slow-burn-reveal` · RTL eligible | ✅ Schema v2 |
| Manga | `shoujo-romance-manga` | `3-panel-horizontal` · `setup-reinforce-turnaround` · RTL eligible | ✅ Schema v2 |
| Manga | `ink-wash-storybook-manga` | `3-panel-horizontal` · `silent-strip` · RTL eligible | ✅ Schema v2 |
| Asian | `manhwa-color-webtoon` | `webtoon-scroll-segment` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Asian | `chibi-kawaii-comic` | `4koma-vertical` · `gag-escalation` | ✅ Schema v2 |
| Asian | `manhua-wuxia-comic` | `multi-page-chapter` · `parallel-action` | ✅ Schema v2 |
| Western | `classic-newspaper-comic` | `3-panel-horizontal` · `gag-escalation` | ✅ Schema v2 |
| Western | `golden-age-superhero-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Western | `silver-age-pop-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Western | `painted-prestige-comic` | `multi-page-chapter` · `slow-burn-reveal` | ✅ Schema v2 |
| European | `ligne-claire-franco-belge` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| European | `moebius-metal-hurlant-sci-fi` | `multi-page-chapter` · `kishotenketsu` | ✅ Schema v2 |
| Horror | `junji-ito-body-horror` | `3-panel-horizontal` · `slow-burn-reveal` · RTL eligible | ✅ Schema v2 |
| Horror | `horror-ec-comics-style` | `3-panel-horizontal` · `slow-burn-reveal` | ✅ Schema v2 |
| Horror | `sin-city-graphic-noir` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Noir | `noir-expressionist-comic` | `3-panel-horizontal` · `slow-burn-reveal` | ✅ Schema v2 |
| Sci-Fi | `cyberpunk-sci-fi-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Sci-Fi | `steampunk-victorian-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Adventure | `bold-woodcut-adventure` | `3-panel-horizontal` · `silent-strip` | ✅ Schema v2 |
| Adventure | `pulp-adventure-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Pop Art | `pop-art-lichtenstein-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Pop Art | `underground-zine-comix` | `3-panel-horizontal` · `gag-escalation` | ✅ Schema v2 |
| Decorative | `elegant-art-nouveau-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Decorative | `watercolor-storybook-comic` | `3-panel-horizontal` · `silent-strip` | ✅ Schema v2 |
| Literary | `autobio-indie-literary-comic` | `3-panel-horizontal` · `setup-reinforce-turnaround` | ✅ Schema v2 |
| Literary | `minimalist-line-webcomic` | `3-panel-horizontal` · `gag-escalation` | ✅ Schema v2 |
| Literary | `reportage-comics-journalism` | `multi-page-chapter` · `parallel-action` | ✅ Schema v2 |
| Cartoon | `saturday-morning-cartoon-comic` | `3-panel-horizontal` · `gag-escalation` | ✅ Schema v2 |
| Cartoon | `rubber-hose-animation-comic` | `3-panel-horizontal` · `gag-escalation` | ✅ Schema v2 |

## Integration
Every style skill must:
1. Load `comic-core`
2. Load `comic-consistency`
3. Enforce its own Style Lock
4. Use the World Bible for story and character context
5. Accept the project contract from `comic-producer` and the shot plan from `comic-director` — style answers *how it's rendered*, never *what gets framed*

---

*Style is not decoration. It is a contract.*
