<!-- Author: Victor.I -->

# Human Factors and Command-and-Control Design for Counter-Swarm Defensive Decision Support: An Epistemic Interface Monograph

**Author:** Victor.I  
**Affiliation:** Counter-Swarm Defence Platform — Product Design / Human–Machine Teaming Research  
**Document type:** Research monograph (defensive decision-support only)  
**Scope constraint:** This work addresses sensing, situation assessment, alerting, incident coordination, and the recording of *authorised response categories*. It does not prescribe weapons employment, electronic attack, jamming parameters, or any effector control path.  
**Product binding:** Screens X01–X08 and I01 of the Counter-Swarm Defence Platform console  
**Version:** 1.0  
**Status:** Archival research draft for engineering and evaluation programmes

---

## Abstract

Counter-swarm defensive operations place human operators and commanders in a high-tempo information environment in which multi-sensor tracks, model inferences, behavioural indicators, and policy recommendations arrive faster than unaided cognition can reliably integrate them. The Counter-Swarm Defence Platform is designed as a *defensive decision-support* system: it assembles an accountable air picture, surfaces graded risk and missing information, and records human-authorised response *categories* for optional external handoff. It deliberately excludes weapon aim, fire, jam, and electronic-attack control surfaces.

This monograph develops a research-grade human-factors account of that console. It formulates the operator command-and-control (C2) problem as an epistemic coordination task under uncertainty, partial observability, and alert pressure. It synthesises Endsley’s situation awareness (SA) model, research on alert fatigue and automation trust, and human–machine teaming (HMT) principles into a design theory for an *epistemic user interface* whose five visible layers—observation, inference, prediction, recommendation, and decision—must remain visually and linguistically separable across product screens X01 (monitor), X02 (alert detail), X03 (track evidence), X04 (record decision), X05 (health), X06 (audit), X07 (replay), X08 (assistant drawer), and I01 (incident workspace).

The contribution is threefold. First, a problem formulation that treats swarm-suspect events as multi-track evidence problems rather than single-label threat declarations. Second, a reference architecture for a map-first operator console that implements progressive disclosure, degrade-in-public health chrome, and fail-closed decision recording. Third, an evaluation programme spanning SAGAT-style SA probes, workload indices, decision latency and quality metrics, and misuse/disuse/abuse indicators drawn from Parasuraman and Riley’s automation taxonomy. The monograph ends with a stepwise build guide that maps wireframes to engineering contracts without inventing faux effector affordances.

**Keywords:** situation awareness; human–machine teaming; alert fatigue; epistemic interface design; command and control; counter-swarm defence; decision support; automation trust; workload; auditability

---

## 1. Introduction

### 1.1 Motivation

Swarm-capable unmanned systems compress the time between first sensing and the need for coordinated human judgement. Operators must decide whether a set of tracks is coordinated, whether sensor coverage is adequate to trust that judgement, and what *category* of authorised response—heighten monitoring, cue an additional sensor, notify an external system, request escalation, open an incident, or dismiss—should be recorded. Those decisions are consequential for downstream organisations, yet they are not weapons releases. Conflating decision support with effector control is both a safety hazard and a design error: it invites automation misuse, legal ambiguity, and interface metaphors that accelerate action before evidence is understood.

The Counter-Swarm Defence Platform therefore adopts a hard product rule: physical effects are never inside the operator loop. Categories are recorded intents for authorised external systems. The console’s job is to make an overloaded human *correctly sceptical and correctly fast*—sceptical of unverified inference, fast at finding evidence and recording an accountable decision (Victor.I, product UX north-star).

### 1.2 Research questions

This monograph addresses four research questions (RQ):

1. **RQ1 (Epistemic structure):** How should observation, inference, prediction, recommendation, and decision be represented so that operators retain Level 1–3 situation awareness under multi-track load?
2. **RQ2 (Console architecture):** What reference architecture binds screens X01–X08 and I01 into a coherent C2 workflow without creating split-brain selection or faux weapon affordances?
3. **RQ3 (Automation & fatigue):** How should alerting, recommendations, and an optional assistant (X08) be bounded to reduce alert fatigue and automation misuse/disuse/abuse?
4. **RQ4 (Proof):** What evaluation protocol can demonstrate that the epistemic UI improves SA, decision quality, and accountability relative to fused “AI threat confirmed” presentations?

### 1.3 Contributions

The monograph contributes:

- A formal problem formulation for counter-swarm *operator C2* as defensive decision support (Section 3).
- A theoretical framework linking Endsley SA, alert fatigue, and HMT to product principles (Section 4).
- An epistemic UI design method with screen-level bindings (Section 5).
- A reference architecture and implementation bridge from wireframes to engineering (Sections 6–7).
- Explicit trade-offs, failure modes, evaluation protocols, and a build guide (Sections 8–11).

### 1.4 Scope and non-goals

**In scope:** Human factors of monitoring, triage, evidence review, incident coordination, decision recording, health awareness, audit, replay, and optional grounded assistance.

**Out of scope:** Weapons employment doctrine; electronic attack or jamming guidance; kinetic/non-kinetic effector parameters; classified tactics that would require operational security review beyond defensive sensing and C2 decision support.

**Assumption statement:** Assumptions that exceed present facts are labelled as such. Where product policy is still open (e.g., auto-open of incidents), the monograph states the human-factors implications of each option rather than pretending closure.

### 1.5 Document map

Section 2 reviews related work. Section 3 formulates the operator problem. Section 4 develops theory. Section 5 presents the design method. Section 6 gives the console reference architecture. Section 7 provides implementation guidance. Sections 8–9 analyse trade-offs and failure modes. Section 10 specifies evaluation. Section 11 is a stepwise build guide. Sections 12–13 discuss and conclude. References follow.

---

## 2. Related Work

### 2.1 Situation awareness in dynamic systems

Endsley’s theory of situation awareness remains the dominant organising frame for real-time operator interfaces (Endsley, 1995). SA is defined as the perception of elements in the environment within a volume of time and space (Level 1), the comprehension of their meaning (Level 2), and the projection of their status in the near future (Level 3). Endsley further distinguishes SA from decision and performance: high SA does not guarantee correct action, but low SA systematically degrades decision quality in dynamic systems.

For counter-swarm consoles, Level 1 maps to observations and track kinematics; Level 2 maps to fusion, classification distributions, behaviour indicators, and risk factors; Level 3 maps to kinematic envelopes and predicted coordination hypotheses. A critical design implication—often violated by “threat score” dashboards—is that collapsing Levels 1–3 into a single coloured label destroys the operator’s ability to diagnose *why* the picture is uncertain.

Endsley and colleagues later emphasised measurement methods such as SAGAT (Situation Awareness Global Assessment Technique), which freezes the simulation and probes operators’ knowledge of the situation (Endsley, 1995; Endsley & Garland, 2000). This monograph adopts SAGAT-style probes as a primary SA evaluation instrument (Section 10).

### 2.2 Attention, clutter, and display design

Wickens’ work on attention and display layout underpins map-first C2 design. Multiple resource theory and principles of proximity compatibility argue that information that must be integrated should be displayed in integrated formats, while information that must be discriminated should remain visually distinct (Wickens & Carswell, 1995; Wickens, Hollands, Banbury, & Parasuraman, 2013). In swarm monitoring, track identity, uncertainty ellipses, and alert tiers must be integrable on the map (X01), while epistemic *type*—observation versus inference—must remain discriminable (X02/X03 strips).

Clutter research shows that excess symbology increases search time and error (Wickens et al., 2013). The product’s “Simplify” density mode—retaining T2+/T3 and active incident tracks—is therefore not a cosmetic preference but an attention-management control.

### 2.3 Humans and automation: use, misuse, disuse, abuse

Parasuraman and Riley (1997) classify problematic automation relationships as misuse (over-reliance), disuse (under-utilisation), and abuse (inappropriate application by designers or managers). In AI-assisted sensing, misuse appears when operators treat class probabilities as ground truth; disuse appears when operators ignore calibrated recommendations under alert storm; abuse appears when product language presents model outputs as “confirmed threats” or when assistants can commit decisions.

Lee and See (2004) argue that trust in automation should be calibrated to system capability. Calibration requires transparency about uncertainty, coverage loss, and model version—precisely the content of epistemic strips and X05 health chrome.

### 2.4 Ironies of automation and resilience

Bainbridge’s “ironies of automation” (1983) warn that automation that removes routine work can leave humans with harder residual tasks—monitoring for rare failures—while deskilling them. Hollnagel’s resilience engineering perspective emphasises graceful extensibility under surprise (Hollnagel, Woods, & Leveson, 2006; Woods, 2015). For counter-swarm defence, the irony is acute: fusion and behaviour models accelerate routine correlation, but the residual tasks—conflict resolution under missing RF, swarm-suspect judgement, category selection under dual-control—are exactly where epistemic honesty matters most.

Woods and colleagues’ work on joint cognitive systems further argues against “substitution myths” (automation replaces humans). The correct frame is *teamwork*: machines extend perception and memory; humans retain authority for accountable category decisions (Woods & Hollnagel, 2006).

### 2.5 Alert fatigue and alarm philosophy

Alert fatigue—desensitisation under high false-alarm or low-value alert rates—is extensively documented in clinical and process-control domains and transfers to C2 (Cvach, 2012; Bliss & Gilson, 1998). Design responses include tiering, duplicate suppression, quiet modes for advisory tiers, and rate metering. The Counter-Swarm Defence Platform’s T0–T3 policy model and fatigue controls (duplicate badges, per-track collapse, T1 quiet mode) instantiate these lessons (Victor.I, alerts UI design).

### 2.6 Human–machine teaming for decision support

HMT literature emphasises shared mental models, predictable automation behaviour, and clear authority boundaries (Klein, Woods, Bradshaw, Hoffman, & Feltovich, 2004; Lyons & Guznov, 2019). For this product, HMT means: recommendations are suggestions bound to policy IDs; X08 assistants are tool-bounded and citation-required; decisions are human-recorded with rationale; and assistants cannot submit X04/I02 commitments.

### 2.7 C2 and air picture systems (defensive framing)

Classic C2 literature on common operating pictures and recognition-primed decision making (Klein, 1993) informs incident workspaces (I01): commanders need a multi-track subset map, shared timeline, missing-information panel, and ownership/handoff state—not a second dashboard of marketing metrics. This monograph does not reproduce offensive employment doctrines; it restricts itself to defensive sensing and category-level intent recording.

### 2.8 Gap this monograph fills

Prior SA and automation literature rarely specifies an *end-to-end epistemic layering contract* for modern ML-assisted multi-sensor consoles with explicit product screen IDs, fail-closed decision APIs, and anti-effector UX constraints. Product documentation for Counter-Swarm Defence states the rules; this monograph supplies the research scaffolding, evaluation programme, and engineering bridge at monograph depth.

---

## 3. Problem Formulation for Counter-Swarm Operator C2

### 3.1 Problem restatement

An operator (or commander) must maintain a continuously updated understanding of airborne objects in a defended volume, triage alerts, investigate evidence, optionally coordinate multi-track incidents, and record an authorised response category—while remaining aware of sensing and system integrity. The system accelerates perception and recommendation; the human remains the accountable decision authority for categories that may trigger external handoff.

### 3.2 Actors and roles

| Role | Primary screens | Authority emphasis |
|---|---|---|
| Security operator | X01, X02, X03, X04 | Triage, evidence, routine categories |
| Sensor operator | X01, X05 | Coverage and adapter integrity |
| Commander | I01, I02/X04, X07/R01 | Multi-track incidents, high-tier categories |
| Analyst | X06, X07 | Audit, replay, after-action |
| Admin / instructor | A01–A04, S01 (lab) | Policy, adapters, simulation (not ops path) |

### 3.3 Formal objects (UI-facing)

