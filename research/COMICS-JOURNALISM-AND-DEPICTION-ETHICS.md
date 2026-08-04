# Comics Journalism and Depiction Ethics – Foundational Study

**For nonfiction comic work: sourcing, attribution, consent, and the limits of drawn reconstruction**

Every other study in this folder describes how comics *work*. This one describes what nonfiction comics owe, and it exists because the repository shipped a contract without one. `reportage-comics-journalism` locks out fabricated documentary detail and `comic-world-bible-system` enforces a `source_register` — both resting on journalism practice this collection could not cite. That gap was named in `research/README.md` before it was filled; this document fills it.

---

## 1. Why Drawing Is a Different Evidentiary Act

Photography and prose each carry a familiar contract with the reader. A photograph asserts *this configuration of light reached a sensor*. Prose asserts *someone claims this*. A drawing asserts neither, and that is the problem it has to solve.

Three consequences follow, and every rule below descends from them:

1. **A drawing has no negative.** There is no unedited original to return to, so provenance cannot be reconstructed after the fact. It must be recorded while drawing, or it is gone.
2. **Every line is a decision.** A photographer can capture a detail without having chosen it. An artist cannot. Nothing in a drawn panel is incidental, so nothing in it is exempt from sourcing.
3. **Drawing renders the unphotographed as fluently as the photographed.** A room nobody entered draws exactly as convincingly as one the artist stood in. This is the form's central hazard: fluency is uncorrelated with fidelity.

The third point is why comics journalism needs *stricter* provenance discipline than prose reporting, not looser. A prose reporter who has not seen a room has to write around it, and the writing shows the gap. An artist who has not seen a room draws it anyway, at full confidence.

## 2. The Three Registers of Nonfiction Panel Content

Practitioners in the field distinguish three kinds of content, and the ethical failure is almost always **collapsing them into one visual treatment** rather than inventing outright.

| Register | What it is | Sourcing requirement |
|----------|-----------|---------------------|
| **Observed** | The artist was present | Direct: notes, photographs, sketches made on site |
| **Reconstructed** | Documented but not witnessed by the artist | Attributable: testimony, records, photographs by others — and the panel should carry a visual marker of its status |
| **Represented** | Deliberately non-literal: a metaphor, a diagram, a mental state | Must be visually unmistakable as non-literal |

The register a panel occupies should be legible from the panel. The commonest real-world failure is a reconstructed scene rendered with the same confident specificity as an observed one — not a lie, but an unmarked claim.

## 3. Sourcing Standards, Operationalised

The working standard in the field is stronger than "do not invent":

- **Every depicted specific traces to a source.** Insignia, signage, uniforms, vehicles, architecture, documents. A generic chair needs no source; a *particular* chair in a *particular* room does.
- **Composite characters are disclosed or forbidden.** Merging several real people into one figure is a documented technique, and an undisclosed composite is misattribution of testimony.
- **Confidence is recorded, not just the source.** `verified` (direct evidence) and `reported` (single-source testimony) are different claims, and a panel cannot express the difference on its own.
- **Absence is sourced too.** Drawing an empty street asserts the street was empty.

## 4. Consent, Identification, and Power

Sourcing answers *is this true*. Consent answers *may this be shown*, and the two are independent — a fully sourced panel can still be one that should not be published.

- **Identification is a graded decision, not binary.** An artist controls how recognisable a face is, and the gradient between exact likeness and unrecognisable is continuous and entirely under the artist's control. This is a capability prose does not have.
- **Consent is contextual.** Agreement to be interviewed is not agreement to be drawn, and agreement to be drawn is not agreement to be drawn *in this scene*.
- **The vulnerable-subject asymmetry.** Subjects with the least power over their depiction are typically those with the most at stake in it. Where consent cannot be meaningfully obtained, the honest options are reduced identifiability or not depicting the person.
- **Consent decisions belong to the publisher, not the renderer.** The person deciding whether a subject may be shown must be the person accountable for publishing.

## 5. The Camera Is an Argument

Direction carries editorial weight that no caption can retract, and in nonfiction that weight is an ethical instrument rather than a stylistic one.

- **Angle editorialises.** A low angle monumentalises; a high angle diminishes. Eye level is the neutral default *because* the alternatives are claims.
- **Framing assigns agency.** Who is in the frame when something happens attributes responsibility.
- **Interiority is the sharpest limit.** Drawing a real person's private feeling — a thought balloon, an unobserved expression alone in a room — asserts access no reporter has. Captions may carry the reporter's own interiority; panels may not invent the subject's.

## 6. Known Failure Modes

- **The fluent reconstruction** — an unwitnessed scene drawn with witnessed confidence
- **The composite that keeps its testimony** — a merged figure still quoted as one person
- **The decorative specific** — invented insignia or signage added because the panel looked empty
- **The editorialising angle** — a subject drawn from below to make them formidable, or above to make them pitiable
- **The borrowed photograph** — a source image traced closely enough to carry its authorship
- **Sourcing that never leaves the artist's head** — accurate work with no register, which cannot be checked, defended, or continued by anyone else

---

## Operationalised In

| Finding | Enforced by |
|---------|-------------|
| Every depicted specific traces to a source; confidence recorded | `comic-world-bible-system` §6 `source_register` (`claim`, `source`, `depicted_in`, `confidence`), validator-enforced for `production_mode: nonfiction` |
| No fabricated documentary detail | `reportage-comics-journalism` negative locks and style quality gates |
| Eye level as the ethical default; angle editorialises | `reportage-comics-journalism` Direction Notes |
| No invented interiority for a real subject | `reportage-comics-journalism` Dialogue & Lettering — captions carry observed fact and attribution only |
| Consent is a publisher decision, distinct from provenance | `comic-producer` contract; the register records provenance, **not** permission — stated explicitly in `comic-world-bible-system` |
| Real subjects carry a source note | `source_register` `source_note` per character, validator-enforced |

## Gaps This Study Leaves Open

- **The three registers are not yet a schema field.** Observed / reconstructed / represented is the sharpest distinction in the literature and the `source_register` cannot currently express it — a panel's register is inferable from `confidence` only by convention
- **Identifiability has no recorded gradient.** The bible stores whether a subject is sourced, not how recognisable the artist chose to make them
- **Composite disclosure is unmodelled** — nothing in the schema marks a character entry as a composite

---

*A photograph can be checked against the world. A drawing can only be checked against its record — so the record is the work.*
