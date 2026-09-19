<!-- Author: Victor.I -->

# Deliverable 2 — System Requirements Document

**Author:** Victor.I  
**Status:** Draft for review (Stage 0)  
**Related:** Product definition, architecture, threat model, open questions

---

## 1. Purpose and scope

This document states functional and non-functional requirements for the Counter-Swarm Defence Platform — a defensive decision-support system for multi-sensor counter-UAS / swarm awareness.

### In scope

Sensor ingestion adapters, normalisation, event streaming, detection/classification/tracking (software + ML), fusion, behaviour analysis, risk assessment, operator console, AI decision-support (bounded), audit, observability, simulation/digital twin, controlled external integration APIs, security and governance.

### Explicitly out of scope

Autonomous weapon control; kinetic/electronic attack execution; weapon guidance; bypassing safety mechanisms; selecting human targets; undocumented proprietary effector protocols as first-class platform dependencies.

---

## 2. Stakeholders and users

| ID | Stakeholder | Interest |
|---|---|---|
| S1 | Security operator | Air picture, alerts, decisions |
| S2 | Sensor operator | Sensor health, cueing |
| S3 | Incident commander | Priority, authorisation |
| S4 | Analyst | Replay, evaluation |
| S5 | System administrator | Deploy, identity, config |
| S6 | Security/governance | Audit, model governance |
| S7 | Integrator / engineer | Adapters, ICD compliance |

---

## 3. Assumptions (requirements baseline)

See also Deliverable 17. Material assumptions:

- A-01: Development starts with simulation; live sensors later under authorisation.  
- A-02: Operators are trained; console is English-first initially.  
- A-03: Site operates on a secured network; internet egress is controlled.  
- A-04: Clocks can be synchronised to a common time source within defined error bounds; residual skew is handled.  
- A-05: External response systems accept abstract “authorised category” messages, not platform-native effector commands.  
- A-06: Single security domain / single site for MVP; multi-site is future.

---

## 4. MoSCoW summary

### Must have

- Canonical observation schema + adapters  
- Event bus with validation  
- Tracking + multi-sensor association (baseline algorithms acceptable)  
- Risk/priority with uncertainty  
- Operator console: map, tracks, alerts, evidence, timeline, health  
- Human decision capture  
- Immutable audit for material events  
- AuthN/AuthZ (RBAC)  
- Simulation environment  
- Observability (health, latency, lag, errors)  
- Safety: no autonomous destructive effects  

### Should have

- Behaviour / coordination indicators  
- Model registry + versioned inference  
- AI assistant for summarisation / NL query (tool-bounded)  
- Replay and after-action packages  
- Schema registry and contract tests  
- Edge/central split design (edge optional in early stages)  

### Could have

- Multi-site tenancy  
- Advanced Bayesian intent models  
- Native hardened clients  
- Automated dual-control workflows  
- Rich digital-twin 3D visualisation  

### Won’t have (this programme)

- Weapon control loops  
- Autonomous jamming / kinetic tasking  
- Open public multi-tenant SaaS without additional hardening programme  

---

## 5. Functional requirements

IDs use FR-area-nnn. Priority: M/S/C.

### 5.1 Sensor ingestion

| ID | Requirement | Pri |
|---|---|---|
| FR-SEN-001 | Platform shall ingest observations via pluggable sensor adapters. | M |
| FR-SEN-002 | Each adapter shall map vendor/SDK data to the canonical observation schema. | M |
| FR-SEN-003 | Platform shall support simulated sensors indistinguishable at the schema boundary. | M |
| FR-SEN-004 | Platform shall record sensor identity, type, and health telemetry. | M |
| FR-SEN-005 | Platform shall tolerate intermittent sensor silence without crashing consumers. | M |
| FR-SEN-006 | Adapters shall not embed vendor-specific types beyond the adapter boundary. | M |

### 5.2 Normalisation and quality

| ID | Requirement | Pri |
|---|---|---|
| FR-NRM-001 | Observations shall be normalised to a common coordinate and time representation (documented CRS + UTC). | M |
| FR-NRM-002 | Invalid observations shall be rejected or quarantined with reason codes. | M |
| FR-NRM-003 | Duplicate detection shall be supported via idempotency keys where provided. | M |
| FR-NRM-004 | Quality metadata (SNR, FOV, calibration age, etc.) shall be preserved when available. | S |
| FR-NRM-005 | Schema evolution shall be versioned and backward compatible within a major version. | M |

### 5.3 Event streaming

| ID | Requirement | Pri |
|---|---|---|
| FR-EVT-001 | Normalised observations shall be published to a durable event stream. | M |
| FR-EVT-002 | Consumers shall process events idempotently. | M |
| FR-EVT-003 | Platform shall expose consumer lag metrics. | M |
| FR-EVT-004 | Platform shall support replay from a retention window for recovery and tests. | M |