Let the operational state at time \(t\) include:

- Observations \(O_t\) — normalised sensing facts with sensor ID, quality, timestamp.
- Detections \(D_t\) — sensor-native or model detections with scores and model versions.
- Tracks \(T_t\) — estimated objects with kinematics, quality, lifecycle state.
- Behaviour indicators \(B_t\) — pattern signals over track sets (indicators, not verdicts).
- Risk assessments \(R_t\) — graded judgements with factors, missing information, policy/model versions.
- Alerts \(A_t\) — prioritised attention requests with tiers and policy IDs.
- Recommendations \(C_t\) — suggested categories bound to policy.
- Decisions \(\Delta_t\) — human-authorised categories with actor, rationale, idempotency key.
- Incidents \(I_t\) — multi-track containers with ownership and state.
- Health \(H_t\) — sensor and platform integrity, bus lag, model route status.

**Epistemic constraint:** The UI must not present elements of \(D_t\), \(B_t\), \(R_t\), or \(C_t\) using the visual grammar reserved for \(O_t\) or \(\Delta_t\).

### 3.4 Decision space (categories only)

Authorised categories (illustrative product enum):

- `DISMISS`
- `HEIGHTEN_MONITORING`
- `CUE_SENSOR`
- `NOTIFY_EXTERNAL`
- `REQUEST_ESCALATION`
- `OPEN_INCIDENT`

**Non-decision:** No category may be labelled or styled as arm, fire, engage, jam, or electronic attack. X04 always displays an explicit non-weapon notice.

### 3.5 Workflow as a human-centred loop

```
MONITOR (X01)
   │
   ├─► DETECT anomaly / new track / sensor fault
   │         │
   │         ▼
   │    TRIAGE (X01 + X02)
   │         │
   │         ├─► ACK / DISMISS (low)
   │         │
   │         └─► INVESTIGATE (X03)
   │                   │
   │                   ▼
   │         ASSESS risk + missing info
   │                   │
   │         ┌─────────┴─────────┐
   │         ▼                   ▼
   │    CONTINUE MONITOR    OPEN / JOIN INCIDENT (I01)
   │         │                   │
   │         └─────────┬─────────┘
   │                   ▼
   │         HUMAN DECISION (X04 / I02)
   │                   │
   │                   ▼
   │         OPTIONAL EXTERNAL HANDOFF (status only)
   │                   │
   │                   ▼
   │              AUDIT (X06) + OUTCOME
   └───────────────────┘
```

### 3.6 Success criteria (operational)

Success is not “fastest click.” Success is:

1. Operator can state, in own words, what is observed vs inferred within a time bound (e.g., 30–60 s for J1 trials).
2. Commander decisions on I01 cite evidence and acknowledge missing information.
3. Degraded coverage is visible on X01 without opening X05.
4. Decision recording fails closed when audit/IAM is unavailable (G02-D4).
5. No interface path that looks like effector control exists in OPS builds.

### 3.7 Ambiguities and open assumptions

| Ambiguity | Why it matters | HF implication |
|---|---|---|
| Auto-open vs manual incidents | Entry volume into I01 | Auto-open raises commander load; needs stronger triage and ownership UI |
| Dual-control thresholds | Latency vs safety | Dual-control reduces misuse, increases decision latency |
| Assistant enablement | Trust calibration | X08 must be hideable (D6) without breaking core path |
| Sound for T3 | Interrupt value vs fatigue | Policy-gated; evaluate with alert rate meters |

If assumptions exceed facts in a deployment, the correct research posture is to instrument these as experimental factors, not to hard-code a single doctrine into the UI metaphor.

### 3.8 Threats to the human–system team (non-cyber framing)

From a human-factors perspective, primary threats include:

- **Epistemic collapse:** Inference displayed as fact.
- **Alert storm:** Tier inflation and duplicate alerts.
- **Split-brain selection:** Panels showing different track IDs.
- **Automation misuse:** Accepting recommendations without evidence glance.
- **Silent degradation:** Coverage loss hidden until decision error.
- **Authority leakage:** Assistant or policy auto-committing categories.

Cyber and adversarial threats to the platform are treated in separate security documentation; this monograph focuses on cognitive and interface failure modes (Section 9).

---

## 4. Theoretical Framework

### 4.1 Endsley SA mapped to epistemic layers

| SA level | Endsley definition | Epistemic layer | Primary screens |
|---|---|---|---|
| L1 Perception | Elements in time/space | Observation; track kinematics; sensor hits | X01 map, X03 obs list, X05 |
| L2 Comprehension | Meaning of elements | Inference (class distributions, fusion), behaviour indicators, risk factors | X02, X03, I01 summary |
| L3 Projection | Near-future status | Prediction envelopes; coordination hypotheses (labelled) | X01 Predict layer, X03 prediction strip |
| Decision (post-SA) | Selection of action | Recommendation (policy) vs Decision (human) | X04, I02 |
| Performance | Outcome | Handoff status, audit, AAR | X06, X07, R01 |

**Design theorem (informal):** An interface that visually merges L1–L3 into a single “threat” glyph systematically reduces the operator’s ability to answer SAGAT probes about sensors involved, missing modalities, and confidence provenance.

### 4.2 Attention and the map-as-truth-surface principle

Wickens’ proximity compatibility principle supports placing spatially meaningful objects on a spatial display. The Counter-Swarm Defence console therefore treats the map as the primary workspace (X01), with lists as triage instruments rather than replacements. Selection is singular: one selected track/incident synchronises panels, preventing split attention across contradictory foci.

### 4.3 Alert fatigue model

Define an operator’s alert value function roughly as:

\[
V(a) = P(\text{actionable} \mid a) \cdot U(\text{correct attention}) - C(\text{interrupt})
\]

Tiering approximates \(P(\text{actionable})\). Duplicate suppression and per-track collapse reduce interrupt cost for correlated alerts. Quiet mode for T1 reduces low-value interrupts. Rate meters make \(C(\text{interrupt})\) visible to admins when storms occur—supporting Bainbridge’s point that operators must remain aware of automation’s residual behaviour under stress.

### 4.4 Automation trust and Parasuraman–Riley modes

| Mode | Manifestation in this product | Mitigation |
|---|---|---|
| Misuse | Treating UAV \(p=0.72\) as confirmed | Inference badges; class *distributions*; forbid green “truth” checks on model labels |
| Disuse | Ignoring recommendations under storm | Stable policy chips; evidence one-click; Simplify mode |
| Abuse | Designer language “AI confirmed”; assistant commits decisions | Microcopy rules; X08 cannot submit decisions; citations required |

Lee and See’s calibrated trust requires that confidence displays track actual capability—including explicit confidence *ceilings* when coverage is degraded (G02-D1).

### 4.5 Human–machine teaming contract

Klein et al. (2004) argue that effective team players make their status and intentions observable. Translating to product:

1. **Observability:** Model version, policy ID, missing info, handoff state always visible where recommendations appear.
2. **Directability:** Recommendations pre-select in X04 but remain changeable.
3. **Predictability:** Density modes and alert tiers behave consistently; degraded modes are named (D1–D6).
4. **Authority:** Only humans record \(\Delta\); dual-control when policy requires.

### 4.6 Resilience under surprise

Hollnagel and Woods emphasise that systems must support operators when the unexpected occurs—sensor loss, contradictory evidence, integration failure. The product’s conflict flags (CLASS_CONFLICT, ASSOC_AMBIGUOUS), coasting track states, and handoff FAILED/DLQ visibility are resilience mechanisms: they keep surprise *representable* rather than smoothed away.

### 4.7 Synthesis: epistemic honesty as the governing principle

Epistemic honesty is the product’s translation of SA theory + trust calibration + HMT observability into UI law:

> Inference never wears the clothes of fact.

All subsequent design method sections instantiate this principle across X01–X08 and I01.

---

## 5. Design Method: The Epistemic UI

### 5.1 Method overview

The design method proceeds as:

1. Identify workflow phases (monitor → triage → investigate → incident → decide → audit).
2. Allocate epistemic layers to regions of each screen.
3. Define visual grammar per layer.
4. Bind microcopy to anti-patterns (no effector language).
5. Specify loading/empty/error/degraded states.
6. Validate with SA probes and misuse checks before visual polish.

### 5.2 The five-layer stack

Every detail view (especially X02, X03, I01 summary) stacks:

```
=== OBSERVATION ===     measured / reported
=== INFERENCE ===       model or fusion judgement
=== PREDICTION ===      forward envelope + assumptions
=== RECOMMENDATION ===  policy suggestion (not executed)
=== DECISION ===        human record (or Pending)
```

These are information-architecture categories, not optional styling.

### 5.3 Visual grammar (intent-level)

| Layer | Visual treatment | Example copy |
|---|---|---|
| Observation | Solid, neutral, “measured” | “Obs from RDR-1 at 12:01:02Z” |
| Inference | Hatched / badge “INFERENCE” | “Class UAV p=0.72 (det-v3.2)” |
| Prediction | Dashed geometry on map | “60s envelope (kinematic)” |
| Recommendation | Policy chip | “Rec: HEIGHTEN_MONITORING (P-12)” |
| Decision | High-contrast stamp + actor | “Decided by j.smith 12:04:11Z” |

**Forbidden:** green checkmarks on model class labels implying ground truth; “AI confirmed threat” banners.

### 5.4 Screen-by-screen epistemic binding

#### 5.4.1 X01 — Operator monitor console

**Job:** Continuous air picture + triage.  
**Epistemic duties:** Map shows tracks and optional uncertainty/prediction layers; risk/action panel shows risk band, missing info, and recommendation for the *single* selection; health pills expose degrade-in-public state.

ASCII reference (product wireframe WF-X01):

```
+==============================================================================+
| COUNTER-SWARM   Site:ALPHA   Mode:MONITOR   op_j.smith   (SYS OK) (SENS 3/4) |
+==============================================================================+
| MAP  [coverage hatch] [uncertainty] [selected track]                         |
| layers:[Tracks][Uncertainty][FOV][Obs][Predict]   [Simplify] [Fit]          |
+------------------+---------------------------+-------------------------------+
| ALERTS           | ACTIVE TRACKS             | RISK / NEXT ACTION            |
| T3 / T2 / T1     | id  class?  p   quality   | Risk + Missing + Rec + Decide |
+------------------+---------------------------+-------------------------------+
| TIMELINE | SENSORS | SYSTEM | AUDIT | ASSISTANT                              |
+==============================================================================+
```

#### 5.4.2 X02 — Alert detail

**Job:** Why this alert, linked objects, next actions.  
**Epistemic duties:** Full five-layer strip; policy ID and tier rationale mandatory; one-click to X03 or I01.

#### 5.4.3 X03 — Track detail / evidence

**Job:** Full evidence pack for one track.  
**Epistemic duties:** Class as *distribution*, not hard label; evidence graph obs→det→track→behaviour?→risk; conflict strip; decision pending vs recorded.

#### 5.4.4 X04 — Record decision

**Job:** Commit authorised category with rationale.  
**Epistemic duties:** Recommendation pre-selected but changeable; rationale required for T2+; non-weapon notice always visible; button label **Record decision** only; dual-control lane when required; blocked under D4.

#### 5.4.5 X05 — Sensor & system health

**Job:** Integrity of sensing and platform.  
**Epistemic duties:** Distinguish sensor DOWN from model route DEGRADED; coverage map hatch; last-obs ages—feeding L1 SA about *whether the picture can be trusted*.

#### 5.4.6 X06 — Audit history

**Job:** Accountable history.  
**Epistemic duties:** Show decision, recommendation, risk, track events with model versions and digests—supporting after-the-fact comprehension and organisational learning.

#### 5.4.7 X07 — Timeline replay

**Job:** Time-scrubbed reconstruction.  
**Epistemic duties:** Historical map frozen to scrub time; event ticks for obs/risk/decision—enabling Level 3 learning and AAR without live pressure.

