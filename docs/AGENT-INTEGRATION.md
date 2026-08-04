# Agent Integration — Load Order and Authority

The README calls this repository an operating system for Hermes agents and LLM creative pipelines. That claim is only useful if an agent knows **what to read, in what order, and who wins when two skills disagree**. This document is that contract.

Nothing here is new policy. It is the load order the layers already imply, written down in one place so an agent does not have to infer it from thirty style files.

## The Load Order

Read in this sequence. Each step depends on decisions the previous one locked, and skipping ahead is the commonest way an agent produces work that passes every gate and still breaks a contract.

| # | Load | From | What it settles |
|---|------|------|-----------------|
| 1 | **Universal rules** | `comic-core/comic-universal-operating-rule` | The non-negotiables that hold regardless of anything below |
| 2 | **Structural contract** | `comic-core/comic-structural-contract` | The default arc, and that variations exist only as locked contracts |
| 3 | **Project contract** | `comic-producer` + the brief | Format, pattern, style, reading direction — the three locks everything downstream obeys |
| 4 | **Format + pattern** | `comic-format-library`, `comic-narrative-patterns` | Panel count, canvas, geometry, beats, and the budget unit |
| 5 | **World bible** | `comic-world-bible-system` | Identity, locations, negatives, and (nonfiction) provenance |
| 6 | **Style skill** | the one locked style | How it is rendered — never what is framed |
| 7 | **Arc ledger** | `comic-emotional-arc-orchestrator` | Serialized work only: where each character must arrive |
| 8 | **Shot plan** | `comic-director` | Every panel decision, before generation |
| 9 | **Assembly** | `comic-image-generation-adapter` | The seven blocks, in canonical order |
| 10 | **Gates** | `comic-quality-gates` | Layer 0 before the render; Layers 1–6 after |

**Step 3 is the hinge.** Almost every rule below it is conditional on what the contract locked, and almost every defect this repository has fixed came from a rule that forgot that.

## Who Wins

Disagreements are common and mostly not bugs. The resolution order is fixed:

1. **Universal operating rule** — beats everything
2. **Locked format** — a format's geometry and budget beat a style's preference
3. **Locked pattern** — a pattern's defining rule beats a style's permission
4. **Style skill** — governs rendering within the space above
5. **Director's judgement** — chooses freely among whatever remains

Two worked cases, both from `examples/`:

- **Format beats style.** `single-panel-gag` grants a caption line. `minimalist-line-webcomic` forbade caption boxes. The format grants the *element*; the style governs how it *looks* — so the caption appears, set boxless in the style's own lettering.
- **Pattern beats style.** `ink-wash-storybook-manga` sanctions sparse SFX. `silent-strip` forbids dialogue. A sound effect in a silent strip is dialogue in a different font, so the pattern wins and the strip spends none.

The general shape: **a permission never overrides a lock.** A style saying "you may" loses to a format or pattern saying "you must not".

## What an Agent Must Not Do

- **Author inside the adapter.** Assembly composes blocks from their owning artifacts. A block written at generation time has no owner, so nothing can check it.
- **Re-roll without changing a shot-plan field.** That is gambling, not directing; `comic-director` names it an anti-pattern.
- **Treat native habitat as a lock.** The index column is the Producer's *routing guidance*. The contract decides.
- **Carry a rule across formats without checking it.** Ask what `CONTRIBUTING.md` ground rule 6 asks: can `4koma-vertical` and `webtoon-scroll-segment` obey this? Seven fixed defects came from rules that could not.
- **Skip the bible on short work.** A single-panel gag has no continuity across panels and everything to protect across a series of them. `examples/deskplant-gag-001/` shows the minimum that still passes.

## Where to Look First

| Question | Answer lives in |
|----------|-----------------|
| What may I never do? | `comic-universal-operating-rule` |
| How many panels, what shape? | `comic-format-library` |
| What are the beats? | `comic-narrative-patterns` |
| Which style for this format? | The Native Habitat column in `comic-styles/SKILL.md` |
| What does this character look like? | The world bible's `character_compendium` |
| Why is this negative here? | The bleed class it belongs to (`comic-world-bible-system` §4) |
| How is the prompt ordered? | `comic-image-generation-adapter` |
| Is it done? | `comic-quality-gates`, Layer 0 first |

## Worked Proof

Seven complete projects live in `examples/`, one per sanctioned format plus the first non-default pattern. Reading one end to end is faster than reading the skill tree, and every decision in them traces to a skill:

`rabot-strip-001` (the full loop) · `rabot-4koma-002` (locked geometry) · `rabot-webtoon-003` (serialized, arc ledger) · `lamplighter-chapter-001` (pages and turns) · `deskplant-gag-001` (one panel) · `kell-grid-002` (the grid) · `tidepool-silent-004` (no words)

---

*An operating system is only an operating system if the load order is written down.*
