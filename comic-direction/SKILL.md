---
name: comic-direction
version: 1.0.0
category: comic-direction
description: The decision-authority layer for comic production. Provides the Producer (production authority — scope, format, schedule, sign-off) and the Director (creative authority — shot planning, camera grammar, pacing, final cut) that command every pipeline run.
---

# Comic Direction Layer

**Purpose**: This layer gives the skill system what raw rules and styles cannot provide — **judgment with authority**. It turns the research on artist decision-making, editorial evaluation, and the manga *name* system into two explicit roles that own every creative and production decision.

## Why This Layer Exists

The lower layers define *laws* (`comic-core`), *memory* (`comic-consistency`), and *visual grammar* (`comic-styles`). None of them decide:

- Which format and narrative pattern fit this project
- How each panel is framed, staged, and paced
- When output is good enough to ship — and who says so

Without these decisions made explicitly, generation defaults to the statistical average: technically correct, artistically lifeless. The direction layer is the structural answer to that failure mode.

## The Two Roles

| Role | Skill | Authority | Owns |
|------|-------|-----------|------|
| **Producer** | `comic-producer` | Production authority | Brief intake, project contract (format + pattern + style + scope), greenlight, schedule, review cadence, escalation, final sign-off |
| **Director** | `comic-director` | Creative authority | Vision statement, shot plans (the *name*), camera grammar, blocking, transitions, pacing, dialogue placement, the final cut |

## Chain of Authority

```
Producer (locks the project contract, greenlights production)
       ↓
Director (plans every panel before generation, owns the final cut)
       ↓
Pipelines (execute the shot plan through the consistency stack)
       ↓
Quality Gates (shared rubric — Director rules on Artistic Life)
       ↓
Producer (accepts deliverables, signs off, archives decisions)
```

**Conflict rule**: The Producer decides *what* gets made and *when it ships*. The Director decides *how it looks and reads*. Neither overrides the other inside the other's domain. Disputes escalate to human review with both positions recorded in the world bible `version_history`.

## When to Load comic-direction

- At the start of **every** project, before the first panel is generated
- Whenever a pipeline runs (pipelines must not execute without a locked project contract and a shot plan)
- When output repeatedly fails quality gates (the Director diagnoses; the Producer reschedules)
- When scope, format, or style changes mid-project (Producer re-locks the contract)

## Integration with Other Layers

| Layer | Relationship |
|-------|--------------|
| `comic-core` | Direction selects from its format library and narrative patterns; enforces its quality gates |
| `comic-consistency` | Producer requires a valid world bible to greenlight; Director's decisions log into `version_history` |
| `comic-styles` | Producer locks one style per project; Director works inside its Style Lock without exception |
| `comic-pipeline` | Every pipeline embeds Producer greenlight → Director shot plan → Director final cut |
| `comic-production` | Tooling adapters execute what the direction layer has already decided |

---

*Rules make output correct. Direction makes it intentional.*
