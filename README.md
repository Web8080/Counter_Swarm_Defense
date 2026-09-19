<!-- Author: Victor.I -->

# Counter-Swarm Defence Platform

Defensive research and decision-support software for multi-sensor counter-UAS operations. The platform fuses fragmented sensing into a coherent operational picture, supports human operators with evidence-backed assessments, and integrates only with authorised external systems through controlled boundaries.

This is a **systems engineering product**, not an isolated detection model.

**Status:** Architecture and requirements phase. Application code is intentionally deferred until document review and approval.

This README is updated as the project progresses. The standalone Deliverable 1 document remains at [docs/product/executive-definition.md](docs/product/executive-definition.md).

---

## What this is

A modular platform that:

- Ingests heterogeneous sensor observations (radar, EO/IR, RF, acoustic, telemetry, other feeds)
- Normalises, validates, and streams events
- Detects, classifies, tracks, and correlates objects
- Analyses potential swarm behaviour and assesses risk with explicit uncertainty
- Presents decision support to operators (never autonomous engagement)
- Maintains immutable audit trails and governance controls

## What this is not

The platform must **not** autonomously:

- Select or engage human targets
- Control weapons or kinetic interceptors
- Conduct electronic attack or jamming
- Trigger destructive effects
- Bypass safety mechanisms

Physical response effects remain outside the platform. Development uses simulation, mock effectors, and abstract response categories.

---

## Discipline map

| Discipline | What you would actually build |
|---|---|
| Software Engineering | Sensor integrations, APIs, event pipelines, command/control interfaces, dashboards, real-time systems and device communication |
| AI Engineering | AI decision-support layer, sensor-fusion workflows, agent/tool orchestration, anomaly assistance and operator assistance |
| ML Engineering | Detection, classification, tracking, behaviour analysis and sensor-fusion models |
| Data Engineering | Ingestion of heterogeneous sensor data, event streams, storage, feature pipelines and historical analysis |
| Data Science | Swarm behaviour analysis, threat modelling, model evaluation, statistical analysis and simulation |
| Product Design | Operator workflows, alert design, decision-support UX, human approval and operational usability |
| Systems Engineering | Integration of sensors, compute, communications, software, simulation and authorised external systems into one reliable platform |
| Security & Governance | Identity, RBAC, auditability, secure APIs, model governance, resilience and controlled access |

---

## Document index (Stage 0 deliverables)

| # | Deliverable | Location |
|---|---|---|
| 1 | Executive product definition + research | [docs/product/executive-definition.md](docs/product/executive-definition.md) |
| 1b | Product design pack (workflows, journeys, IA, wireframes, screens, UX, tokens) | [docs/product/README.md](docs/product/README.md) |
| 1c | UI/UX + simulation visual PDF | [docs/product/pdfs/UI-UX-and-Simulation-Visual-Pack.pdf](docs/product/pdfs/UI-UX-and-Simulation-Visual-Pack.pdf) |
| 1d | Simulation design pack | [docs/simulation/README.md](docs/simulation/README.md) |
| 2 | System requirements | [docs/systems/requirements.md](docs/systems/requirements.md) |
| 3 | Eight-agent responsibility matrix | [docs/systems/agent-responsibility-matrix.md](docs/systems/agent-responsibility-matrix.md) |
| 4 | System architecture | [architecture/system.md](architecture/system.md) |
| 5 | Component dependency map | [architecture/dependencies.md](architecture/dependencies.md) |
| 6 | Data-flow architecture | [architecture/data-flow.md](architecture/data-flow.md) |
| 7 | Interface Control Document | [architecture/interfaces.md](architecture/interfaces.md) |
| 8 | Threat model | [docs/security/threat-model.md](docs/security/threat-model.md) |
| 9 | Failure Mode and Effects Analysis | [architecture/failure-modes.md](architecture/failure-modes.md) |
| 10 | Technology selection matrix | [architecture/tradeoffs.md](architecture/tradeoffs.md) |
| 11 | Digital-twin / simulation architecture | [docs/systems/digital-twin.md](docs/systems/digital-twin.md) |
| 12 | Development roadmap | [docs/systems/roadmap.md](docs/systems/roadmap.md) |
| 13 | Testing strategy | [docs/systems/testing-strategy.md](docs/systems/testing-strategy.md) |
| 14 | Deployment architecture | [architecture/deployment.md](architecture/deployment.md) |
| 15 | Repository structure | [docs/systems/repository-structure.md](docs/systems/repository-structure.md) |
| 16 | This README | [README.md](README.md) |
| 17 | Open questions and assumptions | [docs/systems/open-questions-assumptions.md](docs/systems/open-questions-assumptions.md) |

