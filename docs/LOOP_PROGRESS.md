# Continuous Maintenance Ledger

Durable memory for the continuous hardening loop. This file is the first thing to read
when resuming work: it holds the cycle counter, the rolling backlog, and the notes the
next session needs.

**Session start:** 2026-08-04
**Current cycle:** 9 complete — next cycle starts at 10
**Commits this session:** 54 (cycles 1–8 merged via PRs #4–#9)
**Baseline at session start:** 54 skills (28 styles), validator green, 5 pytest tests passing
**Current state:** 56 skills (30 styles), 5 worked examples, validator green, 103 pytest tests passing
**Formats built:** 5 of 6 sanctioned — only `2x2-grid-page` remains unbuilt

**Commit identity:** commits are authored `obliviousodin <11676741+ObliviousOdin@users.noreply.github.com>`
with no AI co-author trailer, by owner instruction. `main` history was rewritten once
(2026-08-04) to apply this retroactively; the repo's original "no force-push" invariant was
explicitly overridden for that operation and should be treated as superseded.

## How This Loop Works

One cycle = up to 5 atomic, validated, conventionally-named commits. Every commit clears
the pre-commit checklist (`python3 tools/validate.py` exit 0, `python3 -m pytest tests/ -q`
green, `git diff --check` clean, indexes and `CHANGELOG.md` updated when the change
requires it). Fewer than 5 commits is correct when fewer than 5 genuinely high-value
atomic improvements exist — padding is a contract violation, not a shortfall.

## Backlog (rolling, prioritized)

Ordered by value density: contract enforcement first, then coverage, then documentation.

### Validator & Tests (highest leverage — every future contribution inherits these)

1. Consider a validator heuristic for the format-scope defect class: flag unqualified "per strip" / "all three panels" phrasing in `comic-core`/`comic-direction`. Semantic, so it would have to be a WARN, not a FAIL — judge whether the false-positive rate is tolerable before building it

### Examples & Worked Proof (outranks style coverage — every new format has surfaced a real defect, now 4 for 4)

2. `2x2-grid-page` worked project — the last unbuilt format after that; shares the locked-geometry constraint with 4-koma but adds the T-rule and Z-path reading
3. Silent-strip worked project (a *pattern*, not a format — the hardest directorial test, undemonstrated)

### Style Coverage (fill real category gaps, Schema v2 only)

4. Ukiyo-e woodblock sequential (Asian — no pre-modern Japanese print grammar)
5. Risograph limited-palette zine print (Pop Art — technique-native, misregistration as a lock)
6. Sunday-page adventure illustration, Foster/Raymond school (Adventure)
7. Marcinelle-school *gros nez* humour BD (European — only two European styles)
8. Atomic-age retro-futurism (Sci-Fi)
9. Diagrammatic geometric literary comics (Literary — architecture-of-the-page school)
10. Illuminated-manuscript marginalia (Decorative)
11. Silhouette cut-paper theatre (Decorative)

### Layer Depth

12. **Documentary/comics-journalism research study** — `research/README.md` now names this as the one enforced contract resting on assumed practice rather than a cite-able source
13. `comic-consistency`: negative-library taxonomy (identity bleed / style bleed / era bleed / anatomy bleed)
14. `comic-production/comic-export-and-publish`: print CMYK gate refinement
15. `research/`: color and palette science for sequential art, mapped into the traceability table
16. `research/`: lettering typography history, feeding `comic-lettering-and-balloons`

### Documentation Accuracy

17. Hermes integration notes: how an agent loads the layers in order
18. `docs/showcase/README.md` accuracy pass against the 30-style tree

## Recently Completed

**Cycle 1 (2026-08-04) — 5 commits, validator and tests green throughout**

- `docs(docs)`: this ledger
- `feat(tools)`: 40–90 word Prompt Block budget enforced (spec existed since Schema v2, nothing checked it)
- `feat(tools)`: Prompt Block injection guard — pronouns, imperatives, meta-instruction tokens, story content, quoted literals
- `test(tests)`: 25 validator contract tests; mutation-verified (disabling purity fails 5, widening the ceiling fails 1)
- `feat(styles)`: `reportage-comics-journalism` — first nonfiction style; index 28→29, CHANGELOG opened at Unreleased

**Cycle 2 (2026-08-04) — 5 commits, validator and tests green throughout**

- `chore(tests)`: CI runs the pytest suite alongside the validator, both steps named
- `feat(tools)`: `When Not to Use` redirects resolved against the style tree — two distinct failure modes reported (no such skill / skill but not a style)
- `feat(tools)`: Prompt Block collision detection at 0.60 vocabulary overlap, threshold measured against the corpus rather than guessed
- `docs(docs)`: Prompt Block trust boundary documented in `CONTRIBUTING.md` with the reason behind each rule
- `feat(styles)`: `rubber-hose-animation-comic` — Cartoon was a one-style category; index 29→30

**Cycle 3 (2026-08-04) — 5 commits, validator and tests green throughout**

- `feat(consistency)`: world-bible `source_register` (schema section 6) for nonfiction provenance; 1.1.0→1.2.0
- `feat(tools)`: provenance enforced for `production_mode: nonfiction` bibles — fiction untouched
- `feat(tools)`: native-habitat names resolved against the core libraries, vocabulary derived not restated
- `feat(tools)`: `--style` single-file authoring mode; shared reporting tail; `rel()` no longer raises on outside paths
- `docs(docs)`: README validator documentation corrected against live output

**Cycle 4 (2026-08-04) — 5 commits, validator and tests green throughout**

- `feat(examples)`: `rabot-4koma-002` — second worked project; 4koma × kishotenketsu × chibi, bible referenced not copied
- `test(tests)`: `tests/test_examples.py` — parametrized per project, so example #3 is covered on arrival
- `feat(tools)`: ≥2 bullets required in the routing sections
- `feat(core)`: quality-gates **Layer 0**, the pre-generation prompt assembly gate; 1.1.0→1.2.0
- `fix(direction)`: pacing rules scoped to variable-geometry formats; 1.0.0→1.1.0

**Cycle 5 (2026-08-04) — 5 commits, validator and tests green throughout**

The defect-class audit. Three more instances found and fixed, all the same shape:
a rule written against the 3-panel default and stated as universal.

- `fix(core)`: `comic-structural-contract` — panel uniformity attributed to the format, not the style; 1.1.0→1.2.0
- `fix(core)`: `comic-quality-gates` Layer 2 checked "all three panels"; now every panel in the locked format; 1.2.0→1.3.0
- `fix(core)`: `comic-story-derivation` mapped cues to three panels; now to the locked pattern's beats, with a per-pattern table; 1.1.0→1.2.0
- `feat(direction)`: shot-ladder reference table — which rung answers which question, and what overuse costs; 1.1.0→1.2.0
- `feat(tools)`: validator violations grouped under the owning file

**Cycle 6 (2026-08-04) — 5 commits, validator and tests green throughout**

Closed the defect-class audit and turned it into a preventive rule.

- `fix(core)`: `comic-lettering-and-balloons` — scarce elements rationed "per strip"; unit now derives from the locked format. `single-panel-gag` was a hard contradiction (the silence rule forbade the text the format allows); 1.0.0→1.1.0
- `docs(docs)`: `CONTRIBUTING.md` ground rule 6 — every rule names its scope, with all five defects tabled and the diagnostic stated
- `docs(docs)`: `CHANGELOG.md` `[Unreleased]` caught up through cycles 3–6, with the five fixes grouped as one defect class
- `feat(tools)`: `--style` warns that index sync and collision checks were skipped
- `docs(research)`: contracts that cite no study mapped, with the source-register gap named as an open research need

**Audit result**: `comic-universal-operating-rule` and `comic-image-generation-adapter`
came back clean — both already say "Default" or "e.g.". The defect class closes at five
instances. No sixth fix was invented to reach a count.

**Cycle 7 (2026-08-04) — 5 commits, validator and tests green throughout**

Built the serialized format; it surfaced two defects, holding the pattern at 3 for 3.

- `feat(examples)`: `rabot-webtoon-003` — first serialized project and the repository's first filled-in **arc ledger**, including a missed target recorded as arc debt rather than re-rolled
- `feat(pipeline)`: open bible change requests block the shot plan that needs them; 1.0.0→1.1.0
- `fix(direction)`: the counter-vector eyeline licensed under three conditions; 1.2.0→1.3.0
- `test(tests)`: assembled-prompt canonical block order + STYLE-first, parametrized per project
- Test count 69→80; the parametrized example suite picked up the new project automatically

**Cycle 8 (2026-08-04) — 5 commits, validator and tests green throughout**

Built the last unbuilt format. It surfaced two defects, holding the pattern at 4 for 4.

- `feat(pipeline)`: **chapter-map template** — the pipeline mandated the artifact three times and shipped no template; 1.0.0→1.1.0, CONTRIBUTING inventory updated
- `test(tests)`: the shot-plan/brief pattern check assumed one pattern per project, which chapters contradict by design — **the format-scope defect class, found inside the test suite**
- `feat(examples)`: `lamplighter-chapter-001` — cold start in a new world, 3 scenes composing 3 patterns, page-turn beats, the single rationed splash
- Test count 80→89

**Cycle 9 (2026-08-04) — 5 commits, validator and tests green throughout**

Built the second-smallest format; it found a contradiction, holding the pattern at 5 for 5.

- `fix(styles)`: `minimalist-line-webcomic` and `elegant-art-nouveau-comic` forbade captions outright while claiming `single-panel-gag` as native habitat, where the format grants one — **defects 6 and 7** of the format-scope class; both 2.0.0→2.1.0
- `feat(examples)`: `deskplant-gag-001` — implied beats that are never drawn, a `not_applicable` block, the smallest passing bible
- `test(tests)`: arc-ledger and chapter-map validation (7 checks; proof panels, recorded debt, bible-backed states, recto/verso alternation, page coverage, panel-count range)
- `refactor(styles)`: index habitat column rewritten in canonical vocabulary, derived from each skill's Integration line; 2.0.0→2.1.0
- `feat(tools)`: index habitat column verified against each skill — the skill is the authority, the index follows

Test count 89→103.

## Notes for the Next Cycle

- `pytest` is not installed in a fresh container: `python3 -m pip install pytest pyyaml` before running the suite.
- The validator degrades gracefully without `pyyaml` (warns, skips YAML checks) — never make that path fatal.
- All 30 Prompt Blocks measure 56–69 words with zero pronouns and zero imperative verbs.
  The purity checks enforce an invariant the corpus already satisfied — keep it that way.
- `CHANGELOG.md` is at `0.3.0`; new work accumulates under `## [Unreleased]` (now open).
- Purity-guard patterns were tuned against the corpus and legitimate craft vocabulary
  survives: "scroll reading", "character poses", "on-model", "no gradients". Any future
  pattern added to `PROMPT_BLOCK_FORBIDDEN` must be re-scanned against all styles first —
  `tests/test_validate.py::test_every_style_prompt_block_is_within_budget_and_pure` is the
  backstop, but scan before committing rather than after.
- **Building in an unused format has now surfaced a defect five times out of five.**
  4-koma found the pacing rule; webtoon found two (an arc-ledger field with no procedure
  behind it, and an eyeline rule with no exception clause); chapter found two more (a
  mandated artifact with no template, and the pattern-agreement test asserting a rule that
  only held for the formats built so far). This remains the single most productive activity
  in the backlog. Two sanctioned formats are still unbuilt: `single-panel-gag` and
  `2x2-grid-page`.
- **The defect class is not confined to skills.** Cycle 8 found an instance in
  `tests/test_examples.py` — a check written against the three formats that existed at the
  time and stated as universal. Apply ground rule 6's diagnostic to tests and templates too,
  not only to skill prose.
- Both cycle-7 defects were found by *writing a filled-in artifact and hitting a rule that
  the artifact had to argue around in a note*. That is the tell: if a worked example needs
  a footnote explaining why it is allowed to do something, the rule is missing a clause.
- **The format-scope defect class is closed at five instances and now has a preventive
  rule** (`CONTRIBUTING.md` ground rule 6). If a sixth appears, it most likely arrives with
  a new format rather than a new rule — adding a seventh format to `comic-format-library`
  should trigger a re-audit of every unqualified rule in `comic-core` and `comic-direction`.
- The reportage style's source-note obligation is now closed: `comic-world-bible-system`
  carries `source_register` and the validator enforces it for nonfiction bibles. No
  shipped style currently depends on anything unimplemented — keep it that way, and if a
  new style introduces an obligation, land the mechanism in the same cycle.
- Style coverage is the largest open area by count (8 queued) but the corpus is at 30
  across 12 categories, so marginal value per new style is falling.
- **The most valuable findings came from building an example, not from auditing.** The
  4-koma project could not obey `comic-director`'s pacing rule; chasing that one defect
  through the layers found three more of the same shape (structural contract, quality
  gates Layer 2, story derivation). Four defects, one root cause: rules written against
  the 3-panel default and stated as universal.
- **The diagnostic that found them all**: take any rule stated unconditionally and ask
  whether `4koma-vertical` or `webtoon-scroll-segment` can obey it. If not, the rule is
  scoped wrong, not the format. Apply this to any new contract before committing it.
- This is why the remaining example backlog outranks its position: a webtoon or
  silent-strip worked project is the cheapest way to find rules that only ever worked by
  coincidence. Build in an unused format and the defects surface themselves.
- New validator checks now ship with their tests in the same commit; cycle 1 separated
  them only because that suite covered pre-existing checks. Mutation-test each new guard
  before committing — a green suite proves nothing until you have watched it go red.

---

*A loop without a ledger is just a process that forgets.*
