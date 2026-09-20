<!-- Author: Victor.I -->

# Lessons Learned and Build Roadmap (Phases 1–8)

**Author:** Victor.I  
**Status:** Ready for build planning  
**Audience:** All eight disciplines + stakeholders  
**Prerequisite:** Stage 0 documentation complete (`docs/systems/stage0-completion.md`)  
**Related:** Research monographs in `docs/research/`, architecture pack, product pack, simulation pack

---

## Part A — Are we ready?

**Yes — ready to plan and execute a build roadmap.** We are not ready to jump straight to “production C-UAS with real sensors and effectors.”

| Ready for | Not ready for (yet) |
|---|---|
| Phase 1 software vertical slice on x86 + Compose | Field deployment |
| Simulation-driven development | Weapon / effector integration |
| Contract-first schemas and ICD | Claiming certified detection performance |
| Epistemic operator UI skeleton | Full ML fleet on Jetson without evaluation gates |
| Security design embedded from day one | Skipping human approval “for demos” |

Open questions that can wait for later phases: final site CONOPS (Q-01), vendor list (Q-05), air-gap (Q-16). They must not block Phase 1 sim-based coding.

---

## Part B — Lessons learned so far

These lessons come from the requirements, architecture, FMEA, threat model, product/UX pack, digital twin design, edge-hardware decision, and the eight research monographs (~103k words, Pass 1).

### B1. Product and human factors

1. **Integration beats isolated detectors.** Operators need a coherent picture, evidence, and uncertainty — not another raw alert firehose.  
2. **Epistemic honesty is a safety property.** Observation, inference, prediction, recommendation, and decision must stay visually and linguistically distinct (screens X01–X08, I01).  
3. **Alert fatigue is a first-class failure mode.** Tiering, quality gates, and Simplify mode matter as much as model accuracy.  
4. **Never ship faux effector UI.** Labels are “authorised category / Record decision,” never Engage / Fire / Jam.  
5. **Capability loss must be visible.** Coverage holes and degraded modes (D1–D6) beat inventing tracks.

*Refs:* `docs/product/*`, `docs/research/product-design/`, Endsley SA framing in the HF monograph.

### B2. Systems engineering and integration

6. **Interfaces before components.** Canonical observation + ICD freeze the platform; vendors plug in via adapters.  
7. **Simulation before hardware.** Twin + same adapter contracts prove the stack without operational sensors or harmful effects.  
8. **Hybrid compute is the norm.** x86 central for C2/fusion; NVIDIA Jetson for EO edge when cameras arrive; Raspberry Pi only for light/lab adapters — never as the fusion brain.  
9. **Fail visible, fail closed on audit/IAM.** FMEA and safety vetoes are design inputs, not afterthoughts.  
10. **Stages exist to buy down risk.** Skipping twin → HIL → field is how programmes fail audits and operators.

*Refs:* `architecture/*`, `architecture/edge-hardware.md`, `docs/research/systems-engineering/`, `docs/simulation/`.

### B3. Software engineering

11. **Event-driven modular services fit async sensors better than a monolith or nanoservice sprawl.**  
12. **Idempotent consumers, outbox for handoffs, one writable owner per entity.**  
13. **Contract tests on schemas/APIs are the real “proof” early on.**  
14. **Observability is part of the product:** lag, health, model latency, sensor silence.

*Refs:* `docs/research/software-engineering/`, `architecture/system.md`, `docs/software/cicd-and-environments.md`.

### B4. Data engineering

15. **Assume late, missing, duplicate, contradictory data.** Quarantine and quality flags beat silent drops.  
16. **`observation.v1` is the stability hinge.** Schema evolution must be versioned and backward-compatible within a major.  
17. **Replay and retention are recovery tools**, not nice-to-haves.

*Refs:* `schemas/observation.v1.json`, `docs/research/data-engineering/`, `architecture/data-flow.md`.

### B5. ML engineering

18. **Classical tracking first; deep learning where justified by data and latency.** Kalman/PDAF/JPDAF-style association before clever nets.  
19. **Every operator-visible inference needs model version + score calibration awareness.**  
20. **Over-merge is often worse than under-merge** for operator trust.  
21. **Training/serving skew and drift are operational failures**, not academic footnotes. Registry + canary + rollback.

*Refs:* `docs/research/ml-engineering/`, `docs/ml/architecture.md`.

### B6. Data science and risk

22. **Do not collapse uncertainty into a fake binary “threat.”** Graded risk + factors + missing-info list.  
23. **Behaviour/swarm indicators are evidence, not decisions.**  
24. **Evaluate against twin truth offline;** never show instructor truth as live “confirmed fact” to operators under test.

*Refs:* `docs/research/data-science/`, `docs/data-science/analytics-framework.md`.

### B7. AI engineering

25. **LLMs are assistants, not authorities.** No LLM in IAM, audit integrity, safety interlocks, or decision commit.  
26. **Tool allowlists + citations + audit of tool calls.** Prompt injection is an expected abuse case.  
27. **X08 must be dismissible;** core C2 works if AI is off (D6).

