<!-- Author: Victor.I -->

# Observability Architecture

**Author:** Victor.I  
**Status:** Stage 0 complete (design)  
**Related:** NFR-OBS-*, `architecture/deployment.md`, `docs/systems/testing-strategy.md`

---

## 1. Purpose

Every major service must expose health, readiness, latency, throughput, error rate, resource usage, event lag, model latency, model confidence aggregates, and sensor health — without requiring operators to SSH into boxes.

---

## 2. Telemetry model

| Signal | Transport | Examples |
|---|---|---|
| Metrics | OTLP / Prometheus | request rate, p95 latency, consumer lag, infer ms |
| Logs | Structured JSON | correlation_id, service, level, msg |
| Traces | OTLP | ingest → normalise → track → risk → UI |
| Health | HTTP | `/healthz`, `/readyz` |

---

## 3. Dashboards (required)

| Dashboard | Audience | Primary widgets |
|---|---|---|
| SYSTEM HEALTH | Admin / SE | service up, API RED, bus lag, DB |
| MODEL HEALTH | ML / SG | infer latency, error %, version, drift flags |
| SENSOR HEALTH | Sensor ops | last obs age, drop rate, adapter restarts |
| DATA QUALITY | DE / DS | quarantine rate, schema fails, skew |
| SECURITY | SG | auth fails, 403s, integration denials |
| OPERATOR ACTIVITY | PD / command | alert ack time, decisions/hour, handoff fail |

---

## 4. Alerting (platform ops — not C2 threat alerts)

- Bus lag above threshold  
- Readyz failing  
- Audit write failures (page immediately — fail-closed risk)  
- Inference route error budget burn  
- Sensor silent beyond policy  

---

## 5. Implementation deferral

Stage 1: Prometheus + Grafana (or equivalent) in Compose.  
Stage 6: harden retention, RBAC on dashboards, paging.

No application code in Stage 0.

---

## Author

Victor.I
