<!-- Author: Victor.I -->

# Deliverable 9 — Failure Mode and Effects Analysis (FMEA)

**Author:** Victor.I  
**Status:** Draft for review  
**Method:** Component failure → effect → detection → mitigation → residual severity

Severity (Sev): 1 low – 5 critical (safety/ops).  
Likelihood (Lik): 1 rare – 5 frequent without controls.  
Detectability (Det): 1 easy – 5 hard (higher = worse).  
RPN = Sev × Lik × Det (indicative only).

---

## 1. Guiding fail-safe principles

1. Prefer **fail visible** over fail silent.  
2. Prefer **degrade coverage** over inventing tracks.  
3. Prefer **block external handoff** over uncertain automation.  
4. Prefer **preserve audit** even if UI is impaired.  
5. Recommendations never become commands on failure.

---

## 2. FMEA table (selected high-value rows)

| ID | Component | Failure mode | Effect | Sev | Lik | Det | RPN | Detection | Mitigation / recovery |
|---|---|---|---|---|---|---|---|---|---|
| FM-01 | Sensor | Hard silence | Coverage hole | 4 | 4 | 2 | 32 | Health heartbeat | Coverage map; confidence ceiling; alert T1 |
| FM-02 | Sensor | Bias/miscal | Systematic track error | 4 | 3 | 4 | 48 | Cross-sensor residual | Quarantine sensor; calibration workflow |
| FM-03 | Adapter | Crash loop | Loss of modality | 3 | 3 | 2 | 18 | Restart metrics | Supervisor restart; buffer |
| FM-04 | Network edge↔central | Partition | Delayed/lost ops picture | 5 | 3 | 2 | 30 | Link probes | Edge buffer; local degraded UI optional; resync |
| FM-05 | Event bus | Broker outage | Pipeline stop | 5 | 2 | 1 | 10 | Bus health | Multi-broker; produce backpressure; status banner |
| FM-06 | Event bus | Poison message | Consumer stuck | 4 | 2 | 3 | 24 | Error budget / DLQ | Skip-to-DLQ policy; schema guards |
| FM-07 | Normaliser | Bad CRS map | Geospatial wrong | 5 | 2 | 4 | 40 | Geo unit tests; spot checks | Versioned transforms; kill-switch adapter |
| FM-08 | Clock sync | Skew | Mis-association | 4 | 3 | 3 | 36 | Skew metrics | Quality flag; widen gates; NTP/PTP monitor |
| FM-09 | DB hot | Primary down | API/query fail | 4 | 2 | 1 | 8 | Ready checks | Failover; read replica; freeze decisions if needed |
| FM-10 | Tracking | Divergent state | Duplicate/split tracks | 3 | 3 | 3 | 27 | Track quality KPIs | Reinit from bus replay; tuning |
| FM-11 | Fusion | Over-merge | Two objects as one | 4 | 3 | 4 | 48 | Operator reports; sim tests | Conservative assoc thresholds; evidence UI |
| FM-12 | Fusion | Under-merge | Fragmentation | 3 | 3 | 3 | 27 | Track count vs truth (sim) | Tune; still safer than over-merge often |
| FM-13 | Model inference | Timeout/down | Missed detections | 4 | 3 | 2 | 24 | Infer latency/errors | Fail policy: passthrough/last-known; rollback |
| FM-14 | Model inference | Silent bad outputs | Wrong class | 5 | 2 | 5 | 50 | Calibration monitors; spot eval | Canary; human evidence norms; disable route |
| FM-15 | Risk engine | Rule bug | Mis-prioritisation | 4 | 2 | 3 | 24 | Policy tests | Version pin; feature flag |
| FM-16 | Alert service | Storm | Operator overload | 4 | 3 | 2 | 24 | Alert rate SLI | Aggregate; suppress; breakers |
| FM-17 | Operator console | Blank/crash | Loss of HCI | 5 | 2 | 1 | 10 | RUM/synthetic | Redundant workstation; status page; API still audits if decisions via backup channel |
| FM-18 | Approval API | Down | Cannot decide | 4 | 2 | 1 | 8 | Health | Block handoff; paper procedure (ops); queue |
| FM-19 | Integration API | Down/DLQ | External not notified | 3 | 2 | 2 | 12 | Handoff metrics | Retry/DLQ; local record remains |
| FM-20 | Audit store | Write fail | Compliance break | 5 | 2 | 2 | 20 | Audit errors | Fail closed on decisions requiring audit |
| FM-21 | Object store | Outage | No raw replay | 2 | 2 | 1 | 4 | S3 errors | Hot path continues if metadata sufficient |
| FM-22 | Corrupt message | Partial JSON | Consumer errors | 3 | 3 | 2 | 18 | Schema validation | Quarantine |
| FM-23 | Duplicate burst | Reorders | Inflated counts | 2 | 4 | 2 | 16 | Idempotency | Dedup keys |
| FM-24 | Contradictory obs | Conflict | Confused UI | 3 | 4 | 2 | 24 | Conflict flags | Show conflict; don’t auto-resolve silently |
| FM-25 | AI assistant | Hallucination | Operator misled | 3 | 4 | 3 | 36 | Grounding checks | Citations required; not on critical path |
| FM-26 | Secrets leak | Credential theft | Broad compromise | 5 | 2 | 4 | 40 | Scanning; vault audit | Rotate; least privilege |
| FM-27 | Edge compute | Hardware fail | Local loss | 3 | 3 | 2 | 18 | Device health | Spare; central continue with remaining |

---

## 3. Graceful degradation modes

| Mode | Trigger | Behaviour |
|---|---|---|
| **D1 Coverage reduced** | Sensor loss | Map hatching; no synthetic tracks |
| **D2 Model degraded** | Infer errors | Sensor-native detections only; badge |
| **D3 Stale picture** | Bus lag | Banner with lag age; dim tracks |
| **D4 Decision freeze** | Audit/IAM fail | View-only |
| **D5 Integration offline** | External down | Local decisions only |
| **D6 Assistant off** | AI policy trip | Hide assistant |

---

## 4. Recovery and replay

1. Restore bus/DB health  
2. Replay observations from retention watermark  
3. Rebuild projections  
4. Verify audit continuity  
5. Exit degraded mode with operator acknowledgement  

---

## 5. Redundancy recommendations (MVP → later)

| Component | MVP | Hardened |
|---|---|---|
| Bus | Multi-broker single AZ | Multi-AZ |
| DB | Primary + replica | Auto failover |
| Gateway | 2 replicas | N+1 |
| Edge buffer | Optional | Required for field |

---

## 6. Open FMEA actions

- Quantify site-specific Sev with customer CONOPS  
- Add hardware-in-loop rows in Stage 7  
- Run chaos suite mapped to FM-IDs (see testing strategy)  

---

## Author

Victor.I