Discipline deep-dives live under `docs/product`, `docs/software`, `docs/ai`, `docs/ml`, `docs/data`, `docs/data-science`, `docs/security`, and `docs/systems`.

---

## Conceptual pipeline

```
SENSING → NORMALISE → EVENT STREAM → DETECT / TRACK / QUALITY
        → FUSION → BEHAVIOUR → RISK → DECISION SUPPORT
        → HUMAN OPERATOR → AUTHORISED ACTION CATEGORY → AUDIT
```

---

## Roadmap (high level)

```
RESEARCH → REQUIREMENTS → SYSTEM ARCHITECTURE
        → PRODUCT / SOFTWARE / DATA
        → AI / ML → SIMULATION → SENSOR INTEGRATION
        → FUSION → OPERATOR PLATFORM → SECURITY HARDENING
        → HARDWARE-IN-LOOP → CONTROLLED VALIDATION → PRODUCTION
```

Current gate: **document review and approval**. No application implementation until architecture sign-off.

---

## Engineering priorities

reliability > novelty  
evidence > assumptions  
integration > isolated demos  
human oversight > uncontrolled autonomy  
testability > complexity  
clear interfaces > tightly coupled components  
operational usefulness > impressive AI  

---

# Executive product definition

Copied from [docs/product/executive-definition.md](docs/product/executive-definition.md) for visibility on the repository landing page. That file continues to exist and remains Deliverable 1.

**Audience:** Product, systems, security, and engineering leads

---

## 1. Problem statement

Operators defending fixed or mobile assets against unmanned aerial systems (UAS) and coordinated swarms receive fragmented, asynchronous signals from radar, EO/IR, RF, acoustic and other feeds. Each feed is locally useful and globally incomplete. When threats move quickly, isolated detectors create alert noise without a shared track picture, shared uncertainty, or a governed path from observation to human decision.

The product thesis:

> A reliable integrated system delivers more operational value than isolated detection tools when threats move quickly and information is fragmented across sensing systems.

Focus: integration, correlation, visibility, decision support, reliability, and governance — not “another detector.”

---

## 2. Product definition

### 2.1 What we are building

A **counter-swarm decision-support platform** that:

1. Ingests multi-sensor observations through vendor-agnostic adapters  
2. Builds a unified operational picture (tracks, evidence, confidence)  
3. Detects potential swarm/coordinated behaviour patterns  
4. Assesses risk without collapsing uncertainty into false binaries  
5. Supports human review and authorised response *categories*  
6. Audits every material inference and human decision  
7. Integrates with authorised external systems only via controlled APIs  

### 2.2 What we are not building

- Autonomous weapons control or engagement selection  
- Weapon guidance, kinetic effector firmware, or jamming controllers  
- Instructions for constructing weapons or defeating safety mechanisms  
- A vendor-locked single-sensor product  

Physical effects remain outside the platform boundary. Development uses simulation and mock effectors.

### 2.3 Primary value proposition

| Stakeholder need | Platform response |
|---|---|
| “What is in the air right now?” | Track picture with evidence links |
| “How sure are we?” | Calibrated confidence and quality flags |
| “Is this coordinated?” | Behaviour indicators with supporting observations |
| “What should I look at first?” | Prioritised alerts, not raw event floods |
| “Why did the system say that?” | Evidence trail + model/version provenance |
| “Who decided what?” | Immutable audit of human decisions |

---

## 3. Research outcomes (synthesis)

Research below is synthesised from public counter-UAS C2 practice, human-factors literature on alert fatigue, multi-sensor fusion patterns, and defensive SOC-style decision support. Site-specific CONOPS remains an open assumption (see Deliverable 17).

