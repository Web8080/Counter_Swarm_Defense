<!-- Author: Victor.I -->

# Schemas

Canonical JSON Schema drafts for Stage 0. Producers/consumers must not invent parallel shapes.

| File | Purpose |
|---|---|
| [observation.v1.json](observation.v1.json) | Canonical observation (ICD-01/02) |
| [human.decision.v1.json](human.decision.v1.json) | Human authorised category (ICD-10) |

Event families (`detection.v1`, `track.update.v1`, `risk.assessment.v1`, …) will be added as Stage 1 contracts freeze. Conceptual definitions: `architecture/data-flow.md`, `architecture/interfaces.md`.

## Author

Victor.I