*Refs:* `docs/research/ai-engineering/`, `docs/ai/architecture.md`.

### B8. Security, safety, governance

28. **Category-only external handoff is a hard boundary.** Expanding schemas toward effector primitives is a safety veto.  
29. **Tamper-evident audit; decisions fail closed if audit write fails.**  
30. **Model cards and provenance are promotion gates**, not paperwork theatre.  
31. **Public repo ≠ unclassified operational data.** Keep live sensor imagery, sites, and credentials out of git (A-10).

*Refs:* `docs/research/security-governance/`, `docs/security/threat-model.md`, `docs/security/auditability.md`.

### B9. Meta-lessons from how we worked

32. **Research before code reduced thrash** — but research must stay tied to ICD and screens or it becomes shelfware.  
33. **Word-count theatre is not scholarship.** Landmark citations and buildable guidance beat padded “30k words.”  
34. **Discipline RACI prevents silent gaps** (SYS accountable for deploy topology; SE responsible for packaging; SG safety veto).

---

## Part C — Guiding principles for the build (carry into every phase)

```
reliability > novelty
evidence > assumptions
integration > isolated demos
human oversight > uncontrolled autonomy
testability > complexity
clear interfaces > tightly coupled components
operational usefulness > impressive AI
simulation > premature hardware dependence
```

**Safety chain (non-negotiable in software):**

```
DETECT → TRACK → CLASSIFY → ASSESS → PRIORITISE
→ HUMAN REVIEW → AUTHORISED CATEGORY → EXTERNAL (optional) → AUDIT
```

---

## Part D — Phased build roadmap

Each phase lists: **goal**, **lessons applied**, **work breakdown**, **exit criteria**, **owners**, **explicit non-goals**.

---

### Phase 1 — Digital prototype (architecture proof)

**Goal:** Prove the end-to-end software path with simulated sensors only.

```
Sim → Adapter → Normaliser → Bus → Track (baseline) → Risk (rules)
 → Alert → Operator API/Realtime → Console skeleton → Decision → Audit → Mock external
```

**Lessons applied:** 6, 7, 11–14, 15–16, 28–29, 32.

**Work breakdown**

| Workstream | Tasks |
|---|---|
| Repo / infra | Compose: Redpanda/Kafka-API, Postgres+PostGIS, Redis, MinIO; CI lint + unit + schema contract |
| Schemas | Enforce `observation.v1`, `human.decision.v1`; add `track.update.v1`, `alert.v1`, `risk.assessment.v1` drafts |
| Backend | normaliser, tracking (classical), risk (rules), alert, approval, audit, operator-api, realtime-gateway, sim adapters |
| Frontend | X01 minimal (map stub or list+map), X03 evidence strip, X04 decide, G02 banners stub |
| Sim | SCN-TRK-02, SCN-FLT-01, SCN-DEC-01/02 minimum |
| Security | OIDC or local-dev auth stub with RBAC shapes; no open CORS; secrets in `.env` only |

**Exit criteria**

- [ ] One Compose command brings stack up  
- [ ] Sim observations become tracks with evidence IDs  
- [ ] Operator can record a category; audit row exists; mock handoff ACK/FAIL works  
- [ ] Contract tests green on schemas  
- [ ] No effector-shaped fields in integration API  

**Owners:** SE (R), SYS (A), DE (schemas), PD (UX acceptance), SG (boundary review).

**Non-goals:** Real sensors, deep ML, Jetson, production HA, LLM assistant.

---

### Phase 2 — Sensor integration patterns

**Goal:** Prove adapter pattern with representative non-operational sources and richer sim sensors.

**Lessons applied:** 6, 8, 15–17.

**Work breakdown**

- Adapter SDK template (mTLS identity, idempotency, health heartbeats)  
- Clock skew / CRS normalisation hardening  
- Quarantine topic + data-quality dashboard widgets  
- Scenario pack expansion: SCN-MOD-01, SCN-CON-01, SCN-TIM-01, SCN-NET-01  

**Exit criteria**

- [ ] New sensor type = new adapter package, zero core schema forks  
- [ ] Quality/quarantine metrics visible  
- [ ] Replay from retention window documented and tested  

**Non-goals:** Production vendor contracts (unless separately authorised).

---

### Phase 3 — ML pipeline (controlled)

**Goal:** Introduce detection/classification where data and metrics justify it; keep classical tracking core.

**Lessons applied:** 18–21, 24.

**Work breakdown**

- Dataset versioning (synthetic + any approved real)  
- Model registry + `model_version` on detection events  
- Inference gateway; canary route; rollback drill  
- Offline metrics: precision/recall/FPR, calibration (ECE), latency  
- Optional EO detector experiment on **central GPU** before Jetson  

**Exit criteria**

- [ ] Operator-visible inferences always show model version  
- [ ] Promotion requires eval report + owner + limitations (model card)  
- [ ] Fail policy defined when inference down (passthrough / degrade D2)  

**Non-goals:** Edge Jetson fleet; LLM risk scoring.

---

### Phase 4 — Multi-sensor fusion

