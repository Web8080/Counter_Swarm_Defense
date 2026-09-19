<!-- Author: Victor.I -->

# Auditability Design

**Author:** Victor.I  
**Status:** Stage 0 complete (design)  
**Owner:** Security & Governance (Accountable) · Software Engineering (Responsible)  
**Related:** FR-AUD-*, threat model TM-04, ICD-10

---

## 1. Audit chain (mandatory)

```
Observation → Model output → Evidence → Risk assessment
→ Recommendation → Human decision → Outcome / handoff
```

Each material hop produces an append-oriented record that can answer:

| Question | Field sources |
|---|---|
| What happened? | event_type, summary |
| When? | timestamp_utc |
| Which sensor? | sensor_id(s), observation_id(s) |
| Which model / version? | model_id, model_version |
| What evidence? | evidence_refs[] |
| What confidence? | scores / quality flags |
| Who reviewed? | actor_id, role |
| What decision? | category, rationale |
| What system state? | degraded_modes[], policy_version |

---

## 2. Integrity controls

- Append-only store or hash-chained records  
- Decisions **fail closed** if audit write fails  
- Separate read role for investigators; no update/delete for operators  
- Retention ≥ customer policy (design default ≥ 1 year)

---

## 3. Non-goals

- Public blockchain  
- Editable “notes” pretending to be audit  

---

## Author

Victor.I
