<!-- Author: Victor.I -->

# Product Design — 10 System Workflow Diagrams (Visual Pack)

**Author:** Victor.I  
**Status:** Draft for review  
**Companion to:** `01-system-workflow-design.md`  
**Purpose:** Extra diagram-only views for reviews and workshops

---

## 1. Sense-to-decision pipeline

```
┌─────────┐   ┌──────────┐   ┌───────────┐   ┌─────────┐
│ Sensors │──►│ Adapters │──►│ Normalise │──►│  Bus    │
└─────────┘   └──────────┘   └───────────┘   └────┬────┘
                                                   │
         ┌─────────────┬─────────────┬─────────────┤
         ▼             ▼             ▼             ▼
    Detection     Tracking      Quality       (other)
         │             │
         └──────┬──────┘
                ▼
           Fusion ──► Behaviour ──► Risk ──► Alerts
                                              │
                                              ▼
                                      Operator UI
                                              │
                                              ▼
                                         Decision
                                              │
                                              ▼
                                      External API
                                      (category only)
                                              │
                                              ▼
                                           Audit
```

---

## 2. Operator loop (happy path)

```
        ┌──────────────── MONITOR (X01) ◄─────────────────┐
        │                      │                            │
        │                      ▼                            │
        │               ALERT appears                       │
        │                      │                            │
        │                      ▼                            │
        │               TRIAGE (X02)                        │
        │                      │                            │
        │         ┌────────────┼────────────┐               │
        │         ▼            ▼            ▼               │
        │       Ack/Dismiss  Evidence    Incident           │
        │                      │         (I01)              │
        │                      ▼            │               │
        │                   Track X03 ◄─────┘               │
        │                      │                            │
        │                      ▼                            │
        │                 Decide X04/I02                    │
        │                      │                            │
        │                      ▼                            │
        │              Handoff status                       │
        │                      │                            │
        └──────────────────────┴────────────────────────────┘
```

---

## 3. Epistemic stack (every detail view)

```
┌──────────────────────────────────────────┐
│ DECISION        human, stamped, audited  │  ← top authority
├──────────────────────────────────────────┤
│ RECOMMENDATION  policy suggestion only   │
├──────────────────────────────────────────┤
│ PREDICTION      dashed, assumptive       │
├──────────────────────────────────────────┤
│ INFERENCE       labelled, scored, version│
├──────────────────────────────────────────┤
│ OBSERVATION     measured / reported      │  ← bottom foundation
└──────────────────────────────────────────┘
```

---

## 4. Alert severity funnel

```
All events / track updates
        │
        ▼
 Quality + policy gates
        │
        ▼
   ┌────┴────┐
   │ drop /  │
   │ merge   │
   └────┬────┘
        ▼
   Tier assignment
        │
   ┌────┼────┬────┐
   ▼    ▼    ▼    ▼
  T0   T1   T2   T3
 log  list  act  interrupt
```

---

## 5. Incident coordination path

```
Multi-track behaviour hit
         │
         ▼
  Auto or manual incident
         │
         ▼
   I01 workspace
         │
    ┌────┴────┐
    ▼         ▼
 Evidence   Dual-control?
    │         │
    └────┬────┘
         ▼
   Category decision
         │
         ▼
  Handoff + close path
```

---

## 6. Failure visibility path

```
Component fails
      │
      ▼
 Health signal
      │
      ▼
 G02 degraded banner + mode Dn
      │
      ├─► Map coverage hatch (sensors)
      ├─► Disable Decide (audit/IAM)
      └─► Handoff FAILED module (integration)
      │
      ▼
 Recovery event ──► clear mode (audited)
```

---

## 7. Workshop use

Print or screen-share this file with `04-wireframes.md` side-by-side: left = workflow, right = layout.

---

## Author

Victor.I
