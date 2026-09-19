<!-- Author: Victor.I -->

# Product Design — 04 Wireframes

**Author:** Victor.I  
**Status:** Draft for review  
**Fidelity:** Low — structure, hierarchy, and regions (not final visual design)  
**Screen specs:** `05-ui-screen-inventory.md`

---

## 1. Conventions

```
[ ] interactive control
( ) status / read-only
=== epistemic strip labels
```

All wireframes assume desktop operations (primary). Responsive notes at end.

---

## 2. WF-X01 — Operator console (Monitor) — P0

```
+==============================================================================+
| COUNTER-SWARM   Site:ALPHA   Mode:MONITOR   op_j.smith   (SYS OK) (SENS 3/4) |
+==============================================================================+
| MAP                                                                          |
|  ..........................................................................  |
|  .  coverage hatch (RF-02 lost)      * T-091                                 |
|  .                         (ellipse) @ T-104  << selected                    |
|  .                              geofence ----                                |
|  ..........................................................................  |
|  layers:[Tracks][Uncertainty][FOV][Obs][Predict]   [Simplify] [Fit]         |
+------------------+---------------------------+-------------------------------+
| ALERTS           | ACTIVE TRACKS             | RISK / NEXT ACTION            |
| * T3 Swarm ind.  | T-104  UAV? 0.72  q:GOOD  | Track T-104                   |
|   T2 New track   | T-105  UAV? 0.68  q:FAIR  | Risk: ELEVATED (v3)           |
|   T1 RF-02 down  | T-091  Bird? 0.61         | Missing: RF corroboration     |
|                  | T-088  Unk  0.40  COAST   | Rec: HEIGHTEN_MONITORING      |
|                  |                           | [Review evidence] [Decide]    |
+------------------+---------------------------+-------------------------------+
| TIMELINE | SENSORS | SYSTEM | AUDIT | ASSISTANT                              |
| --12:01:02 obs RDR-1 | 12:01:03 det | 12:01:04 track upd | 12:01:05 risk -- |
+==============================================================================+
```

**Notes:** Map is the hero surface. Side panels serve triage. No card grid of marketing stats in the first viewport.

---

## 3. WF-X02 — Alert detail (drawer or split) — P0

```
+--------------------------------------------------+
| ALERT A-8841                         Tier: T2    |
| Reason: New track quality crossed policy P-14    |
| Linked: T-104                                    |
|--------------------------------------------------|
| === OBSERVATION ===                              |
| 3 obs in last 8s · sensors RDR-1, EO-3           |
| === INFERENCE ===                                |
| class UAV p=0.72 · model det-v3.2                |
| === PREDICTION ===                               |
| 60s kinematic envelope (toggle on map)           |
| === RECOMMENDATION ===                           |
| CUE_SENSOR (optional)                            |
|--------------------------------------------------|
| [Acknowledge] [Open track] [Open incident]       |
| [Decide...]                                      |
+--------------------------------------------------+
```

---

## 4. WF-X03 — Track detail / evidence — P0

```
+==============================================================================+
| Track T-104   state:ACTIVE   age:00:01:14   quality:GOOD                     |
+==============================================================================+
| MAP FOCUS (dim others)          | EPISTEMIC STACK                            |
|   uncertainty ellipse           | === OBSERVATION ===                        |
|   selected track path           | list obs ids · quality · sensor            |
|                                 | === INFERENCE ===                          |
|                                 | class distribution bars                    |
|                                 | fusion contributors                        |
|                                 | === PREDICTION ===                         |
|                                 | envelope + assumptions                     |
|                                 | === RECOMMENDATION ===                     |
|                                 | policy P-12 → HEIGHTEN_MONITORING          |
|                                 | === DECISION ===                           |
|                                 | Pending                                    |
+---------------------------------+--------------------------------------------+
| EVIDENCE GRAPH                                                           |
|  obs-1 ─┐                                                                |
|  obs-2 ─┼─► det-9 ─► track T-104 ─► behaviour? ─► risk ELEVATED          |
|  obs-3 ─┘                                                                |
| CONFLICT: none | CLASS_CONFLICT | ASSOC_AMBIGUOUS                            |
+------------------------------------------------------------------------------+
| [Acknowledge] [Cue sensor] [Open incident] [Decide] [Copy link]              |
+==============================================================================+
```

---

## 5. WF-X04 — Human approval dialog — P0

```
+----------------------------------------------------------+
| Record authorised response category                      |
|----------------------------------------------------------|
| Context: Track T-104 · Incident I-22 (optional)          |
| Recommended: HEIGHTEN_MONITORING                         |
|                                                          |
| Select category:                                         |
|  ( ) DISMISS                                             |
|  (•) HEIGHTEN_MONITORING                                 |
|  ( ) CUE_SENSOR                                          |
|  ( ) NOTIFY_EXTERNAL                                     |
|  ( ) REQUEST_ESCALATION                                  |
|  ( ) OPEN_INCIDENT                                       |
|                                                          |
| Rationale (required for T2+): [________________________] |
|                                                          |
| Notice: This records intent for authorised systems.      |
| It does not control weapons or electronic attack.        |
|                                                          |
| Dual-control: (not required by policy)                   |
|                                                          |
| [Cancel]                          [Record decision]      |
+----------------------------------------------------------+
```