#### 5.4.8 X08 — Assistant drawer

**Job:** Grounded Q&A via allowlisted tools.  
**Epistemic duties:** Citations required; cannot submit decisions; unavailable/tool-denied states explicit; hideable when policy disables assistant (D6). Core path must work with X08 absent.

#### 5.4.9 I01 — Incident workspace

**Job:** Multi-track coordinated event handling.  
**Epistemic duties:** Map subset of member tracks; summary of risk, behaviour *indicators*, missing info, recommendation; shared timeline; participants/handoff; decide/transfer/close. Commander must not treat swarm score as confirmed fact (J2 failure mode).

### 5.5 Microcopy principles (operational)

| Prefer | Avoid |
|---|---|
| Elevated risk (model/policy) | Threat confirmed |
| Authorised category | Engage / Fire / Jam |
| Inference (near model outputs) | AI verified |
| Coverage reduced | Silent loss |
| Record decision | Launch / Execute effect |

### 5.6 Progressive disclosure

Summary first on X01 risk panel; evidence on demand in X03; raw observations and FOV default off on map layers. Progressive disclosure protects attention resources (Wickens) while preserving deep evidence for investigation.

### 5.7 Calm urgency

T3 is assertive (sticky until ack optional by policy), not theatrical. Continuous glow pulses are rejected (noise + accessibility risk). Motion limited to purposeful transitions: alert insert, selection focus, degraded banner.

### 5.8 Design method checklist (gate before engineering)

- [ ] Observation vs inference separable in X02/X03  
- [ ] No fire/effector language in X04  
- [ ] Degraded coverage visible on X01 without opening health  
- [ ] Decision blocked path shown when audit/IAM down  
- [ ] Assistant optional; citations required  
- [ ] Class shown as distribution on X03  
- [ ] Single selection bus across X01 panels  

---

## 6. Reference Architecture for the Console

### 6.1 Architectural goals

1. Map-first shell with deterministic selection bus.
2. Projection APIs that preserve epistemic types end-to-end.
3. Decision service that is idempotent, RBAC-enforced, and fail-closed.
4. Health and degraded modes as first-class UI state (G02).
5. Assistant off the critical path.

### 6.2 Logical architecture

```
                    ┌─────────────────────────────────────┐
                    │           OPS SHELL (SPA)            │
                    │  Brand | Site | Mode | User | Pills  │
                    └─────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          ▼                           ▼                           ▼
   ┌─────────────┐            ┌─────────────┐            ┌─────────────┐
   │  X01 Monitor │◄──select──►│ X02 / X03   │            │ I01 Incident│
   │  map+panels  │            │ drawers     │            │ workspace   │
   └──────┬───────┘            └──────┬──────┘            └──────┬──────┘
          │                           │                           │
          └─────────────┬─────────────┴─────────────┬─────────────┘
                        ▼                           ▼
                 ┌─────────────┐             ┌─────────────┐
                 │ X04 Decide  │             │ X08 Assist* │
                 │ modal       │             │ optional    │
                 └──────┬──────┘             └─────────────┘
                        │
                        ▼
        ┌───────────────────────────────────────────────┐
        │              PLATFORM SERVICES                 │
        │  Tracks | Alerts | Risk | Policy | Decision    │
        │  Health | Audit | Replay | Handoff Outbox      │
        └───────────────────────────────────────────────┘
```

\*X08 uses allowlisted read tools only; never decision write APIs.

### 6.3 Selection bus contract

```
selected_entity := { type: track|incident|alert|none, id: string }
```

Rules:

1. Exactly one primary selection.
2. X01 panels, X02/X03 drawers, and map highlight bind to it.
3. Deep link `/tracks/T-104` opens X01+X03 pattern with that selection.
4. Changing selection must not reset map pan/zoom unexpectedly (annotation from screen inventory).

### 6.4 Epistemic DTO sketch

```
EvidencePack {
  observations: Observation[]      // layer 1
  inferences: {
    class_distribution: {label, p}[]
    model_version: string
    fusion_contributors: id[]
    conflicts: ConflictFlag[]
  }
  prediction: {
    envelope: Geometry
    assumptions: string[]
  }
  recommendation: {
    category: Category
    policy_id: string
    policy_version: string
    factors: string[]
    executed: false
  }
  decision: Decision | Pending
}
```

Engineering must not flatten this into a single `threat_level` field for UI consumption without retaining provenance fields.

### 6.5 Degraded mode architecture (G02)

| Mode | Banner intent | UI effect |
|---|---|---|
| D1 Coverage reduced | Sensing coverage reduced — track confidence capped | Map hatch |
| D2 Model degraded | Detection model unavailable — sensor-native only | Badge on inferences |
| D3 Stale picture | Event lag {n}s — picture may be stale | Dim live indicators |
| D4 Decision freeze | Decisions unavailable — view only | Disable Decide |
| D5 Integration offline | External handoff unavailable | Handoff status only |
| D6 Assistant off | Assistant disabled by policy | Hide X08 |

Degraded modes are chrome-visible, not toast-only—supporting Endsley L1 about system elements and Lee–See trust calibration.

### 6.6 Decision and handoff state machine

```
RECOMMENDATION_SHOWN → DECISION_RECORDED → HANDOFF_QUEUED
  → HANDOFF_ACKED | HANDOFF_FAILED | HANDOFF_NOT_REQUIRED
```

UI must show handoff status distinctly from decision validity: a FAILED handoff does not erase a recorded decision; operators see retry/DLQ paths without re-metaphorising as weapon recycle.

### 6.7 Security-relevant UX constraints (HF view)

- No data leakage in G03 access-denied bodies.
- Export on X06 role-gated.
- Lab screens (S01) carry LAB badge and are build-flagged out of OPS.
- Dual-control UI shows who is waiting (I02).

### 6.8 Non-architecture: what must not exist

```
[FORBIDDEN IN OPS CONSOLE]
- Aimpoint widgets
- Fire / arm / safe toggles
- Jam frequency / power controls
- "Engage swarm" one-click macros
- Assistant tools that POST /decisions
```

If a customer’s external system later consumes categories, that integration is outside the operator console’s visual language.

---

## 7. Implementation Guidance: Wireframes to Engineering

### 7.1 Translation principles

1. Wireframe regions become layout landmarks with stable test IDs.
2. Epistemic strips become shared components with enforced variants.
3. Category enums are shared between policy engine and X04.
4. Every fetchable view implements loading / loaded / empty / error (screen inventory rule).
5. Visual tokens follow operational night-console intent—not marketing SaaS clichés.

### 7.2 Component inventory (suggested)

| Component | Used by | Notes |
|---|---|---|
| `EpistemicStack` | X02, X03, I01 | Five sections; inference hatched |
| `AlertRow` | X01, X02 | Tier icon+label (not colour alone) |
| `TrackListItem` | X01 | Quality + class hypothesis + coasting |
| `RiskActionPanel` | X01, I01 | Missing info + Rec + Decide |
| `DecisionModal` | X04, I02 | Non-weapon notice; rationale rules |
| `HealthPills` | Shell | Sensor count + SYS |
| `CoverageHatch` | X01 map, X05 | D1 visualisation |
| `EvidenceGraph` | X03 | Obs–det–track links |
| `AuditTable` | X06 | Filters + digest pane |
| `ReplayScrubber` | X07 | Obs/risk/decision ticks |
| `AssistantDrawer` | X08 | Citations; no decide |

### 7.3 State matrix excerpt (X04)

| State | UI behaviour |
|---|---|
| editing | Category selectable; rationale validated |
| submitting | Controls locked; idempotency key held |
| success | Decision id + handoff module |
| error | Generic user message; detail logged server-side |
| blocked (D4) | Decide disabled; banner explains view-only |
| validation | Rationale required for T2+/incident |

### 7.4 Accessibility implementation notes

- WCAG 2.2 AA contrast for text/chips.
- Tier not by colour alone (icons + text).
- Keyboard: acknowledge, open evidence, open decide; `Esc` closes drawers.
- `prefers-reduced-motion` disables non-essential motion.
- Screen reader labels must say “inference” explicitly where badges appear visually.

### 7.5 Testing hooks for HF evaluation

Expose non-production evaluation harness flags (lab/staging):

- Freeze clock for SAGAT probes.
- Event markers for alert onset, evidence open, decision commit.
- Workload self-report prompts (NASA-TLX) at scenario end.
- Ground-truth overlay for instructors only (S01)—never in OPS.

### 7.6 Anti-patterns to reject in code review

- Mapping `class_argmax` to a green check icon.
- Default-on prediction clutter without toggle.
- Toast-only presentation of D1–D4.
- Primary button strings containing Engage/Fire/Jam/Launch.
- Shared mutable selection without a single store/bus.
- Assistant markdown that omits citations.

### 7.7 Worked engineering story: J1 unknown object

1. Alert appears on X01 within NFR latency (~1–2 s of risk update).
2. Operator selects alert → X02 opens with epistemic stack.
3. Operator opens track → X03 evidence graph.
4. Operator chooses `CUE_SENSOR` → X04 records with rationale.
5. Audit row written with model version and evidence count.
6. HF success: operator can verbalise observation vs inference.

### 7.8 Worked engineering story: J2 suspected swarm

1. Behaviour indicators on T-104, T-105, T-109 → T3 + incident I-22.
2. Commander opens I01; sees missing RF on one track.
3. Optional X08 summary with citations—not required.
4. Dual-control `NOTIFY_EXTERNAL` via I02/X04 pattern.
5. Handoff ACKED; audit chain complete.
6. HF failure to avoid: treating swarm indicator as confirmed coordination fact.

---

## 8. Trade-offs

### 8.1 Epistemic separation vs speed

**Gain:** Better SA, fewer misuse errors, audit clarity.  
**Loss:** Extra visual structure; slightly longer first glance.  
**Later hardness:** Retrofitting epistemic types after shipping flattened threat scores is costly (data model + training).  
**Risk:** Teams under schedule pressure “temporarily” merge layers—becomes permanent.

**Recommendation:** Keep separation as a non-negotiable P0.

### 8.2 Map-first vs list-first

**Gain:** Spatial integration for multi-track events.  
**Loss:** Harder on small screens; mobile deferred to P2.  
**Risk:** Card-soup dashboards creep into first viewport.

**Recommendation:** Preserve map-first for OPS desktop; constrained layouts only if CONOPS demands handheld.

### 8.3 Rich recommendations vs operator autonomy

**Gain:** Faster category selection, policy consistency.  
**Loss:** Anchoring bias toward pre-selected category.  
**Mitigation:** Pre-select but require explicit confirm; rationale for T2+; training on override.

### 8.4 Auto-open incidents vs manual open

**Gain:** Faster commander attention on coordination indicators.  
**Loss:** I01 entry volume; alarm fatigue at incident level.  
**Evaluation:** A/B in lab with false-positive behaviour indicators.

### 8.5 Dual-control vs tempo

**Gain:** Reduced abuse and single-actor error on high-impact categories.  
**Loss:** Added latency; waiting-state complexity.  
**Recommendation:** Policy-scoped; UI must make waiting party visible.

### 8.6 Assistant (X08) on vs off critical path

**Gain:** Faster narrative synthesis under load.  
**Loss:** New misuse channel; citation failures; availability coupling.  
**Recommendation:** Default off critical path; D6 hide; never write decisions.

### 8.7 Simplify mode vs completeness

**Gain:** Attention protection under swarm load.  
**Loss:** Hidden low-tier objects may matter later.  
**Mitigation:** Clear mode badge; easy exit; audit still complete.

### 8.8 Transparency depth vs clutter

Showing all fusion contributors always can overwhelm. Progressive disclosure (summary → X03 graph) is the managed trade-off, aligned with Wickens’ clutter findings.

