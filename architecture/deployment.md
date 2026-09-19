<!-- Author: Victor.I -->

# Deliverable 14 — Deployment Architecture

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Environments

```
[Dev laptop / Compose]
        │
        ▼
[CI images]
        │
        ▼
[Lab / Digital Twin cluster]
        │
        ▼
[Staging (hardened)]
        │
        ▼
[Operational site: Central + optional Edge]
```

Promotion requires signed artifacts and changelog; production needs SG+SYS approval.

---

## 2. Logical deployment (central-primary)

```
                    CENTRAL SITE
 ┌─────────────────────────────────────────────┐
 │ Ingress / API Gateway / WAF                 │
 │ Identity (OIDC)                             │
 │ Operator API + Realtime GW + Console static │
 │ Stream cluster (Redpanda/Kafka)             │
 │ Processors: detect/track/fuse/behaviour/risk│
 │ Alert / Approval / Audit / Integration      │
 │ Postgres+PostGIS, Redis, Object store       │
 │ Obs stack (metrics/logs/traces)             │
 │ Inference GW (+ GPU node pool optional)     │
 └─────────────────────────────────────────────┘
                      │ secure network
     ┌────────────────┼────────────────┐
     ▼                ▼                ▼
  EDGE-1           EDGE-2           EDGE-3
  adapters         adapters         adapters
  optional infer   buffer           health
  sensors          sensors          sensors
```

---

## 3. Stage 1 lab topology (Compose)

Single host or small VM:

- bus, postgres, redis, minio  
- normaliser, tracking, risk, alert, approval, operator-api, realtime, console, sim  

Sufficient to prove data path; not HA.

---

## 4. Hardened topology (K8s)

- Namespaces: `ingest`, `process`, `serve`, `data`, `obs`, `security`  
- NetworkPolicies default deny  
- mTLS (mesh or sidecar)  
- Pod security restricted  
- HPA on stateless services  
- PDBs on bus/DB gateways  
- Separate node pool for GPU inference  

---

## 5. Edge node profile

| Capability | MVP | Field |
|---|---|---|
| Adapter processes | Yes (lab sim) | Yes |
| Local buffer disk | Optional | Yes |
| Local UI | No | Optional degraded |
| Local inference | No | As bandwidth requires |
| Secrets | Injected | TPM/secure element preferred |

---

## 6. Configuration management

- 12-factor env + versioned config maps  
- Policy packs (alert/risk) versioned and audited  
- Feature flags for model routes and AI assistant  
- No secret values in git  

---

## 7. Rollback

| Layer | Mechanism |
|---|---|
| App deploy | Previous image tag |
| Schema | Expand/contract; no destructive migrate unattended |
| Model | Registry pin rollback |
| Config/policy | Prior version + audit |
| Data | PITR for Postgres; bus replay |

---

## 8. Observability deployment

Collector per node → central backend; dashboards:

- System health  
- Model health  
- Sensor health  
- Data quality  
- Security  
- Operator activity  

---

## 9. Integration network

External handoff endpoints in isolated net zone; egress allowlist; mTLS required in staging+ ops.

---

## Author

Victor.I