**Goal:** Correlate heterogeneous, incomplete, contradictory observations into shared tracks with evidence.

**Lessons applied:** 15, 20, 22–23.

**Work breakdown**

- Association gates + conflict flags (`CLASS_CONFLICT`, etc.)  
- Fusion evidence graph exposed on X03  
- Twin stress: SCN-TRK-03, SCN-SWM-01/02, SCN-CLT-01  
- Scorer vs truth (lab only)  

**Exit criteria**

- [ ] Contradictions retained and shown, not silently discarded  
- [ ] Over-merge rate tracked in sim regression  
- [ ] Behaviour indicators optional input to risk — never sole decision  

---

### Phase 5 — Operator platform

**Goal:** Production-shaped console: map, tracks, confidence, evidence, alerts, timeline, health, audit, incidents.

**Lessons applied:** 1–5, 25–27.

**Work breakdown**

- Full X01–X07, I01–I03 per screen inventory  
- Epistemic stack CSS/tokens from `08-design-tokens.md`  
- Alert fatigue controls + Simplify  
- HF dry-run with scripted scenarios (time-to-evidence)  
- Optional X08 behind feature flag (default off)  

**Exit criteria**

- [ ] PD HF checklist pass on scripted trials  
- [ ] D1–D4 banners verified  
- [ ] No “AI confirmed threat” copy in UI strings  

---

### Phase 6 — Security hardening

**Goal:** Make the system defensible under the threat model for lab→staging.

**Lessons applied:** 28–31, 14.

**Work breakdown**

- Full OIDC; RBAC enforcement; dual-control hook for configured categories  
- mTLS service identity; secret manager; network policies (K8s profile)  
- Tamper-evident audit verification  
- Dependency/container scanning in CI; signed images  
- Prompt-injection corpus if X08 enabled  
- Observability dashboards: system, sensor, model, security, operator  

**Exit criteria**

- [ ] Threat-model controls mapped to implemented checks  
- [ ] Decision fail-closed on audit write failure proven  
- [ ] Staging deploy reproducible from IaC  

**Deploy target:** Harden toward K8s; still central x86 (+ optional GPU).

---

### Phase 7 — Hardware-in-the-loop (no harmful effects)

**Goal:** Connect representative hardware/test systems; measure latency, reliability, recovery.

**Lessons applied:** 7–10, 8.

**Work breakdown**

- Jetson EO edge profile (detect + adapter + buffer) if cameras in scope  
- Vendor/test harness adapters  
- Chaos: sensor death, link loss, model timeout  
- Latency budgets vs NFR-LAT-*  
- Still **mock** external response systems  

**Exit criteria**

- [ ] Measured p95 path ingest→UI under HIL profile  
- [ ] Edge buffer survives partition and resyncs  
- [ ] No expansion of integration schema toward effector params  

**Non-goals:** Field authorities; real destructive effects.

---

### Phase 8 — Controlled validation → production candidate

**Goal:** Authorised site trial of software + sensing under CONOPS; production readiness if gates pass.

**Lessons applied:** 9–10, 31, open questions Q-01/Q-05/Q-16 must be answered before this phase starts.

**Work breakdown**

- Site survey, CRS, time sync (NTP/PTP), coverage maps  
- Operator workload and false-alarm measurement  
- Runbooks, on-call, rollback drills  
- Limitation register signed by SYS + SG  
- External category handoff only to **authorised** systems engineered separately  

**Exit criteria**

- [ ] Programme DoD from master prompt §23 satisfied for the agreed scope  
- [ ] Limitations documented and accepted  
- [ ] SG + SYS sign field/production gate  

**Non-goals:** Autonomous engagement; unsupervised model promotion.

---

## Part E — Cross-phase cadence (how to go about things week to week)

1. **Plan the phase** against exit criteria (this document).  
2. **Implement behind ICD** — no schema freelancing.  
3. **Prove with sim/chaos/contracts** before adding complexity (ML, edge, AI).  
4. **Review with RACI owners** (especially SG on anything near autonomy or handoff).  
5. **Update living README** and open-questions register.  
6. **Only then** open the next phase.

Suggested early team split for Phase 1:

| Track | Focus |
|---|---|
| A | Compose + bus + schemas + normaliser |
| B | Tracking + risk rules + alerts |
| C | Operator API + X01/X04 skeleton |
| D | Sim scenarios + contract tests |

SYS holds integration board; SE leads daily build; SG reviews boundaries weekly.

---

## Part F — What “done” for the whole product still means

Not “the app runs.” Done when requirements, architecture, ICD, threat model, data model, simulation, tests, ML eval (if ML shipped), failure tests, security controls, audit, monitoring, validated operator workflows, hardware boundaries, reproducible deploy, rollback, explainability, and limitations are all true for the **agreed scope**.

---

## Part G — Immediate next action

1. Stakeholder accept this phased roadmap (or amend phase exits).  
2. Open **Phase 1 implementation plan** (ticket breakdown + Compose skeleton).  
3. Start coding Phase 1 on an **x86 lab host** — not Pi-first, not Jetson-first.

---

## Author

Victor.I
