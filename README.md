# foundational-comic-skills

**A production-grade, modular skill system for consistent, long-form comic generation.**

This repository provides a complete, layered foundation for building comics with strong character consistency, style control, and world coherence — especially for 100+ panel arcs. It is designed to work directly with Hermes agents and other LLM-based creative pipelines.

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
- Multiple style skills (e.g., `retro-hand-inked-manga`, `ligne-claire`, etc.)

---

## Core Philosophy

**Every consistency decision must trace back to a single, versioned source of truth.**

This repository treats the **World Bible** as the central nervous system for long-running comic projects. Instead of relying on scattered reference images and ad-hoc prompting, all consistency artifacts (DNA templates, model sheets, negative libraries, LoRA recommendations) are **derived** from a structured, queryable world bible.

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

---

## Repository Structure

```
foundational-comic-skills/
├── README.md
├── comic-core/                    # Universal rules, quality gates, structural standards
├── comic-consistency/             # World bible, character DNA, style memory, long-sequence orchestration
│   ├── comic-world-bible-system/
│   ├── comic-character-consistency-system/
│   ├── comic-style-memory-system/
│   ├── comic-long-sequence-orchestrator/
│   └── comic-image-generation-adapter/
├── comic-styles/                  # 25+ individual style skills with Style Locks
├── research/                      # 6 foundational technical papers
└── exports/                       # Generated artifacts and templates
```

---

## Research Foundation

This system is grounded in six core research documents:

| Document | Focus | Path |
|----------|-------|------|
| Advanced Consistency Systems | IP-Adapter, InstantID, LoRA orchestration, world bible architecture | `research/ADVANCED-CONSISTENCY-SYSTEMS.md` |
| Style-Specific Technical Mastery | Screentone simulation, ligne claire, gekiga framing, ink physics | `research/STYLE-SPECIFIC-TECHNICAL-MASTERY.md` |
| Comic Art Evaluation Frameworks | Professional rubrics, failure modes, human vs AI signals | `research/COMIC-ART-EVALUATION-FRAMEWORKS.md` |
| Artistic Decision-Making Process Modeling | Micro-decisions, PINS model, embodied cognition | `research/ARTISTIC-DECISION-MAKING-PROCESS-MODELING.md` |
| Panel Composition Theory | McCloud transitions, gutters, Golden Ratio, eyelines | `research/PANEL-COMPOSITION-THEORY.md` |
| Comic Timing and Pacing | Setup–Reinforce–Turnaround, gutter rhythm | `research/COMIC-TIMING-AND-PACING.md` |

---

## Goals

- Provide a **single source of truth** for long-form comic consistency
- Enable **derivable, versioned** consistency artifacts
- Support **Hermes agents** and other LLM pipelines with clear, structured skills
- Bridge research and production with practical, implementable systems

---

*Last updated: May 2026*  
*Maintained by ObliviousOdin*