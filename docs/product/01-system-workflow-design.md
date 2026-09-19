<!-- Author: Victor.I -->

# Product Design — 01 System Workflow Design

**Author:** Victor.I  
**Status:** Draft for review  
**Audience:** Systems, product, software, security  
**Related:** `architecture/data-flow.md`, `architecture/system.md`

---

## 1. Purpose

Define how work moves through the platform from sensing to human decision — independently of pixel layouts. UI screens must implement these workflows; they must not invent alternate control paths.

---

## 2. Operational workflow (human-centred)

```
MONITOR
  │
  ├─► DETECT anomaly / new track / sensor fault
  │         │
  │         ▼
  │    TRIAGE alert (tier, evidence glance)
  │         │
  │         ├─► DISMISS / ACKNOWLEDGE (low)
  │         │
  │         └─► INVESTIGATE
  │                   │
  │                   ▼
  │              REVIEW evidence pack
  │              (obs / inference / prediction separated)
  │                   │
  │                   ▼
  │              ASSESS risk + missing info
  │                   │
  │         ┌─────────┴─────────┐
  │         ▼                   ▼
  │    CONTINUE MONITOR    OPEN / JOIN INCIDENT
  │         │                   │
  │         │                   ▼
  │         │            COMMANDER REVIEW
  │         │                   │
  │         └─────────┬─────────┘
  │                   ▼
  │         HUMAN DECISION
  │         (authorised response CATEGORY only)
  │                   │
  │                   ▼
  │         OPTIONAL EXTERNAL HANDOFF
  │                   │
  │                   ▼
  │              AUDIT + OUTCOME
  │                   │
  └───────────────────┘
         back to MONITOR
```

**Hard rule:** Physical effects are never inside this loop. Categories are recorded intents for authorised external systems.

---

## 3. Platform workflow (system-centred)

```
PHYSICAL / SIM SENSORS
        │
        ▼
   SENSOR ADAPTERS
        │
        ▼
   NORMALISE + VALIDATE
        │
        ▼
     EVENT BUS
        │
   ┌────┼────┬──────────┐
   ▼    ▼    ▼          ▼
DETECT TRACK QUALITY  (parallel)
   │    │
   └────┤
        ▼
   SENSOR FUSION
        ▼
 BEHAVIOUR INDICATORS
        ▼
  RISK ASSESSMENT
        ▼
 ALERT POLICY ENGINE
        ▼
 DECISION SUPPORT UI
        ▼
  HUMAN APPROVAL
        ▼
 INTEGRATION API (category)
        ▼
     AUDIT LOG
```

Safety chain (must match requirements):

```
DETECTION → TRACK → CLASSIFY → ASSESS → PRIORITISE
→ HUMAN REVIEW → AUTHORISED RESPONSE CATEGORY → EXTERNAL SYSTEM
```

---

## 4. Swimlanes (who does what)

| Phase | Sensors / Edge | Platform | Operator | Commander | External |
|---|---|---|---|---|---|
| Sense | Emit raw | Adapt/normalise | — | — | — |
| Correlate | — | Detect/track/fuse | Monitor map | — | — |
| Alert | Health events | Policy tiers | Triage | Escalation inbox | — |
| Investigate | Cue request (category) | Evidence assembly | Drill into track | — | — |
| Decide | — | Enforce RBAC + audit | Propose / decide (role) | High-tier decide | — |
| Handoff | — | Outbox + retry | Confirm | Confirm | Ack/fail |
| Learn | — | Metrics | After-action notes | AAR review | — |

---

## 5. Workflow variants

### 5.1 Nominal single-object

New observation → track birth → class hypothesis → low/med risk → T1/T2 alert → operator acknowledges or cues sensor → continue monitor.

### 5.2 Suspected coordination / swarm

Multiple tracks pass behaviour gates → elevated risk → incident auto-open (policy) → commander queue → multi-track evidence → category decision → handoff optional.

### 5.3 Sensor degradation

Heartbeat miss → coverage degraded mode → confidence ceilings applied → operator notified of capability loss → fusion continues on remaining sensors → recovery event clears mode.

### 5.4 Contradictory evidence

Conflict flag on track → UI shows conflict strip → risk may widen uncertainty rather than pick a side → human resolves operationally (not forced auto-merge).

### 5.5 Integration failure

Decision saved locally → handoff status failed/DLQ → operator sees handoff state → retry per policy — decision itself remains valid.

### 5.6 Audit / IAM failure (fail closed)

Approval API refuses commit → UI blocks “Record decision” → view-only until restored.

---

## 6. State machines (logical)

### 6.1 Track lifecycle

```
CANDIDATE → ACTIVE → COASTING → REACQUIRED → DROPPED
                │
                └─► MERGED (into another track id, with audit link)
```

### 6.2 Alert lifecycle

```
RAISED → DELIVERED → ACKNOWLEDGED → IN_PROGRESS → RESOLVED
                              │
                              └─► SUPPRESSED (policy / duplicate)
```

### 6.3 Incident lifecycle

```
OPEN → ACTIVE → PENDING_DECISION → DECIDED → CLOSED
         │
         └─► ESCALATED
```

### 6.4 Decision / handoff

```
RECOMMENDATION_SHOWN → DECISION_RECORDED → HANDOFF_QUEUED
 → HANDOFF_ACKED | HANDOFF_FAILED | HANDOFF_NOT_REQUIRED
```

---

## 7. Timing expectations (UX-facing)

| Step | Operator expectation |
|---|---|
| New high-tier alert visible | Within ~1–2 s of risk update (see NFRs) |
| Open evidence for track | < 1 interaction from alert row |
| Record decision | Explicit confirm; no accidental single-click fire metaphor |
| Know system degraded | Persistent status chrome, not toast-only |

---

## 8. Workflow → screen mapping (preview)

| Workflow step | Primary screens |
|---|---|
| Monitor | `X01` Operator console |
| Triage | `X01` + `X02` Alert detail |
| Investigate | `X03` Track detail / evidence |
| Incident | `I01` Incident workspace |
| Decide | `X04` / `I02` Approval dialog |
| Health | `X05` Sensor & system health |
| Audit | `X06` Audit / history |
| Replay | `X07` Timeline replay |
| Admin adapters | `A01`–`A03` |
| Sim control | `S01` (lab) |

Full inventory: `05-ui-screen-inventory.md`.

---

## 9. What this workflow deliberately excludes

- Weapon aim / fire / jam parameter entry  
- Auto-execution of categories without human decision (except explicitly approved T0 notify policies, still audited)  
- Hidden AI decisions presented as sensor facts  

---

## Author

Victor.I
