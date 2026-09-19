<!-- Author: Victor.I -->

# Deliverable 4 — System Architecture

**Author:** Victor.I  
**Status:** Draft for review — Agent 8 reconciled view  
**Principle:** Minimum reliable system; interfaces before components; human oversight mandatory

---

## 1. Mission definition (Phase 1)

### Operational problem

Defenders must form a timely, evidence-backed air picture from heterogeneous sensors and support human decisions about authorised response *categories* under uncertainty — including possible coordinated/swarm behaviour — without autonomous harmful effects.

### System objectives

1. Reliable multi-sensor ingest and normalisation  
2. Coherent tracks with provenance  
3. Behaviour and risk decision support with uncertainty  
4. Operator-usable console under load  
5. Governed AI/ML with audit  
6. Controlled external integration  
7. Testability via digital twin before hardware  

### Users

Security operators, sensor operators, incident commanders, analysts, admins, governance officers, integrators.

### Operating environments (assumed)

Secured facility or field network; mixed edge sensor posts; central operations node; simulation lab. Exact RF/weather/threat libraries are site-specific (open questions).

### Draft quality attributes

| Attribute | Draft objective |
|---|---|
| Latency | See NFR-LAT-* |
| Availability | 99.5% single-site MVP |
| Safety | No autonomous destructive actuation |
| Security | Zero-trust oriented service identity + RBAC |
| Explainability | Evidence-linked assessments |

### MoSCoW / out of scope

See `docs/systems/requirements.md`. Hard out-of-scope: weapon control, EA execution, guidance algorithms.

---

## 2. Architectural drivers

1. Heterogeneous, late, missing, contradictory data is normal  
2. Operator cognitive load is a first-class constraint  
3. Safety boundary must be enforceable in software and process  
4. Vendor independence via adapters  
5. Simulation-first delivery  
6. Prefer boring proven infrastructure unless justified  

---

## 3. System decomposition

```
COUNTER-SWARM PLATFORM
│
├── Sensor Integration
│   ├── Radar Adapter
│   ├── EO/IR Adapter
│   ├── RF Adapter
│   ├── Acoustic Adapter
│   ├── Telemetry Adapter
│   └── Simulation Adapter
│
├── Data Platform
│   ├── Validation / Normalisation
│   ├── Schema Registry
│   ├── Event Bus
│   ├── Hot Store (ops)
│   ├── Historical / Object Store
│   ├── Analytics Store
│   └── Data Quality Service
│
├── Intelligence
│   ├── Detection Service
│   ├── Classification Service
│   ├── Tracking Service
│   ├── Sensor Fusion Service
│   ├── Behaviour Analysis Service
│   └── Risk Assessment Service
│
├── Decision Support
│   ├── Alert Service
│   ├── Recommendation Policy Engine
│   ├── Evidence Assembly
│   └── Human Approval Service
│
├── AI Assistance (optional path)
│   ├── Policy / Tool Gateway
│   ├── Summarisation / NL Query
│   └── Retrieval (runbooks, docs)
│
├── Operator Platform
│   ├── Web Console (map, tracks, alerts, timeline, health)
│   ├── Realtime Gateway
│   └── Incident / Replay Views
│
├── Security & Governance
│   ├── Identity Provider integration
│   ├── RBAC / policy
│   ├── Audit Log (tamper-evident)
│   ├── Secrets
│   └── Model Registry governance metadata
│
├── Observability
│   ├── Metrics / Logs / Traces
│   └── Health aggregation
│
└── Integration
    ├── Authorised External Systems API (category handoff)
    ├── Mock Effector / External Simulator
    └── Hardware-in-the-loop adapters (later stages)
```

---

## 4. Logical architecture

```
                         ┌─────────────────┐
                         │  API Gateway    │
                         │  (AuthZ edge)   │
                         └────────┬────────┘
              ┌───────────────────┼───────────────────┐
              │                   │                   │
        Identity/OIDC      Operator API         Integration API
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                         ┌────────┴────────┐
                         │  Event Stream   │
                         └────────┬────────┘
                                  │
     Sensor Adapters → Normaliser ┘
                                  │
        ┌──────────────┬──────────┼──────────┬──────────────┐
        ▼              ▼          ▼          ▼              ▼
   Detection      Tracking     Quality    Fusion      ML Inference
        │              │          │          │              │
        └──────────────┴──────────┼──────────┴──────────────┘
                                  ▼
                         Behaviour → Risk → Alerts
                                  ▼
                         Decision Support + Audit
                                  ▼
                           Operator Console
                                  ▼
                    Authorised External Category API
```

---

## 5. Service catalogue (software view)

