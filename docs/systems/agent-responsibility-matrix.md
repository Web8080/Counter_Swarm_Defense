<!-- Author: Victor.I -->

# Deliverable 3 — Eight-Agent Responsibility Matrix

**Author:** Victor.I  
**Status:** Draft for review  
**Role of Agent 8:** System architect and integration lead — challenges and reconciles all others

---

## 1. Purpose

Define ownership so eight disciplines collaborate like an engineering organisation without duplicate authority or silent gaps.

---

## 2. RACI legend

| Code | Meaning |
|---|---|
| **R** | Responsible — does the work |
| **A** | Accountable — one owner for outcome |
| **C** | Consulted — input before decision |
| **I** | Informed — notified of decision |

Agents:

1. Product Design & Human Factors (PD)  
2. Software Engineering (SE)  
3. AI Engineering (AI)  
4. ML Engineering (ML)  
5. Data Engineering (DE)  
6. Data Science & Analytics (DS)  
7. Security, Safety & Governance (SG)  
8. Systems Engineering & Integration (SYS)

---

## 3. Responsibility matrix

| Workstream / artefact | PD | SE | AI | ML | DE | DS | SG | SYS |
|---|---|---|---|---|---|---|---|---|
| Problem / CONOPS framing | C | I | I | I | I | C | C | **A/R** |
| Personas, journeys, UX principles | **A/R** | C | C | I | I | C | C | C |
| System requirements (FR/NFR) | C | C | C | C | C | C | C | **A/R** |
| MoSCoW / out-of-scope gate | C | C | C | C | C | C | **A** (safety) | **A/R** (system) |
| System architecture | C | **R** | C | C | C | C | C | **A** |
| ICD / interfaces | I | **R** | C | C | **R** (events) | C | C | **A** |
| Event schemas / canonical observation | I | C | I | C | **A/R** | C | C | C |
| Storage / streaming design | I | C | I | I | **A/R** | C | C | C |
| Detection / tracking / fusion models | I | C | C | **A/R** | C | **C** | C | C |
| Behaviour / risk analytics methods | C | I | C | C | C | **A/R** | C | C |
| Risk engine software service | I | **A/R** | C | C | C | **C** | C | C |
| AI assistant / tool orchestration | C | C | **A/R** | I | C | I | **C** | C |
| Operator console | **A** (UX) | **R** (impl) | C | I | I | I | C | C |
| AuthN/AuthZ, secrets, TM | I | **R** | C | C | C | I | **A** | C |
| Audit design | C | **R** | C | C | C | I | **A** | C |
| Model governance / cards | I | I | C | **R** | I | **C** | **A** | C |
| Digital twin / simulation | C | C | I | C | C | **R** (scenarios) | C | **A** |
| Deployment / edge-central | I | **R** | I | C | C | I | C | **A** |
| FMEA / failure engineering | I | C | C | C | C | C | C | **A/R** |
| Test strategy | C | **R** | C | **R** (ML) | **R** (contracts) | **R** (eval) | **R** (sec) | **A** |
| Roadmap / release gate | C | C | C | C | C | C | C | **A/R** |
| Field test authorisation gate | C | I | I | I | I | C | **A** | **R** |
| External integration boundary | I | **R** | I | I | C | I | **A** | **A** (joint) |
| README / repo structure | I | **R** | I | I | I | I | I | **A** |
| Contradiction resolution | C | C | C | C | C | C | C | **A/R** |

Note: Where two **A** appear (safety vs system), SYS owns system coherence; SG can **veto** on safety/autonomy boundaries.

---

## 4. Agent missions and artefacts

### Agent 1 — Product Design & Human Factors

- **Owns:** Personas, journeys, IA, wireframes, UX principles, alert ethics, workload metrics  
- **Publishes to:** `docs/product/`  
- **Interfaces with:** SE (console), AI (assistant UX), SG (approval workflows), SYS (CONOPS)  
- **Must not build:** Backend services, models, infra  

