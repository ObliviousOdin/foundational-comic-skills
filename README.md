# foundational-comic-skills

**A production-grade, modular skill system for consistent, long-form comic generation.**

This repository provides a complete, layered foundation for building comics with strong character consistency, style control, world coherence, and explicit creative direction — especially for 100+ panel arcs. It is designed to work directly with Hermes agents and other LLM-based creative pipelines.

**The stack in one sentence**: `comic-core` defines the laws, `comic-consistency` is the memory, `comic-styles` (28 production-grade skills) is the visual grammar, `comic-direction` (Producer + Director) is the judgment, and `comic-pipeline` turns it all into output across six formats and six narrative patterns — with a validator and CI keeping every contract checkable.

**New here?** Read the worked example first: [`examples/rabot-strip-001/WALKTHROUGH.md`](examples/rabot-strip-001/WALKTHROUGH.md) shows one strip travel the entire system — brief → contract → shot plan → assembled prompt → RETAKE → sign-off.

---

## Quick Start (Hermes)

### 1. Clone the Repository

```bash
cd ~/Documents
git clone https://github.com/ObliviousOdin/foundational-comic-skills.git
```

### 2. Install the Skills

```bash
# Install core consistency layer (recommended first)
hermes skills install ~/Documents/foundational-comic-skills --layer comic-consistency

# Install style skills
hermes skills install ~/Documents/foundational-comic-skills --layer comic-styles

# Or install everything
hermes skills install ~/Documents/foundational-comic-skills
```

### 3. Verify Installation

```bash
hermes skills list | grep comic
```

You should see skills such as:
- `comic-world-bible-system`
- `comic-character-consistency-system`
- `comic-long-sequence-orchestrator`
- `comic-producer` and `comic-director` (the direction layer)
- `comic-narrative-patterns` and `comic-format-library` (variation libraries)
- Multiple style skills (e.g., `retro-hand-inked-manga`, `ligne-claire`, etc.)

---

## Core Philosophy

**Every consistency decision must trace back to a single, versioned source of truth — and every creative decision must be made before generation, by a role with authority to make it.**

This repository treats the **World Bible** as the central nervous system for long-running comic projects. Instead of relying on scattered reference images and ad-hoc prompting, all consistency artifacts (DNA templates, model sheets, negative libraries, LoRA recommendations) are **derived** from a structured, queryable world bible.

On top of the bible sits the **direction layer**: a **Producer** who locks every project's contract (format + narrative pattern + style + scope) and a **Director** who plans every panel as a shot — camera, staging, transition, pacing — before anything is rendered, and who owns the final cut.

---

## The Direction Layer (Producer + Director)

The biggest failure mode in AI comics is not inconsistency — it is the absence of decisions. The `comic-direction/` layer makes the decisions explicit:

| Role | Authority | Key Artifacts |
|------|-----------|---------------|
| `comic-producer` | What gets made, when it ships | Project contract (`production-brief.yaml`), greenlight gate, review cadence, sign-off |
| `comic-director` | How it looks and reads | Vision statement, per-strip shot plans (`shot-plan-template.yaml`), final cut verdicts |

**Every pipeline run follows the same shape:**

```
Producer locks the contract → Director plans the shots → consistency stack generates
→ Director cuts (flow → words → everything → Artistic Life) → Producer signs off
```

Pipelines refuse to run without a locked contract, and nothing generates without a shot plan. See `comic-direction/SKILL.md` for the chain of authority.

---

## Variation: Formats × Patterns × Styles

A project composes one choice from each library — locked in the contract, disciplined by the core:

| Library | Options |
|---------|---------|
| `comic-core/comic-format-library` | 3-panel horizontal (default), 4-koma vertical, webtoon scroll segment, single-panel gag, 2×2 grid page, multi-page chapter |
| `comic-core/comic-narrative-patterns` | Setup→Reinforce→Turnaround (default), kishōtenketsu, gag escalation, slow-burn reveal, parallel action, silent strip |
| `comic-styles/` | 28 style skills across 12 categories |
| `comic-pipeline/` | One pipeline per format family: 3-panel, 4-koma/grid, webtoon scroll, multi-page chapter |

---

## Primary Skill: `comic-world-bible-system`

This is the foundational skill. All other consistency systems depend on it.

### How to Use It

**Best Practice Prompt Template:**

```
Using the `comic-world-bible-system` skill, create a production-ready world bible for a new comic series.

Project name: [Your Series Name]
Target length: [e.g., 500–1000+ panels]
Style direction: [e.g., retro hand-inked manga with gekiga influences]
Main characters: [List 2–4 characters with brief descriptions]
Key locations: [List recurring environments]
Special requirements: [Any specific constraints or themes]

Please:
1. Generate a complete `world-bible.yaml` following the defined schema.
2. Create the corresponding folder structure.
3. Generate the initial DNA templates for each character.
4. Provide the negative prompt library.
5. Output the recommended consistency configuration.
```

### Concrete Example

**User Prompt:**

```
Using the `comic-world-bible-system` skill, initialize a world bible for a series called "Rabot".

- Style: Clean retro manga with strong linework and subtle screentone
- Main character: Rabot – young man, sharp features, navy jacket, small scar on left cheek
- Supporting character: Echo – female, silver hair, tech aesthetic
- Primary location: A dimly lit control room with cool fluorescent lighting
- Target: 1000+ panel serialized story
```