---

## 9. Failure Modes / What Goes Wrong

### 9.1 Cognitive failure modes

| ID | Failure | Mechanism | Detection | Design response |
|---|---|---|---|---|
| F1 | Inference→fact confusion | Visual/linguistic collapse | SAGAT L1/L2 probes | EpistemicStack enforcement |
| F2 | Alert desensitisation | High false/low-value rate | Ack latency↑, miss rate↑ | Tier hygiene, suppression, quiet T1 |
| F3 | Anchoring on recommendation | Pre-select + time pressure | Override rate anomalously low | Training; rationale; show factors/missing |
| F4 | Split-brain panels | Multiple selections | Conflicting IDs in usability tests | Single selection bus |
| F5 | Missed coverage loss | Toast-only health | Decisions under D1 without awareness | Chrome pills + hatch |
| F6 | Swarm-score reification | Behaviour indicator as truth | Commander verbal reports | “Indicator” language; missing-info panel |
| F7 | Automation disuse | Storm + distrust | Ignore all Rec | Simplify; rate meter; policy retune |
| F8 | Assistant overtrust | Fluent uncited answers | Citation audit fails | Tool-deny; require citations; hide X08 |

### 9.2 Workflow failure modes

| ID | Failure | Notes |
|---|---|---|
| W1 | Decision recorded, handoff failed | Decision remains valid; show FAILED/DLQ |
| W2 | Audit/IAM down | Fail closed (D4); view-only |
| W3 | Contradictory evidence auto-resolved wrongly | Prefer conflict flags over forced merge |
| W4 | Coasting track treated as live certainty | Quality/coast badges on X01/X03 |
| W5 | Close incident without decision | Restricted + audited reason path only |

### 9.3 Ironies realised

If detection models are highly accurate in lab but brittle in novel swarm geometries, operators may misuse automation in familiar regimes and disuse it in novel ones—exactly Bainbridge’s irony. Training and replay (X07) are mitigations: keep humans practised at evidence reading, not only score reading.

### 9.4 Organisational failure modes

- Managers measuring “mean time to decide” without measuring decision *appropriateness* → rewards reckless speed.
- Policy authors inflating T3 → chronic fatigue.
- Enabling X08 in OPS without citation telemetry → uncorrectable misuse.

### 9.5 Explicit safety boundary failures (design)

Any PR that introduces effector-like controls into X04/I01 is a product-safety defect, not a feature request. Review checklists must include language and affordance scans.

---

## 10. Evaluation and Proof

### 10.1 Evaluation goals

Demonstrate that the epistemic UI improves (a) situation awareness, (b) calibrated trust, (c) decision quality/accountability, and (d) manageable workload relative to a fused baseline UI that presents single “threat confirmed” labels.

### 10.2 Hypotheses

- **H1:** Operators using epistemic strips achieve higher SAGAT accuracy on sensor involvement and confidence provenance than baseline.
- **H2:** Under degraded coverage (D1), epistemic UI users more often correctly report capability loss before deciding.
- **H3:** Recommendation override rates fall in a healthy band (neither ~0% misuse nor ~100% disuse) when factors and missing info are shown.
- **H4:** NASA-TLX global workload under swarm scenarios is not significantly worse than baseline *given* Simplify mode, while miss rates improve.
- **H5:** X08-off does not degrade primary decision quality on J1/J2 (assistant non-critical).

### 10.3 Metrics

| Metric | Definition | Collection |
|---|---|---|
| SA-L1 accuracy | % correct probes on obs/sensors present | SAGAT freeze |
| SA-L2 accuracy | % correct on risk factors / conflicts | SAGAT |
| SA-L3 accuracy | % correct on short-horizon projection | SAGAT |
| Time-to-evidence | Alert onset → X03/I01 open | Instrumentation |
| Time-to-decision | Alert/incident → recorded decision | Instrumentation |
| Decision appropriateness | Expert-coded vs scenario key | Blind scoring |
| Rationale quality | Rubric: cites evidence / missing info | Expert coding |
| Override rate | Human category ≠ recommendation | Logs |
| Missed T3 rate | Unacked T3 beyond threshold | Logs |
| Coverage awareness | Correct D1 report before decide | Probe + logs |
| NASA-TLX | Subjective workload | Post-scenario |
| Trust calibration | Self-report vs actual model accuracy | Lee–See style items |
| Citation compliance | X08 answers with valid entity cites | Logs (if on) |

### 10.4 SAGAT-style protocol

**Setting:** Lab with S01 simulation director; instructor truth overlay hidden from participants.

**Procedure:**

1. Train participants on epistemic grammar (15–20 min).
2. Run scenario blocks: (A) single unknown object J1; (B) suspected coordination J2; (C) sensor degradation J3; (D) alert storm.
3. At freezes (2–3 per scenario), blank the UI and administer probes, e.g.:
   - Which sensors contributed observations to the selected track in the last 10 s?
   - Is the class label observation or inference?
   - What information is marked missing?
   - Is coverage degraded? Which sector?
   - What recommendation is showing, and which policy ID?
4. Resume scenario; complete decision tasks.
5. Administer NASA-TLX and trust items.
6. Debrief for language/affordance confusion (effector metaphors).

**Scoring:** Compare epistemic UI vs baseline fused UI within subjects (counterbalanced) or between subjects (larger N).

### 10.5 Workload protocol

Use NASA-TLX dimensions: mental demand, temporal demand, effort, performance, frustration, physical demand (Hart & Staveland, 1988). Pair with behavioural spare-capacity checks if feasible (e.g., secondary detection of a planted low-tier cue).

### 10.6 Alert fatigue protocol

Manipulate false-advisory rate and duplicate bursts. Outcomes: ack latency, suppression usage, Simplify usage, missed critical alerts. Validate fatigue controls (duplicate badges, quiet T1).

### 10.7 Misuse / disuse / abuse checklist (Parasuraman & Riley)

| Check | Pass criterion |
|---|---|
| Misuse | Participants distinguish inference in ≥ target % probes |
| Disuse | Under calibrated recommendations, useful Rec not ignored wholesale |
| Abuse | No participant interprets X04 as weapon control; copy review clean |

### 10.8 Sample size and analysis (guidance)

Exact power depends on effect sizes from pilot. Pilot 6–8 operators; estimate variance on SA-L1; then power for primary H1. Analyse with mixed models if repeated scenarios; pre-register primary endpoints where organisationally possible.

### 10.9 Operational proof (post-deployment)

Shadow metrics in OPS (no experiment freeze): override rates, D1-aware decisions (banner dwell + decide), handoff failure handling, audit completeness, X08 citation compliance. Couple with periodic replay-based training exams on X07.

### 10.10 What counts as “proof” for this product

Proof is *not* model mAP alone. Proof is joint cognitive performance: humans + console produce accountable, epistemically coherent decisions under load and degradation, without effector-metaphor errors.

---

## 11. Build Guide (Stepwise)

### 11.1 Stage A — Contracts

1. Freeze category enum and non-weapon notice text.
2. Define EvidencePack / Alert / Incident DTOs with epistemic fields.
3. Define G02 degraded mode event schema.
4. Define decision API: RBAC, idempotency, fail-closed behaviour.
5. Author: Victor.I — record decisions in architecture ADRs.

### 11.2 Stage B — Shell and X01 skeleton

1. Implement OPS shell with health pills.
2. Map canvas with track layer + selection.
3. Alerts list, tracks list, risk/action panel wired to selection bus.
4. Simplify toggle.
5. Bottom dock placeholders (Timeline/Sensors/System/Audit/Assistant).

### 11.3 Stage C — Epistemic components

1. Ship `EpistemicStack` with visual variants.
2. Apply to X02 and X03.
3. Evidence graph for X03.
4. Class distribution display (no hard checkmark).

### 11.4 Stage D — Decision path

1. X04 modal with categories, rationale rules, notice.
2. Dual-control lane (I02) behind policy flag.
3. Handoff status module.
4. Block Decide under D4; verify with chaos test (audit down).

### 11.5 Stage E — Health and degrade-in-public

1. X05 sensor/platform panels.
2. Coverage hatch on X01 for D1.
3. D2–D6 banners per inventory.
4. Ensure degrade visible without opening X05.

### 11.6 Stage F — Incidents

1. I01 workspace regions: map subset, summary, timeline, people, handoff.
2. Incident list entry points.
3. Auto-open behind feature flag; evaluate before defaulting OPS on.

### 11.7 Stage G — Audit and replay

1. X06 filters + digest.
2. X07 scrubber with event ticks.
3. Export role gates.

### 11.8 Stage H — Assistant (optional)

1. X08 drawer with allowlisted tools.
2. Citation UI mandatory.
3. Hard deny decision tools.
4. D6 hides drawer; confirm J1/J2 without assistant.

### 11.9 Stage I — Lab evaluation harness

1. S01 scenario controls; LAB badge.
2. Freeze + probe overlay for SAGAT.
3. Instrumentation for metrics in Section 10.
4. Instructor truth overlay permissioned.

### 11.10 Stage J — HF gate before OPS harden

Pass checklist in Section 5.8 and abuse checklist in Section 10.7. No effector language. No silent degrade. Epistemic separation intact.

### 11.11 Suggested milestone ASCII

```
A contracts ──► B X01 ──► C epistemic ──► D X04
                              │
                              ▼
                         E health/D-modes
                              │
                              ▼
                         F I01 ──► G audit/replay
                              │
                              ▼
                         H X08 optional ──► I lab harness ──► J HF gate
```

---

## 12. Discussion

### 12.1 Returning to the research questions

**RQ1:** The five-layer epistemic stack, bound to Endsley L1–L3 and post-SA decision, provides a coherent representation strategy. Its force comes from making layer membership *legible*—not from adding more data.

**RQ2:** The map-first shell with a single selection bus, drawers for X02/X03, modal X04, chrome health, and I01 as multi-track coordination space forms a reference architecture that matches the human-centred workflow without inventing parallel control paths.

**RQ3:** Tiered alerts, suppression, quiet modes, changeable recommendations, and a non-critical, citation-bound assistant operationalise Parasuraman and Riley’s warnings and Lee and See’s calibrated trust.

**RQ4:** SAGAT-style probes, workload indices, override metrics, and abuse checklists constitute a proof programme aligned to joint cognitive performance rather than model accuracy alone.

### 12.2 Implications for ML engineering

Models should emit distributions, versions, and abstentions that UI can render. Point labels without provenance actively harm SA. Behaviour models should be named as indicators. Risk engines should emit missing-information fields as first-class outputs—the UI already depends on them.

### 12.3 Implications for policy authors

Every T3 must earn its tier. Policy IDs visible in X02/X04 create accountability loops between operators and policy designers. Dual-control thresholds should be evaluated for tempo impact.

### 12.4 Limitations

This monograph is grounded in product design artefacts and established HF literature; it is not a completed empirical trial. Effect sizes for H1–H5 remain to be measured. Cultural and organisational factors in live defence enterprises may dominate UI effects. Mobile C2 is intentionally under-specified.

### 12.5 Ethical and legal posture

Recording categories that notify external systems still carries organisational and legal weight. Epistemic honesty and auditability are ethical controls: they reduce the chance that fluent automation language launders uncertainty into false certainty. The exclusion of effector UI is both a safety boundary and an ethical scoping choice for this research programme.

### 12.6 Future research

- Adaptive alerting that optimises \(V(a)\) online under operator state estimates (with privacy care).
- Empirical comparison of auto-open vs manual incidents.
- Gaze-aware declutter (research only; OPS caution).
- Cross-competency training effects of X07 replay exams.
- Formal verification of UI state machines against D4 fail-closed properties.

### 12.7 Pre-ship gate (governing constitution style)

