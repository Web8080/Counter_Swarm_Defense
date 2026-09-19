<!-- Author: Victor.I -->

# Deliverable 12 — Development Roadmap

**Author:** Victor.I  
**Status:** Draft for review  
**Gate:** No Stage 1 coding until Stage 0 documents approved

---

## 1. Visual roadmap

```
RESEARCH
   │
   ▼
REQUIREMENTS
   │
   ▼
SYSTEM ARCHITECTURE          ← you are here (Stage 0)
   │
   ├──────────────┬───────────────┐
   ▼              ▼               ▼
PRODUCT        SOFTWARE          DATA
   │              │               │
   └──────────────┼───────────────┘
                  ▼
             AI / ML
                  │
                  ▼
             SIMULATION
                  │
                  ▼
          SENSOR INTEGRATION
                  │
                  ▼
          SENSOR FUSION
                  │
                  ▼
         OPERATOR PLATFORM
                  │
                  ▼
          SECURITY HARDENING
                  │
                  ▼
       HARDWARE-IN-LOOP TESTING
                  │
                  ▼
         CONTROLLED VALIDATION
                  │
                  ▼
             PRODUCTION
```

---

## 2. Stages

### Stage 0 — Research (current)

**Deliver:** problem definition, user research synthesis, threat model, requirements, assumptions, tech research, architecture pack (Deliverables 1–17).  
**Exit:** Document approval by stakeholders.  
**Code:** None (scaffolding folders only).

### Stage 1 — Digital prototype

Sim → bus → fusion/tracking (baseline) → risk (rules) → dashboard skeleton.  
**Goal:** Prove architecture wiring.

### Stage 2 — Sensor integration patterns

Representative non-operational sources + richer sim sensors; validate schemas, timestamps, reliability.

### Stage 3 — ML pipeline

Detection/classification/tracking models as justified; registry; evaluation; rollback drills.

### Stage 4 — Multi-sensor fusion

Heterogeneous, contradictory, incomplete observation tests at scale in twin.

### Stage 5 — Operator platform

Map, tracks, confidence, evidence, alerts, timeline, health, audit UX polish; HF evaluation.

### Stage 6 — Security hardening

RBAC, service identity, encryption, secrets, scanning, monitoring, audit integrity verification.

### Stage 7 — Hardware-in-the-loop

Representative hardware/test systems; still no real harmful effects; measure latency/reliability/recovery.

### Stage 8 — Controlled field testing

Only with authorisation; response systems abstracted/simulated unless separately engineered by qualified specialists.

### Production

Reproducible deploy, runbooks, SLOs, on-call, limitation docs signed.

---

## 3. Parallelism after approval

| Track | Start after |
|---|---|
| Sim engine + schemas | Stage 0 exit |
| Platform services skeleton | Stage 0 exit |
| Console IA implementation | Stage 0 exit (with PD) |
| Baseline tracker (classical) | Early Stage 1 |
| ML detectors | Stage 3 (data ready) |
| AI assistant | After Stage 5 core UX stable |
| K8s hardening | Stage 6 |

---

## 4. Definition of done (programme)

Not “it runs.” Complete only when requirements, architecture, ICD, threat model, data model, simulation, tests, ML eval, failure tests, security controls, audit, monitoring, validated operator workflows, documented hardware boundaries, reproducible deploy, rollback, explainability, and limitations are all satisfied (see master prompt §23).

---

## Author

Victor.I
