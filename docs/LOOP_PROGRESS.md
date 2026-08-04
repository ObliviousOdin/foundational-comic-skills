# Continuous Maintenance Ledger

Durable memory for the continuous hardening loop. This file is the first thing to read
when resuming work: it holds the cycle counter, the rolling backlog, and the notes the
next session needs.

**Session start:** 2026-08-04
**Current cycle:** 2 complete — next cycle starts at 3
**Commits this session:** 10
**Baseline at session start:** 54 skills (28 styles), validator green, 5 pytest tests passing
**Current state:** 56 skills (30 styles), validator green, 38 pytest tests passing, CI runs both

## How This Loop Works

One cycle = up to 5 atomic, validated, conventionally-named commits. Every commit clears
the pre-commit checklist (`python3 tools/validate.py` exit 0, `python3 -m pytest tests/ -q`
green, `git diff --check` clean, indexes and `CHANGELOG.md` updated when the change
requires it). Fewer than 5 commits is correct when fewer than 5 genuinely high-value
atomic improvements exist — padding is a contract violation, not a shortfall.

## Backlog (rolling, prioritized)

Ordered by value density: contract enforcement first, then coverage, then documentation.

### Validator & Tests (highest leverage — every future contribution inherits these)

1. Validate that every `Native habitat` entry in the style index names a real format/pattern from the core libraries — the index makes routing promises nothing checks
2. Require ≥2 bullets in `When to Use` and `When Not to Use`
3. Add `--style <path>` single-file validator mode for fast authoring loops
4. Validator error output: group violations by file rather than a flat list (30 styles makes flat output hard to act on)
5. Check that `Integration` native-habitat pattern names resolve, same as formats
6. Exit-code contract test: run `tools/validate.py` end-to-end as a subprocess and assert 0 on the clean tree (nothing currently tests `main()`)

### Style Coverage (fill real category gaps, Schema v2 only)

7. Ukiyo-e woodblock sequential (Asian — no pre-modern Japanese print grammar)
8. Risograph limited-palette zine print (Pop Art — technique-native, misregistration as a lock)
9. Sunday-page adventure illustration, Foster/Raymond school (Adventure)
10. Marcinelle-school *gros nez* humour BD (European — only two European styles)
11. Atomic-age retro-futurism (Sci-Fi)
12. Diagrammatic geometric literary comics (Literary — architecture-of-the-page school)
13. Illuminated-manuscript marginalia (Decorative)
14. Silhouette cut-paper theatre (Decorative)

### Examples & Worked Proof

15. 4-koma worked project (format × `kishotenketsu` × a manga-family style)
16. Webtoon scroll worked project (scroll-gap timing + emotional arc ledger in use)
17. Silent-strip worked project (the hardest directorial test, undemonstrated)
18. `examples/README.md` index row for every example added

### Layer Depth

19. `comic-core/comic-quality-gates`: explicit style-purity gate referencing the Prompt Block trust boundary
20. `comic-consistency`: negative-library taxonomy (identity bleed / style bleed / era bleed / anatomy bleed)
21. `comic-direction/comic-director`: shot-ladder reference table (which shot answers which beat)
22. `comic-production/comic-export-and-publish`: print CMYK gate refinement
23. `research/`: color and palette science for sequential art, mapped into the traceability table
24. `research/`: lettering typography history, feeding `comic-lettering-and-balloons`
25. `comic-world-bible-system`: source-note protocol for depicted-fact traceability — `reportage-comics-journalism` requires it and nothing implements it yet

### Documentation Accuracy

26. README quickstart prints `OK: repository contracts hold`; the validator actually prints `All repository contracts hold.` — fix the sample
27. README validator description lists five checks; the Prompt Block and redirect rules are not among them
28. Hermes integration notes: how an agent loads the layers in order

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
- The reportage style introduced a source-note obligation on the world bible (depicted
  facts must trace). Backlog item 25 closes that loop in `comic-world-bible-system` — it
  is the only open item where a shipped style depends on something not yet implemented,
  so it outranks its position in the Layer Depth section.
- New validator checks now ship with their tests in the same commit; cycle 1 separated
  them only because that suite covered pre-existing checks. Mutation-test each new guard
  before committing — a green suite proves nothing until you have watched it go red.

---

*A loop without a ledger is just a process that forgets.*
