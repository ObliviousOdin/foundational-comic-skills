---
name: comic-director
version: 1.0.0
category: comic-direction
description: The creative authority for every comic project. Owns the directorial vision, per-panel shot planning (the digital "name"), camera grammar, staging, transition selection, pacing, and the final cut. Operationalizes the repository's research on artistic decision-making and editorial evaluation.
---

# Comic Director

**Core principle**: Every panel is a decision, and every decision is made **before** generation — never discovered afterward. The Director is the system's answer to "technically correct but artistically lifeless."

This skill turns the research foundation (`ARTISTIC-DECISION-MAKING-PROCESS-MODELING`, `PANEL-COMPOSITION-THEORY`, `COMIC-TIMING-AND-PACING`, `COMIC-ART-EVALUATION-FRAMEWORKS`) into an executable role with final-cut authority.

## When to Use

- After the Producer locks the project contract, before any generation
- To produce the **shot plan** for every strip, page, or scroll segment
- To review rendered output and issue the final cut (accept / corrective notes / re-plan)
- When output passes technical gates but still feels generic — the Director diagnoses why

## Framework

### 1. Directorial Vision Statement (Once Per Project)

Before the first shot plan, write a 3-line vision and register it in the world bible:

1. **Register**: three adjectives that every panel must serve (e.g., *quiet, warm, precise*)
2. **Camera bias**: the project's default distance and angle temperament (e.g., "medium shots, eye level, step close only for emotional peaks")
3. **Signature motif**: one recurring visual device the project owns (e.g., negative space around the character when alone)

The vision constrains all later decisions. A panel that obeys every rule but betrays the register fails direction.

### 2. The Shot Plan — Digital *Name* (Every Strip, No Exceptions)

Comics are planned the way manga *name* storyboards are: structure first, rendering later. For each panel, decide and record (template in `assets/templates/shot-plan-template.yaml`):

| Decision | Vocabulary | Guidance |
|----------|------------|----------|
| **Beat role** | From the locked narrative pattern (e.g., SETUP / REINFORCE / TURNAROUND, or *ki/shō/ten/ketsu*) | One role per panel; never two |
| **Shot size** | establishing / wide / medium / close-up / extreme close-up | Step closer as emotion intensifies; ECU is earned, not default |
| **Camera angle** | eye-level / low / high / dutch / overhead | Eye-level is neutral; deviation must serve the beat |
| **Staging** | foreground–midground–background placement | Depth staging beats flat lineups; protect figure–ground separation (no tangents) |
| **Eyeline vector** | where the character looks; where the reader exits | Gaze and action lines must point toward the next panel |
| **Transition in** | McCloud: moment / action / subject / scene / aspect | See §3 transition budget |
| **Pacing weight** | small / medium / large panel; gutter before it: narrow / standard / wide | Space = time; the payoff panel gets room |
| **Dialogue beat** | bubble count, ≤8 words each, placement | Bubbles hide art — place them where they hide the least |
| **Crop check** | the four questions | Action legible? Context present? Mood served? Composition satisfying? |

A shot plan passes the **five *name* criteria** before generation:
1. Strong first panel? 2. Layout effortless to follow? 3. Always clear where characters are and what they do? 4. Time/scene shifts convincing? 5. Emotion legible in every beat?

### 3. Camera Grammar & Continuity Rules

- **The shot ladder**: across any strip, vary at least two of {shot size, angle, staging}. Three identical framings in a row is a direction failure, not a style choice.
- **180° rule**: keep all cameras on one side of the action axis; characters must not swap screen sides between panels without an on-camera move or an establishing re-set.
- **Eyeline choreography**: in LTR formats, exit vectors point right (down for vertical scroll; left for RTL manga). The reader's eye is choreographed, never abandoned.
- **Transition budget**: action-to-action and subject-to-subject are the workhorses. Each scene-to-scene or aspect-to-aspect transition must buy something (time jump, atmosphere) and costs reader effort — spend at most one per short strip.
- **Lens language**: wide-angle distortion for disorientation or scale; telephoto compression for intimacy or claustrophobia. Use deliberately, log in the shot plan.

### 4. Pacing & Emotional Modulation

- Map the strip's **beat rhythm** before sizing panels: fast → build → release is the default curve
- The emotional peak gets the **largest panel and the widest preceding gutter**; silence lands harder than dialogue at the peak
- Modulate rendering intensity with emotion where the style permits: crop tighter, increase hatching/spot-black density, or open negative space as the beat demands (per `STYLE-SPECIFIC-TECHNICAL-MASTERY`)
- One **breathing panel** (low detail, low text) per strip is a feature, not waste

### 5. The Final Cut (Flow-First Review)

Review rendered output in strict editorial order — flow first, words second, everything else third:

1. **Flow**: Can the eye traverse it in one pass? Panel order unambiguous? Balloon order obvious? 180° intact?
2. **Words**: Dialogue inside budget, in character, advancing (not explaining) the beat?
3. **Everything else**: Style Lock fidelity, consistency, rendering quality — then the full `comic-quality-gates` run
4. **Artistic Life (Layer 6)**: The Director personally rules on it. Gesture energy over polish; intentional imperfection over synthetic smoothness; would a human artist sign this?

Verdicts: **ACCEPT** / **RETAKE** (corrective note tied to one shot-plan field) / **RE-PLAN** (the shot plan itself was wrong). Never issue a bare rejection — every RETAKE names the field to change.

### 6. The Decision Log

Every non-default choice (unusual angle, broken symmetry, silent panel, transition splurge) gets one line: *decision → intended effect*. Logs feed the world bible `version_history` and make the project's taste reproducible across sessions and models.

## Anti-Patterns

- Planning by prompt: writing image prompts before a shot plan exists
- Re-rolling a failed panel without changing a shot-plan field (that is gambling, not directing)
- Centering every character at eye level in medium shot (the statistical average — the exact thing this system exists to prevent)
- Letting dialogue carry information the camera should carry

## Integration

- Requires the Producer's locked project contract (`comic-producer`)
- Selects beats from `comic-core/comic-narrative-patterns`; works inside the format from `comic-core/comic-format-library`
- Hands shot plans to `comic-pipeline` skills; receives renders back for the final cut
- Acts as the "Director agent" referenced by `comic-long-sequence-orchestrator`
- Defers identity/state resolution to `comic-consistency`; defers visual grammar to the locked style skill

---

*Anyone can render. The Director decides what is worth rendering.*
