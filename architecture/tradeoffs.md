<!-- Author: Victor.I -->

# Deliverable 10 — Technology Selection Matrix and Trade-offs

**Author:** Victor.I  
**Status:** Draft for review  
**Rule:** Justify every choice against requirements; novelty is not a reason

---

## 1. Decision framework

Score qualitatively: Fit to NFRs, operability, team leverage, ecosystem, risk, cost.

Selected stack aims for a **minimum reliable system** that skilled teams can own for years.

---

## 2. Major decisions

### D1 — Event streaming

| Option | Pros | Cons | Fit |
|---|---|---|---|
| **Apache Kafka** | Ubiquitous, mature ACLs, huge ecosystem | Ops weight | Strong |
| **Redpanda** | Kafka API, simpler ops, lower latency potential | Younger ops lore at some orgs | Strong |
| **NATS/JetStream** | Simple, fast | Weaker wide ecosystem for exactly-once patterns / tooling familiarity | Medium |
| **Cloud pub/sub only** | Managed | Lock-in; edge replay story harder | Medium |

**Recommendation:** Kafka-compatible bus; **prefer Redpanda for lab/MVP ops simplicity**, keep Kafka API so migration is possible. Re-evaluate if customer mandates Kafka.

**Trade-off:** Ecosystem familiarity vs. operational simplicity.

---

### D2 — API style

| Option | Pros | Cons |
|---|---|---|
| REST only | Universal, cacheable | Chatty for internal ML |
| gRPC only | Efficient | Browser friction |
| **Both** | REST external/UI; gRPC internal infer/adapters | Two stacks |

**Recommendation:** **REST (+ OpenAPI) for Operator/Integration**; **gRPC for inference and high-rate adapter→normaliser** where needed; WebSocket/SSE for realtime UI.

**Trade-off:** Some dual-stack cost for clear boundary performance.

---

### D3 — Hot storage

| Option | Pros | Cons |
|---|---|---|
| **PostgreSQL + PostGIS** | One system for relational + geo; proven | Extreme TS ingest may need care |
| Specialised TSDB (Timescale/Influx) | TS optimised | Extra system early |
| Pure document DB | Flexible | Weak relational integrity for audit/IAM |

**Recommendation:** **Postgres + PostGIS** MVP; Timescale extension optional if track/obs history pressure demands.

**Trade-off:** Simplicity vs specialised scale — choose simplicity first.

---

### D4 — Cache / ephemeral

**Redis** for sessions, rate limits, short-lived locks. Not system of record.

---

### D5 — Object storage

**S3-compatible** (MinIO in lab, cloud S3 in deployed). Raw media + models.

---

### D6 — Backend language

| Option | Pros | Cons |
|---|---|---|
| **Python (FastAPI)** | ML adjacency, speed of service dev | Perf ceilings — mitigate with scale-out / critical paths in richer runtimes later |
| Go | Excellent for adapters/ingress | ML friction |
| Java/Kotlin | Enterprise | Heavier for MVP team |

**Recommendation:** **Python/FastAPI for control and many services**; consider **Go for ultra-high-rate adapters** if profiling demands. Do not rewrite preemptively.

---

### D7 — Frontend

| Option | Pros | Cons |
|---|---|---|
| **React + TypeScript** | Ecosystem, maps libs | — |
| Next.js | SSR/ops benefits | Extra complexity if purely private authenticated SPA |
| Native | Offline rugged | Slow iteration |

**Recommendation:** **React + TypeScript SPA** behind gateway; Next.js optional if SSR/auth-BFF desired later. Map: MapLibre or similar (open).

**Trade-off:** Web deployability vs native ruggedisation (defer native).

---

### D8 — ML inference

| Option | Pros | Cons |
|---|---|---|
| Central only | Simple | Bandwidth/latency |
| Edge only | Low latency | Fleet ops |
| **Hybrid** | Flexible | Complexity |

**Recommendation:** **Central inference for MVP**; design model packaging for edge later. Classical trackers (Kalman / hypothesising filters) before deep models where sufficient.

---

### D9 — Orchestration

| Option | Pros | Cons |
|---|---|---|
| Docker Compose | Fast lab | Not prod HA |
| **Kubernetes** | Prod standard | Complexity |
| VM systemd | Simple | Scaling pain |

**Recommendation:** **Compose for Stage 1 lab**; **Kubernetes for Stage 6+ hardened deploy**. Edge: k3s or supervised containers later.

---

### D10 — IaC / CI

**Terraform or equivalent** for cloud; **GitHub Actions** for CI (repo target `web8080`). Policy: no secrets in repo.

---

### D11 — Identity

**OIDC** via existing IdP (Keycloak/Auth0/Okta/customer AD). Do not build custom auth.

---

### D12 — AI assistant stack

Only after core C2 works. Tool-calling agent with **strict allowlist**, server-side RAG over runbooks, full tool audit. Model hosting: customer policy (private endpoint preferred).

---

## 3. Summary selection matrix

| Area | Selected (proposed) | Explicit non-goals |
|---|---|---|
| Streaming | Redpanda (Kafka API) | Custom broker |
| UI API | REST OpenAPI | GraphQL unless justified later |
| Internal infer | gRPC | Ad-hoc HTTP without schema |
| DB | Postgres + PostGIS | Multi-DB sprawl MVP |
| Cache | Redis | Redis as SoR |
| Objects | S3 API | Local disk as prod store |
| Backend | FastAPI/Python (+ Go if needed) | Premature polyglot explosion |
| Frontend | React TS | Native MVP |
| Deploy lab | Docker Compose | K8s day-1 mandate |
| Deploy hardened | Kubernetes | Snowflake PaaS lock-in without review |
| Auth | OIDC + mTLS services | Roll-your-own auth |
| Maps | MapLibre (or approved) | Unlicensed map data |

---

## 4. Challenge note (Agent 8)

If the implementing team lacks Kafka/Redpanda skills, still prefer a durable log over DB-as-queue — sensor systems outgrow table-polling. Budget training/ops time rather than deleting the bus.

If customer forbids Python in prod, revisit D6 with SYS+SE before coding.

---

## Author

Victor.I
