# Continuous Maintenance Ledger

Durable memory for the continuous hardening loop. This file is the first thing to read
when resuming work: it holds the cycle counter, the rolling backlog, and the notes the
next session needs.

**Session start:** 2026-08-04
**Current cycle:** 1 complete — next cycle starts at 2
**Commits this session:** 5
**Baseline at session start:** 54 skills (28 styles), validator green, 5 pytest tests passing
**Current state:** 55 skills (29 styles), validator green, 30 pytest tests passing

## How This Loop Works

One cycle = up to 5 atomic, validated, conventionally-named commits. Every commit clears
the pre-commit checklist (`python3 tools/validate.py` exit 0, `python3 -m pytest tests/ -q`
green, `git diff --check` clean, indexes and `CHANGELOG.md` updated when the change
requires it). Fewer than 5 commits is correct when fewer than 5 genuinely high-value
atomic improvements exist — padding is a contract violation, not a shortfall.

## Backlog (rolling, prioritized)

Ordered by value density: contract enforcement first, then coverage, then documentation.

### Validator & Tests (highest leverage — every future contribution inherits these)

1. Run the pytest suite in CI alongside the validator — CI currently proves nothing about the 30 new tests (`.github/workflows/validate.yml`)
2. Resolve backticked *style-skill* cross-references (`When Not to Use` redirect targets are unchecked — `REF_RE` only matches `comic-*`, so a typo'd redirect ships silently)
3. Require ≥2 bullets in `When to Use` and `When Not to Use`
4. Detect duplicate or near-duplicate Prompt Blocks across styles (style-collision check — two styles resolving to the same fragment is a silent merge)
5. Add `--style <path>` single-file validator mode for fast authoring loops
6. Validate that every `Native habitat` entry in the style index names a real format/pattern from the core libraries
7. Document the Prompt Block purity contract in `CONTRIBUTING.md` so authors meet it before the validator does

### Style Coverage (fill real category gaps, Schema v2 only)

8. Rubber-hose 1930s animation (Cartoon — one cartoon style covers the whole category)
9. Ukiyo-e woodblock sequential (Asian — no pre-modern Japanese print grammar)
10. Risograph limited-palette zine print (Pop Art — technique-native, misregistration as a lock)
11. Sunday-page adventure illustration, Foster/Raymond school (Adventure)
12. Marcinelle-school *gros nez* humour BD (European — only two European styles)
13. Atomic-age retro-futurism (Sci-Fi)
14. Diagrammatic geometric literary comics (Literary — architecture-of-the-page school)
15. Illuminated-manuscript marginalia (Decorative)
16. Silhouette cut-paper theatre (Decorative)

### Examples & Worked Proof

17. 4-koma worked project (format × `kishotenketsu` × a manga-family style)
18. Webtoon scroll worked project (scroll-gap timing + emotional arc ledger in use)
19. Silent-strip worked project (the hardest directorial test, undemonstrated)
20. `examples/README.md` index row for every example added

### Layer Depth

21. `comic-core/comic-quality-gates`: explicit style-purity gate referencing the new Prompt Block contract
22. `comic-consistency`: negative-library taxonomy (identity bleed / style bleed / era bleed / anatomy bleed)
23. `comic-direction/comic-director`: shot-ladder reference table (which shot answers which beat)
24. `comic-production/comic-export-and-publish`: print CMYK gate refinement
25. `research/`: color and palette science for sequential art, mapped into the traceability table
26. `research/`: lettering typography history, feeding `comic-lettering-and-balloons`
27. `research/README.md`: source note protocol for depicted-fact traceability, now that a nonfiction style depends on it

### Documentation Accuracy

28. README quickstart prints `OK: repository contracts hold`; the validator actually prints `All repository contracts hold.` — fix the sample
29. README validator description lists five checks; the Prompt Block budget and purity rules are now a sixth
30. Hermes integration notes: how an agent loads the layers in order

## Recently Completed

**Cycle 1 (2026-08-04) — 5 commits, validator and tests green throughout**

- `docs(docs)`: this ledger
- `feat(tools)`: 40–90 word Prompt Block budget enforced (spec existed since Schema v2, nothing checked it)
- `feat(tools)`: Prompt Block injection guard — pronouns, imperatives, meta-instruction tokens, story content, quoted literals
- `test(tests)`: 25 validator contract tests; mutation-verified (disabling purity fails 5, widening the ceiling fails 1)
- `feat(styles)`: `reportage-comics-journalism` — first nonfiction style; index 28→29, CHANGELOG opened at Unreleased

## Notes for the Next Cycle

- `pytest` is not installed in a fresh container: `python3 -m pip install pytest pyyaml` before running the suite.
- The validator degrades gracefully without `pyyaml` (warns, skips YAML checks) — never make that path fatal.
- All 28 existing Prompt Blocks measure 56–69 words and contain zero pronouns and zero
  imperative verbs, so the incoming purity checks are enforcing an invariant the corpus
  already satisfies. Keep it that way.
- `CHANGELOG.md` is at `0.3.0`; new work accumulates under `## [Unreleased]` (now open).
- Purity-guard patterns were tuned against the corpus and legitimate craft vocabulary
  survives: "scroll reading", "character poses", "on-model", "no gradients". Any future
  pattern added to `PROMPT_BLOCK_FORBIDDEN` must be re-scanned against all styles first —
  `tests/test_validate.py::test_every_style_prompt_block_is_within_budget_and_pure` is the
  backstop, but scan before committing rather than after.
- The reportage style introduced a source-note obligation on the world bible (depicted
  facts must trace). Backlog item 27 closes that loop in `comic-world-bible-system`.

---

*A loop without a ledger is just a process that forgets.*