### 5.4 Detection, classification, tracking

| ID | Requirement | Pri |
|---|---|---|
| FR-DET-001 | Platform shall produce detections from applicable observation modalities (incl. passthrough of sensor-native detections). | M |
| FR-CLS-001 | Platform shall attach class hypotheses with scores, not single silent labels. | M |
| FR-TRK-001 | Platform shall maintain tracks with unique IDs and state estimates. | M |
| FR-TRK-002 | Platform shall associate observations to tracks using documented algorithms. | M |
| FR-TRK-003 | Track drop, coast, and reacquire behaviours shall be defined and observable. | M |
| FR-TRK-004 | Multi-object tracking under clutter shall be evaluated against simulation scenarios. | S |

### 5.5 Fusion

| ID | Requirement | Pri |
|---|---|---|
| FR-FUS-001 | Platform shall correlate observations across sensors into shared tracks where association criteria are met. | M |
| FR-FUS-002 | Contradictory observations shall be retained as evidence with conflict flags, not silently discarded. | M |
| FR-FUS-003 | Fusion outputs shall cite contributing observation IDs. | M |

### 5.6 Behaviour and anomaly

| ID | Requirement | Pri |
|---|---|---|
| FR-BEH-001 | Platform shall compute behaviour indicators (e.g., proximity clustering, similar trajectories, timing coordination) with uncertainty. | S |
| FR-BEH-002 | Anomaly scores shall be explainable via contributing features. | S |
| FR-BEH-003 | Behaviour modules shall not alone authorise response categories. | M |

### 5.7 Risk assessment

| ID | Requirement | Pri |
|---|---|---|
| FR-RSK-001 | Platform shall produce risk assessments from evidence, behaviour, context, and confidence. | M |
| FR-RSK-002 | Risk shall be presented as graded levels or scores with rationale, not unverified binary “threat/no threat.” | M |
| FR-RSK-003 | Missing information shall be explicitly listed when material. | M |
| FR-RSK-004 | Risk engine rules/models shall be versioned. | M |

### 5.8 Alerts and decision support

| ID | Requirement | Pri |
|---|---|---|
| FR-ALT-001 | Platform shall generate prioritised alerts per policy. | M |
| FR-ALT-002 | Alerts shall link to tracks, evidence, and assessments. | M |
| FR-ALT-003 | Platform may recommend predefined response categories only. | M |
| FR-ALT-004 | Recommendations shall never execute physical effects. | M |
| FR-ALT-005 | Operators shall acknowledge, escalate, dismiss, or decide with mandatory audit fields. | M |

### 5.9 Operator visualisation

| ID | Requirement | Pri |
|---|---|---|
| FR-UI-001 | Console shall provide map, tracks, alerts, timeline, sensor health, system status. | M |
| FR-UI-002 | UI shall visually distinguish observation, inference, prediction, recommendation, decision. | M |
| FR-UI-003 | Console shall support near-real-time updates (see NFR latency). | M |
| FR-UI-004 | Console shall support incident replay for authorised roles. | S |
| FR-UI-005 | AI assistant (if enabled) shall operate through an allowlisted tool policy. | S |

### 5.10 Audit

| ID | Requirement | Pri |
|---|---|---|
| FR-AUD-001 | Material events (observations consumed into decisions, model outputs used, assessments, recommendations, human decisions) shall be audit-logged. | M |
| FR-AUD-002 | Audit records shall be tamper-evident (append-only store or hash chaining). | M |
| FR-AUD-003 | Audit shall answer what/when/who/which model version/evidence/confidence/decision. | M |

### 5.11 External integration

| ID | Requirement | Pri |
|---|---|---|
| FR-EXT-001 | External systems shall integrate only via versioned controlled APIs. | M |
| FR-EXT-002 | Handoff payloads shall express authorised categories and context, not effector primitives. | M |
| FR-EXT-003 | Integrations shall require explicit enablement and credentials per environment. | M |
| FR-EXT-004 | Mock external systems shall be available in simulation. | M |

### 5.12 Simulation / digital twin

| ID | Requirement | Pri |
|---|---|---|
| FR-SIM-001 | Simulator shall generate multi-object scenarios with noise, delay, dropout, false and contradictory observations. | M |
| FR-SIM-002 | Simulator shall exercise sensor and network failure modes. | M |
| FR-SIM-003 | Platform under test shall consume simulated observations through the same adapter contracts as real adapters. | M |

### 5.13 Identity and access

| ID | Requirement | Pri |
|---|---|---|
| FR-IAM-001 | All operator and service actions shall be authenticated. | M |
| FR-IAM-002 | Authorisation shall enforce RBAC at minimum; ABAC hooks for site/policy later. | M |
| FR-IAM-003 | Least privilege for service identities. | M |