### Agent 2 — Software Engineering

- **Owns:** Service boundaries, APIs, gateway, realtime console implementation, CI/CD skeletons (post-approval), service SLIs  
- **Publishes to:** `docs/software/`, later `backend/`, `frontend/`, `api/`  
- **Interfaces with:** DE (events), ML (inference APIs), SG (auth), SYS (deployment)  
- **Must not build:** Unbounded LLM autonomy; effector control  

### Agent 3 — AI Engineering

- **Owns:** Assistant architecture, tool allowlists, RAG boundaries, AI eval, prompt-injection defences  
- **Publishes to:** `docs/ai/`  
- **Interfaces with:** SE (tool APIs), SG (policy), DS (explanations), PD (UX)  
- **Must not put LLMs in:** IAM, audit integrity, safety interlocks, event validation  

### Agent 4 — ML Engineering

- **Owns:** Detection/classification/tracking/anomaly model pipelines, metrics, registry, drift, rollback  
- **Publishes to:** `docs/ml/`, later `models/`  
- **Interfaces with:** DE (features), DS (eval design), SE (serving), SG (model cards)  
- **Must not assume:** Deep learning everywhere; ship classical trackers when sufficient  

### Agent 5 — Data Engineering

- **Owns:** Canonical schemas, bus, hot/warm/cold stores, lineage, quality, retention, replay  
- **Publishes to:** `docs/data/`, `schemas/`  
- **Interfaces with:** All producers/consumers via ICD  
- **Must not:** Encode business risk policy inside raw ingest  

### Agent 6 — Data Science & Analytics

- **Owns:** Swarm/behaviour methods, uncertainty frameworks, scenario design, offline evaluation, simulation analytics  
- **Publishes to:** `docs/data-science/`  
- **Interfaces with:** ML (metrics), DE (analytic stores), PD (what to show), SYS (validation)  
- **Must not:** Collapse uncertainty into silent binary threat labels  

### Agent 7 — Security, Safety & Governance

- **Owns:** Threat model, RBAC/ABAC policy, audit integrity, supply chain, AI/ML governance, safety veto  
- **Publishes to:** `docs/security/`  
- **Interfaces with:** Everyone at trust boundaries  
- **Must not:** Be bypassed by “demo mode” in shared environments  

### Agent 8 — Systems Engineering & Integration

- **Owns:** Mission definition, decomposition, ICD approval, edge/central, FMEA, roadmap gates, integration truth  
- **Publishes to:** `docs/systems/`, `architecture/`  
- **Interfaces with:** All; resolves contradictions  
- **Must not:** Rubber-stamp conflicting proposals  

---

## 5. Collaboration workflow

```
SYSTEM ENGINEER (Agent 8)
        │
 ┌──────┼──────────────┐
 │      │              │
PD     SE             SG
 │      │              │
 └──────┼──────────────┘
        │
 ┌──────┼──────────────┐
 │      │              │
AI     ML             DE
 │      │              │
 └──────┼──────────────┘
        │
       DS
        │
 SYSTEM INTEGRATION → VALIDATION → RELEASE
```

Each agent answers the research protocol (problem, users, inputs, outputs, dependencies, failures, alternatives, evidence, trade-offs, security, testing, operationalisation) before proposing implementation.

---

## 6. Decision rights

| Decision type | Authority |
|---|---|
| Safety / autonomy boundary | SG veto; SYS records |
| Interface breaking change | SYS + producer + consumer owners |
| UX information hierarchy | PD accountable |
| Technology selection for platform defaults | SYS accountable after SE/DE/SG consult |
| Model promotion to operator-critical path | ML + DS recommend; SG + SYS approve |
| Go to field testing | SG + SYS |

---

## 7. Definition of “integrated” for Stage 0

Stage 0 is complete when all agents have published their research/architecture artefacts under the agreed folders and SYS has produced reconciled `architecture/*` documents without unresolved contradictions (open questions explicitly listed).

---

## Author

Victor.I