---

## 6. WF-X05 — Sensor & system health — P0

```
+==============================================================================+
| HEALTH                                                                       |
+----------------------------------+-------------------------------------------+
| SENSORS                          | PLATFORM                                  |
| RDR-1   OK    last 0.4s          | API       OK                              |
| EO-3    OK    last 1.1s          | Bus lag   120ms                           |
| RF-02   DOWN  last 42s           | Tracking  OK                              |
| MIC-1   OK    last 0.8s          | Models    det-v3.2 OK                     |
|                                  | Audit     OK                              |
+----------------------------------+-------------------------------------------+
| COVERAGE MAP (sectors)           | RECENT FAULTS                             |
|  [hatched RF sector]             | 12:00:51 RF-02 heartbeat miss             |
+==============================================================================+
```

---

## 7. WF-X06 — Audit history — P0

```
+==============================================================================+
| AUDIT  filters:[time][user][track][category][model]                          |
+------------------------------------------------------------------------------+
| 12:04:11  DECISION  j.smith  HEIGHTEN_MONITORING  T-104  evid:3  model:v3.2|
| 12:04:10  RECOMMEND policy P-12                                              |
| 12:04:09  RISK      elevated  factors:[coord,prox]                           |
| 12:03:55  TRACK     merge candidate rejected                                 |
| ...                                                                          |
+------------------------------------------------------------------------------+
| Detail pane: full JSON digest + hash chain ref (read-only)                   |
+==============================================================================+
```

---

## 8. WF-X07 — Timeline replay — P1

```
+==============================================================================+
| REPLAY  Incident I-22 / free range                                           |
| [<] =====|==================== [>]  12:01:00 --- 12:05:00   [Play] [1x][4x] |
| MAP historical + TRACK LIST frozen to scrub time                             |
| EVENT TICKS under scrubber (obs / risk / decision)                           |
+==============================================================================+
```

---

## 9. WF-I01 — Incident workspace — P0

```
+==============================================================================+
| INCIDENT I-22  SUSPECTED_COORDINATION  owner:cmdr.lee  state:ACTIVE          |
+------------------------------------------------------------------------------+
| MAP (incident tracks only)     | SUMMARY                                     |
|  T-104 T-105 T-109             | Risk: HIGH band                             |
|                                | Behaviour: formation-like (indicator)       |
|                                | Missing: RF on T-109                        |
|                                | Rec: NOTIFY_EXTERNAL                        |
+--------------------------------+---------------------------------------------+
| SHARED TIMELINE + NOTES        | PARTICIPANTS / HANDOFF STATUS               |
|                                | [Decide] [Transfer ownership] [Close]       |
+==============================================================================+
```

---

## 10. WF-I02 — Commander decision (dual-control variant) — P1

```
+----------------------------------------------------------+
| Decision requires dual-control (policy)                  |
| Category: NOTIFY_EXTERNAL                                |
| Approver A: cmdr.lee     [Signed]                        |
| Approver B: waiting...                                   |
| [Request second approval]        [Cancel]                |
+----------------------------------------------------------+
```

---

## 11. WF-A01 — Adapters admin — P1

```
+==============================================================================+
| ADAPTERS                                                     env badge: LAB  |
| id           type    schema   health   last obs   errors   [Enable] [Edit]   |
| rdr-sim-01   radar   obs.v1   OK       0.4s       0                          |
| eo-sim-02    eo      obs.v1   DEGRADED 12s        clock skew                 |
| [Add adapter]                                                                |
+==============================================================================+
```

---

## 12. WF-S01 — Simulation director (lab) — P1

```
+==============================================================================+
| SIM DIRECTOR                                                 env: LAB ONLY   |
| Scenario: [swarm_crossing_v3 v]  seed:42  [Load] [Start] [Pause] [Inject]  |
| Faults: [ ] drop RF  [ ] delay EO  [ ] duplicate  [ ] corrupt               |
| Truth overlay: ( ) off  (•) instructor only                                  |
| Link: console X01 receiving sim observations                                 |
+==============================================================================+
```

---

## 13. Mobile / constrained — P2

Not primary. If required later: alert queue + selected track summary + decide; map is secondary. Wireframe deferred until CONOPS demands handheld.

---

## 14. Wireframe review checklist

- [ ] Observation vs inference visually separable in X02/X03  
- [ ] No “Fire” / effector language in X04  
- [ ] Degraded coverage visible on X01 without opening health  
- [ ] Decision blocked path shown when audit/IAM down  
- [ ] Lab screens carry LAB badge  

---

## Author

Victor.I
