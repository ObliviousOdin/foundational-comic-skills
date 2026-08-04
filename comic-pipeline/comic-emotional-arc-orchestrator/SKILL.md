---
name: comic-emotional-arc-orchestrator
version: 1.1.0
category: comic-pipeline
description: Series-level emotional continuity. Plans each character's emotional throughline across episodes, tracks state in an arc ledger, and feeds per-episode emotional targets into the Producer's contract and the Director's shot plans.
---

# Comic Emotional Arc Orchestrator

**Core principle**: A strip has a beat arc; a series has an emotional throughline. Without orchestration, every episode resets to the same feeling — technically consistent, emotionally static.

This skill operates **above** individual pipelines: it decides what each episode must do to each character's inner state, then hands those targets down.

## When to Use

- Any serialized project (2+ episodes with recurring characters)
- When episodes feel interchangeable — same character, same mood, no growth
- When planning season/arc structure before the Producer locks episode scopes
- After delivery of each episode, to update the ledger before the next

## Framework

### 1. Throughline Design (Once Per Arc)

For each recurring character, define in the arc ledger (template in `assets/templates/arc-ledger-template.yaml`):

- **Baseline state**: the emotional register the character starts from (must match the world bible's expression library)
- **Arc shape**: one of `rise` (gathering confidence/hope), `fall` (erosion), `thaw` (guarded → open), `spiral` (repetition with deepening), `flat-with-spikes` (stable register punctuated by episodes that crack it)
- **Destination state**: where the arc lands and in which episode
- **Forbidden resets**: feelings the character may not "forget" once earned (e.g., once trust forms in ep. 4, no ep. 6 stranger-coldness)

### 2. Episode Emotional Targets

Each episode receives a one-line target per featured character: *enter at X, exit at Y, because Z happens*. Rules:

- An episode moves each featured character **at most one step** along the throughline (big jumps are season finales, budgeted by the Producer)
- The episode's **narrative pattern** must be able to carry the move (a `gag-escalation` episode rarely carries a `fall` step — flag mismatches to the Producer)
- Silent episodes can still move state; the ledger does not require dialogue evidence

### 3. Ledger Tracking (After Every Episode)

- Record exit state per character, with the panel that proves it (panel reference, not vibes)
- Diff exit state against the target; a miss is a **continuity debt** — the next episode must either pay it (re-plan) or the throughline is re-versioned with rationale
- Sync the ledger with the world bible: expression-library gaps discovered here (a needed state with no canonical reference) become bible change requests
- **An open change request blocks the shot plan that needs it.** A raised request is not a note to action later — until the state has a canonical reference, any panel calling for it hands the generator an expression it has never been shown, and the generator will invent one. That is the precise drift the consistency layer exists to prevent, arriving through the ledger instead of the prompt. Either the bible gains the state (with a reference) or the episode re-plans around the states that exist

### 4. Handoffs

| Receives | What |
|----------|------|
| `comic-producer` | Episode targets become contract inputs; arc-shape budget (where the big beats land) constrains episode scheduling |
| `comic-director` | Entry/exit states constrain the vision check and panel-1 emotional baseline; the turnaround must land the *exit* state, not a generic payoff |
| `comic-story-derivation` | The mood cue is read **through** the current ledger state (a "joyful" reference image during a `fall` arc becomes strained brightness, not a reset) |
| `comic-long-sequence-orchestrator` | Ledger state is part of persistent world state; drift detection includes emotional-state violations |

## Anti-Patterns

- **The sitcom reset**: every episode ends where it began despite events that should have moved the ledger
- **The mood lottery**: episode emotion driven by each reference image in isolation, ignoring the throughline
- **Unearned arrival**: hitting the destination state without the intermediate steps appearing on-page
- **Ledger by memory**: tracking states in the conversation instead of the versioned ledger file

## Integration

- Sits above `comic-3-panel-horizontal-pipeline`, `comic-4koma-pipeline`, `comic-webtoon-scroll-pipeline`, and `comic-multi-page-chapter-pipeline`
- Reads/writes the arc ledger in `exports/`; states must reference the world bible expression library
- Subsumes the originally planned `comic-emotional-arc-tracking` core extension

---

*Consistency keeps the face the same. Orchestration keeps the heart moving.*
