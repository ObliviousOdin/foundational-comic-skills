# Changelog

Repository milestones. Individual skills carry their own semver in frontmatter.

Format: [Keep a Changelog](https://keepachangelog.com/). Dates are merge dates.

## [Unreleased]

### Added
- `comic-styles/literary/reportage-comics-journalism`: drawn nonfiction in the alternative-press reportage tradition — hatch-only value, researched specificity, unidealized faces, licensed caption boxes carrying observed fact, and a negative lock against fabricated documentary detail
- `comic-styles/cartoon/rubber-hose-animation-comic` (30 styles): late-1920s theatrical cartoon grammar — boneless hose limbs, circular construction, grey-wash monochrome, performing scenery, and licensed musical SFX
- **Prompt Block trust boundary**: the validator now enforces the 40–90 word budget, rejects injection surfaces (pronouns, imperatives, meta-instruction tokens, story content, quoted literals), and fails builds where two styles inject near-identical fragments (≥60% vocabulary overlap)
- `When Not to Use` redirects are resolved against the style tree — a typo'd routing instruction no longer ships green
- `tests/test_validate.py`: 33 contract tests covering the validator's own checks; CI now runs the suite alongside the validator
- `docs/LOOP_PROGRESS.md`: continuous-maintenance ledger with the rolling backlog

## [0.3.0] — 2026-06-10 · "Deep & Sustainable"

### Added
- **Sustainability infrastructure**: `tools/validate.py` (frontmatter, Style Schema v2, index↔directory sync, cross-reference resolution, YAML health), CI workflow (`.github/workflows/validate.yml`), `CONTRIBUTING.md` with the Style Skill Schema v2 spec
- **Style Skill Schema v2**: all 28 style skills rewritten from ~27-line stubs to full production specs (negative locks, story harness, world guardrail, dialogue & lettering deltas, direction notes, consistency notes, injectable prompt block, style-specific quality gates)
- `comic-core/comic-lettering-and-balloons`: balloon taxonomy, placement law, reading-order rules, SFX policy
- **Multi-character support**: input contract accepts 1–3 references; RELATIONSHIP cue in story derivation; multi-character scene rules (DNA stacking, identity-bleed negatives, contrast anchors, paired 180° axis) in the character consistency system
- `comic-pipeline/comic-emotional-arc-orchestrator` + arc ledger template: series-level emotional throughlines, episode targets, continuity debt
- **Prompt assembly contract** in `comic-image-generation-adapter` v1.1: canonical 7-block order, budget rule, backend dialects, generation log
- `comic-production/comic-export-and-publish`: platform matrix (Instagram/X/webtoon/print/PDF), lettering minimums, re-cut rules, naming, archival
- `examples/rabot-strip-001/`: complete worked project (brief → bible → shot plan → assembled prompt → RETAKE → sign-off)
- `research/README.md`: research→skill traceability map
- Anti-template variation check in `comic-story-derivation` (series-level story diversity)

### Fixed
- Dangling `comic-emotional-arc-orchestrator` reference (skill now exists)
- Style index now validator-enforced against the directory tree

## [0.2.0] — 2026-06-10 · "Direction & Variation"

### Added
- `comic-direction/` layer: `comic-producer` (contract, greenlight, review cadence, sign-off) and `comic-director` (vision, shot plans, camera grammar, final cut) with YAML templates
- `comic-core/comic-format-library`: 6 sanctioned canvases (3-panel default, 4-koma, webtoon scroll, single-panel, 2×2 grid, multi-page chapter) + reading-direction rule
- `comic-core/comic-narrative-patterns`: 6 sanctioned beat arcs (default, kishōtenketsu, gag escalation, slow-burn reveal, parallel action, silent strip) + McCloud transition guidance
- Pipelines: `comic-4koma-pipeline`, `comic-webtoon-scroll-pipeline`, `comic-multi-page-chapter-pipeline`; direction stages embedded in the 3-panel pipeline
- Styles: `minimalist-line-webcomic`, `painted-prestige-comic`, `saturday-morning-cartoon-comic` (28 total)
- `exports/README.md` (was referenced but missing)

### Changed
- Core contracts to v1.1: quality gates validate against the locked format/pattern instead of hardcoding 3-panel horizontal (resolves the manhwa-webtoon contradiction)

### Fixed
- `ink-wash-storybook-manga` moved from `sci-fi/` to `manga/`
- Styles index: 22→28 rows, categories matched to directories
- Stale "Planned" lists naming skills that already existed
- README structure (3 missing directories, phantom `exports/`)

## [0.1.0] — 2026-05 · Initial Foundation

- `comic-core` contracts, `comic-consistency` stack with world bible system, 25 foundation style skills, 6 research documents, original harness pack