### 5.14 ML / AI governance hooks

| ID | Requirement | Pri |
|---|---|---|
| FR-MLG-001 | Deployed models shall have version, owner, intended use, limitations. | M |
| FR-MLG-002 | Inference used in operator decisions shall record model version in audit. | M |
| FR-AIG-001 | LLM/AI tools shall not bypass policy, IAM, or safety constraints. | M |

---

## 6. Non-functional requirements

Targets below are **design targets for the first operational candidate**; final SLOs require site CONOPS (open question).

### 6.1 Latency

| ID | Requirement | Target (draft) |
|---|---|---|
| NFR-LAT-001 | Observation accept → normalised event available | p95 ≤ 200 ms (in-cluster sim path) |
| NFR-LAT-002 | Event → track update visible to console | p95 ≤ 1 s |
| NFR-LAT-003 | Alert policy evaluation after track/risk update | p95 ≤ 500 ms |
| NFR-LAT-004 | Operator console event-to-paint | p95 ≤ 1.5 s end-to-end after track update |

### 6.2 Availability and reliability

| ID | Requirement | Target (draft) |
|---|---|---|
| NFR-AVL-001 | Control-plane + core pipeline availability | 99.5% monthly (single site MVP) |
| NFR-REL-001 | No silent data loss on acknowledged events within retention | Required |
| NFR-REL-002 | Graceful degradation when a sensor or model is down | Required |

### 6.3 Scalability

| ID | Requirement | Target (draft) |
|---|---|---|
| NFR-SCL-001 | Sustain observation ingress | ≥ 2k obs/s sustained in lab; headroom plan to 10k |
| NFR-SCL-002 | Active tracks | ≥ 500 concurrent in MVP lab profile |
| NFR-SCL-003 | Horizontal scale for stateless services | Required |

### 6.4 Security

| ID | Requirement |
|---|---|
| NFR-SEC-001 | TLS in transit for all external and service meshes as deployed |
| NFR-SEC-002 | Encryption at rest for databases and object storage |
| NFR-SEC-003 | Secrets never in source control |
| NFR-SEC-004 | Dependency and container scanning in CI |
| NFR-SEC-005 | Rate limiting on exposed APIs |
| NFR-SEC-006 | Security requirements per threat model TM controls |

### 6.5 Maintainability and testability

| ID | Requirement |
|---|---|
| NFR-MNT-001 | Service boundaries match ICD; no undocumented cross-DB writes |
| NFR-TST-001 | Contract tests for schemas and APIs in CI |
| NFR-TST-002 | Simulation suite gates releases |
| NFR-TST-003 | Chaos scenarios for sensor/network/DB/model loss |

### 6.6 Observability

| ID | Requirement |
|---|---|
| NFR-OBS-001 | Health and readiness per service |
| NFR-OBS-002 | RED/USE metrics + event lag + model latency |
| NFR-OBS-003 | Distributed tracing across ingest→fusion→UI path |
| NFR-OBS-004 | Dashboards: system, model, sensor, data quality, security, operator activity |

### 6.7 Recoverability

| ID | Requirement |
|---|---|
| NFR-REC-001 | Documented RPO/RTO for hot store (draft RPO ≤ 1 min, RTO ≤ 30 min MVP) |
| NFR-REC-002 | Event replay procedures |
| NFR-REC-003 | Model and config rollback procedures |

### 6.8 Explainability

| ID | Requirement |
|---|---|
| NFR-XAI-001 | Operator-facing assessments include evidence references |
| NFR-XAI-002 | Model outputs used in UI include version and score calibration notes where applicable |

---

## 7. Regulatory / compliance considerations (preliminary)

Not legal advice. Programme must confirm jurisdiction and customer constraints.

- Export control / dual-use classification of software and models  
- Privacy if cameras observe public spaces (data minimisation, retention)  
- Sector standards for logging and access control (customer-specific)  
- Rules of engagement and authorities for any external response integration (customer-owned)  

---

## 8. Requirements traceability

Each FR/NFR shall map to:

- Architecture components (`architecture/system.md`)  
- Interfaces (`architecture/interfaces.md`)  
- Tests (`docs/systems/testing-strategy.md`)  
- Threat model controls (`docs/security/threat-model.md`)  

Traceability matrix to be maintained once implementation begins; at Stage 0, IDs above are the controlled vocabulary.

---

## 9. Acceptance (document-level)

This requirements draft is accepted when product, systems, security, and engineering leads agree MoSCoW split, out-of-scope boundaries, and draft NFRs — or formally amend them in Deliverable 17.

---

## Author

Victor.I