### 3.1 Counter-UAS operator workflows

Typical cycle: detect → cue sensors → establish track → classify → assess intent/risk → escalate → authorise response category → record outcome. Bottlenecks are correlation across sensors, false alarms, and handover between roles.

### 3.2 Alert fatigue

Operators degrade when low-value alerts dominate. Design implication: tiered alerts, suppression of duplicate track noise, quality gating before human-facing alerts, and explicit “why this alert now.”

### 3.3 Human-machine teaming

AI/ML should explain and prioritise; humans own consequential decisions. Visual language must separate observation, inference, prediction, recommendation, and decision.

### 3.4 Geospatial and multi-threat monitoring

Map-centric SITREP with declutter controls; multi-select tracks; time-linked replay. Uncertainty must be spatial (ellipses/cones) and semantic (class probability / track quality).

### 3.5 Incident and approval workflows

Incident objects bind tracks, evidence, recommendations, assignees, and decisions. Dual-control options for high-severity actions (configurable policy).

### 3.6 What operators do *not* want

- Raw model logits and every intermediate detection  
- Undifferentiated event firehoses  
- “AI confirmed threat” language without evidence  
- Controls that look like they fire effectors when they only request categories  

---

## 4. Personas

| Persona | Goals | Pain | Success signal |
|---|---|---|---|
| **Security operator** | Maintain air picture; triage alerts; escalate | Too many low-confidence alerts; unclear evidence | Correct prioritisation under load |
| **Sensor operator** | Keep sensors healthy; cue EO/IR; validate tracks | Blind spots; clock skew; vendor UI sprawl | Single health + coverage view |
| **Incident commander** | Decide response category; coordinate teams | Incomplete picture; slow correlation | Decision within SLA with audit |
| **Analyst** | Investigate patterns; tune thresholds; after-action | Hard to replay; weak lineage | Replayable incidents with provenance |
| **System administrator** | Availability, access, config | Brittle integrations; secret sprawl | Reproducible deploy + RBAC |
| **Technical engineer** | Integrate sensors/adapters; debug pipelines | Proprietary SDKs; schema drift | Canonical observation contract |
| **Security/governance officer** | Assurance, audit, policy | Opaque models; weak trail | Model cards + immutable audit |

---

## 5. User journeys

### Journey A — Unknown object

```
Unknown object detected (sensor adapter)
        ↓
Normalised observation on event bus
        ↓
Detection / association → candidate track
        ↓
Operator receives Tier-2+ alert (if policy met)
        ↓
Console shows confidence, quality, supporting observations
        ↓
Additional sensors correlate → track quality rises
        ↓
Behaviour / risk engines update assessment
        ↓
Operator reviews recommendation (category only)
        ↓
Human decision recorded
        ↓
Optional handoff to authorised external system API
        ↓
Audit complete
```

### Journey B — Suspected swarm

```
Multiple tracks with spatial-temporal proximity
        ↓
Behaviour engine flags coordination indicators
        ↓
Risk assessment elevates priority with uncertainty band
        ↓
Incident auto-opened (policy)
        ↓
Commander reviews evidence pack + missing-info panel
        ↓
Approve / modify / reject recommended category
        ↓
Audit + after-action analytics feed
```

### Journey C — Sensor degradation

```
Sensor health drop / silence
        ↓
Coverage map degrades; confidence ceilings applied
        ↓
Operator notified of capability loss (not fake tracks)
        ↓
Fusion continues with remaining sensors
        ↓
Recovery → quality restored; logged
```

---

## 6. System workflow (product view)

```
                    COUNTER-SWARM PLATFORM
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
     SENSING               ANALYSIS             RESPONSE
   Radar/EO/IR          Detect/Classify      Operator decision
   RF/Acoustic          Track/Fuse           Authorised category
   Telemetry/Other      Behaviour/Risk       External controlled API
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                       FUSION + DATA PLATFORM
                              │
                       OPERATOR CONSOLE
                              │
                            AUDIT
```

Safety chain (mandatory):

```
DETECTION → TRACK → CLASSIFY → ASSESS → PRIORITISE
→ HUMAN REVIEW → AUTHORISED RESPONSE CATEGORY → EXTERNAL SYSTEM
```

