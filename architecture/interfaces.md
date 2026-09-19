<!-- Author: Victor.I -->

# Deliverable 7 — Interface Control Document (ICD)

**Author:** Victor.I  
**Status:** Draft for review  
**Rule:** No implementation against undocumented interfaces

---

## 1. Conventions

| Field | Meaning |
|---|---|
| Producer / Consumer | Owning services |
| Protocol | Transport |
| Format | Schema family |
| Auth | Required authentication |
| Latency | Draft budget |
| Retry | Client behaviour |
| Failure | Expected degraded behaviour |
| Versioning | Compatibility policy |
| Observability | Required signals |

Versioning: additive changes in minor; breaking in major. Consumers must ignore unknown fields.

---

## 2. Interface index

| ID | Interface |
|---|---|
| ICD-01 | Sensor/Adapter → Normaliser |
| ICD-02 | Normaliser → Event Bus (`observation.v1`) |
| ICD-03 | Event Bus → Detection / Tracking / Quality |
| ICD-04 | Detection → Event Bus (`detection.v1`) |
| ICD-05 | Tracking/Fusion → Event Bus (`track.update.v1`) |
| ICD-06 | Behaviour → Event Bus (`behaviour.indicator.v1`) |
| ICD-07 | Risk → Event Bus (`risk.assessment.v1`) |
| ICD-08 | Alert → Event Bus / Operator API (`alert.v1`) |
| ICD-09 | Operator UI ↔ Operator API / Realtime |
| ICD-10 | Approval → Audit + Decision store |
| ICD-11 | Integration API → External system |
| ICD-12 | Inference Gateway ↔ Models |
| ICD-13 | AI Assistant ↔ Tool Policy ↔ Operator API |
| ICD-14 | Services → Observability backend |
| ICD-15 | Sim Engine → Sim Adapters |

---

## 3. Interface definitions

### ICD-01 — Sensor adapter internal output

| Attribute | Specification |
|---|---|
| Producer | `sensor-adapter-*` |
| Consumer | `normaliser` |
| Protocol | gRPC or in-process queue (edge); HTTPS push allowed |
| Format | Candidate observation JSON matching schema draft |
| Auth | mTLS service identity |
| Latency | Adapter local p95 ≤ 50 ms transform |
| Retry | At-least-once to normaliser with idempotency key |
| Failure | Buffer locally (bounded); shed oldest with metric; never crash bus |
| Versioning | `adapter_version` + schema_version |
| Observability | transform latency, drop count, skew |

### ICD-02 — Normaliser → Bus

| Attribute | Specification |
|---|---|
| Producer | `normaliser` |
| Consumer | Bus subscribers |
| Protocol | Kafka API (produce) |
| Format | `observation.v1` (Avro/JSON Schema — TBD in tech matrix) |
| Auth | SASL/mTLS to bus |
| Latency | See NFR-LAT-001 |
| Retry | Producer retries with idempotent producer enabled |
| Failure | Quarantine topic on validation fail |
| Versioning | Subject `observation-value` with compatibility BACKWARD |
| Observability | produce errors, quarantine rate |

### ICD-03 — Bus → processors

| Attribute | Specification |
|---|---|
| Producer | Event bus |
| Consumer | detection, tracking, quality, audit samplers |
| Protocol | Kafka API (consume) |
| Format | As published |
| Auth | Per-principal ACLs |
| Latency | Consumer lag SLO alert |
| Retry | Checkpoint after successful side effects; idempotent handlers |
| Failure | Lag grows; UI degraded banner when lag > threshold |
| Versioning | Consumer can read N and N-1 |
| Observability | lag, processing time, error rate |

### ICD-04 — Detection events

| Attribute | Specification |
|---|---|
| Producer | `detection` |
| Consumer | `tracking`, projections |
| Protocol | Kafka produce |
| Format | `detection.v1` including `model_id`, `model_version`, scores |
| Auth | Service identity |
| Latency | Modality-dependent; budget published per model card |
| Retry | Idempotent by `detection_id` |
| Failure | Passthrough sensor detections may continue if model down (policy) |
| Versioning | Major for semantic change of score meaning |
| Observability | inference latency, throughput, NaN/guardrail hits |

### ICD-05 — Track updates