| Question | Answer | Justification |
|---|---|---|
| Understand failure modes? | YES | Section 9 catalogue |
| Observable in prod? | YES | Metrics in 10.9 |
| Safe rollback? | YES | Feature flags for auto-open, X08; categories stable |
| Complexity proportional? | YES if epistemic components reused | Avoid one-off screen logic |
| Want 3-year ownership? | YES if effector UI remains forbidden and tests guard grammar | Drift toward fused scores would reverse |

---

## 13. Conclusion

Counter-swarm defensive decision support succeeds when humans remain correctly sceptical and correctly fast. The Counter-Swarm Defence Platform’s screens X01–X08 and I01 instantiate an epistemic interface: observations, inferences, predictions, recommendations, and decisions are separable; the map is the truth surface; degradation is public; decisions are human-recorded categories with audit trails; and no faux effector affordance exists in the operator path.

This monograph has formulated that problem, grounded it in Endsley’s SA theory, automation trust and irony literatures, and HMT principles, and translated it into architecture, implementation guidance, trade-offs, failure modes, evaluation protocols, and a stepwise build guide. The research claim is modest but firm: without epistemic honesty, faster models make faster mistakes look like facts. With it, the console can support accountable C2 under swarm pressure—defensively, and only defensively.

---



---

## Supplement S1 — Extended Related Work and Positioning (Continues Section 2)

### S1.1 Measurement traditions for SA

Beyond definitional theory, Endsley’s programme insisted that SA is measurable independently of decision outcome (Endsley, 1995; Endsley & Garland, 2000). SAGAT’s freeze–probe method trades ecological continuity for query control: the simulation pauses, displays blank, and operators answer queries about the world as it was. Alternative methods include real-time probes (less disruptive, more dual-task load) and observer ratings (scalable, more subjective). For Counter-Swarm Defence evaluation, SAGAT-style freezes are preferred in lab scenarios driven by S01 because the epistemic UI’s value proposition is precisely the operator’s *knowledge state*—whether they know which sensors contributed, whether a class is inferred, and whether coverage is degraded—not merely whether they clicked a category quickly.

SPAM-like approaches (Situation Present Assessment Method) keep the display visible and measure query response time as a workload/SA hybrid. Those can complement SAGAT in later stages when freeze interruptions are operationally unrealistic. The monograph recommends a staged measurement ladder: SAGAT in formative lab evaluation; SPAM-like timed queries in high-fidelity dress rehearsals; shadow telemetry in OPS.

### S1.2 Display design and the proximity compatibility principle in multi-track C2

Wickens and Carswell (1995) formalised the proximity compatibility principle (PCP): if tasks require mental integration of information sources, those sources should be displayed in close perceptual proximity (and often in integral formats); if tasks require separate processing, sources should be separated. Counter-swarm monitoring simultaneously demands both. Spatial integration of tracks, geofences, and uncertainty on X01’s map satisfies PCP for “where are the objects and how uncertain are their positions?” Epistemic *type* discrimination—observation versus inference—requires the opposite: deliberate separation via badges, hatching, and labelled strips on X02/X03. Design failure modes occur when teams apply only one half of PCP: either scattering track data into disconnected cards (hurting spatial SA) or fusing all attributes into one glyph (hurting epistemic SA).

Wickens et al. (2013) further emphasise clutter’s cost to visual search. Prediction envelopes, raw observation dots, and sensor FOV overlays are therefore default-*off* layers on X01, with an explicit Predict toggle when Level 3 projection is task-relevant. Simplify mode is an emergency attention allocation policy, not a permanent impoverishment of the world model: the underlying tracks remain in the system; the display withholds low-tier clutter.

### S1.3 Trust, reliance, and the perfect automation schema

Lee and See (2004) distinguish trust (an attitude) from reliance (a behaviour). Appropriate reliance requires that trust track capability across contexts. Lyons and Guznov (2019) examine individual differences related to beliefs that automation is perfect—schemas that predict misuse when systems are fallible. In ML-assisted classification, a “perfect automation schema” is especially dangerous because softmax outputs look precise. The epistemic UI’s insistence on distributions, model versions, and missing-information fields is a counter-schema intervention: it continuously presents fallibility cues without requiring operators to recall training slogans under stress.

### S1.4 Joint cognitive systems and observability

Woods and Hollnagel (2006) describe joint cognitive systems in which humans and machines co-produce performance. Klein et al. (2004) list challenges for making automation a team player, including observability of status and intentions, directability, and common ground. Mapping those challenges to product screens:

| Team-player challenge | Product manifestation |
|---|---|
| Observability | Model version, policy ID, bus lag, handoff state |
| Directability | Changeable recommendation in X04; layer toggles |
| Predictability | Named degraded modes D1–D6; stable tier meanings |
| Common ground | Shared I01 timeline and notes; selection bus |
| Revealing limits | Conflict flags; confidence ceilings under D1 |

Bainbridge (1983) remains the cautionary tale: if the console hides the work of fusion until failure, operators will be least ready when most needed. X03’s evidence graph and X07 replay exist partly to keep the “how we know” muscle exercised.

### S1.5 Alarm philosophy across domains

Clinical alarm fatigue literature (Cvach, 2012) and earlier emergency signal research (Bliss & Gilson, 1998) converge on a small set of design levers: reduce false alarms, differentiate criticality, provide informative alarm text, and avoid redundant signalling. Counter-Swarm Defence’s alert row anatomy—“[TIER] Reason · link · age · policy id · [Ack]” plus a “why now” secondary line—implements informative signalling. Duplicate suppression (“+12 similar”) attacks redundancy. T0 as log-only prevents advisory noise from becoming interrupt noise. These are not cosmetic; they are the primary defence against Parasuraman and Riley’s disuse (operators silencing everything) and misuse (operators treating every interrupt as equally meaningful).

### S1.6 Recognition-primed decision making and incident workspaces

Klein’s recognition-primed decision (RPD) model (1993) argues that experienced decision makers often recognise situations as exemplars and enact known responses, mentally simulating only when needed. I01 should therefore support recognition: multi-track spatial pattern, behaviour *indicator* chips, missing-info gaps, and prior similar incidents via audit/replay—not a lengthy form wizard. X04’s category set is intentionally small so recognition can map situations to authorised responses without inventing effector parameters.

### S1.7 Positioning relative to “AI cockpit” trends

Contemporary AI product patterns often maximise fluency: chat overlays, single confidence meters, and auto-actions. For defensive C2, fluency without provenance is a hazard. This monograph positions Counter-Swarm Defence against that trend: the optional X08 assistant is tool-bounded and citation-required; the critical path (X01→X03→X04/I01) works with assistant disabled (D6). The research stance is that large language models may summarise allowlisted evidence but must not become an unaccountable decision authority.

### S1.8 Gap analysis (refined)

| Literature cluster | What it gives | What it lacks for this product |
|---|---|---|
| Endsley SA | Levels, measurement | Screen-level epistemic contracts for ML fusion UIs |
| Wickens attention | Clutter, PCP | Swarm multi-track + degrade-in-public chrome patterns |
| Parasuraman & Riley | Misuse/disuse/abuse | Concrete anti-effector UX law for category C2 |
| Bainbridge / Woods | Ironies, resilience | Implementation bridge to fail-closed decision APIs |
| Alarm fatigue | Tiering, false alarms | Binding to policy IDs and behaviour indicators |
| HMT / trust | Observability, calibration | Product IDs X01–X08/I01 and evaluation harness design |

The monograph fills the “lacks” column by binding theory to the Counter-Swarm Defence screen inventory and engineering gates.

---

## Supplement S2 — Formalising Operator C2 as an Epistemic Coordination Problem (Extends Section 3)

### S2.1 Partial observability and missing-information as first-class state

Let \(M_t\) be the set of modalities expected for high-confidence assessment in a site policy (e.g., radar, EO, RF). For track \(\tau\), define missing information:

\[
\text{Missing}(\tau, t) = \{ m \in M_t : \text{no recent qualifying obs from } m \text{ associated to } \tau \}
\]

Risk assessment \(R_t(\tau)\) should widen uncertainty or cap confidence when \(\text{Missing}\) is non-empty, and the UI must surface \(\text{Missing}\) in X01’s risk panel and X03/I01 summaries. Operators cannot be blamed for “not noticing RF absence” if the interface never states it. Journey J2’s worked example—commander sees missing RF on T-109—is exactly this principle in narrative form.

### S2.2 Multi-track hypotheses versus single-object labels

Swarm-suspect assessment is a hypothesis over a *set* of tracks. Behaviour indicators \(B_t(S)\) for set \(S \subseteq T_t\) are evidence *about coordination patterns*, not ontological proof of swarm identity. The problem formulation therefore forbids UI copy that converts \(B_t(S)\) into “swarm confirmed.” I01’s job is to hold set \(S\), shared timeline, and collective missing info while a human records a category.

### S2.3 Utility of categories under organisational constraints

Each category \(c\) has organisational effects \(E(c)\) (attention shift, sensor cueing request, external notification, escalation). The operator maximises expected organisational utility under uncertainty, subject to RBAC and dual-control constraints—not physical effect optimisation. This distinction matters for evaluation: scoring “correctness” requires scenario keys about *appropriate category given evidence and policy*, not about simulated kinetic outcomes.

### S2.4 Timing envelopes and cognitive deadlines

Product timing expectations (alert visible ~1–2 s after risk update; evidence within one interaction; degrade visible in chrome) define cognitive deadlines. Human-factors success is meeting those deadlines *without* epistemic collapse. A system that shows a red “THREAT” in 200 ms but cannot show provenance has failed RQ1 even if it meets latency NFRs.

### S2.5 Explicit non-goals restated as constraints

Constraint C-NO-EFFECTOR: For all screens in OPS builds, no control affords weapon or EA parameterisation.  
Constraint C-HUMAN-DELTA: All \(\Delta_t\) writes require authenticated human actors (and second actor when policy says so).  
Constraint C-FAIL-CLOSED: If audit or IAM unavailable, decision writes are rejected and UI enters D4.  
Constraint C-EPISTEMIC: Inference fields cannot render with observation visual grammar.

These constraints are part of the problem formulation, not afterthoughts.

### S2.6 Personas and failure stories (condensed)

**Security operator (J1):** Needs to explain an unknown track to themselves and supervisors. Failure: reports “UAV confirmed” when UI showed \(p=0.72\) inference.  
**Commander (J2):** Needs set-level judgement. Failure: equates behaviour indicator with hostile swarm fact and notifies externally without noting missing RF.  
**Sensor operator (J3):** Needs coverage truth. Failure: continues high-confidence language while RF sector hatched.  
**Analyst:** Needs replayable causality. Failure: audit lacks model versions, making AAR impossible.

### S2.7 Information flow vs authority flow

```
Information flow (machines dominate):
  sensors → adapters → bus → detect/track/fuse → behaviour → risk → alerts → UI

Authority flow (humans dominate):
  UI evidence → human judgement → category decision → (optional) handoff ack by external org
```

Design errors occur when information-flow components seize authority-flow privileges (auto-decide, assistant POST /decisions, or UI that looks like an effector panel).

---

## Supplement S3 — Deepening the Theoretical Frame (Extends Section 4)

### S3.1 Level 3 projection without false precision

Prediction envelopes must carry assumptions (e.g., constant-velocity kinematics; no mode change). Dashed geometry on X01 communicates tentativeness. Animating envelopes slowly is acceptable when toggled; continuous aggressive animation creates noise and false urgency. Level 3 SA is “what might happen if assumptions hold,” not “the future is known.”

### S3.2 Attention as a scarce resource and tier economics

Every alert spends operator attention. Policy authors are attention economists. The theoretical claim: tier inflation is an organisational failure mode isomorphic to printing too much currency—value collapses. Evaluation must include policy retuning loops using rate meters, not only operator training.

### S3.3 Calibrated trust under non-stationary models

