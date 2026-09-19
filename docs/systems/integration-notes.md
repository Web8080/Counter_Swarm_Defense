<!-- Author: Victor.I -->

# Agent 8 — Systems Engineering Integration Notes

**Author:** Victor.I  
**Status:** Stage 0 research note  
**Primary artefacts:** `architecture/*`, `docs/systems/*`

---

## Integration stance

Do not concatenate agent proposals. Challenge contradictions:

| Tension | Resolution |
|---|---|
| PD wants rich AI UX vs SG risk | Assistant off critical path; epistemic UI rules |
| ML wants edge GPU vs SE ops cost | Central-primary MVP; edge-ready packaging |
| DE wants many stores vs simplicity | Postgres + bus + S3 only for MVP |
| SE microservices vs timeline | Modular services, not nanoservices |

## Hardware integration pattern

```
PHYSICAL SENSOR → VENDOR SDK → ADAPTER → CANONICAL OBSERVATION → PLATFORM
PLATFORM → CONTROLLED API → EXTERNAL SYSTEM
```

Never depend on undocumented proprietary behaviour in core modules.

## Stage gates

Owned by SYS with SG co-approval on field test and any autonomy-adjacent change.

## What not to build

One-off vendor cores; irreversible coupling to a single radio/effector.
