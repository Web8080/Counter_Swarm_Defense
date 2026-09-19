<!-- Author: Victor.I -->

# Product Design Pack — Index

**Author:** Victor.I  
**Status:** Draft for review  
**Purpose:** Split product, workflow, wireframe, and UI/UX design into reviewable documents (not one mega-file).

---

## How to read this pack

| Order | Document | What you get |
|---|---|---|
| 1 | [executive-definition.md](executive-definition.md) | Problem, personas, value, research summary |
| 2 | [01-system-workflow-design.md](01-system-workflow-design.md) | End-to-end operational and system workflows |
| 3 | [02-user-journeys.md](02-user-journeys.md) | Role-based journeys with decision points |
| 4 | [03-information-architecture.md](03-information-architecture.md) | Navigation, regions, object model for UI |
| 5 | [04-wireframes.md](04-wireframes.md) | Low-fidelity layout wireframes |
| 6 | [05-ui-screen-inventory.md](05-ui-screen-inventory.md) | Screen IDs, states, annotations for build |
| 7 | [06-ux-principles-and-visual-language.md](06-ux-principles-and-visual-language.md) | Epistemic UX rules, typography, colour intent |
| 8 | [07-alerts-approvals-and-incidents-ui.md](07-alerts-approvals-and-incidents-ui.md) | Alert triage, human approval, incident UI |
| 9 | [08-design-tokens.md](08-design-tokens.md) | Tokens for later implementation |
| 10 | [09-open-design-decisions.md](09-open-design-decisions.md) | Blocking vs non-blocking design questions |
| 11 | [10-system-workflow-diagrams.md](10-system-workflow-diagrams.md) | Extra diagram pack for workshops |
| — | [VISUALS.md](VISUALS.md) | HTML + PDF visual pack index |
| — | [html/simulation-and-ui-pack.html](html/simulation-and-ui-pack.html) | Rendered UI & simulation screens |
| — | [pdfs/UI-UX-and-Simulation-Visual-Pack.pdf](pdfs/UI-UX-and-Simulation-Visual-Pack.pdf) | PDF for review |
| — | [../simulation/README.md](../simulation/README.md) | Simulation design pack |

Supporting: [agent-notes.md](agent-notes.md)

---

## Design priority marks

- **P0** — Cannot ship Stage 5 operator platform without  
- **P1** — Should ship; workaround exists  
- **P2** — Later  
- **BLOCKED** — Needs CONOPS / policy answer  

---

## Screen ID convention

| Prefix | Surface |
|---|---|
| `X` | Operator console (primary C2) |
| `I` | Incident workspace |
| `A` | Admin / configuration |
| `S` | Simulation / instructor (lab) |
| `R` | Reports / after-action |

IDs are permanent. Do not renumber; supersede with a new ID if replaced.

---

## Author

Victor.I