Model routes change (det-v3.2 → det-v3.3). Trust calibration must be version-aware. X02/X03/X06 showing model versions is therefore theoretically required by Lee and See’s framework: capability is not a static trait of “the AI,” but of a specific routed model under specific coverage.

### S3.4 Resilience markers in the UI

Woods (2015) discusses resilience concepts including graceful extensibility. UI markers that support extensibility under surprise:

- Conflict strips instead of silent arbitration.
- Coasting state instead of pretending tracks are equally live.
- Handoff FAILED distinct from decision absence.
- D3 stale-picture dimming when bus lag exceeds threshold.

These markers keep the joint cognitive system adaptable when the world violates training distributions.

### S3.5 HMT authority gradient

```
Low authority automation          High authority automation
(read/recommend)                  (write/actuate)
     |                                    |
  X08 tools, Rec chips ---- X04 human ---- [FORBIDDEN effector]
```

The product occupies the left–centre of this gradient by design. Research on higher authority automation is out of scope and would require a different safety case.

### S3.6 Workload theory and Simplify mode

Hart and Staveland’s NASA-TLX (1988) operationalises subjective workload. Temporal demand spikes in swarm scenarios. Simplify mode is a workload control that trades Level 1 completeness for Level 2 focus on high-tier objects. Theory predicts TLX temporal/mental demand decreases while miss risk for suppressed T1 increases—hence quiet T1 must be a conscious policy choice, and evaluation must measure missed criticality, not only comfort.

### S3.7 Putting it together: a design theory statement

**Proposition 1 (Epistemic legibility):** Interfaces that preserve separable observation/inference/prediction/recommendation/decision representations improve SA probe accuracy on provenance items relative to fused threat labels.  
**Proposition 2 (Degrade publicity):** Chrome-visible degraded modes improve coverage awareness before decision relative to toast-only health.  
**Proposition 3 (Bounded recommendation):** Changeable, policy-identified recommendations improve appropriate reliance versus either no recommendation or auto-committed categories.  
**Proposition 4 (Non-critical assistance):** Removing X08 does not reduce decision appropriateness on core journeys if evidence packs remain intact.  
**Proposition 5 (Anti-effector affordance):** Absence of weapon/EA metaphors reduces authority-misinterpretation errors in usability abuse checks to near zero among trained operators.

These propositions structure Section 10’s hypotheses.

---

## Supplement S4 — Design Patterns Catalogue (Extends Section 5)

### S4.1 Pattern: Epistemic stack

**Problem:** Operators confuse model outputs with sensor facts.  
**Solution:** Fixed-order labelled stack with distinct visual grammar.  
**Use in:** X02, X03, I01 summary.  
**Test:** SAGAT item “observation or inference?”

### S4.2 Pattern: Single selection bus

**Problem:** Split-brain panels.  
**Solution:** One selected entity ID shared across map and lists.  
**Use in:** X01 and linked drawers.  
**Test:** Forced multi-click scenarios; assert ID consistency.

### S4.3 Pattern: Missing-info chip row

**Problem:** Absence is invisible.  
**Solution:** Explicit chips (“Missing: RF corroboration”).  
**Use in:** X01 risk panel, I01 summary, X03.  
**Test:** D1/J2 scenarios; verbal reports.

### S4.4 Pattern: Recommendation as non-execution

**Problem:** Operators believe recommendation already acted.  
**Solution:** Policy chip + “not executed” state until \(\Delta\) recorded.  
**Use in:** X01, X04.  
**Test:** Ask “has anything been sent externally?” pre-decision.

### S4.5 Pattern: Record-decision modal

**Problem:** Accidental high-impact actions; effector metaphor risk.  
**Solution:** Modal with category enum, rationale rules, non-weapon notice, cancel.  
**Use in:** X04, I02.  
**Test:** Copy review; single-click attempt should fail (require confirm).

### S4.6 Pattern: Degrade-in-public

**Problem:** Silent capability loss.  
**Solution:** Pills + banners + map hatch; confidence ceilings.  
**Use in:** Shell, X01, X05.  
**Test:** Heartbeat miss injection in S01.

### S4.7 Pattern: Evidence graph

**Problem:** Opaque fusion.  
**Solution:** Node-link obs→det→track→optional behaviour→risk with conflict flags.  
**Use in:** X03.  
**Test:** Operator recounts causal chain.

### S4.8 Pattern: Citation-bound assistant

**Problem:** Fluent ungrounded answers.  
**Solution:** Allowlisted tools; citations; no decide tools; hideable.  
**Use in:** X08.  
**Test:** Tool-deny states; citation compliance metric.

### S4.9 Pattern: Incident subset map

**Problem:** Global clutter during coordination events.  
**Solution:** I01 map filters to member tracks; summary holds set-level risk.  
**Use in:** I01.  
**Test:** Commander identifies member set and missing info.

### S4.10 Pattern: Audit as narrative substrate

**Problem:** AAR without causality.  
**Solution:** Decision/risk/track events with versions and digests; X07 scrub.  
**Use in:** X06, X07, R01.  
**Test:** Analyst reconstructs why a category was chosen.

### S4.11 Anti-pattern gallery

| Anti-pattern | Why it fails theory |
|---|---|
| Dashboard stat cards in first viewport | Splits attention from map truth surface |
| “AI confirmed threat” banner | Epistemic collapse; misuse |
| Green check on class argmax | False ground truth |
| Glow-pulse all tracks | Noise; accessibility harm |
| Engage/Fire primary button | Authority leakage; legal/safety |
| Toast-only D1 | Violates degrade publicity |
| Assistant auto-decide | Violates HMT authority gradient |

---

## Supplement S5 — Reference Architecture Details (Extends Section 6)

### S5.1 Frontend module boundaries

```
apps/ops-console/
  shell/                 # brand, site, mode, pills, routing
  map/                   # layers, hatch, selection highlight
  panels/                # alerts, tracks, risk-action
  epistemic/             # EpistemicStack, badges, distributions
  decision/              # X04/I02 modal flows
  incident/              # I01 workspace
  health/                # X05
  audit/                 # X06
  replay/                # X07
  assistant/             # X08 (feature flagged)
  state/selectionBus.ts
  state/degradedModes.ts
```

Boundary rule: `assistant/` may import read APIs and citation UI; it must not import decision mutation clients.

### S5.2 Backend service boundaries (HF-relevant)

| Service | UI dependency | Fail behaviour |
|---|---|---|
| Track projection | X01/X03 | Empty/error states; no fabricated tracks |
| Alert policy | X01/X02 | Tier+policy id required |
| Risk | X01/I01 | Factors + missing info required |
| Decision | X04/I02 | Fail closed if audit/IAM down |
| Handoff outbox | status modules | FAILED/DLQ visible |
| Health | pills/X05 | Drives D1–D5 |
| Replay | X07 | Buffering/error explicit |
| Assistant tools | X08 | Deny-by-default tools |

### S5.3 Event taxonomy for timeline docks

Operators scanning X01’s timeline need typed events: obs, det, track upd, risk, alert, decision, health. Colour alone is insufficient; icons+labels required (accessibility). Timeline is supportive, not a replacement for map selection.

### S5.4 Idempotency and double-submit

X04 must hold an idempotency key for the submit lifecycle. Human factors angle: double-click anxiety should not create duplicate external notifications. Success UI shows one decision id.

### S5.5 Dual-control sequence diagram (textual)

```
Approver A                Decision Service              Approver B
    |                            |                           |
    | submit category+rationale  |                           |
    |--------------------------->|                           |
    |                     PENDING_SECOND                     |
    |                            |------ notify/wait ------->|
    |                            |                           |
    |                            |<-- approve / reject ------|
    |                            |                           |
    |<------ DECIDED or cancelled -------------------------|
```

UI on I02 must show “waiting…” with identity, not a spinner without meaning.

### S5.6 Environment badges as cognitive fences

LAB vs STAGING vs OPS badges prevent mode confusion—a classic human-factors hazard (operating on simulated truth as if live, or vice versa). S01 truth overlay is instructor-only to avoid training scars where operators expect omniscience in OPS.

---

## Supplement S6 — Implementation Playbook (Extends Section 7)

### S6.1 From WF-X01 regions to CSS/landmarks

| Wireframe region | Landmark / test id | Notes |
|---|---|---|
| Shell | `ops-shell` | Includes pills |
| Map | `map-canvas` | Hero surface |
| Alerts | `panel-alerts` | Tiered rows |
| Tracks | `panel-tracks` | Quality + coast |
| Risk/action | `panel-risk` | Missing + Rec |
| Bottom dock | `dock-*` | Tabs |

### S6.2 Shared token intents (operational)

Night-operable tactical console: cool dark canvas; selected accent; T3 warm danger; T2 amber; T1 cool info; degrade hatch reserved for system impairment. Exact hex lives in product design tokens; HF rule is role consistency, not brand experimentation on the map.

### S6.3 Microcopy lint rules (CI-oriented)

Deny list in UI strings for OPS builds: `Fire`, `Engage`, `Jam`, `Arm`, `Weapon`, `Kill`, `EA `, `Electronic attack` (case-insensitive, whole-word where applicable). Allow list contexts only in docs stating exclusion. This is an engineering enforcement of Constraint C-NO-EFFECTOR.

### S6.4 Empty/error copy patterns

Empty tracks: “No active tracks in filter” + clear filters.  
Error: Retry + status link; no stack traces.  
Not found alert/track: explicit not-found vs generic error (avoid data leakage).

### S6.5 Performance and SA

If projection lag grows, D3 must appear before operators silently trust a stale map. Performance is an SA feature. Engineering NFRs on lag are human-factors requirements.

### S6.6 Instrumentation schema (minimal)

```
hf_event {
  ts, scenario_id?, user_role,
  type: alert_shown | evidence_opened | decide_opened | decision_recorded |
        mode_simplify_on | degraded_shown | assistant_query | assistant_denied,
  entity_ids[], tier?, category?, policy_id?, model_version?
}
```

Without instrumentation, Section 10 metrics cannot be collected.

### S6.7 Code review prompts for HF

1. Does this PR merge inference into observation styling?  
2. Does any button imply effector action?  
3. Is degrade visible in chrome for new health faults?  
4. Can X08 reach decision APIs?  
5. Is class shown as distribution on evidence views?  
6. Is recommendation labelled with policy id?

---

## Supplement S7 — Extended Trade-off Analysis (Extends Section 8)

### S7.1 Information richness vs recognition speed

RPD-friendly UIs favour chunked recognition cues; epistemic honesty adds structure that novices may parse slowly. Mitigation: training on grammar; summary-first progressive disclosure; Simplify under load. Expect novices to be slower initially and more accurate on provenance—acceptable if training budget exists.

### S7.2 Centralised policy vs local adaptation

Central policy IDs enable audit and retuning; local ad-hoc “operator preference tiers” destroy comparability. Trade-off favours central policy with measured retuning.

### S7.3 Strict fail-closed vs availability

D4 protects accountability but can block categories during outages. Mitigation: clear view-only state; escalate via out-of-band SOP documented operationally—not by silently writing unaudited decisions in the console.

### S7.4 Multi-site future

If multi-site selection appears in G01, SA challenges multiply (which site’s coverage?). Architecture should keep site context in shell always visible—already hinted in wireframes (“Site:ALPHA”).

### S7.5 Trade-off decision record template

For each major UI decision, record: gains, losses, irreversibility, risk, evaluation plan. Example:

**Decision:** Recommendations pre-selected in X04.  
**Gains:** Speed, policy consistency.  
**Losses:** Anchoring.  
**Irreversibility:** Low (can default to none).  
**Risk:** Misuse.  
**Evaluation:** Override rate + appropriateness coding.

---

## Supplement S8 — Failure Mode Effects Analysis (Extends Section 9)

### S8.1 Cognitive FMEA excerpt