Platform does not implement the physical effect.

---

## 7. UI / UX / workflow design pack (expanded)

Wireframes, screen specs, workflows, and UX language are expanded in the product pack:

| Doc | Contents |
|---|---|
| [docs/product/README.md](docs/product/README.md) | Pack index and reading order |
| [docs/product/01-system-workflow-design.md](docs/product/01-system-workflow-design.md) | Operational + platform workflows, state machines |
| [docs/product/02-user-journeys.md](docs/product/02-user-journeys.md) | J1–J8 role journeys |
| [docs/product/03-information-architecture.md](docs/product/03-information-architecture.md) | Nav, sitemap, object model |
| [docs/product/04-wireframes.md](docs/product/04-wireframes.md) | Low-fi layouts (X01–S01) |
| [docs/product/05-ui-screen-inventory.md](docs/product/05-ui-screen-inventory.md) | Screen IDs, states, annotations |
| [docs/product/06-ux-principles-and-visual-language.md](docs/product/06-ux-principles-and-visual-language.md) | Epistemic UX + visual rules |
| [docs/product/07-alerts-approvals-and-incidents-ui.md](docs/product/07-alerts-approvals-and-incidents-ui.md) | Alert/approval/incident UI |
| [docs/product/08-design-tokens.md](docs/product/08-design-tokens.md) | Colour, type, motion tokens |
| [docs/product/09-open-design-decisions.md](docs/product/09-open-design-decisions.md) | Blocking UI decisions |
| [docs/product/10-system-workflow-diagrams.md](docs/product/10-system-workflow-diagrams.md) | Workshop diagram pack |

---

## 8. Dashboard regions (summary)

Map-first shell: **Map** · **Alerts** · **Tracks** · **Risk / actions** · **Timeline** · **Sensors** · **System** · **Audit**. Full IA in `docs/product/03-information-architecture.md`; wireframes in `docs/product/04-wireframes.md`.

---

## 9. UX principles (summary)

Epistemic honesty; observation ≠ inference ≠ prediction ≠ recommendation ≠ decision; priority over volume; degrade in public; no faux effector UI. Full treatment in `docs/product/06-ux-principles-and-visual-language.md`.

---

## 10. Product trade-offs

| Decision | Option A | Option B | Choice (proposed) | Why |
|---|---|---|---|---|
| Alert richness | Show all detections | Tiered, quality-gated | B | Reduces fatigue |
| Autonomy | Auto-select category | Recommend only | Recommend + optional auto-tier-0 notify | Safety boundary |
| Map density | Everything always | Layers + declutter | Layers | Cognitive load |
| AI in UI | Chat everywhere | Scoped assistant | Scoped | Reliability > novelty |
| Web vs native | Native C2 | Web console | Web first (+ later hardened clients if required) | Speed of iteration; deployability |
| Multi-tenancy | Single site | Multi-site tenants | Single-site first, tenant-ready identity | Min reliable system |

---

## 11. MVP (smallest valuable system)

Must prove:

1. Simulated multi-sensor observations → canonical events  
2. Tracks with confidence and evidence links  
3. Risk/priority with uncertainty  
4. Operator console (map, tracks, alerts, timeline, health)  
5. Human decision recording + audit  
6. Mock external integration boundary  

Out of MVP: production vendor SDKs, advanced LLM assistants, multi-region HA, real effectors.

---

## 12. Success metrics (product)

| Metric | Intent |
|---|---|
| Time-to-understand (alert → evidence viewed) | Decision support speed |
| False-alert rate to operator (Tier ≥2) | Fatigue control |
| Track continuity under multi-sensor drop | Fusion value |
| % decisions with complete audit fields | Governance |
| Operator SUS / workload scores in trials | Human factors |

---

## 13. Stop condition for this deliverable

The executive definition (above and in `docs/product/executive-definition.md`) defines product intent and research synthesis. Detailed workflows, wireframes, and UI specs live in the product design pack (`docs/product/01`–`10`). Nothing here authorises application implementation.

**Next:** Review the product pack, then Requirements (Deliverable 2) and architecture review.

---

## Author

Victor.I
