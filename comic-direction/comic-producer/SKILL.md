---
name: comic-producer
version: 1.0.0
category: comic-direction
description: The production authority for every comic project. Owns brief intake, the project contract (format + narrative pattern + style + scope), greenlight gates, production scheduling, review cadence, drift policy, deliverables, and final sign-off.
---

# Comic Producer

**Core principle**: Nothing gets generated without a contract, and nothing ships without sign-off. The Producer is accountable for the project, not the panels.

The Producer converts vague creative intent into a locked, executable production plan — then protects that plan from scope creep, drift, and silent quality erosion.

## When to Use

- At the start of any comic project, before loading style or pipeline skills
- When a request arrives underspecified ("make me a comic about…")
- When scope, format, or deadline changes mid-project
- When quality-gate failures or consistency drift require a production decision
- At delivery, to run the sign-off protocol

## Framework

### 1. Brief Intake (Mandatory First Step)

Every project starts by resolving the brief into these fields. Missing fields are filled with explicit, recorded assumptions — never silently defaulted:

| Field | Question | Example |
|-------|----------|---------|
| **Premise** | What is this comic about? | "A courier robot discovers a stray cat" |
| **Audience & tone** | Who reads it, and how should it land? | All-ages, warm with dry humor |
| **Reference input** | Is there a reference image / world bible / existing canon? | One reference photo; no bible yet |
| **Length & scope** | One strip? A series? How many panels total? | 12 weekly strips (~36–48 panels) |
| **Format** | Which entry from `comic-format-library`? | `3-panel-horizontal` (default) |
| **Narrative pattern** | Which entry from `comic-narrative-patterns`? | `setup-reinforce-turnaround` (default) |
| **Style** | Which single skill from `comic-styles`? | `retro-hand-inked-manga-comic` |
| **Constraints** | Deadlines, platforms, print vs. digital, RTL vs. LTR | Instagram + print zine, LTR |

### 2. The Project Contract

The intake resolves into a **project contract** — the single document every other skill obeys for the duration of the project:

- Exactly **one** format, **one** narrative pattern, **one** style skill (changes require a contract re-lock with rationale)
- A **panel budget**: total panels, panels per episode, and reserve for re-renders (recommend 20% reserve)
- An **episode breakdown** for serialized work: beats per episode mapped to the narrative pattern
- The **review cadence** (see §4)

Store the contract as `production-brief.yaml` (template in `assets/templates/`) and register it in the world bible `version_history`.

### 3. Greenlight Gate (Non-Negotiable)

Production may not begin until every box is checked:

- [ ] Project contract locked and recorded
- [ ] World bible exists and passes `comic-world-bible-system` validation (any project > 20 panels)
- [ ] Character DNA templates derived for every recurring character
- [ ] Negative prompt library is non-empty
- [ ] Style skill loaded and its Style Lock acknowledged
- [ ] Director has produced a vision statement and the first shot plan
- [ ] Consistency configuration exported (`consistency-config.json`) for the chosen backend

A failed greenlight produces a **blocking list**, not a partial start.

### 4. Review Cadence & Escalation

The Producer owns *when* humans look at output; the Director owns *what* they look for.

| Trigger | Action | Owner |
|---------|--------|-------|
| Every episode boundary | Human review of full episode against quality gates | Producer schedules, Director presents |
| Character/style drift detected | Pause batch, re-anchor to canonical reference | Producer pauses, Director re-anchors |
| 2 consecutive quality-gate failures on the same panel | Stop re-rolling; Director revises the shot plan instead | Producer enforces |
| Bible conflict (canon violation) | Escalate to human with proposed resolution; never auto-resolve | Producer escalates |
| Scope change request | Re-run intake §1, re-lock contract, bump bible version | Producer |

**Anti-pattern**: re-generating a failing panel more than twice with the same shot plan. Repeated failure is a planning problem, not a sampling problem.

### 5. Drift Policy

- Re-anchor every character to canonical reference sheets at minimum every **10 panels** (tighter for action-heavy sequences)
- Compare each episode's first panel against the master style references before continuing
- Log every re-anchor in the production state; three re-anchors in one episode triggers a Director review of the consistency configuration

### 6. Deliverables & Sign-Off Protocol

At delivery, the Producer verifies:

- [ ] Every panel passed all six quality gates (Director certified Layer 6)
- [ ] Deliverables match the contract (format, resolution, platform variants)
- [ ] Exports generated per the world bible export matrix (`exports/`)
- [ ] Production state document is complete: panel log, re-render count, open issues
- [ ] World bible `version_history` updated with project outcome and lessons

Sign-off is explicit. "It looks done" is not sign-off.

## Integration

- Commands all `comic-pipeline` skills — pipelines refuse to run without a locked contract
- Depends on `comic-world-bible-system` for validation and versioning
- Partners with `comic-director` (see `comic-direction` layer index for the chain of authority)
- Selects from `comic-core/comic-format-library` and `comic-core/comic-narrative-patterns`

---

*The Producer's job is to make quality boring: planned, scheduled, and inevitable.*