| Service | Responsibility | Inputs | Outputs | Scale notes |
|---|---|---|---|---|
| **sensor-adapter-*** | Vendor/sim → canonical obs | Raw SDK/sim | `observation.v1` events | Per sensor class; edge-friendly |
| **normaliser** | Validate, CRS/time, enrich | Raw canonical candidates | Validated events + quarantine | Stateless HPA |
| **event-bus** | Durable pub/sub | Events | Events | Partition by site/sensor |
| **detection** | Modality detectors / passthrough | Observations | Detection events | GPU optional |
| **tracking** | MOT / track state | Detections/obs | Track updates | Stateful; careful failover |
| **fusion** | Cross-sensor association | Tracks/obs | Fused tracks + evidence links | Stateful |
| **behaviour** | Coordination/anomaly indicators | Tracks | Behaviour features/events | Stateless/batch+stream |
| **risk** | Assessment + missing-info | Tracks, behaviour, context | Risk assessments | Rule+model hybrid |
| **alert** | Policy-based prioritisation | Risk/track events | Alerts | Stateless |
| **approval** | Human decisions | Operator actions | Decision records | Strong audit |
| **audit** | Tamper-evident append | All material events | Audit queries | Write-optimised |
| **operator-api** | REST/WS for console | Commands/queries | DTOs + streams | Stateless |
| **realtime-gateway** | Fanout to UI | Track/alert events | WS/SSE | Sticky sessions optional |
| **ai-assistant** | Tool-bounded LLM help | Operator prompts | Grounded answers | Isolated; no safety bypass |
| **inference-gateway** | Model serving facade | Features/frames | Predictions + version | Canary/rollback |
| **integration-api** | External category handoff | Approved decisions | Ack/status | Strict allowlist |
| **sim-engine** | Digital twin scenarios | Scenario configs | Synthetic obs + faults | Lab only / gated |
| **identity** | AuthN (IdP), token mint | Creds | Tokens | External IdP preferred |
| **obs-collector** | Telemetry pipeline | Metrics/logs/traces | Dashboards/alerts | Sidecar/agent |

---

## 6. Data architecture (summary)

- **Hot:** PostgreSQL + PostGIS for tracks, incidents, config; Redis for ephemeral sessions/rate limits  
- **Stream:** Kafka-compatible bus (see tradeoffs) for observations, detections, tracks, assessments  
- **Cold:** Object storage for raw frames/clips, large payloads, model artifacts  
- **Analytics:** Warehouse/OLAP optional Stage 4+; start with Postgres + export  

Canonical observation is the stability hinge — see `schemas/` (Stage 0 conceptual) and DE docs.

---

## 7. Edge vs central (Phase 5)

**Recommended: hybrid, central-primary for MVP.**

| Function | Edge | Central |
|---|---|---|
| Adapter + light preprocess | Yes | Optional |
| Hard real-time detector (EO) | Prefer edge when bandwidth-bound | Optional |
| Multi-sensor fusion across posts | Limited local | Yes |
| Behaviour/risk across site | No | Yes |
| Operator console | Thin/cache | Yes |
| Audit system of record | Buffer+forward | Yes |
| Model training | No | Yes |

Rationale: MVP reliability and operability beat early edge fleet complexity. Design adapters and schemas so edge promotion is non-breaking.

---

## 8. Safety architecture

```
Recommendation Policy Engine
        │
        ▼
 Human Approval Service  ←── RBAC + optional dual-control
        │
        ▼
 Integration API (category only)
        │
        ▼
 External authorised system / mock
```

Software interlocks:

- No service credentials that can invoke weapon interfaces in this repo’s integration layer  
- Recommendation ≠ command; separate event types  
- “Demo mode” cannot enable real integration endpoints without SG-approved config  

---

## 9. Competing architectures challenged (Agent 8)

### A. Monolith “C2 app”

- **Pros:** Simple deploy  
- **Cons:** Sensor rate coupling, hard to isolate ML, weak independent scale  
- **Verdict:** Reject for production path; optional modular monolith only for earliest spike if needed, not target  

### B. Fine-grained microservices everywhere

- **Pros:** Scale purity  
- **Cons:** Operational burden early  
- **Verdict:** Reject extreme split; prefer **modular services** along domain boundaries listed above  

### C. Event-driven core + query services (selected)

- **Pros:** Fits async sensors; replay; decoupling  
- **Cons:** Eventual consistency complexity  
- **Verdict:** **Selected** with explicit consistency notes in ICD  

---

## 10. What should NOT be built (yet / ever in-platform)

| Item | Why |
|---|---|
| Effector fire-control | Safety / scope |
| LLM deciding risk alone | Reliability / governance |
| Per-vendor core schemas | Lock-in |
| Multi-region active-active MVP | Complexity vs value |
| Custom DB engine | Unjustified |
| Crypto mining of novel chain for audit | Prefer hash-chained append log or immutable storage |

---

## 11. Architecture decision record index (initial)

| ADR | Decision | Status |
|---|---|---|
| ADR-001 | Event-driven modular services | Proposed |
| ADR-002 | Postgres+PostGIS hot store | Proposed |
| ADR-003 | Kafka-API bus (Redpanda candidate) | Proposed |
| ADR-004 | Web operator console first | Proposed |
| ADR-005 | Central-primary hybrid edge | Proposed |
| ADR-006 | Category-only external API | Accepted (safety) |
| ADR-007 | Simulation-first delivery | Accepted |

---

## 12. Pre-ship gate (architecture)

| Question | Answer |
|---|---|
| Failure modes understood? | Drafted in FMEA — needs review |
| Observable? | Yes, NFR-OBS |
| Safe rollback? | Config/model/event replay — yes in design |
| Complexity proportional? | Challenged; MVP trimmed |
| Want 3-year ownership? | Yes if interfaces stay stable |

---

## Author

Victor.I