| Failure | Cause | Effect | Severity | Detection | Control |
|---|---|---|---|---|---|
| F1 Inference/fact | Styling collapse | Wrong verbal SA; bad category | High | SAGAT | EpistemicStack |
| F2 Fatigue | Tier inflation | Missed T3 | High | Miss metrics | Policy+suppression |
| F5 Silent degrade | Toast-only | Overconfidence | High | Probe+logs | G02 chrome |
| F6 Swarm reification | Indicator as fact | Inappropriate NOTIFY | High | Debrief coding | Copy+missing info |
| F8 Assistant overtrust | Uncited fluency | Wrong mental model | Med | Citation logs | Tool allowlist |

### S8.2 Latent organisational conditions

Reason’s latent conditions framing (organisational) applies even without citing Reason extensively here: metrics that reward only speed, policies that over-alert, and disabled audit in “emergencies” create latent paths to F1–F8. The console cannot fix all organisational latent conditions, but it can refuse to offer unaudited decide paths (D4).

### S8.3 Recovery playbooks (UI-supported)

| Condition | Operator-visible recovery |
|---|---|
| RF down | Hatch + X05 detail; confidence capped |
| Model route down | D2 badges; sensor-native only |
| Handoff fail | FAILED status; retry if permitted |
| Audit down | D4 view-only; wait/restore |
| Alert storm | Simplify; suppressions; admin rate meter |

### S8.4 Training against ironies

Schedule recurring X07 exams: freeze a historical swarm-suspect incident; require epistemic narration before category selection. This directly counters Bainbridge deskilling.

---

## Supplement S9 — Full Evaluation Protocols (Extends Section 10)

### S9.1 Formative vs summative

**Formative (design iterations):** 4–6 participants; think-aloud; bug-finding on epistemic grammar; refine copy.  
**Summative (gate):** Powered comparison epistemic vs fused baseline on H1–H3 primary endpoints.

### S9.2 Scenario scripts (lab)

**Scenario A — J1 Unknown object:** Single track birth; class distribution ambiguous; recommendation HEIGHTEN_MONITORING; inject optional conflict flag variant.

**Scenario B — J2 Coordination indicators:** Three tracks; behaviour indicator; missing RF on one; T3+incident; dual-control NOTIFY_EXTERNAL path.

**Scenario C — J3 Degradation:** Mid-scenario RF heartbeat miss; assert hatch+pills; decision should acknowledge capped confidence.

**Scenario D — Storm:** Burst of T1 duplicates + one T3; measure suppression use and T3 miss.

**Scenario E — Assistant ablation:** Same as A/B with X08 on vs off (within or between subjects).

### S9.3 Expert scoring rubric for decision appropriateness (0–3)

- 0: Category contradicts clear policy/evidence; or effector misconception.  
- 1: Plausible but ignores stated missing info or conflict.  
- 2: Appropriate category; thin rationale.  
- 3: Appropriate category; rationale cites evidence IDs and missing info.

### S9.4 Trust items (illustrative)

Adapted from trust-in-automation practice (Lee & See, 2004 tradition): agreement scales on “I understood when the system was uncertain,” “I knew which outputs were model inferences,” “I would notice if sensing coverage dropped.” Pair with objective coverage-awareness probes to detect miscalibration.

### S9.5 Analysis plan sketch

Primary endpoint: SA provenance composite (mean of sensor-involvement, inference-identification, missing-info probes).  
Secondary: decision appropriateness, coverage awareness, TLX temporal demand, override rate band.  
Safety endpoint: effector-metaphor interpretation count (target 0).  
Use mixed-effects models with participant random intercepts; report effect sizes and confidence intervals; avoid claiming proof from pilots alone.

### S9.6 Ethical evaluation conduct

Lab participants should know scenarios are simulated; no deception that simulated notifications are real external alerts. Instructor truth overlay not shown to participants. Data retention minimal and role-separated.

### S9.7 OPS shadow evaluation

After release, monitor: T3 miss proxies, override distributions, D4 incidents, handoff failure handling time, X08 citation compliance, Simplify usage during high track counts. Quarterly replay exams for crews.

---

## Supplement S10 — Extended Build Guide with Acceptance Tests (Extends Section 11)

### S10.1 Acceptance tests per stage

**Stage B (X01):** Selection syncs three panels; Simplify hides low tiers; map remains primary.  
**Stage C:** Inference badge present; class distribution renders; conflict strip appears when flagged.  
**Stage D:** Non-weapon notice visible; deny-list strings absent; D4 disables Decide; idempotent submit.  
**Stage E:** Heartbeat miss → hatch+pill within NFR; X05 shows last obs age.  
**Stage F:** I01 member filter; ownership transfer; close rules enforced.  
**Stage G:** Audit shows model version on decision rows; replay scrub updates map.  
**Stage H:** Assistant cannot call decide; citations required; D6 hides drawer.  
**Stage I:** Freeze probe harness works; LAB badge visible.  
**Stage J:** HF checklists signed by Victor.I (or delegate) before OPS promote.

### S10.2 Definition of done for epistemic honesty

A release is not done when pixels match comps. It is done when: (1) automated lint passes deny-list; (2) component tests lock EpistemicStack order; (3) chaos test for audit-down shows D4; (4) formative SA probes beat fused baseline on provenance items or qualitative gate is explicitly waived with documented risk.

### S10.3 Rollout sequence

Lab → Staging (with replay packs) → limited OPS watch floor with X08 off → enable features by flag (auto-open incidents, sound, X08) only after metrics review.

---

## Supplement S11 — Discussion Addenda (Extends Section 12)

### S11.1 What would falsify this design theory?

If summative tests show epistemic UI *reduces* SA-L1 on spatial items due to clutter from strips *and* Simplify cannot compensate; or if decision appropriateness drops because operators drown in provenance; or if operators still verbalise effector control despite notices—then redesign (not just training) is required.

### S11.2 Relation to security threat model

Product security notes operator over-trust in AI labels as a risk mitigated by epistemic honesty. This monograph is the HF deep treatment of that row: trust is not a colour; it is a calibrated relationship supported by interface structure.

### S11.3 Maintenance burden

Epistemic components are an investment against three-year entropy. Without them, each new model output will invent a new badge language. Centralising grammar is the maintainable path.

### S11.4 Claims discipline

This work makes no certification claims about regulatory compliance. It claims a defensible HF design and evaluation programme for defensive decision support. Customer-facing compliance language must follow separate governance.

---

## Supplement S12 — Glossary

| Term | Meaning in this monograph |
|---|---|
| Category | Authorised response intent recorded by a human |
| Epistemic UI | Interface that separates knowledge types visually/linguistically |
| Evidence pack | X03 assembly of obs/inference/prediction/rec/decision |
| Handoff | Delivery of category to external system; statusful |
| Indicator | Behaviour signal; not ontological confirmation |
| Selection bus | Single shared selected entity across console regions |
| Simplify | Density mode retaining high-tier/incident focus |
| SAGAT | Freeze–probe SA measurement technique |

---

## Supplement S13 — Acknowledgements and Author Line

Research monograph authored by **Victor.I** for the Counter-Swarm Defence Platform. Product screen semantics follow internal design artefacts (workflow, IA, wireframes, inventory, UX principles, alerts/approvals). Theoretical framing draws on the cited human-factors literature. Defensive decision-support scope is intentional and exclusive of weapons/EA guidance.



---

## Supplement S14 — End-to-End Worked Narratives with Epistemic Commentary

### S14.1 Narrative N1 — Unknown object (maps to J1)

At 12:01:02Z, RDR-1 contributes observations that birth track T-104. X01 shows a new T2 alert: “New track quality crossed policy P-14.” The operator selects the alert. X02 renders:

- OBSERVATION: three obs in 8 s from RDR-1 and EO-3.  
- INFERENCE: class UAV \(p=0.72\), model det-v3.2.  
- PREDICTION: 60 s kinematic envelope available on map toggle.  
- RECOMMENDATION: CUE_SENSOR optional.  
- DECISION: Pending.

The operator opens X03, inspects the evidence graph, and notes no conflict. They still see only \(p=0.72\), not certainty. They open X04, change or accept a category, write a rationale for T2+, and record. Audit captures actor, category, evidence count, model version.

**Epistemic commentary:** Success is the operator’s ability to say “radar and EO observed something; the model infers UAV at 0.72; I chose to cue an additional sensor.” Failure is “UAV confirmed, engaging.”

### S14.2 Narrative N2 — Suspected coordination (maps to J2)

Behaviour indicators fire on T-104, T-105, T-109. Risk elevates; policy opens incident I-22; T3 asserts. Commander on I01 sees subset map, HIGH risk band, formation-like *indicator*, missing RF on T-109, recommendation NOTIFY_EXTERNAL. They may open X08 for a cited summary; they may not. Dual-control completes. Handoff ACKED.

**Epistemic commentary:** The indicator language and missing-info panel are load-bearing. If either is absent, Parasuraman–Riley misuse becomes likely under time pressure.

### S14.3 Narrative N3 — Sensor degradation (maps to J3)

RF-02 heartbeat times out. Shell pills show SENS 3/4; map hatches RF sector; confidence ceilings apply. Sensor operator uses X05 to see last obs age and adapter errors. Fusion continues on remaining sensors. Recovery clears mode with audit.

**Epistemic commentary:** This is Endsley Level 1 about *system* elements. Without it, Level 2 comprehension of tracks is falsely precise.

### S14.4 Narrative N4 — Contradictory evidence

X03 shows CLASS_CONFLICT. Risk widens rather than picking a side. Operator heightens monitoring instead of notifying externally.

**Epistemic commentary:** Conflict flags are resilience markers (Woods). Auto-resolving conflicts in the UI to keep the picture “pretty” recreates Bainbridge’s irony when the resolution is wrong.

### S14.5 Narrative N5 — Integration failure after good decision

Decision recorded; handoff FAILED. Operator sees status and retry/DLQ path. Decision remains valid.

**Epistemic commentary:** Separating decision validity from handoff success prevents thrashing re-entry into X04 and duplicate organisational signals.

### S14.6 Narrative N6 — Audit/IAM outage

Decide controls disabled; D4 banner; view-only. No shadow write path.

**Epistemic commentary:** Availability loss is preferred over unaccountable authority. This is an ethical and safety choice encoded as UX state.




---

## Supplement S15 — Comparative Architecture Options (Mandatory Exploration)

Before converging on the map-first epistemic console, three architecture families were considered for Counter-Swarm Defence operator C2. This section records the exploration explicitly, including why alternatives become liabilities.

### S15.1 Option A — Fused “threat dashboard”

**Components:** Central threat score, ranked object cards, sparse map thumbnail.  
**Data ownership:** Model service owns the score; UI displays rank.  
**Read path:** Score stream → cards.  
**Write path:** One-click “act” macros.  
**Scaling:** Easy to add cards; hard to preserve spatial SA as track count grows.  
**Failure modes:** Epistemic collapse; alert-card fatigue; effector metaphor creep.  
**When it becomes a liability:** Immediately under swarm-suspect multi-track geometry and degraded sensing.  
**Why it can be a bad idea:** Optimises for glanceable certainty that does not exist; maximises Parasuraman–Riley misuse.

### S15.2 Option B — Chat-first AI co-pilot

**Components:** Conversational pane as primary; tools fetch tracks on demand.  
**Data ownership:** Assistant orchestration layer.  
**Read path:** NL query → tools → narrative.  
**Write path:** Risk of “please notify external” language actions.  
**Scaling:** Fluent under low load; brittle under alert storms (serial chat vs parallel map).  
**Failure modes:** Ungrounded fluency; authority leakage; slow spatial tasks.  
**Liability:** Becomes a single point of cognitive failure when citations slip.  
**Why bad as primary:** Violates map-as-truth-surface and non-critical assistant principle.