| Attribute | Specification |
|---|---|
| Producer | `tracking`, `fusion` |
| Consumer | behaviour, risk, realtime, audit |
| Protocol | Kafka + hot DB projection |
| Format | `track.update.v1` (state, cov, evidence_obs_ids, quality) |
| Auth | Service identity |
| Latency | NFR-LAT-002 |
| Retry | State machine must handle duplicates |
| Failure | Coast with increasing uncertainty; mark `COASTING` |
| Versioning | Backward compatible fields |
| Observability | active tracks, association rate, coast count |

### ICD-06 / ICD-07 / ICD-08 — Behaviour, risk, alerts

Shared pattern: Kafka events + DB projection; never write decisions.

Alert policy evaluated synchronously on risk/track; output `alert.v1` with `policy_id`, `tier`, `track_ids`.

### ICD-09 — Operator UI

| Attribute | Specification |
|---|---|
| Producer/Consumer | Browser ↔ `operator-api` + `realtime-gateway` |
| Protocol | HTTPS REST + WebSocket/SSE |
| Format | JSON DTOs versioned `/api/v1` |
| Auth | OIDC bearer; short-lived access + refresh |
| Latency | NFR-LAT-004 |
| Retry | UI reconnect with backoff; REST idempotent GETs |
| Failure | Read-only cache banner; block decisions if approval API down |
| Versioning | URL major version |
| Observability | WS connects, API RED metrics |

### ICD-10 — Human decision

| Attribute | Specification |
|---|---|
| Producer | `approval` |
| Consumer | `audit`, outbox→`integration-api` |
| Protocol | Internal API + DB transaction + outbox |
| Format | `human.decision.v1` |
| Auth | User JWT + RBAC permission `decision.write` |
| Latency | Interactive p95 ≤ 300 ms persist |
| Retry | Client safe retry with idempotency key |
| Failure | No silent success; user sees error |
| Versioning | Enum for categories controlled vocabulary |
| Observability | decision rate by category, denials |

### ICD-11 — External handoff

| Attribute | Specification |
|---|---|
| Producer | `integration-api` |
| Consumer | Authorised external system or mock |
| Protocol | HTTPS REST (mTLS preferred) |
| Format | `{ decision_id, category, site_id, track_ids, evidence_digest, timestamp }` |
| Auth | mTLS + scoped token; IP allowlist |
| Latency | Best-effort; async with retry budget |
| Retry | Exponential backoff; DLQ after N |
| Failure | Local decision remains valid; handoff status=`failed` |
| Versioning | `/external/v1/handoff` |
| Observability | success/fail, latency, DLQ depth |

**Forbidden fields:** weapon aimpoints, RF jam parameters, fuse arming, etc.

### ICD-12 — Inference gateway

| Attribute | Specification |
|---|---|
| Producer | detection/classification services |
| Consumer | model runtimes |
| Protocol | gRPC preferred (REST allowed) |
| Format | Tensor/feature payloads + metadata |
| Auth | mTLS |
| Latency | Per model card |
| Retry | Fail open/closed per policy flag on route |
| Failure | Return explicit error; caller applies policy |
| Versioning | Model version pin + canary header |
| Observability | queue depth, p95, batch size |

### ICD-13 — AI assistant tools

| Attribute | Specification |
|---|---|
| Producer | `ai-assistant` |
| Consumer | Allowlisted Operator API tools |
| Protocol | HTTPS internal |
| Format | Tool JSON schemas |
| Auth | User token + service policy engine |
| Latency | Soft real-time; UX timeout |
| Retry | Limited; show partial |
| Failure | Graceful message; core console unaffected |
| Versioning | Tool manifest version |
| Observability | tool call audit, injection blocks |

### ICD-14 — Observability

OTLP metrics/logs/traces to collector; each service: `/healthz`, `/readyz`.

### ICD-15 — Simulator

Sim engine emits vendor-shaped or canonical-candidate payloads into sim adapters; fault injectors implement delay/drop/dup/corrupt.

---

## 4. Controlled vocabularies (initial)

### Response categories (examples — final list TBD with customer)

- `DISMISS`  
- `HEIGHTEN_MONITORING`  
- `CUE_SENSOR`  
- `NOTIFY_EXTERNAL`  
- `REQUEST_ESCALATION`  
- `OPEN_INCIDENT`  

No category implies kinetic or EA execution.

### Alert tiers

- `T0` informational  
- `T1` advisory  
- `T2` operator action suggested  
- `T3` commander attention  

---

## 5. Compatibility test requirements

Every ICD entry requires a contract test fixture before the producing service merges a schema change.

---

## Author

Victor.I
