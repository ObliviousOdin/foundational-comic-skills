# Continuous Maintenance Ledger

Durable memory for the continuous hardening loop. This file is the first thing to read
when resuming work: it holds the cycle counter, the rolling backlog, and the notes the
next session needs.

**Session start:** 2026-08-04
**Current cycle:** 1
**Commits this session:** 0
**Baseline at session start:** 54 skills (28 styles), validator green, 5 pytest tests passing

## How This Loop Works

One cycle = up to 5 atomic, validated, conventionally-named commits. Every commit clears
the pre-commit checklist (`python3 tools/validate.py` exit 0, `python3 -m pytest tests/ -q`
green, `git diff --check` clean, indexes and `CHANGELOG.md` updated when the change
requires it). Fewer than 5 commits is correct when fewer than 5 genuinely high-value
atomic improvements exist — padding is a contract violation, not a shortfall.

## Backlog (rolling, prioritized)

Ordered by value density: contract enforcement first, then coverage, then documentation.

### Validator & Tests (highest leverage — every future contribution inherits these)

1. ~~Enforce the 40–90 word Prompt Block budget that `CONTRIBUTING.md` specifies but the validator never checked~~
2. ~~Guard Prompt Blocks against prompt-injection and story content (pronouns, imperatives, narrative markers)~~
3. ~~Pytest coverage for the validator's style-schema, index-sync, and prompt-block rules~~
4. Run the pytest suite in CI alongside the validator (`.github/workflows/validate.yml`)
5. Resolve backticked *style-skill* cross-references (`When Not to Use` redirect targets currently unchecked — `REF_RE` only matches `comic-*`)
6. Require ≥2 bullets in `When to Use` and `When Not to Use`
7. Detect duplicate or near-duplicate Prompt Blocks across styles (style collision check)
8. Add `--style <path>` single-file validator mode for fast authoring loops
9. Validate that every `Native habitat` entry in the style index names a real format/pattern from the core libraries

### Style Coverage (fill real category gaps, Schema v2 only)

10. ~~Comics-journalism crosshatch reportage (Literary) — nonfiction/documentary register is entirely missing~~
11. Rubber-hose 1930s animation (Cartoon — only one cartoon style exists)
12. Ukiyo-e woodblock sequential (Asian — no pre-modern Japanese print grammar)
13. Risograph limited-palette zine print (Pop Art — technique-native, misregistration as a lock)
14. Sunday-page adventure illustration, Foster/Raymond school (Adventure)
15. Marcinelle-school *gros nez* humour BD (European — only two European styles)
16. Atomic-age retro-futurism (Sci-Fi)
17. Diagrammatic geometric literary comics (Literary — architecture-of-the-page school)
18. Illuminated-manuscript marginalia (Decorative)
19. Silhouette cut-paper theatre (Decorative)

### Examples & Worked Proof

20. 4-koma worked project (format × `kishotenketsu` × a manga-family style)
21. Webtoon scroll worked project (scroll-gap timing + emotional arc ledger in use)
22. Silent-strip worked project (the hardest directorial test, undemonstrated)

### Layer Depth

23. `comic-core/comic-quality-gates`: add an explicit style-purity gate referencing the new Prompt Block contract
24. `comic-consistency`: negative-library taxonomy (identity bleed / style bleed / era bleed / anatomy bleed)
25. `comic-direction/comic-director`: shot-ladder reference table (which shot answers which beat)
26. `comic-production/comic-export-and-publish`: print CMYK gate refinement
27. `research/`: color and palette science for sequential art, mapped into the traceability table
28. `research/`: lettering typography history, feeding `comic-lettering-and-balloons`

### Documentation Accuracy

29. README quickstart prints `OK: repository contracts hold`; the validator actually prints `All repository contracts hold.` — fix the sample
30. Hermes integration notes: how an agent loads the layers in order

## Recently Completed

- (Cycle 1 in progress)

## Notes for the Next Cycle

- `pytest` is not installed in a fresh container: `python3 -m pip install pytest pyyaml` before running the suite.
- The validator degrades gracefully without `pyyaml` (warns, skips YAML checks) — never make that path fatal.
- All 28 existing Prompt Blocks measure 56–69 words and contain zero pronouns and zero
  imperative verbs, so the incoming purity checks are enforcing an invariant the corpus
  already satisfies. Keep it that way.
- `CHANGELOG.md` is at `0.3.0`; new work accumulates under `## [Unreleased]`.

---

*A loop without a ledger is just a process that forgets.*
