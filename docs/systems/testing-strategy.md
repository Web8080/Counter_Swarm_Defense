<!-- Author: Victor.I -->

# Deliverable 13 — Testing Strategy

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Principles

- Tests follow interfaces (ICD), not accidental implementation details  
- Simulation is a first-class test harness  
- Safety tests prove we **cannot** trigger forbidden effects through platform APIs  
- ML evaluation is versioned and gating for operator-critical routes  

---

## 2. Test layers

### Unit

Every pure function in geo transform, association gates, risk rules, authz helpers, schema validators.

### Integration

Service pairs: adapter→normaliser, normaliser→bus, tracking←detections, approval→audit, handoff→mock external.

### Contract

- OpenAPI consumer/provider checks  
- Event schema compatibility (BACKWARD)  
- ICD fixtures per interface ID  

### ML

- Offline metrics: precision, recall, F1, mAP (as applicable), FPR/FNR, MOTA/IDF1 or equivalent, latency, calibration (ECE)  
- Slice metrics: range, clutter, lighting, swarm density  
- Adversarial/smoke robustness where feasible  
- Regression vs last promoted model  

### Simulation

Scenario pack in digital-twin doc; golden runs in CI nightly; scorer thresholds as release gates for fusion/tracking.

### Chaos

Mapped to FMEA IDs:

- Lost sensor, lost network, corrupted message, delayed message, duplicated message  
- DB unavailable, model failure, bus partition, clock skew  

### Security

- AuthN/AuthZ positive/negative  
- IDOR on track/incident IDs  
- Injection on APIs and assistant tools  
- Rate limit behaviour  
- Privilege escalation attempts  
- Dependency/container scan gates  
- Prompt-injection corpus for AI tools  
- Schema fuzz on ingest  

### Human factors (non-CI)

Scripted operator trials: time-to-evidence, error rates, subjective workload; feed PD.

---

## 3. Safety-specific tests

| Test | Expected |
|---|---|
| Recommendation cannot call integration without decision | Pass deny |
| Integration schema rejects effector-like fields | Pass reject |
| Demo flag cannot target prod integration URL | Pass block |
| Audit write failure blocks decision commit | Pass fail-closed |

---

## 4. Environments

| Env | Purpose |
|---|---|
| Local compose | Dev |
| CI | Unit/contract/sim smoke |
| Lab twin | Nightly full scenarios |
| Staging hardened | Security + perf |
| HIL | Stage 7 |
| Field | Stage 8 authorised |

---

## 5. Exit criteria examples

- Contract tests green on main  
- Sim scenarios 1–12 pass agreed thresholds  
- Chaos FM-05/09/13/20 drills documented  
- Critical CVEs addressed per SG SLA  
- No open Sev-1 security findings  

---

## Author

Victor.I