### S15.3 Option C — Map-first epistemic console (selected)

**Components:** X01 shell/map/panels; epistemic drawers; modal decisions; health chrome; optional X08.  
**Data ownership:** Projection services own typed evidence; decision service owns \(\Delta\); UI owns presentation grammar.  
**Read path:** Bus → projections → selection bus → panels/map.  
**Write path:** Human-only decision API; handoff outbox separate.  
**Scaling:** Layer toggles + Simplify manage clutter; incidents subset maps for set tasks.  
**Failure modes:** Implementation cost; novice parse time; requires training on grammar.  
**Liability if neglected:** Teams may “simplify” by removing epistemic labels under deadline pressure.  
**Why selected:** Best alignment with Endsley levels, Wickens PCP (dual integration/discrimination needs), calibrated trust, and product safety boundary (no effector UI).

### S15.4 Trade-off summary table

| Dimension | A Fused dashboard | B Chat-first | C Epistemic map-first |
|---|---|---|---|
| L1 spatial SA | Weak | Weak | Strong |
| Provenance SA | Weak | Variable | Strong if enforced |
| Tempo under swarm | Poor (card thrash) | Poor (serial) | Good with Simplify |
| Misuse risk | High | High | Lower |
| Engineering cost | Low initially | Medium | Higher upfront |
| 3-year ownership | Poor | Poor without hard gates | Good with lint/tests |
| Effector creep risk | High | High | Controlled |

**Recommendation:** Option C, with X08 strictly optional and Option A explicitly rejected as a baseline only for evaluation contrasts—not for OPS delivery.

---

## Supplement S16 — Metrics Dictionary and Data Collection Spec

### S16.1 Metric dictionary

| ID | Name | Formula / rule | Unit | Good direction |
|---|---|---|---|---|
| M1 | SA-Provenance | Mean correct on probes {sensor list, inference ID, missing info, model version awareness} | 0–1 | Up |
| M2 | SA-Spatial | Mean correct on probes {track count in sector, selected kinematics band} | 0–1 | Up |
| M3 | SA-Project | Mean correct on near-future probes under stated assumptions | 0–1 | Up |
| M4 | TTE | \(t_{\text{evidence open}} - t_{\text{alert shown}}\) | s | Down (to floor) |
| M5 | TTD | \(t_{\text{decision recorded}} - t_{\text{alert or incident}}\ | s | Context-dependent |
| M6 | Appropriateness | Expert rubric 0–3 | score | Up |
| M7 | OverrideRate | Share of decisions where category ≠ recommendation | 0–1 | Mid band |
| M8 | T3Miss | T3 unacked beyond policy threshold | rate | Down |
| M9 | CoverageAware | Correct D1 report before decide when D1 active | 0–1 | Up |
| M10 | TLX-Global | NASA-TLX weighted or raw mean | score | Down if quality holds |
| M11 | CiteCompliance | X08 answers with valid cites / all answers | 0–1 | Up |
| M12 | EffectorMisread | Count interpreting X04 as weapon control | count | 0 |

### S16.2 Collection points in product

| Metric | X01 | X02 | X03 | X04 | X05 | X06 | X07 | X08 | I01 |
|---|---|---|---|---|---|---|---|---|---|
| M4 TTE | alert | | open | | | | | | open |
| M5 TTD | | | | record | | | | | via I02 |
| M7 | | | | yes | | audit | | | yes |
| M9 | pills/hatch | | | before | detail | | | | summary |
| M11 | | | | | | | | yes | |

### S16.3 Healthy override band (interpreting M7)

There is no universal correct override rate. Interpretation protocol:

1. Stratify by scenario difficulty and recommendation quality.  
2. If M7 ≈ 0 across hard conflict scenarios → suspected misuse/anchoring.  
3. If M7 ≈ 1 despite strong calibrated recommendations → suspected disuse or poor Rec quality.  
4. Retune policy and UI factors before blaming operators.

### S16.4 Reporting template for evaluation campaigns

```
Campaign ID:
UI build (epistemic | fused baseline):
N participants / roles:
Scenarios run:
Primary endpoint M1 result (effect size, CI):
Safety endpoint M12:
Deviations from protocol:
Decision: promote / iterate / waive (signed)
Author sign-off: Victor.I (or delegate)
```

---

## Supplement S17 — Wireframe-to-Test Traceability Matrix

| Wireframe | Requirement trace | Automated test idea | HF probe link |
|---|---|---|---|
| WF-X01 | Map hero; panels; pills | selection bus unit tests | SA-Spatial |
| WF-X02 | Epistemic strips; policy id | snapshot + policy id assert | SA-Provenance |
| WF-X03 | Distribution; evidence graph | render class bars; conflict | SA-Provenance |
| WF-X04 | Categories; notice; no effector | string deny-list CI | M12 |
| WF-X05 | Sensor ages; coverage | heartbeat miss → UI mode | M9 |
| WF-X06 | Filters; digest | audit row schema | AAR tasks |
| WF-X07 | Scrub; ticks | scrub updates projection time | training exams |
| WF-I01 | Subset map; missing info | member filter | J2 debrief |
| X08 (inv.) | citations; no decide | tool allowlist test | M11 |

---

## Supplement S18 — Operator Cognitive Task Analysis (CTA) Sketch

### S18.1 Goals hierarchy (security operator)

1. Maintain valid air picture awareness.  
2. Triage alerts by earned tier.  
3. Discriminate observation vs inference.  
4. Identify missing information.  
5. Select authorised category when required.  
6. Verify system integrity continuously.

### S18.2 Critical cues

Track quality transitions; coasting; conflict flags; tier changes; coverage hatch; bus lag dimming; recommendation policy chips; dual-control waiting state.

### S18.3 Likely errors (CTA)

Cue confusion (inference as obs); attentional tunnelling on one track during multi-track incident; premature NOTIFY under incomplete RF; ignoring D3 staleness.

### S18.4 Design implications already taken

EpistemicStack; I01 subset; missing-info chips; G02 chrome; X04 rationale; Simplify.

### S18.5 Remaining CTA work

Live ride-alongs (where permitted) to validate cue lists; refine quiet-mode policies per site; measure whether timeline dock is used or ignored (remove if unused noise).

---

## Supplement S19 — Parasuraman–Sheridan–Wickens Levels Applied Conservatively

Parasuraman, Sheridan, and Wickens (2000) describe levels of automation from none to full autonomy across information acquisition, analysis, decision selection, and action implementation. Mapping for this product:

| Stage | Automation level (conceptual) | Product choice |
|---|---|---|
| Information acquisition | High (multi-sensor ingest) | Adapters + normalisation |
| Information analysis | Medium–high (detect/track/fuse/risk) | Models + policy; UI shows provenance |
| Decision selection | Low–medium (recommend only) | Rec chips; human selects category |
| Action implementation | None in-console | External systems only after handoff; no effector UI |

Sheridan and Verplank’s classic teleoperator levels (1978) similarly caution against leaping to high autonomy without corresponding feedback quality. Counter-Swarm Defence intentionally caps in-console automation below action implementation.

---

## Supplement S20 — Closing Engineering Invariants (Checklist for Ownership)

Print and keep with release trains:

1. Inference never uses observation styling.  
2. Class is a distribution on evidence views.  
3. Recommendations show policy id and non-executed state.  
4. Decisions are human-recorded categories with audit.  
5. D1–D6 are chrome-visible.  
6. D4 fail-closed is tested in CI/chaos.  
7. X08 cannot write decisions; citations required.  
8. No effector strings/controls in OPS builds.  
9. Single selection bus.  
10. Lab-only features cannot appear without LAB badge.

**Author invariant owner:** Victor.I (design research); engineering delegates enforce via lint and tests.


## References

Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775–779.

Bliss, J. P., & Gilson, R. D. (1998). Emergency signal failure: Implications and recommendations. *Ergonomics, 41*(1), 57–72.

Cvach, M. (2012). Monitor alarm fatigue: An integrative review. *Biomedical Instrumentation & Technology, 46*(4), 268–277.

Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64.

Endsley, M. R., & Garland, D. J. (Eds.). (2000). *Situation awareness analysis and measurement*. Lawrence Erlbaum Associates.

Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. In P. A. Hancock & N. Meshkati (Eds.), *Human mental workload* (pp. 139–183). North-Holland.

Hollnagel, E., Woods, D. D., & Leveson, N. (Eds.). (2006). *Resilience engineering: Concepts and precepts*. Ashgate.

Klein, G. (1993). A recognition-primed decision (RPD) model of rapid decision making. In G. A. Klein, J. Orasanu, R. Calderwood, & C. E. Zsambok (Eds.), *Decision making in action: Models and methods* (pp. 138–147). Ablex.

Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten challenges for making automation a “team player” in joint human-agent activity. *IEEE Intelligent Systems, 19*(6), 91–95.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80.

Lyons, J. B., & Guznov, S. Y. (2019). Individual differences in human–machine trust: A multi-study look at the perfect automation schema. *Theoretical Issues in Ergonomics Science, 20*(4), 440–458.

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253.

Wickens, C. D., & Carswell, C. M. (1995). The proximity compatibility principle: Its psychological foundation and relevance to display design. *Human Factors, 37*(3), 473–494.

Wickens, C. D., Hollands, J. G., Banbury, S., & Parasuraman, R. (2013). *Engineering psychology and human performance* (4th ed.). Pearson.

Woods, D. D. (2015). Four concepts for resilience and the implications for the future of resilience engineering. *Reliability Engineering & System Safety, 141*, 5–9.

Woods, D. D., & Hollnagel, E. (2006). *Joint cognitive systems: Patterns in cognitive systems engineering*. CRC Press.


Endsley, M. R. (1988). Design and evaluation for situation awareness enhancement. In *Proceedings of the Human Factors Society Annual Meeting* (Vol. 32, pp. 97–101). Human Factors Society.

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans, 30*(3), 286–297.

Sheridan, T. B., & Verplank, W. L. (1978). *Human and computer control of undersea teleoperators* (Technical Report). MIT Man-Machine Systems Laboratory.

Victor.I. (2026). Counter-Swarm Defence Platform product design artefacts: system workflow, information architecture, wireframes, UI screen inventory, UX principles, and alerts/approvals/incidents UI. Internal technical documentation, Counter-Swarm Defence repository (`docs/product/`).

---

## Appendix A — Screen-to-theory quick map

| Screen | Primary SA support | Primary risk controlled |
|---|---|---|
| X01 | L1 air picture; attention triage | Clutter; missed degrade |
| X02 | L2 alert meaning | Alert without why |
| X03 | L1–L3 evidence pack | Inference/fact collapse |
| X04 | Accountable decision | Effector metaphor; misuse |
| X05 | L1 system/sensor elements | Silent failure |
| X06 | Organisational memory | Unauditable acts |
| X07 | Learning / L3 review | Deskilling (irony) |
| X08 | Optional comprehension aid | Overtrust; authority leak |
| I01 | Multi-object L2/L3 | Swarm-score reification |

## Appendix B — Evaluation probe bank (starter)

1. List sensor IDs with observations on selected track in the last N seconds.  
2. State whether the displayed class is observation or inference.  
3. Report the top two risk factors shown.  
4. Report any conflict flags.  
5. State missing information listed by the system.  
6. State whether coverage is degraded and identify the sector if hatched.  
7. State the current recommendation and policy ID.  
8. State whether a decision is pending or recorded (actor if recorded).  
9. State handoff status if a decision exists.  
10. Identify whether assistant is available.

## Appendix C — Author responsibility

All product-facing human-factors claims in this monograph are authored by **Victor.I** for the Counter-Swarm Defence Platform research and design programme. Implementation teams should treat epistemic honesty and the non-effector boundary as safety-critical product invariants.

---

**End of monograph**

**Author:** Victor.I