**Expected Output from the skill:**
- A validated `world-bible.yaml`
- DNA template blocks ready for prompt injection
- Negative prompt library
- Consistency configuration (LoRA/IP-Adapter weights)
- Folder structure ready for asset organization

---

## Best Practices

### 1. Always Start with a World Bible
Never begin generating panels without first establishing (or updating) the world bible. This is the single highest-leverage practice for long-sequence consistency.

### 2. Version Everything
Treat the world bible as version-controlled source code. Every significant change (new character, style rule update, location addition) should bump the version and include rationale.

### 3. Derive, Don’t Duplicate
Use the derivation capabilities of the system:
- Generate DNA templates from the bible instead of writing them manually
- Generate model sheet prompts from character entries
- Generate negative libraries by combining global + per-character rules

### 4. Human-in-the-Loop for Conflicts
When the system detects character conflicts or bible violations, escalate to human review rather than letting the model resolve them autonomously.

### 5. Keep Canonical References Sacred
The reference images and descriptions in the world bible are the single source of truth. Generated variations should never override canonical references.

### 6. Use Layered Conditioning
Combine multiple techniques (IP-Adapter + LoRA + negative prompting + style memory) rather than relying on a single method.

### 7. No Generation Without a Shot Plan
Prompts are the last step, not the first. Let the Director decide beat role, shot size, angle, staging, transition, and pacing for every panel before anything renders. Re-rolling a failed panel without changing the shot plan is gambling, not directing.

### 8. Lock the Contract Before the First Panel
Format, narrative pattern, and style are chosen once per project by the Producer and recorded. Mid-project changes are re-locks with rationale — never silent drift.

---

## Repository Structure

```
foundational-comic-skills/
├── README.md / CONTRIBUTING.md / CHANGELOG.md
├── tools/validate.py              # Repo validator — run before every commit
├── .github/workflows/validate.yml # CI: validator on every push/PR
├── comic-core/                    # Laws: contracts, gates, patterns, formats, lettering
│   ├── comic-universal-operating-rule/   comic-structural-contract/
│   ├── comic-narrative-patterns/         comic-format-library/
│   ├── comic-lettering-and-balloons/     comic-quality-gates/
│   └── comic-story-derivation/
├── comic-consistency/             # Memory: world bible, character DNA, style memory,
│   │                              #   long-sequence orchestration, prompt assembly
├── comic-styles/                  # 28 production-grade style skills (Schema v2, 12 categories)
├── comic-direction/               # Judgment: Producer (contract/sign-off) + Director (shots/cut)
├── comic-pipeline/                # Workflows: 3-panel, 4-koma, webtoon scroll, chapter,
│   │                              #   emotional arc orchestrator
├── comic-production/              # Delivery: export & publish specs, tool adapters
├── examples/                      # Complete worked projects (start here)
├── research/                      # 6 studies + traceability map (research/README.md)
├── skills/                        # Original portable harness pack (repo skill tree is canonical)
└── exports/                       # Generated artifacts (derived, never hand-edited)
```

## Sustainability

The repository enforces its own discipline:

- **Validator**: `python3 tools/validate.py` checks frontmatter, the Style Skill Schema v2, style-index↔directory sync, cross-reference resolution, and YAML health. CI runs it on every push and PR.
- **Schema v2**: every style skill carries negative locks, an injectable prompt block, direction and consistency notes, and style-specific gates — uniform, testable, and validator-enforced (see `CONTRIBUTING.md`).
- **Versioning**: skills use semver in frontmatter; repository milestones live in `CHANGELOG.md`.
- **Traceability**: `research/README.md` maps every research finding to the skill that enforces it; generation logs trace every panel back to bible version + shot plan.

---

## Research Foundation

This system is grounded in six core research documents. **Every finding is mapped to the skill that operationalizes it in [`research/README.md`](research/README.md)** — research that no skill enforces is treated as trivia.

| Document | Focus | Path |
|----------|-------|------|
| Advanced Consistency Systems | IP-Adapter, InstantID, LoRA orchestration, world bible architecture | `research/ADVANCED-CONSISTENCY-SYSTEMS.md` |
| Style-Specific Technical Mastery | Screentone simulation, ligne claire, gekiga framing, ink physics | `research/STYLE-SPECIFIC-TECHNICAL-MASTERY.md` |
| Comic Art Evaluation Frameworks | Professional rubrics, failure modes, human vs AI signals | `research/COMIC-ART-EVALUATION-FRAMEWORKS.md` |
| Artistic Decision-Making Process Modeling | Micro-decisions, PINS model, the manga *name* system | `research/ARTISTIC-DECISION-MAKING-PROCESS-MODELING.md` |
| Panel Composition Theory | McCloud transitions, gutters, Golden Ratio, eyelines | `research/PANEL-COMPOSITION-THEORY.md` |
| Comic Timing and Pacing | Setup–Reinforce–Turnaround, gutter rhythm | `research/COMIC-TIMING-AND-PACING.md` |

---

## Goals

- Provide a **single source of truth** for long-form comic consistency
- Make every creative decision **explicit, owned, and made before generation** (the direction layer)
- Enable **derivable, versioned** consistency artifacts
- Support **disciplined variation**: six formats × six narrative patterns × 28 styles
- Support **Hermes agents** and other LLM pipelines with clear, structured skills
- Bridge research and production with practical, implementable systems

---

*Last updated: June 2026*  
*Maintained by ObliviousOdin · [MIT License](LICENSE)*