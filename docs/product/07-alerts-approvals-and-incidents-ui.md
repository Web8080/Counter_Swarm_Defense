<!-- Author: Victor.I -->

# Product Design — 07 Alerts, Approvals, and Incidents UI

**Author:** Victor.I  
**Status:** Draft for review  
**Related:** journeys J1–J2–J8, screens X02/X04/I01/I02

---

## 1. Alert design

### 1.1 Tier meanings (operator-facing)

| Tier | Meaning | UI behaviour |
|---|---|---|
| T0 | Informational | Log/timeline; no interrupt |
| T1 | Advisory | Listed; soft highlight |
| T2 | Action suggested | Listed + optional sound policy |
| T3 | Commander attention | Assertive row + optional sticky until ack |

### 1.2 Alert row anatomy

```
[TIER] Reason (short) · Track/Incident link · Age · Policy id · [Ack]
```

Secondary line: “Why now” one sentence from policy template.

### 1.3 Fatigue controls (UI)

- Duplicate suppression badge (“+12 similar”)  
- Per-track collapse  
- Quiet mode for T1 (role/policy)  
- Rate meter for operators/admins when storm detected  

### 1.4 Alert → evidence

One click from row to X03 or incident; do not force a separate search.

---

## 2. Recommendation UI

Recommendations appear in the risk/action panel and inside X04 pre-selected but **changeable**.

Must show:

- Policy id / version  
- Category  
- Supporting factor chips  
- Explicit “not executed” state  

---

## 3. Approval / decision UI

### 3.1 Required fields

| Field | Rule |
|---|---|
| Category | Required enum |
| Rationale | Required for T2+ / incident decisions |
| Context links | Auto-filled track/incident ids |
| Idempotency | Client key hidden |

### 3.2 Confirm pattern

Primary button label: **Record decision** — never “Launch”, “Engage”, “Fire”, “Jam”.

Secondary: Cancel.

Success state shows decision id + handoff status module.

### 3.3 Dual-control

When policy requires:

1. First approver submits → state PENDING_SECOND  
2. Second approver sees locked category (or allowed delta per policy)  
3. On completion → DECIDED  

UI must show who is waiting.

### 3.4 Fail-closed

If audit or IAM unavailable: Decide controls disabled with G02-D4 banner.

---

## 4. Incident UI

### 4.1 When incidents appear

- Manual open from tracks/alerts  
- Auto-open from behaviour/risk policy  

### 4.2 Workspace jobs (one purpose each)

| Region | Job |
|---|---|
| Map subset | See members spatially |
| Summary | Risk + missing info + recommendation |
| Timeline | Shared narrative |
| People | Ownership / dual-control |
| Handoff | External status |

### 4.3 Closing

Close requires state DECIDED or explicit “close without decision” reason (audited, restricted).

---

## 5. Handoff status UI

| Status | Operator sees |
|---|---|
| NOT_REQUIRED | — |
| QUEUED | Spinner / queued |
| ACKED | Success with external ref if any |
| FAILED | Error + retry if permitted |
| DLQ | Needs admin |

---

## 6. Notification channels (product rules)

| Channel | Use |
|---|---|
| In-console | Primary |
| Sound | Policy optional for T3 |
| Email/SMS | Out of MVP unless customer mandates |
| Mobile push | P2 |

---

## 7. Worked example (swarm)

1. Behaviour indicator fires on three tracks → T3 alert + incident I-22  
2. Commander opens I01, reads missing RF on one track  
3. Chooses NOTIFY_EXTERNAL with rationale  
4. Dual-control completes  
5. Handoff ACKED  
6. Audit shows full chain with model versions  

Wireframes: `04-wireframes.md` WF-I01, WF-X04, WF-I02.

---

## Author

Victor.I
