# Continuous Maintenance Ledger

Durable memory for the continuous hardening loop. This file is the first thing to read
when resuming work: it holds the cycle counter, the rolling backlog, and the notes the
next session needs.

**Session start:** 2026-08-04
**Current cycle:** 5 complete — next cycle starts at 6
**Commits this session:** 27 (cycles 1–2 merged via PR #4; cycles 3–4 via PR #5)
**Baseline at session start:** 54 skills (28 styles), validator green, 5 pytest tests passing
**Current state:** 56 skills (30 styles), 2 worked examples, validator green, 67 pytest tests passing

## How This Loop Works

One cycle = up to 5 atomic, validated, conventionally-named commits. Every commit clears
the pre-commit checklist (`python3 tools/validate.py` exit 0, `python3 -m pytest tests/ -q`
green, `git diff --check` clean, indexes and `CHANGELOG.md` updated when the change
requires it). Fewer than 5 commits is correct when fewer than 5 genuinely high-value
atomic improvements exist — padding is a contract violation, not a shortfall.

## Backlog (rolling, prioritized)

Ordered by value density: contract enforcement first, then coverage, then documentation.

### Validator & Tests (highest leverage — every future contribution inherits these)

1. `comic-lettering-and-balloons` is the last unaudited layer skill for the 3-panel defect class — the per-panel bubble budget may assume strip length
2. `--style` skips whole-corpus checks by necessity; print a one-line reminder so authors know a full run is still required
3. Style index `Native Habitat` column is prose ("strip or chapter") while `Integration` uses canonical names — reconcile so the column is checkable too
4. `comic-universal-operating-rule` and the pipelines still describe the 3-panel default in places that read as universal; re-read with the defect class in mind

### Style Coverage (fill real category gaps, Schema v2 only)

5. Ukiyo-e woodblock sequential (Asian — no pre-modern Japanese print grammar)
6. Risograph limited-palette zine print (Pop Art — technique-native, misregistration as a lock)
7. Sunday-page adventure illustration, Foster/Raymond school (Adventure)
8. Marcinelle-school *gros nez* humour BD (European — only two European styles)
9. Atomic-age retro-futurism (Sci-Fi)
10. Diagrammatic geometric literary comics (Literary — architecture-of-the-page school)
11. Illuminated-manuscript marginalia (Decorative)
12. Silhouette cut-paper theatre (Decorative)

### Examples & Worked Proof

Outranks its position — see the notes below. Each new format has surfaced a real defect.

13. Webtoon scroll worked project (scroll-gap timing + arc ledger in use); expect it to test whether the lettering budget assumes strip length
14. Silent-strip worked project (the hardest directorial test, undemonstrated)
15. Multi-page chapter worked project (page-turn beats have no filled-in artifact anywhere)

### Layer Depth

16. `comic-consistency`: negative-library taxonomy (identity bleed / style bleed / era bleed / anatomy bleed)
17. `comic-production/comic-export-and-publish`: print CMYK gate refinement
18. `research/`: color and palette science for sequential art, mapped into the traceability table
19. `research/`: lettering typography history, feeding `comic-lettering-and-balloons`
20. `research/README.md`: add rows for contracts that now exist but trace to no study (Prompt Block trust boundary, source register)

### Documentation Accuracy

21. Hermes integration notes: how an agent loads the layers in order
22. `docs/showcase/README.md` accuracy pass against the 30-style tree
23. `CHANGELOG.md` `[Unreleased]` needs the cycle 3–5 work (provenance, Layer 0, the four defect fixes)

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
