<!-- Author: Victor.I -->

# Product Design — 02 User Journeys

**Author:** Victor.I  
**Status:** Draft for review  
**Related:** `01-system-workflow-design.md`, personas in `executive-definition.md`

---

## 1. Journey map legend

```
[Actor] step
   │
   ▼
(system) automated step
   │
   ▼
{decision} human choice
```

Priority: **P0** journeys must be supported by Stage 5 UI.

---

## 2. Journey J1 — Unknown object (Security Operator) — P0

**Goal:** Understand what appeared, how sure we are, what to do next.

```
Operator on X01 Monitor
   │
   ▼
(system) raises T2 alert "New track T-104"
   │
   ▼
Operator selects alert
   │
   ▼
X02 / X03 shows:
  OBSERVATION strip | INFERENCE class | confidence band | sensors involved
   │
   ▼
Operator opens evidence graph (obs → assoc → track)
   │
   ▼
{decision}
  ├─ Acknowledge + continue monitor
  ├─ Cue sensor (category CUE_SENSOR) → X04
  ├─ Open incident
  └─ Dismiss with reason
   │
   ▼
(system) writes audit; updates alert state
```

**Success:** Operator states class hypothesis and confidence in own words within 30–60 s in trials.  
**Failure:** Operator cannot tell inference from observation.

---

## 3. Journey J2 — Suspected swarm (Commander) — P0

**Goal:** Decide whether coordination indicators warrant elevated category.

```
(system) behaviour indicators on tracks T-104, T-105, T-109
   │
   ▼
(system) risk elevated + incident I-22 auto-opened (policy)
   │
   ▼
Commander opens I01 Incident workspace
   │
   ▼
Reviews multi-track map subset + shared timeline + missing-info panel
   │
   ▼
Optional: ask AI assistant for summary (tool-bounded) — not required
   │
   ▼
{decision} on I02
  ├─ HEIGHTEN_MONITORING
  ├─ NOTIFY_EXTERNAL
  ├─ REQUEST_ESCALATION
  └─ Reject recommendation / choose other category
   │
   ▼
(system) handoff if required → status visible
   │
   ▼
Audit complete; incident → DECIDED / CLOSED path
```

**Success:** Decision cites evidence IDs; handoff state understood.  
**Failure:** Commander treats swarm score as confirmed fact.

---

## 4. Journey J3 — Sensor degradation (Sensor Operator) — P0

```
(system) RF-02 heartbeat timeout
   │
   ▼
X01 status: COVERAGE DEGRADED; map hatching on RF sector
   │
   ▼
Sensor operator opens X05
   │
   ▼
Sees last obs age, error, adapter version
   │
   ▼
{action} escalate to engineer / switch backup feed (ops process)
   │
   ▼
(system) recovery → mode clear event audited
```

**Success:** No fake tracks invented to “fill” the hole.

---

## 5. Journey J4 — Contradictory classification (Analyst / Operator) — P1

```
Track shows class conflict (radar UAV-like vs EO bird-like)
   │
   ▼
X03 conflict strip + both hypotheses with scores + model versions
   │
   ▼
Operator cues EO / requests another look
   │
   ▼
Risk uncertainty widens rather than forced pick
   │
   ▼
Human notes resolution in decision/incident comment
```

---

## 6. Journey J5 — After-action replay (Analyst) — P1

```
Analyst opens X07 Replay for incident I-22
   │
   ▼
Scrubs timeline; map shows historical tracks
   │
   ▼
Exports evidence pack (role-gated)
   │
   ▼
Feeds DS evaluation / training notes (offline)
```

---

## 7. Journey J6 — Admin onboards simulator adapter (Engineer) — P1

```
A01 Adapter list → A02 Create/edit sim adapter
   │
   ▼
Schema version validate → enable in lab env only
   │
   ▼
S01 start scenario → observations appear on X01
```

---

## 8. Journey J7 — AI-assisted investigation (optional) — P2

```
Operator on X03 → opens assistant drawer
   │
   ▼
"Why is T-104 elevated?"
   │
   ▼
(system) policy tools fetch risk + evidence; returns cited answer
   │
   ▼
Operator still uses X04 for any decision (assistant cannot commit)
```

---

## 9. Journey J8 — Failed external handoff — P0

```
Decision recorded NOTIFY_EXTERNAL
   │
   ▼
(system) integration fails / DLQ
   │
   ▼
UI shows HANDOFF_FAILED with retry eligibility
   │
   ▼
{action} retry / escalate IT / accept local-only
```

---

## 10. Cross-journey UX requirements

| Need | Rule |
|---|---|
| Orientation | Role + site + mode always visible |
| Interrupt | T3 alerts assert without wiping map context |
| Undo | Dismiss/ack reversible per policy window; decisions are not “casual undo” |
| Handover | Incident ownership transferable with audit |

---

## Author

Victor.I
