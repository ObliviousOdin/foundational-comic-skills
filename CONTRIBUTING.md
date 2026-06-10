# Contributing to foundational-comic-skills

This repository is a **contract library**: skills are specifications that agents obey, not prose that humans skim. Contributions are held to the same discipline the skills themselves enforce.

## Ground Rules

1. **The skill tree is canonical.** `skills/IMAGE-DRIVEN-COMIC-STRIP-SKILL-HARNESSES.md` is a historical excerpt; never update it instead of the tree.
2. **Every change runs the validator.** `python3 tools/validate.py` must pass before any commit. CI runs it on every push and pull request.
3. **Semantic versioning per skill.** Patch = clarification; minor = new rules or sections that don't break consumers; major = schema or contract changes. Every bump is reflected in `CHANGELOG.md`.
4. **Derive, don't duplicate.** If content exists in a library skill (formats, patterns, lettering), reference it — never paste a second copy that can drift.
5. **No vapor.** A skill marked ✅ must be fully written. Planned skills live only in layer-index tables, marked `Planned`, and are listed in the validator's planned-skills allowlist.

## Repository Layers (where things go)

| Layer | Contents | Add here when… |
|-------|----------|----------------|
| `comic-core/` | Laws: contracts, gates, patterns, formats, lettering | The rule applies to every style and pipeline |
| `comic-consistency/` | Memory: bible, DNA, style memory, orchestration, generation adapter | The rule is about identity/state surviving across panels |
| `comic-styles/` | Visual grammars (one folder per category) | You are adding a distinct artistic style |
| `comic-direction/` | Judgment: Producer + Director | The rule is about who decides, when |
| `comic-pipeline/` | Workflows per format family | You are wiring layers into an end-to-end flow |
| `comic-production/` | Tooling and platform adapters, export specs | The rule is about delivery, not creation |
| `research/` | Source studies | Cite-able foundations; map them in `research/README.md` |
| `examples/` | Complete worked projects | Show, don't tell |

## Style Skill Schema v2 (Mandatory)

Every `comic-styles/*/*/SKILL.md` follows this exact structure, in this order. The validator enforces headings, ordering, and minimum content.

```markdown
---
name: <kebab-case, must equal the directory name>
version: <semver, 2.0.0+ for schema-v2 files>
category: comic-styles
description: <one sentence: what it looks like + what stories it serves>
---

# <Display Title>

**Style Lock (do not deviate)**

- <5–10 bullets: line quality, tone/color system, rendering texture,
  panel borders & bubble character, era anchor. Concrete and testable —
  name real tools and techniques (e.g., "G-pen outlines", "Ben-Day dots
  at consistent ruling"), never vibes ("high quality").>

## Negative Locks

- <3–8 bullets: what must NEVER appear in this style. These merge into
  the generation negative-prompt block via the world bible.>

## When to Use

- <2–4 bullets: stories, moods, and reference-image cues this style serves>

## When Not to Use

- <2–3 bullets: honest mismatches — and which style to use instead>

## Story Harness (Image-Driven)

- <How the four cues translate in THIS style>
- **SETUP**: <panel-1 guidance with style-native devices>
- **REINFORCE**: <panel-2 guidance with named visual tropes>
- **TURNAROUND**: <payoff tone for this style + what "earned" means here>

## World Guardrail

- <Default settings, era, props, technology policy>

## Dialogue & Lettering

- <Bubble shape and lettering feel; SFX policy; per-panel budget.
  Inherit comic-lettering-and-balloons; state only style deltas.>

## Direction Notes

- <For comic-director: camera tendencies, transition diet, pacing/gutter
  habits, what the shot ladder looks like in this style>

## Consistency Notes

- <For comic-consistency: what drifts FIRST in this style, anchoring
  advice, technique-specific stability (screentone ruling, wash layers,
  cel flats…)>

## Prompt Block

```text
<A ready-to-inject style fragment, 40–90 words, declarative,
present tense, no character or story content — pure style.>
```

## Style Quality Gates

- [ ] <3–6 style-specific checks beyond comic-quality-gates>

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: <formats + patterns from the libraries; RTL eligibility if manga-family>

---

*<One-line closing aphorism in italics.>*
```

### Adding a New Style — Checklist

- [ ] Directory: `comic-styles/<category>/<skill-name>/SKILL.md` (categories: adventure, asian, cartoon, decorative, european, horror, literary, manga, noir, pop-art, sci-fi, western)
- [ ] File follows Schema v2 exactly
- [ ] Row added to the index table in `comic-styles/SKILL.md` with category matching the folder and a native-habitat entry
- [ ] `python3 tools/validate.py` passes
- [ ] `CHANGELOG.md` entry added

## Non-Style Skills

Layer indexes and system skills are freer in structure but must have:
- Complete YAML frontmatter (`name`, `version`, `category`, `description`)
- A closing italic aphorism line
- No references to skills that don't exist (planned skills go in the validator allowlist with a `Planned` table row)

## Templates

Machine-readable templates live under `assets/templates/` inside the owning skill and must parse as YAML. Current templates: character DNA, world bible (example in skill), production brief, shot plan, arc ledger.

## Commit Conventions

Conventional commits, scoped by layer: `feat(styles): …`, `fix(core): …`, `docs(readme): …`. One logical change per commit.

## Release & Versioning of the Repository

The repo itself versions by milestone in `CHANGELOG.md` (Keep-a-Changelog format). Skill versions are independent semver per file.

## Recommended (Owner Decisions)

- **License**: the repository currently has no license (all rights reserved by default). Adding one (MIT/CC-BY for a skill library) is recommended but is the maintainer's call.

---

*A contract library stays alive exactly as long as its contracts stay checkable.*
