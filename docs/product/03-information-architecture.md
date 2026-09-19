<!-- Author: Victor.I -->

# Product Design — 03 Information Architecture

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Primary navigation

Operator console is **map-first**, not menu-first.

```
┌─ Shell ────────────────────────────────────────────────────────┐
│ Brand | Site | Mode | Role user | Health pills | Help | Logout │
├────────────────────────────────────────────────────────────────┤
│                         MAP CANVAS                              │
│                    (primary workspace)                          │
├──────────────┬─────────────────────┬───────────────────────────┤
│ Alerts       │ Tracks / Incidents  │ Risk & actions            │
├──────────────┴─────────────────────┴───────────────────────────┤
│ Bottom dock tabs: Timeline | Sensors | System | Audit | AI*    │
└────────────────────────────────────────────────────────────────┘
* AI tab only if enabled by policy
```

Admin and Simulation are separate apps/routes with clear env badges (`LAB`, `STAGING`, `OPS`).

---

## 2. Object model (UI-facing)

| Object | Meaning | Key fields shown |
|---|---|---|
| Observation | Raw normalised sensing fact | time, sensor, quality |
| Detection | Model or sensor detection | score, model version |
| Track | Estimated object over time | id, state, kinematics, quality |
| Evidence link | Obs/det contributing to track | ids, weights |
| Behaviour indicator | Pattern signal | type, score, track set |
| Risk assessment | Graded judgement | level, factors, missing info, version |
| Alert | Prioritised attention request | tier, reason, links |
| Recommendation | Suggested category | category, policy id |
| Decision | Human-authorised category | actor, time, rationale |
| Incident | Container for multi-track event | ownership, state |
| Sensor | Source health & coverage | status, last obs |
| Handoff | External category delivery | status |

---

## 3. Epistemic layers (must be IA-visible)

Every detail view stacks:

1. **Observation** — measured / reported  
2. **Inference** — model or fusion judgement  
3. **Prediction** — forward envelope  
4. **Recommendation** — policy suggestion  
5. **Decision** — human record  

These are IA categories, not optional styling.

---

## 4. Sitemap

```
/app
  /monitor          X01
  /alerts/:id       X02
  /tracks/:id       X03
  /decide           X04 (modal/route)
  /health           X05
  /audit            X06
  /replay           X07
  /incidents        I01 list
  /incidents/:id    I01 workspace
  /incidents/:id/decide  I02

/admin
  /adapters         A01
  /adapters/:id     A02
  /policies         A03
  /users-roles      A04

/lab
  /sim              S01
  /scenarios        S02

/reports
  /aar/:id          R01
```

---

## 5. Declutter & layers (map IA)

Default on: tracks (active), geofences, alert highlights.  
Default off: raw observations, predictions, sensor FOV (toggle).  
Emergency: “Simplify” preset hides all but T2+/T3 and active incidents.

---

## 6. Permissions → visible IA

| Role | Sees |
|---|---|
| Security operator | Monitor, alerts, tracks, decide (per policy), audit read |
| Sensor operator | Monitor, health emphasis, limited decide |
| Commander | Incidents, high-tier decide, AAR |
| Analyst | Replay, audit, export |
| Admin | Admin tree |
| Instructor (lab) | Sim + optional truth overlay |

---

## Author

Victor.I
