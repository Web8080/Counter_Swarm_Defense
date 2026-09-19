<!-- Author: Victor.I -->

# Deliverable 5 — Component Dependency Map

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Purpose

Show runtime and design-time dependencies so teams do not create hidden coupling. Arrows mean **depends on** (consumer → provider).

---

## 2. Tiered dependency view

```
                         [IdP / Identity]
                               ▲
                               │
                        [API Gateway]
                               ▲
               ┌───────────────┼───────────────┐
               │               │               │
        [Operator UI]   [Integration    [Admin APIs]
               │          Clients]
               ▼               │
        [Operator API]◄────────┘
               │
               ▼
        [Realtime GW] ──────────► [Event Bus]
               │                      ▲
               │                      │
               ▼                      │
        [Approval] [Alert] [Risk] [Behaviour] [Fusion] [Tracking] [Detection]
               │       │      │        │         │         │          │
               └───────┴──────┴────────┴─────────┴─────────┴──────────┘
                                      │
                                      ▼
                               [Event Bus]
                                      ▲
                                      │
                         [Normaliser]─┘
                                      ▲
                                      │
                            [Sensor Adapters]
                                      ▲
                                      │
                           [Sensors / Simulator]

        [Audit] ◄── subscribes to material topics + approval writes
        [Inference GW] ◄── Detection/Classification (and optional others)
        [Model Registry] ◄── Inference GW
        [Hot DB / PostGIS] ◄── Operator API, Tracking, Fusion, Approval, Alert
        [Object Store] ◄── Adapters (raw), Models, Replay artifacts
        [Observability] ◄── all services (sidecar/agent)
        [AI Assistant] → Operator API tools + policy (never direct DB write for decisions)
```

---

## 3. Dependency matrix (core)

| Component | Depends on | Depended on by |
|---|---|---|
| Sensor adapters | Vendor/sim SDK, object store (optional raw), identity (mTLS) | Normaliser |
| Normaliser | Schema registry, event bus | Detection, quality, tracking |
| Event bus | Disk/quorum storage | Nearly all processors + realtime |
| Detection | Event bus, inference GW (optional) | Tracking, fusion |
| Tracking | Event bus, hot DB | Fusion, behaviour, risk, UI |
| Fusion | Event bus, hot DB | Behaviour, risk, UI |
| Behaviour | Event bus / tracks | Risk |
| Risk | Tracks, behaviour, policy config | Alert, UI |
| Alert | Risk/track events, policy | UI, notifications |
| Approval | IAM, audit, hot DB | Integration API |
| Integration API | Approval records, IAM | External systems |
| Operator API | Hot DB, event projections, IAM | UI, AI tools |
| AI Assistant | Policy layer, Operator API tools | UI |
| Audit | Append store | Compliance queries |
| Sim engine | Scenario configs | Adapters (sim) |
| Inference GW | Model registry, GPU/CPU runtime | Detection/classification |
| Observability | All | Operators/admins |

---

## 4. Acyclic rule for writes

Allowed write paths:

1. Adapters → bus (observations)  
2. Processors → bus (derived events) + own projections to hot DB  
3. Approval service → decisions table + audit + optional integration outbox  
4. No processor may write another processor’s tables directly  

Violations are architecture defects.

---

## 5. Critical path (alert to operator)

```
Sensor/Sim → Adapter → Normaliser → Bus
  → Detection → Tracking → Fusion → Behaviour → Risk → Alert
  → Realtime GW → Operator UI
```

Parallel: Quality service annotates; does not block track publish unless policy says hard-fail.

---

## 6. Failure isolation notes

| If down | Impact | Isolation expectation |
|---|---|---|
| Single adapter | Local coverage loss | Others continue |
| Event bus | Major — pipeline pause | Buffer at edge if configured; fail loud |
| Tracking | Stale tracks | UI shows degraded |
| AI Assistant | No chat/summaries | Core C2 unaffected |
| Integration API | No external handoff | Decisions still audited locally |
| Object store | Raw replay limited | Hot path may continue if payloads inline/small |

---

## 7. Shared libraries (design-time)

| Library | Used by | Contains |
|---|---|---|
| `schemas` | All | JSON Schema / Avro / protobuf defs |
| `auth-sdk` | Services | Token validation helpers |
| `obs-sdk` | Services | Metrics/trace bootstrap |
| `geo-sdk` | Normaliser, fusion, UI API | CRS transforms |

Keep libraries thin; avoid “god” shared domain package.

---

## Author

Victor.I
