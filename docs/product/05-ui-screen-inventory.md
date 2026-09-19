<!-- Author: Victor.I -->

# Product Design — 05 UI Screen Inventory

**Author:** Victor.I  
**Status:** Draft for review  
**Audience:** Engineers and reviewers building Stage 5 UI  
**Rule:** Every fetchable view documents loading / loaded / empty / error

---

## 1. Inventory summary

| ID | Name | Priority | Primary journey |
|---|---|---|---|
| X01 | Operator monitor console | P0 | J1, J2, J3 |
| X02 | Alert detail | P0 | J1 |
| X03 | Track detail / evidence | P0 | J1, J4 |
| X04 | Record decision | P0 | J1, J2, J8 |
| X05 | Sensor & system health | P0 | J3 |
| X06 | Audit history | P0 | governance |
| X07 | Timeline replay | P1 | J5 |
| X08 | Assistant drawer | P2 | J7 |
| I01 | Incident workspace | P0 | J2 |
| I02 | Incident decision / dual-control | P1 | J2 |
| I03 | Incident list | P1 | J2 |
| A01 | Adapter list | P1 | J6 |
| A02 | Adapter create/edit | P1 | J6 |
| A03 | Alert/risk policy editor | P1 | admin |
| A04 | Roles & permissions view | P1 | admin |
| S01 | Sim director | P1 | J6 |
| S02 | Scenario library | P2 | lab |
| R01 | After-action report | P2 | J5 |
| G01 | Sign-in / session | P0 | all |
| G02 | Global degraded banner states | P0 | FMEA modes |
| G03 | Access denied | P0 | security |

---

## 2. Screen specifications

### G01 — Sign-in / session — P0

| Item | Spec |
|---|---|
| Purpose | OIDC login, show site selection if multi-site later |
| Entry | Unauthenticated hit to `/app` |
| Actions | Sign in, cancel |
| States | loading IdP · ready · error (IdP down) · session expired modal |
| Notes | No local password DB in-app |

### G02 — Global degraded banners — P0

| Mode | Banner copy (intent) | UI effect |
|---|---|---|
| D1 Coverage reduced | Sensing coverage reduced — track confidence capped | Map hatch |
| D2 Model degraded | Detection model unavailable — sensor-native only | Badge on inferences |
| D3 Stale picture | Event lag {n}s — picture may be stale | Dim live indicators |
| D4 Decision freeze | Decisions unavailable — view only | Disable Decide |
| D5 Integration offline | External handoff unavailable | Handoff status only |
| D6 Assistant off | Assistant disabled by policy | Hide X08 |

### X01 — Operator monitor — P0

| Item | Spec |
|---|---|
| Purpose | Continuous air picture + triage |
| Regions | Shell, map, alerts, tracks, risk/action, bottom dock |
| Data | tracks, alerts, risk for selection, health pills, timeline stream |
| Actions | select alert/track, layer toggles, Simplify, open Decide, open Health |
| States | loading skeleton map+lists · loaded · empty (no tracks) · error (API) · degraded (G02) |
| Empty | “No active tracks in filter” + clear filters |
| Error | Retry + status link |
| Annotation | Selected track syncs all panels; T3 asserts without losing map pan context |

### X02 — Alert detail — P0

| Item | Spec |
|---|---|
| Purpose | Why this alert, linked objects, next actions |
| Data | alert, linked tracks, epistemic strips, policy id |
| Actions | ack, open track, open incident, decide |
| States | loading · loaded · not found · error |
| Annotation | Must show policy id and tier rationale |

### X03 — Track detail / evidence — P0

| Item | Spec |
|---|---|
| Purpose | Full evidence pack for one track |
| Data | track state, obs list, detections, fusion links, class distribution, behaviour flags, risk, recommendation, conflicts |
| Actions | cue (via decide category), incident, decide, copy deep link |
| States | loading · loaded · dropped track read-only · error |
| Annotation | Class shown as distribution, not single hard label |

### X04 — Record decision — P0

| Item | Spec |
|---|---|
| Purpose | Commit authorised category with rationale |
| Data | context ids, recommendation, category enum, dual-control flag |
| Actions | cancel, record (idempotent key) |
| States | editing · submitting · success · error · blocked (D4) · validation (rationale required) |
| Annotation | Explicit non-weapon notice always visible |
| Safety | No category control that looks like arm/fire |

### X05 — Health — P0

| Item | Spec |
|---|---|
| Purpose | Sensor + platform integrity |
| Data | sensor health events, bus lag, service health, model route status |
| Actions | open adapter (if permitted), acknowledge fault |
| States | loading · loaded · error |

### X06 — Audit — P0

| Item | Spec |
|---|---|
| Purpose | Accountable history |
| Data | audit records, filters, digest |
| Actions | filter, export (role-gated), open related track/incident |
| States | loading · loaded · empty · error · export denied |

### X07 — Replay — P1

| Item | Spec |
|---|---|
| Purpose | Time-scrubbed reconstruction |
| Data | historical projections / bus replay API |
| Actions | play, speed, scrub, export pack |
| States | loading range · playing · buffering · error · no data in range |

### X08 — Assistant drawer — P2

| Item | Spec |
|---|---|
| Purpose | Grounded Q&A via allowlisted tools |
| Actions | ask, clear, open cited entity |
| States | idle · thinking · answered · tool-denied · unavailable |
| Annotation | Cannot submit decisions; citations required |

### I01 — Incident workspace — P0

| Item | Spec |
|---|---|
| Purpose | Multi-track coordinated event handling |
| Data | incident, track set, shared risk, notes, participants, handoff |
| Actions | decide, transfer, close, add note |
| States | loading · active · decided · closed · error |

### I02 — Incident decision — P1

Extends X04 with incident context and optional dual-control lane.

### I03 — Incident list — P1

Filterable list by state, owner, severity; row opens I01.

### A01–A04 — Admin — P1

Adapters CRUD (env-scoped), policy version editor (diff + publish), roles read/assign (IdP-backed).

### S01–S02 — Lab — P1/P2

Scenario run controls; never available in OPS env build flags.

### R01 — After-action — P2

Read-only narrative assembled from audit + timeline; export PDF/JSON later.

### G03 — Access denied — P0

Clear role message; no data leakage in error body.

---

## 3. Cross-screen interaction rules

1. Deep links: `/tracks/T-104` opens X01+X03 pattern.  
2. Selection bus: one selected track id shared across X01 panels.  
3. Toasts only for transient success; durable state uses banners/status.  
4. Destructive/high impact = modal X04/I02 only.  
5. Keyboard: `/` focus filter, `Esc` close drawer, `g h` health (optional later).

---

## 4. Content & microcopy principles

- Prefer “Elevated risk (model/policy)” over “Threat confirmed”  
- Prefer “Authorised category” over “Engage”  
- Prefer “Inference” label near model outputs  
- Prefer “Coverage reduced” over hiding loss  

---

## 5. Screenshot placeholders (for later design renders)

When visual comps exist, store under `docs/product/screenshots/`:

| File | Screen |
|---|---|
| `x01-monitor.png` | X01 |
| `x03-evidence.png` | X03 |
| `x04-decide.png` | X04 |
| `i01-incident.png` | I01 |
| `x05-health.png` | X05 |

![X01 Monitor placeholder](./screenshots/x01-monitor.png)  
![X03 Evidence placeholder](./screenshots/x03-evidence.png)  
![X04 Decide placeholder](./screenshots/x04-decide.png)

(Images to be added after visual design pass; wireframes in `04-wireframes.md` are authoritative until then.)

---

## Author

Victor.I
