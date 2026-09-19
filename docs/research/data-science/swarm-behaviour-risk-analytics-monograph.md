<!-- Author: Victor.I -->

# Data Science for Swarm Behaviour Analysis, Uncertainty, and Risk Assessment in Counter-UAS Defensive Decision Support

**Author:** Victor.I  
**Document type:** Research monograph (research-structured)  
**Programme:** Counter-Swarm Defence — Data Science & Analytics  
**Scope:** Defensive decision-support software only (sensing, fusion, behaviour indicators, graded risk, human approval, audit). No weaponisation, kinetic fire control, or electronic-attack execution content.  
**Integrity rule:** Citations are landmark works that exist in the public scholarly record. No fabricated DOIs.

---

## Abstract

Counter-uncrewed aerial system (counter-UAS) defence against coordinated multi-object activity is fundamentally a data-science problem under missingness, sensor heterogeneity, and operational time pressure. The Counter-Swarm Defence platform is designed so that operators receive a fused air picture, behaviour indicators of possible coordination, and graded risk assessments that preserve uncertainty rather than collapsing evidence into unverified binary threat labels. This monograph develops the analytic foundations for that design: spatial–temporal clustering for proximity and group structure; trajectory similarity and formation stability metrics; anomaly detection with explainable feature attributions; Bayesian and evidential combination of modality reliability; probabilistic calibration and proper scoring; explicit missing-information panels; and simulation-based evaluation against digital-twin truth.

The central thesis is that **behaviour engines must emit indicators with uncertainty, and risk engines must emit graded assessments with rationale and missingness**, never silent “threat / no threat” decisions. Causality is treated carefully: Pearl’s structural framework is used only where interventions and counterfactuals are well-defined; most operational claims remain associational or predictive. Calibration follows Gneiting’s programme of proper scoring, calibration, and sharpness. Anomaly methods are anchored in the survey literature (Chandola, Banerjee, and Kumar; Hodge and Austin; and subsequent classical detectors such as LOF and Isolation Forest). The monograph maps methods onto Counter-Swarm services (`behaviour`, `risk`), event contracts (`behaviour.indicator.v1`, `risk.assessment.v1`), requirements (FR-BEH-*, FR-RSK-*), and product surfaces (evidence packs, missing-info panels, uncertainty bands). It closes with trade-offs, failure modes, proof obligations, an incremental build guide, and an evaluation protocol that refuses to treat simulator scores as live “confirmed threat.”

**Keywords:** swarm behaviour analytics; trajectory similarity; clustering; Bayesian fusion; Dempster–Shafer evidence; calibration; graded risk; missing information; counter-UAS decision support; simulation evaluation.

---

## 1. Introduction

### 1.1 Motivation

Defenders of fixed or mobile assets face asynchronous, incomplete signals from radar, electro-optical / infrared (EO/IR), radio-frequency (RF), acoustic, and other sensors. Each modality is locally informative and globally incomplete. When multiple objects move in ways that may indicate coordination, isolated detectors produce alert noise without a shared track picture, shared uncertainty, or a governed path from observation to human decision. The operational need is not a black-box “swarm score.” It is a defensible chain:

```
Observation → Evidence → Confidence → Behaviour indicators → Context → Graded risk → Human decision → Audit
```

This chain is the explicit risk framework in the platform’s Data Science analytics note and is restated in product journeys (suspected swarm: behaviour indicators elevate risk with an uncertainty band; the commander reviews an evidence pack and a missing-info panel). Requirements FR-BEH-001–003 and FR-RSK-001–004 encode the same discipline in contractual form: behaviour indicators with uncertainty; explainable anomaly features; behaviour alone never authorises response categories; risk from evidence, behaviour, context, and confidence; graded levels with rationale, not unverified binary threat; explicit missing information; versioned rules and models.

### 1.2 Problem restatement

In own words: given streams of multi-sensor observations transformed into tracks with covariance and quality metadata, compute (i) indicators that multi-object motion may be coordinated or anomalous relative to a background model, (ii) graded risk assessments that combine those indicators with context and sensor health, and (iii) operator-facing artefacts that make confidence, rationale, and missing information inspectable—without pretending that association equals causation or that a calibrated probability is a policy decision.

### 1.3 Ambiguities and underspecification

Several terms are operationally overloaded:

| Term | Ambiguity | Working definition in this monograph |
|---|---|---|
| Swarm | Biological flocking vs. coordinated UAS vs. dense independent traffic | **Multi-object coordination hypothesis** supported by measurable indicators (proximity clustering, trajectory similarity, timing synchrony), always uncertain |
| Threat | Object class vs. hostile intent vs. policy priority | **Graded risk** conditioned on evidence and context; never a silent binary label from analytics alone |
| Intent | Latent goal of remote operators | Generally **not identifiable** from kinematics alone; treat as speculative hypothesis with explicit caveats |
| Anomaly | Statistical rarity vs. operational relevance | Separate **novelty** (distributional) from **priority** (policy); both may feed risk factors |
| Calibration | Sensor metrology vs. probabilistic forecast calibration | Distinguish **sensor calibration age** (quality metadata) from **score calibration** (Gneiting / ECE / reliability diagrams) |

### 1.4 Assumptions (and how they can fail)

1. **Tracks exist with usable uncertainty.** If association fails or IDs switch, behaviour features poison risk. Mitigation: consume track quality flags, coasting state, and fusion conflicts; widen risk bands under conflict (product principle: widen uncertainty rather than force a pick).
2. **Background behaviour is learnable or rule-specifiable.** Dense civilian corridors, bird flocks, and hobby traffic can mimic “swarm-like” geometry. Mitigation: context layers (airspace class, known corridors, time-of-day priors) and simulation slices that include lookalikes.
3. **Operators can use graded uncertainty.** If UI collapses bands to colour alone, the science is wasted. Mitigation: product epistemic rules (distinguish observation, inference, prediction, recommendation, decision).
4. **Simulation approximates relevant sensor faults.** If twin faults omit bias, delay, or dropout patterns that dominate live ops, offline metrics overstate readiness. Mitigation: fault catalogue (DELAY, DROP, BIAS) tied to evaluation scenarios.
5. **Causality of “coordination” is rarely interventional.** We usually observe association among trajectories. Claiming that object A *caused* object B to manoeuvre requires stronger assumptions than the platform can typically justify. Mitigation: label outputs as indicators and predictive risk factors, not causal intent findings, unless a Pearl-style identification strategy is explicit and audited.

### 1.5 What must be true for success

- Behaviour outputs are versioned indicators with confidence and contributing features (FR-BEH-001/002).
- Risk outputs are graded, rationalised, missingness-aware, and versioned (FR-RSK-001–004).
- Neither module authorises physical effects; recommendations are category enums for human approval (FR-ALT-003/004; safety architecture).
- Evaluation uses twin truth offline; scorer output is never shown as live confirmed threat.
- Calibration and sharpness are measured; overconfident models are blocked by release gates.
- Audit can answer what / when / who / which model version / evidence / confidence / decision.

### 1.6 Non-goals

This monograph does not design kinetic effector logic, jammer waveforms, spoofing recipes, or autonomous engagement. It does not claim that kinematic clustering proves hostile intent. It does not treat large language models as authorities for risk finalisation. It does not invent citations.

### 1.7 Contribution map

| Chapter | Contribution |
|---|---|
| 2 | System grounding to Counter-Swarm architecture and contracts |
| 3 | Literature foundations with careful causality and calibration |
| 4 | Clustering for proximity and group structure |
| 5 | Trajectory similarity and formation metrics |
| 6 | Anomaly detection and explainability |
| 7 | Bayesian and evidential reasoning |
| 8 | Calibration, proper scores, and reliability |
| 9 | Graded risk and anti-binary design |
| 10 | Missing-information panels as first-class analytics |
| 11 | Simulation evaluation and proof obligations |
| 12 | Trade-offs and failure modes |
| 13 | Build guide for behaviour and risk engines |
| 14 | Open problems and research programme |
| 15 | Conclusions |
| 16 | References |

---

## 2. Counter-Swarm system context for analytics

### 2.1 Services and data path

In the software service catalogue, **behaviour** consumes tracks and emits coordination / anomaly indicators (stateless or batch-plus-stream). **Risk** consumes tracks, behaviour, and context, and emits assessments plus missing-info (rule-plus-model hybrid). Upstream: adapters, normaliser, event bus, detection, tracking, fusion. Downstream: alert policy, decision support, human approval, audit, operator console. Behaviour and risk across a site are central-primary in the MVP edge/central split; that matters for latency budgets and for where analytic state (rolling windows, cluster caches) lives.

Logical event contracts relevant to this monograph:

| Event | Producer | Consumers | Analytic meaning |
|---|---|---|---|
| `track.update.v1` | Tracking / fusion | Behaviour, risk, UI, audit | State estimate + covariance; coasting and conflict flags matter |
| `behaviour.indicator.v1` | Behaviour | Risk, UI | **Not a decision** |
| `risk.assessment.v1` | Risk | Alert, UI, audit | Graded + rationale + missing info + version |
| `sensor.health.v1` | Adapters | UI, risk context | Coverage gaps drive missing-info |
| `model.inference.v1` | Inference gateway | Audit, drift monitors | Versioned scores for calibration monitoring |

### 2.2 Requirements that bind data science

Behaviour (Stage priority S/M as documented):

- FR-BEH-001: proximity clustering, similar trajectories, timing coordination — with uncertainty.
- FR-BEH-002: anomaly scores explainable via contributing features.
- FR-BEH-003: behaviour modules shall not alone authorise response categories.

Risk:

- FR-RSK-001: assessments from evidence, behaviour, context, and confidence.
- FR-RSK-002: graded levels or scores with rationale; not unverified binary threat/no threat.
- FR-RSK-003: missing information explicitly listed when material.
- FR-RSK-004: rules/models versioned.

Cross-cutting: NFR-XAI-002 (calibration notes where applicable); testing strategy requires offline calibration (e.g., ECE) and swarm-density slices; product journeys require uncertainty bands and missing-info panels.

### 2.3 Product surfaces that analytics must feed

The operator console is not a dashboard of raw model logits. Relevant surfaces include: track uncertainty ellipses; evidence chains (obs → detection → track → behaviour? → risk); risk factors and missing-info lists; conflict strips that widen uncertainty; incident packs for suspected swarm; AI assistant citations that must ground in `risk.assessment.v1` and `behaviour.indicator` identifiers rather than free invention. Data science therefore owns not only estimators but the **semantic contract** of what those UI elements may claim.

### 2.4 Questions the platform must answer

Restating the Stage 0 analytics framework:

1. What observations exist?
2. How reliable are they?
3. Which likely refer to the same object?
4. How many objects may be present?
5. Are movement patterns unusual?
6. Is coordinated behaviour indicated?
7. How confident is the assessment?
8. What evidence supports it?
9. What information is missing?

Items 5–9 are the core of this monograph; items 1–4 are mostly owned by data engineering, tracking, and fusion, but behaviour/risk must **consume their quality metadata honestly**.

---

## 3. Literature foundations

### 3.1 Collective motion and “swarm-like” kinematics

Classic models of collective motion (Reynolds’ boids; Vicsek’s alignment-driven phase transition) show that simple local rules can produce macroscopic order. For defensive analytics, the lesson is dual: (i) coordinated appearance can arise from simple coupling, and (ii) similar appearance can arise without shared intent (e.g., common wind, shared corridors, independent pursuit of the same waypoint). Therefore **kinematic coordination indicators are evidence of pattern, not proof of command structure**.

### 3.2 Trajectory data mining and similarity

Trajectory similarity is a mature subfield: Dynamic Time Warping (DTW) and related elastic distances; Longest Common Subsequence (LCSS) variants for noisy trajectories; Fréchet and Hausdorff geometric distances; edit distances on symbolic discretisations; and survey treatments of trajectory mining (e.g., Zheng’s trajectory data mining survey tradition; Toohey and Duckham on similarity measures). For streaming counter-UAS tracks, computational cost, partial observability, and unequal sampling rates dominate textbook batch settings.

### 3.3 Clustering

Density-based clustering (DBSCAN and successors) is a natural fit for proximity grouping under noise. Model-based clustering and hierarchical methods remain useful for offline analysis and for choosing bandwidths. Graph clustering on proximity or similarity graphs supports “formation” views. The analytic risk is **reification**: a cluster ID is a computational object, not an ontological swarm.

### 3.4 Anomaly detection surveys

Chandola, Banerjee, and Kumar (2009) organise anomaly detection by problem formulation, techniques, and application domains, emphasising that “anomaly” is context-dependent. Hodge and Austin (2004) survey outlier methodologies across statistical, neural, and machine-learning families. Classical algorithms with operational relevance include Local Outlier Factor (Breunig et al., 2000), Isolation Forest (Liu, Ting, and Zhou, 2008), and one-class approaches in the support-vector tradition (Schölkopf et al.). Aggarwal’s outlier analysis programme stresses that high-dimensional and contextual anomalies need different treatments than point anomalies in low dimension.

For Counter-Swarm, anomalies may be: single-track kinematic novelty; multi-track coordination novelty; sensor-consistency anomalies; or policy-context anomalies (e.g., presence in a restricted volume). Conflating these types produces unexplainable scores and violates FR-BEH-002.

### 3.5 Probabilistic forecasting, calibration, and proper scoring

Gneiting and Raftery (2007) develop strictly proper scoring rules as the principled way to evaluate probabilistic forecasts. Gneiting, Balabdaoui, and Raftery (2007) articulate the maxim: maximise sharpness subject to calibration. Reliability diagrams, the Brier score, continuous ranked probability score (CRPS), and related tools operationalise that programme. For classifiers, Platt scaling (1999) and isotonic regression (Niculescu-Mizil and Caruana, 2005) remain baseline calibration maps; Guo et al. (2017) document miscalibration in modern neural networks and popularise temperature scaling and Expected Calibration Error (ECE) style diagnostics (building on earlier reliability work and Naeini et al.’s calibration error tradition).

Counter-Swarm implication: a behaviour or risk score that is sharp but uncalibrated will drive false confidence in the UI. Release gates should require calibration diagnostics on simulation and, later, on carefully labelled operational slices.

### 3.6 Bayesian and evidential reasoning

Bayesian updating is the default language for combining likelihoods when a joint model is credible (Gelman et al.; Murphy; Bishop). When models are incomplete, Dempster–Shafer theory of evidence (Dempster; Shafer, 1976) and transferable belief models (Smets) allow mass on ignorance explicitly—attractive for missing-sensor panels. The cost is interpretability for operators and careful handling of conflict (combination rules can behave counter-intuitively under high conflict). Hybrid designs—Bayesian within modalities, evidential across coverage gaps—are often more operable than pure belief-function stacks.

### 3.7 Causality (used carefully)

Pearl’s causality framework distinguishes association, intervention, and counterfactuals, and supplies graphical criteria for identification. In this domain:

- **Safe uses:** analysing effects of *our* system interventions that we control (e.g., does enabling an extra RF sensor reduce track fragmentation? does a UI change reduce time-to-acknowledge?). Offline A/B or interrupted time series with explicit graphs.
- **Unsafe uses:** asserting that similar trajectories *mean* that one UAS’s autopilot caused another’s path; asserting hostile command hierarchy from clustering alone; using “causal swarm intent” language in operator UI.

Where the monograph discusses coordination, it means **predictive and descriptive indicators**, unless an identification strategy is stated. Confusing \(P(y \mid x)\) with \(P(y \mid do(x))\) is a scientific and governance failure mode.

### 3.8 Human decision support under uncertainty

Situation awareness research (Endsley) and automation trust literature caution that opaque confidence destroys calibrated human–machine teams. Recognition-primed decision models (Klein) remind us that operators pattern-match under time pressure; therefore missing-info lists and rationale factors must be scannable, not essay-length. Product design owns layout; data science owns the honesty of the quantities displayed.

### 3.9 Tracking and fusion backdrop

Behaviour analytics sit atop tracking and fusion. Multi-object tracking literature (Reid’s MHT lineage; Blackman and Popoli; Bar-Shalom’s association and filtering programme; Mahler’s random finite set / PHD filter family) defines what track IDs and covariances mean. Data science must not invent certainty the tracker does not provide: coasting tracks grow uncertainty; ID switches scramble trajectory similarity; unresolved fusion conflicts should widen risk bands.

---

## 4. Spatial–temporal clustering for multi-object coordination indicators

### 4.1 Analytic goal

Clustering answers: which tracks are spatially and temporally proximate in a way that suggests a group structure worth operator attention? It does **not** answer: is this group hostile?

### 4.2 Feature spaces

Recommended default feature space for online proximity clustering:

- Position in a local ENU or site-projected frame (not raw lat/lon for metric clustering).
- Time synchronisation to a common clock with explicit watermarking for late observations.
- Optional velocity for “co-moving” clusters (objects near in space but opposing in velocity may be coincidental crossings).
- Optional altitude band separation (different flight levels may be independent even if ground projections overlap).

Quality gates: exclude or down-weight tracks marked `COASTING` beyond a threshold, tracks with exploded covariance, or tracks under active fusion conflict—unless a dedicated “uncertain group” indicator is desired.

### 4.3 Algorithmic families and trade-offs

**Approach A — Density-based (DBSCAN / HDBSCAN-class).**  
Core idea: groups are dense regions separated by sparsity.  
Gains: no need to pre-specify \(k\); noise points labelled as noise.  
Losses: parameter sensitivity (epsilon, minPts); struggles with variable density; streaming variants need careful windowing.  
Failure modes: corridor traffic forms elongated dense regions that look like “swarms”; parameter drift across sites.  
When it becomes a liability: multi-site deployment with one global epsilon.

**Approach B — Graph clustering on proximity graphs.**  
Edges if distance \(< \tau\) within time window \(\Delta t\); cluster via connected components or modularity methods.  
Gains: interpretable (“these IDs were mutually within 200 m for 8 s”); easy to explain in UI.  
Losses: threshold \(\tau\) is policy-laden; chain effects (A near B near C) can create large components.  
Failure modes: transitive chaining across a busy volume.  
Mitigation: require edge persistence over time; use velocity-compatible edges; cap component size for alerting.

**Approach C — Model-based / mixture models.**  
Gains: soft membership; uncertainty in assignment.  
Losses: heavier compute; model misspecification; harder streaming.  
Best role: offline analysis and simulation scoring, not necessarily MVP online path.

**Recommendation for Counter-Swarm MVP:** graph proximity with persistence filters for online indicators; HDBSCAN-class or equivalent for offline tuning and scenario analytics; expose parameters as versioned policy, not hidden constants.

### 4.4 Uncertainty in clustering

Cluster membership should carry:

- Soft score or stability across bootstrap temporal jitter.
- Fraction of member tracks that are coasting / low quality.
- Sensitivity band: how membership changes if \(\tau\) varies by \(\pm 20\%\).

Emit these into `behaviour.indicator.v1` as structured fields, e.g. indicator type `PROXIMITY_CLUSTER`, member track IDs, persistence duration, confidence, and contributing features. Confidence must decrease when members are low quality—even if geometry looks perfect.

### 4.5 Timing coordination

Beyond spatial proximity, timing synchronisation (aligned manoeuvre onsets, shared periodicities, simultaneous altitude changes) is a separate indicator family. Methods include cross-correlation of speed/heading time series, change-point alignment, and simple rule hits (“\(n\) tracks commence turn within \(\delta\) seconds”). Timing indicators are often higher specificity than spatial density alone but fail when sampling is irregular; always condition on observation rate.

### 4.6 Proof obligations for clustering indicators

Let \(G_t\) be the proximity graph at time \(t\). A minimal formal property for release:

1. **Determinism under identical inputs:** same track window and policy version \(\Rightarrow\) same indicator payload (bit-identical or within documented float tolerance).
2. **Monotonicity of missingness:** removing a sensor’s tracks must not silently *increase* confidence of a cluster that depended on them; confidence should be non-increasing when evidence is removed (unless a documented “conflict resolution” path applies).
3. **Non-authorisation:** indicator publication does not write `human.decision.v1` or integration handoff events.

These are testable in CI with golden scenarios from the simulation catalogue (e.g., coordinated trio vs. dense lookalike cluster).

---

## 5. Trajectory similarity and formation stability

### 5.1 Why similarity is not clustering

Clustering asks “who is near whom.” Similarity asks “who moves alike,” including objects that are spatially separated (parallel paths, spaced formations). Both feed coordination hypotheses; they can disagree (tight ball of diverse manoeuvres vs. spaced identical paths).

### 5.2 Distance families

| Family | Intuition | Strengths | Weaknesses in C-UAS streams |
|---|---|---|---|
| DTW / soft-DTW | Elastic alignment of time series | Handles local timing shifts | Costly; sensitive to outliers; needs normalisation |
| LCSS / EDR-style | Match under thresholds | Robust to gaps | Threshold tuning; discrete decisions |
| Fréchet / discrete Fréchet | Continuous curve resemblance | Geometric meaning | Sensitive to spikes; costly |
| Hausdorff | Set distance between sampled points | Simple | Ignores order/time |
| PCA / spline shape descriptors + Euclidean | Compact embeddings | Fast online | May miss timing nuance |
| Learned embeddings | Metric learning | Flexible | Data-hungry; calibration and drift risk |

### 5.3 Normalisation and frame choice

Compare trajectories in a common projected frame; normalise for:

- Start-time alignment (relative time from first co-visible sample).
- Optional translation invariance for shape-only similarity (formation pattern vs. absolute approach geometry). Absolute geometry matters for asset-relative risk; shape-only matters for “same manoeuvre library” indicators. **Do not mix without labelling which.**

Velocity and heading series often discriminate better than raw position for “coordinated turn” hypotheses.

### 5.4 Formation stability metrics

Useful derived metrics:

- Inter-track distance variance over a sliding window (tightness stability).
- Relative bearing consistency.
- Spacing entropy (very regular spacing may indicate structured formation; very irregular may indicate coincidental cluster).
- Leader–follower lag estimates (associational only; do not assert command hierarchy in UI copy).

### 5.5 Streaming computation pattern

Maintain per-track ring buffers of state (position, velocity) for window \(W\) seconds. On each tick or on track update:

1. Candidate generation: only compare pairs within a coarse spatial hash or within existing proximity graph neighbourhoods (avoid all-pairs at scale).
2. Compute similarity scores for candidates.
3. Persist edges above threshold with hysteresis (enter at \(s_hi\), exit at \(s_lo\)) to reduce flicker.
4. Emit indicators when connected similarity components persist for \(T\) seconds.

### 5.6 Uncertainty

Similarity confidence should incorporate:

- Overlap length of the compared windows (short overlap → low confidence).
- Average track quality over the window.
- Sensitivity to time-warping band width.

### 5.7 Trade-off summary

| Choice | Gains | Losses | Harder later if wrong |
|---|---|---|---|
| Rule thresholds on heading correlation | Explainable, fast | Brittle across airframes | Retuning per site becomes tribal knowledge |
| Full DTW all-pairs | High recall of elastic matches | CPU blow-up; latency NFR risk | Must rebuild candidate generation |
| Learned embeddings early | Fancy demos | Uncalibrated; opaque | Governance and audit debt |

**Recommendation:** start with normalised velocity/heading correlation plus discrete Fréchet or DTW on short windows for candidates; defer deep metric learning until labelled simulation and limited operational review data exist.

---

## 6. Anomaly detection without unexplainable “swarm scores”

### 6.1 Separate novelty from priority

A rare bird flock may be statistically anomalous and operationally low priority. A common corridor path aimed at a protected asset may be statistically normal and operationally high priority. Risk engines combine **novelty factors** with **context factors**; behaviour engines should label which.

### 6.2 Point, contextual, and collective anomalies

Following Chandola et al.’s taxonomy adapted to tracks:

- **Point:** single track feature vector outlier (speed, climb rate).
- **Contextual:** outlier given airspace class, time, sensor mode.
- **Collective:** a set of tracks is anomalous as a set (coordination patterns), even if each track is mundane alone.

Collective anomalies are the distinctive swarm-analytics problem. They require set-level features (cluster size, similarity graph density, synchrony scores) and must remain explainable (FR-BEH-002).

### 6.3 Classical detectors as baselines

- **LOF:** local density deviation; good for contextual geometric outliers; needs neighbourhood sizing.
- **Isolation Forest:** efficient; less natural for collective anomalies unless features are engineered at set level.
- **One-class SVM / SVDD:** useful offline; kernel and nu selection matter.
- **Statistical process control / residual charts** on kinematic residuals relative to a motion model: highly explainable (“exceeded turn-rate residual 3σ”).

Black-box deep autoencoders can be research options but fail the explainability and calibration bar unless paired with feature attributions and reliability diagnostics.

### 6.4 Explainability contract

Every anomaly score published to the bus should include a ranked list of contributing features with signs/directions, e.g.:

- high pairwise heading correlation (0.91)
- proximity persistence 12.4 s
- RF coverage missing for 2 of 3 members

This is what the product evidence pack cites. “Anomaly = 0.87” alone is non-compliant with FR-BEH-002 and with the analytics framework’s “what not to build” warning against black-box swarm scores.

### 6.5 Failure modes

1. **Training on the wrong background:** if “normal” is learned from quiet nights, daytime corridor traffic floods anomalies.
2. **Label leakage from simulation:** twin scripts that always place swarms in one quadrant teach spurious geography.
3. **ID switch poisoning:** tracker fragmentation creates false collective novelty.
4. **Adversarial nuisance (defensive awareness only):** an adversary who knows thresholds may slowly change spacing to stay under \(\tau\). Defence is hysteresis bands, multi-indicator fusion, and human review—not a promise of undetectable evasion immunity.

---

## 7. Bayesian and evidential combination of modality reliability

### 7.1 Why combination is required

Risk is not a function of kinematics alone. RF silence, EO classification conflict, radar SNR, and sensor health all change confidence. The risk engine must combine heterogeneous evidence without pretending modalities are conditionally independent when they are not (shared weather, shared geometry, common clock faults).

### 7.2 Bayesian template

Let \(H\) be a hypothesis of interest, e.g., “multi-object coordination indicator should be raised” or “risk band should be at least elevated given policy features.” Let \(e_1,\ldots,e_m\) be evidence elements (behaviour features, class posteriors, health flags).

A maintainable approach for MVP:

1. Encode a **factor graph** or naive-Bayes-with-documented-dependence-warnings for a small set of discrete hypotheses (risk grades).
2. Use likelihood ratios from simulation-calibrated tables where full generative models are unavailable.
3. Propagate track covariance into feature uncertainty (e.g., distance features as distributions, not points).

Posterior odds form:

\[
\frac{P(H \mid e)}{P(\neg H \mid e)} = \frac{P(H)}{P(\neg H)} \prod_{i} \frac{P(e_i \mid H)}{P(e_i \mid \neg H)}
\]

only under conditional independence. When independence fails, replace the product with a smaller set of joint factors or use copula / noisy-OR structures explicitly.

### 7.3 Evidential (Dempster–Shafer) template for ignorance

When a modality is **absent** (not merely low SNR), belief-function mass on the full frame \(\Theta\) represents ignorance better than forcing a 0.5/0.5 Bernoulli. Example: no RF coverage → do not invent an RF likelihood; assign mass to “unknown RF consistency” and list `MISSING_RF` in the missing-info panel (FR-RSK-003).

Dempster’s rule combines belief masses but can yield counter-intuitive normalisation under high conflict. Operational practice:

- Use evidential combination for **coverage / presence of evidence**.
- Use Bayesian or rule tables for **interpretation of present evidence**.
- On high conflict, **widen risk uncertainty** and surface conflict factors rather than producing a spuriously peaked posterior (aligns with product conflict UX).

### 7.4 Reliability weights

Modality reliability should be a function of:

- Declared sensor health and calibration age (quality metadata; FR-NRM-004 spirit).
- Empirical calibration of that modality’s detectors on recent slices.
- Geometry (EO confidence vs. range/lighting).

Reliability enters as likelihood tempering or as evidence discounting in DS theory. Both must be versioned (FR-RSK-004).

### 7.5 Causality caution inside fusion stories

Do not describe multi-sensor agreement as “causal confirmation of threat.” Agreement increases reliability of an observational claim (object present / kinematics such-and-such) under conditional independence assumptions; it does not identify intent. Pearl’s ladder: association is not intervention. UI and assistant copy must stay on the correct rung.

### 7.6 Architectural placement

Combination logic belongs in the **risk** service (and secondarily in fusion for track-level association confidence). Behaviour should publish raw-ish indicators with local confidence; risk performs cross-source aggregation and missingness accounting. This preserves FR-BEH-003 (behaviour alone does not authorise categories) and matches ICD-06/ICD-07 separation (`behaviour.indicator.v1` is not a decision; `risk.assessment.v1` is graded judgement).

---

## 8. Calibration, sharpness, and trust

### 8.1 The Gneiting programme applied

For any probabilistic output \(F\) (class probabilities, risk grade probabilities, behaviour indicator probabilities):

1. **Calibration:** events predicted with probability \(p\) should occur with frequency \(\approx p\).
2. **Sharpness:** among calibrated forecasts, prefer concentrated ones.
3. **Proper scoring:** evaluate with strictly proper scores (log score, Brier, CRPS) so that honesty is rewarded.

Reliability diagrams and ECE-style summaries are mandatory offline artefacts for model cards used by the inference gateway.

### 8.2 What to calibrate in Counter-Swarm

| Output | Calibration target | Notes |
|---|---|---|
| Detector confidence | Empirical precision by bin | Per modality, range, clutter slice |
| Track existence / quality | Match to twin truth existence | Not the same as class calibration |
| Behaviour indicator probability | Rate of true coordination scripts vs. lookalikes | Needs negative scenarios |
| Risk grade distribution | Policy-aligned outcomes on scenarios | Risk is partly normative; calibrate predictive components separately from policy thresholds |

Important: **policy thresholds are not calibration.** A well-calibrated 0.2 probability of “elevated coordination” may still map to a T2 alert if policy says so. Keep layers separate in code and in audit fields.

### 8.3 Recalibration methods

- Platt scaling / temperature scaling for scores with held-out sim + review sets.
- Isotonic regression when monotonicity is plausible and data suffice.
- Avoid repeatedly stacking calibrators without version control; each calibrator is a model version (FR-RSK-004; NFR-XAI-002).

### 8.4 Anti-patterns

- Training until Brier is good on the same scenarios used for threshold tuning (leakage).
- Displaying uncalibrated deep model logits as “confidence %” in UI.
- Using a single global ECE number to hide slice failures (night EO, dense swarm, coasting-heavy windows).

### 8.5 Monitoring in production

Subscribe to `model.inference.v1` samples and periodic offline replays. Alert on calibration drift and on sharpness collapse (models that hedge to 0.5 constantly after a data shift). Drift monitors are DE/ML operational concerns; DS owns the metric definitions and pass/fail policy.

---

## 9. Graded risk and the refusal to collapse to binary threat

### 9.1 Why binary collapse fails

Binary “threat / no threat” from analytics alone fails scientifically (intent not identified), operationally (alert fatigue or missed nuance), and legally/governance-wise (FR-RSK-002; safety architecture requiring human approval for categories). The platform’s executive definition explicitly requires assessing risk without collapsing uncertainty into false binaries.

### 9.2 Recommended risk state

A `risk.assessment.v1` payload should include at minimum:

- `grade`: ordered categorical (e.g., LOW / MODERATE / ELEVATED / HIGH) or a score plus mapped grade.
- `uncertainty_band`: interval or distribution summary (not a single false-precision float).
- `factors[]`: signed, human-readable contributions with evidence links (track IDs, behaviour indicator IDs, sensor health IDs).
- `missing_info[]`: material absences (FR-RSK-003).
- `policy_version` / `model_version`: provenance (FR-RSK-004).
- `recommendations[]` (optional): category enums only, never effector commands.
- `conflicts[]`: unresolved fusion/class conflicts that widened the band.

### 9.3 Factorisation of risk

Conceptually:

\[
\text{RiskGrade} = f(\text{exposure}, \text{kinematics}, \text{behaviour indicators}, \text{classification hypotheses}, \text{context}, \text{confidence})
\]

with \(f\) implemented as versioned rules plus optional calibrated models. Exposure might include proximity to protected asset volumes; context includes schedules, NOTAMs-like layers, known friendly activity. Behaviour indicators enter as factors, not as overrides that auto-fire integration APIs.

### 9.4 Mapping to alerts

Alert tiering is a **policy evaluation** on risk/track events (ICD-08 path), synchronous and auditable. Data science supplies the assessment; it does not silently mutate policy. Auto-open incidents from behaviour+risk (product decision D-UI-03) must remain a configurable policy with human-visible rationale, not a hidden model side effect.

### 9.5 Worked narrative (non-weaponised)

Scenario aligned to Journey J2: tracks T-104, T-105, T-109 show proximity clustering and trajectory similarity; RF missing on T-109; risk elevated with widened band; commander sees missing-info “RF on T-109” and evidence citations. The correct analytic behaviour is to elevate grade and list missing RF—not to invent an RF classification, not to output `THREAT=true`, and not to authorise any physical response category without a human decision record.

---

## 10. Missing-information panels as first-class analytics

### 10.1 Missingness is not low confidence

Low confidence says “we measured, but the estimate is noisy.” Missing information says “a material channel or context layer is absent.” Operators need both. Collapsing absence into a middling score hides actionable cueing (“slew EO,” “check RF coverage,” “wait for track maturity”).

### 10.2 Materiality rules

A missing-info item is material when, under the current policy version, its presence could change grade, uncertainty band width, or recommended category set. Examples:

- No independent modality confirming a track near an asset volume.
- Behaviour cluster members without classification hypotheses.
- Sensor health covering the volume marked DEGRADED or OFF.
- Track coasting beyond threshold while risk grade depends on kinematics.
- Absent context layer (e.g., schedule feed stale) when policy references it.

### 10.3 Schema sketch

```json
{
  "missing_info": [
    {
      "code": "MISSING_RF",
      "track_ids": ["T-109"],
      "materiality": "HIGH",
      "cue": "No RF association in current coverage",
      "related_sensor_health": ["RF-2"]
    }
  ]
}
```

Codes should be enumerated and stable for UI and for assistant citations.

### 10.4 Interaction with evidential reasoning

Missingness maps cleanly to DS mass on ignorance or to Bayesian nodes explicitly marginalised as unobserved. Implementation choice matters less than **exporting the list**. FR-RSK-003 is satisfied only if the panel is populated, not merely if internal maths handled NaNs.

### 10.5 Evaluation of missing-info quality

Simulation should include faults that remove modalities. Score:

- Recall of material missing items (did we list what the scorer knows is absent?).
- Precision (did we spam irrelevant missing items?).
- Cue usefulness (did the listed cue match the instructor’s expected next action category—cue sensor, wait, escalate—without prescribing harming actions).

---

## 11. Simulation-based evaluation and proof

### 11.1 Twin truth vs. operator display

The digital twin holds truth objects and swarm scripts; sim adapters publish observations through the same contracts as real adapters. Offline scorers compare estimates to truth. **Scorer output is not shown as live confirmed threat** (simulation evaluation doc). This boundary protects operators from circular certainty.

### 11.2 Metric families for behaviour and risk

| Family | Examples | Pass intent |
|---|---|---|
| Detection / tracking backdrop | Precision/recall, ID switches, MOTA/IDF1-like | Behaviour inputs sane |
| Behaviour indicator | Precision/recall vs. scripted coordination; false positive rate on lookalike dense traffic | FR-BEH-001 quality |
| Explainability | Feature attribution present on 100% of anomaly indicators | FR-BEH-002 |
| Risk grade | Agreement with scenario expectations within band; no illegal binary field | FR-RSK-002 |
| Missing info | Material missing recall/precision under DROP/BIAS/DELAY faults | FR-RSK-003 |
| Calibration | ECE/Brier/CRPS on predictive components by slice | NFR-XAI-002 / testing strategy |
| Latency | Behaviour and risk within NFR budgets after track update | Operational fitness |
| Safety | No path from indicator to integration handoff without `human.decision.v1` | FR-BEH-003, FR-ALT-004 |

### 11.3 Scenario design (minimum set)

Align to simulation catalogue themes:

- Coordinated trio (true positive coordination).
- Dense swarm-like cluster of independent objects (false coordination lookalike; alert fatigue test).
- Partial modality dropout mid-incident (missing-info and confidence widening).
- Track coast / reacquire (uncertainty growth).
- Fusion conflict (widen band, do not force pick).
- Timing-synchronised manoeuvre without tight spatial cluster (similarity without proximity).

Each scenario needs expected observable outcomes for console and for offline thresholds—not a single scalar “threat score.”

### 11.4 Proof sketch: non-authorisation invariant

**Claim.** The behaviour service cannot alone authorise a response category.

**Argument.** Authorisation requires `human.decision.v1` (approval service) before `integration.handoff.v1`. Behaviour publishes only `behaviour.indicator.v1`. Alert and recommendation services may consume risk, but recommendations are non-executing category enums. CI contract tests assert no producer path from behaviour module credentials to integration topic without approval events. This is an architectural safety invariant, not a statistical theorem—but it is a proof obligation in the engineering sense (testable, falsifiable, audited).

### 11.5 Proof sketch: evidence removal monotonicity (local)

**Claim (design target).** For risk confidence \(c\) derived from evidence set \(E\), if \(E' \subset E\) by removing a supporting modality without adding conflict-resolving information, then \(c(E') \le c(E)\) under the declared combination rule.

**Note.** This fails for some DS conflict normalisations and for models that treat absence as negative evidence incorrectly. Therefore treat monotonicity as a **property to verify on the chosen rule**, with unit tests on synthetic evidence sets. Where conflict exists, the correct behaviour is often wider bands, not higher confidence.

### 11.6 Causal evaluation (limited, legitimate)

Use Pearl-style thinking for **system interventions we control**, e.g., estimate the effect of enabling an additional simulated sensor on ID-switch rate, with scenario randomisation. Do not claim causal identification of hostile intent from observational kinematics in the twin.

---

## 12. Trade-offs and failure modes

### 12.1 Major design decisions

**Decision 1 — Indicators vs. monolithic swarm score.**  
Gains: explainability, audit, modular testing.  
Losses: more UI complexity; more engineering interfaces.  
Risk if reversed: governance failure and FR violations.

**Decision 2 — Rules-first risk with optional models.**  
Gains: operable MVP; clear versioning; easier safety review.  
Losses: less flexible; may underfit complex patterns.  
Liability: hidden Python notebooks becoming production policy without versions.

**Decision 3 — Central behaviour/risk for MVP.**  
Gains: simpler ops; cross-sensor correlation.  
Losses: backhaul dependence; edge autonomy limited.  
Mitigation: keep schemas edge-promotable.

**Decision 4 — Graph proximity + persistence for online clustering.**  
Gains: explainable; cheap.  
Losses: threshold brittleness.  
Mitigation: site-calibrated policy packs; simulation regression.

**Decision 5 — DS ignorance for missing modalities.**  
Gains: honest missing-info.  
Losses: operator training needed; combination complexity.  
Mitigation: keep DS shallow; export codes humans understand.

### 12.2 Ranked failure modes (analytics-centric)

1. **Tracker ID switches** → false coordination / broken similarity (evidence: MOT metrics; fix: consume quality, delay behaviour on unstable IDs).
2. **lookalike density** → false behaviour indicators (evidence: SCN dense cluster; fix: context + timing features + calibrated thresholds).
3. **uncalibrated confidences** → operator overtrust (evidence: reliability diagrams; fix: temperature scaling + display discipline).
4. **missingness collapsed into 0.5** → wrong cues (evidence: dropout scenarios; fix: explicit missing_info).
5. **policy leakage into behaviour** → behaviour effectively authorises (evidence: bus ACLs / contract tests; fix: hard service separation).
6. **sim-reality gap** → false release confidence (evidence: live shadow mode disagreement; fix: fault catalogue expansion, slice metrics).
7. **causal language in UI** → legal/governance exposure (evidence: copy review; fix: indicator wording standards).
8. **all-pairs DTW** → latency budget breach (evidence: p95 NFR; fix: candidate gating).

### 12.3 Pre-ship gate (constitution style)

| Question | Answer | Justification |
|---|---|---|
| Understand failure modes? | YES if Section 12.2 tests exist in CI | Otherwise NO |
| Observable in prod? | YES if inference samples + risk versions audited | Need dashboards |
| Safe rollback? | YES if policy/model versions switchable | Registry required |
| Complexity proportional to value? | YES for rules+indicators MVP; NO if deep causal intent models added early | Defer |
| Want 3-year ownership? | YES if explainable factors and tests; NO if black-box swarm score | Architectural |

---

## 13. Build guide: from Stage 0 to operable engines

### 13.1 Module boundaries

```
behaviour/
  features/          # windowed kinematics, pair features
  cluster/           # proximity graph, persistence
  similarity/        # candidate pair scores
  anomaly/           # explainable scores
  emit/              # behaviour.indicator.v1 mapper
risk/
  factors/           # evidence assembly
  combine/           # Bayesian / rules / DS ignorance
  missing/           # materiality engine
  grade/             # graded output + band
  emit/              # risk.assessment.v1 mapper
eval/
  scenarios/         # twin configs expectations
  scores/            # proper scores, ECE, behaviour PR
  reports/           # model cards fragments
```

Interfaces first: protobuf/JSON schemas frozen with DE/SE; golden fixtures committed.

### 13.2 Incremental milestones

**M0 — Contracts and fixtures.**  
Freeze indicator types, risk grades, missing-info codes. Publish consumer stubs in UI with mock payloads.

**M1 — Deterministic behaviour rules.**  
Proximity graph + persistence; heading correlation similarity; emit indicators with feature lists. No ML required.

**M2 — Risk rules + missing-info.**  
Factor table from tracks, behaviour, sensor health; graded output; material missing codes; version field.

**M3 — Simulation regression.**  
P0 scenarios nightly; thresholds file; block release on regressions.

**M4 — Calibration harness.**  
Reliability diagrams for any probabilistic components; slice ECE.

**M5 — Limited models.**  
Optional calibrated classifiers on set features; temperature scaling; shadow mode before controlling alerts.

**M6 — Drift and site packs.**  
Per-site threshold packs; monitoring; canary.

### 13.3 Implementation notes (engineering, not weapons)

- Use projected coordinates; document CRS.
- Watermark late tracks; define recompute policy for behaviour windows.
- Hysteresis on all binary-ish indicator entries to reduce flicker.
- Hard timeout budgets; degrade to fewer pair comparisons under load (operational resilience).
- Never log raw sensitive payloads beyond policy; follow SG retention.
- Unit test monotonicity and non-authorisation invariants.
- Feature flags for each indicator family.

### 13.4 Collaboration boundaries

- DS owns methods, metrics, scenario expectations, calibration definitions (agent matrix).
- ML owns model training/serving when models appear; DS owns evaluation design.
- DE owns analytic export paths and schemas.
- PD owns presentation; DS owns numeric honesty.
- SG owns veto on causal overclaim and safety boundaries.
- SE/SYS own ICD approval and latency budgets.

### 13.5 What not to build (explicit)

- Black-box swarm score without factors.
- Leaderboards that incentivise overclaiming detections.
- LLM-only risk finalisation.
- UI copy that says “hostile intent confirmed” from clustering.
- Any analytic path that bypasses human approval for external categories.

---

## 14. Open problems and research programme

1. **Identifiability of coordination vs. shared environment:** wind and corridor effects as confounders; need context features and possibly causal graphs for *environment* interventions, not intent.
2. **Calibration under severe class imbalance and shifting priors:** proper scores with time-varying base rates.
3. **Collective anomaly benchmarks** for defensive C-UAS with lookalike negatives—public benchmarks are scarce; twin scenario libraries must compensate.
4. **Scalable streaming Fréchet/DTW** with provable candidate pruning.
5. **Operator-calibrated displays:** whether showing intervals improves decisions (human-subjects studies with PD).
6. **Cross-site transfer** of behaviour thresholds without silent miscalibration.
7. **Formal verification** of policy engines that map risk to alert tiers (model checking of safety invariants).

Pass 2+ of the research programme should deepen proofs, expand related work, and add empirical results from twin campaigns without fabricating citations.

---

## 15. Conclusions

Swarm behaviour analysis for counter-UAS defensive decision support is a problem of **indicators, uncertainty, and graded risk**, not binary threat oracles. Clustering and trajectory similarity supply measurable coordination hypotheses; anomaly detection must remain explainable and must separate novelty from policy priority; Bayesian and evidential methods combine modalities while exporting ignorance as missing information; calibration à la Gneiting keeps probabilistic outputs honest; simulation against twin truth provides regression proof without contaminating the live console with scorer “confirmation.”

Tied to Counter-Swarm, these principles instantiate as the `behaviour` and `risk` services, their event contracts, FR-BEH/FR-RSK requirements, and product surfaces that already demand uncertainty bands and missing-info panels. The build path is deliberately boring first: deterministic, versioned, testable indicators and rules; then calibrated models; always human approval before external categories. Causality is respected by restraint. Weaponisation content is out of scope by design.

The measure of success is not a higher swarm score. It is whether a commander can see why risk elevated, what is missing, how uncertain the claim is, and what evidence an auditor would reconstruct tomorrow.

---

## 16. References

Aggarwal, C. C. (2013). *Outlier Analysis*. Springer.

Bar-Shalom, Y., Willett, P. K., & Tian, X. (2011). *Tracking and Data Fusion: A Handbook of Algorithms*. YBS Publishing.

Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

Blackman, S., & Popoli, R. (1999). *Design and Analysis of Modern Tracking Systems*. Artech House.

Breunig, M. M., Kriegel, H.-P., Ng, R. T., & Sander, J. (2000). LOF: Identifying density-based local outliers. *Proceedings of ACM SIGMOD*.

Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys, 41*(3), 1–58.

Dempster, A. P. (1967). Upper and lower probabilities induced by a multivalued mapping. *Annals of Mathematical Statistics, 38*(2), 325–339.

Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64.

Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *KDD*.

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.

Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society: Series B, 69*(2), 243–268.

Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association, 102*(477), 359–378.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *Proceedings of ICML*.

Hodge, V., & Austin, J. (2004). A survey of outlier detection methodologies. *Artificial Intelligence Review, 22*, 85–126.

Klein, G. (1993). A recognition-primed decision (RPD) model of rapid decision making. In *Decision Making in Action*. Ablex.

Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008). Isolation forest. *Proceedings of IEEE ICDM*.

Mahler, R. P. S. (2007). *Statistical Multisource-Multitarget Information Fusion*. Artech House.

Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.

Niculescu-Mizil, A., & Caruana, R. (2005). Predicting good probabilities with supervised learning. *Proceedings of ICML*.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Platt, J. (1999). Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. In *Advances in Large Margin Classifiers*. MIT Press.

Reid, D. B. (1979). An algorithm for tracking multiple targets. *IEEE Transactions on Automatic Control, 24*(6), 843–854.

Reynolds, C. W. (1987). Flocks, herds, and schools: A distributed behavioral model. *Computer Graphics (SIGGRAPH), 21*(4), 25–34.

Sakoe, H., & Chiba, S. (1978). Dynamic programming algorithm optimization for spoken word recognition. *IEEE Transactions on Acoustics, Speech, and Signal Processing, 26*(1), 43–49.

Schölkopf, B., Platt, J. C., Shawe-Taylor, J., Smola, A. J., & Williamson, R. C. (2001). Estimating the support of a high-dimensional distribution. *Neural Computation, 13*(7), 1443–1471.

Shafer, G. (1976). *A Mathematical Theory of Evidence*. Princeton University Press.

Smets, P., & Kennes, R. (1994). The transferable belief model. *Artificial Intelligence, 66*(2), 191–234.

Toohey, K., & Duckham, M. (2015). Trajectory similarity measures. *SIGSPATIAL Special, 7*(1), 43–50.

Vicsek, T., Czirók, A., Ben-Jacob, E., Cohen, I., & Shochet, O. (1995). Novel type of phase transition in a system of self-driven particles. *Physical Review Letters, 75*(6), 1226–1229.

Zheng, Y. (2015). Trajectory data mining: An overview. *ACM Transactions on Intelligent Systems and Technology, 6*(3), 1–41.

---



## 17. Extended method catalogue: from features to factors

### 17.1 Single-track feature library

Behaviour and risk both need a stable feature dictionary. Features should be computable from `track.update.v1` windows without reading raw pixels in the critical path (raw media stays in object storage for offline review).

**Kinematic.** Ground speed; vertical rate; turn rate; specific energy proxy; path curvature; stop-start counts; time-in-volume for protected geometries.

**Uncertainty-aware.** Trace of position covariance; coasting duration; time since last association; number of supporting modalities; fusion conflict boolean.

**Contextual.** Local time bin; airspace class encoding; distance to asset; distance to known corridor centreline; sensor coverage flags at current position.

Each feature declaration includes unit, valid range, missing policy, and whether it may appear in operator-facing attributions. Features that are too technical for UI still may drive scores but then need mapped human labels.

### 17.2 Pairwise and set features

**Pairwise.** Distance; closing speed; relative heading; heading correlation; lag estimate; DTW/Fréchet distances; co-visibility time.

**Set / collective.** Component size; mean pairwise similarity; synchrony index (fraction of members with change-point in \(\delta\)); spacing coefficient of variation; fraction coasting; fraction with class conflict; modality coverage histogram.

Collective features are the right inputs to `COLLECTIVE_ANOMALY` and to risk factors, not an opaque embedding alone.

### 17.3 From features to behaviour indicators

Transformation rules should be monotonous and testable where possible: larger persistence should not decrease proximity confidence holding quality fixed. When non-monotonic ML is introduced, document and constrain with monotonic calibrated wrappers if policy requires.

### 17.4 From indicators to risk factors

Many-to-many mapping is allowed (one indicator feeds multiple factors; one factor aggregates multiple indicators), but audit must expand to evidence refs. Avoid double-counting the same kinematic signal as both a behaviour factor and a raw kinematic factor without weight caps.

### 17.5 Temporal aggregation

Operators think in incidents, not in 1-second ticks. Aggregate indicators with:

- peak confidence in window
- time-above-threshold
- trend (increasing persistence)

Risk assessments should be re-emitted on meaningful change (grade change, new missing_info, band widen), not on every track tick, to protect UI and audit volume—while still meeting latency NFRs when a meaningful change occurs.

---

## 18. Uncertainty taxonomy for Counter-Swarm analytics

### 18.1 Aleatoric vs. epistemic (operationalised)

**Aleatoric:** sensor noise, inherent process randomness—represented in covariances and stochastic twin faults.  
**Epistemic:** model misspecification, unknown coordination status, missing modalities—represented in missing_info, widened bands, DS ignorance mass, and ensemble disagreement.

Kendall and Gal’s distinction (what uncertainties we need in Bayesian deep learning) is useful vocabulary, but the platform should expose **operational** uncertainty types operators can act on: measurement noise, association doubt, coverage gap, model disagreement, policy ambiguity. Policy ambiguity (“is this grade worth T3?”) is not a DS probability; it is a command decision.

### 18.2 Second-order uncertainty

When calibrators themselves are fit on small samples, consider beta-binomial or bootstrap intervals on ECE and on grade posteriors. Showing second-order clouds in UI is optional; storing them for offline governance is valuable.

### 18.3 Conflict as a first-class uncertainty source

Fusion conflict and class conflict are not averageable into a happy medium without cost. Product guidance already says widen uncertainty rather than force a pick. Analytics must implement that as band expansion and conflict factors, not as silent averaging of incompatible modes.

---

## 19. Simulation design for behaviour/risk scientific validity

### 19.1 Threats to validity

| Threat | Example | Mitigation |
|---|---|---|
| Construct | “Coordination” script ≠ real C2 | Multiple scripts; avoid intent labels |
| Internal | Seed leakage into thresholds | Held-out seeds; pre-registration |
| External | Twin sensors too clean | Fault catalogue DELAY/DROP/BIAS |
| Statistical | Too few Monte Carlo runs | Power analysis on FPR bounds |
| Ecological | Operators not in loop | PD studies on console builds |

### 19.2 Negative corpus importance

A behaviour suite without strong negatives will overfit to “any density = swarm.” Mandatory negatives: independent dense traffic; bird-like wandering; converging waypoints without synchrony; staggered launches with different headings.

### 19.3 Fault injection for missing-info

Independently inject DROP of RF sector, EO glare, radar bias, clock delay. Expected analytic outcomes are specified a priori. Scorers measure missing_info recall and unjustified confidence.

### 19.4 Reproducibility

Scenario config + seed + policy pack version + code hash must reproduce indicators within tolerance. Store these in evaluation reports. Bit-flaky floating point across CPU architectures should be bounded and documented.

---

## 20. Governance hooks for analytic claims

### 20.1 Model cards (analytic section)

Each probabilistic component ships a card fragment: intended use, out-of-scope uses (intent confirmation), training/eval data (sim IDs), metrics (Brier/ECE by slice), failure modes, version, approver.

### 20.2 Claim tiers

Define claim tiers for UI and assistant:

- **T0 Observation:** measured/track fields
- **T1 Inference:** behaviour indicators
- **T2 Assessment:** graded risk
- **T3 Recommendation:** category enum
- **T4 Decision:** human only

Analytics may produce T1–T3; never T4. Mixing tiers in one sentence is a copy defect.

### 20.3 Red-team prompts for overclaim

SG/DS joint exercise: attempt to make the assistant say “hostile intent confirmed” from clustering alone; the allowlisted tools must refuse or rephrase. This is governance testing, not offensive cyber content.

---

## 21. Comparative notes on classical vs. deep trajectory models

Classical elastic distances and correlation features remain the backbone for MVP explainability. Deep sequence models (temporal convolutions, sequence autoencoders, transformer set models) can propose additional features in shadow mode. Requirements for promotion:

1. Slice-calibrated probabilities
2. Stable attributions or surrogate features that match FR-BEH-002
3. No worsening of lookalike FPR beyond bound
4. Latency within budget with candidate gating
5. Versioned artefacts and rollback drills

Until then, deep models are research options, not risk authorities.

---

## 22. Metrics dictionary (normative for DS eval packs)

| Metric | Definition sketch | Use |
|---|---|---|
| Behaviour precision | TP indicators / emitted indicators vs. script mask | Quality |
| Behaviour recall | TP / scripted coordination events | Quality |
| Lookalike FPR | Indicators on negative dense scenarios | Safety ops |
| Attribution coverage | Fraction of anomaly indicators with ≥1 feature | FR-BEH-002 |
| Missing-info recall | Material codes listed / material codes true | FR-RSK-003 |
| Grade agreement | Match to expected grade set (not exact if band OK) | Scenario |
| Band hit rate | Truth grade ∈ predicted band | Uncertainty honesty |
| Brier / Log / CRPS | Proper scores | Calibration |
| ECE | Bin reliability gap | Calibration |
| p95 latency | Track update → assessment visible | NFR |
| Illegal binary rate | Count of forbidden threat boolean fields | Compliance (must be 0) |

---

## Appendix A — Mapping to Counter-Swarm artefacts

| Monograph concept | Platform artefact |
|---|---|
| Behaviour indicators | Service `behaviour`; event `behaviour.indicator.v1`; FR-BEH-* |
| Graded risk + missing info | Service `risk`; event `risk.assessment.v1`; FR-RSK-* |
| Uncertainty bands | Product journeys; UI tokens; conflict widen policy |
| Calibration notes | NFR-XAI-002; testing strategy ECE |
| Simulation scoring | `docs/simulation/05-evaluation-and-scoring.md`; twin truth offline |
| Non-binary threat | FR-RSK-002; analytics framework; executive definition |
| Agent ownership | Agent 6 DS in responsibility matrix |

## Appendix B — Indicator type catalogue (draft)

| Code | Family | Inputs | Uncertainty drivers |
|---|---|---|---|
| `PROXIMITY_CLUSTER` | Clustering | Positions, \(\tau\), persistence | Coasting members, \(\tau\) sensitivity |
| `TRAJECTORY_SIMILARITY` | Similarity | Windowed state pairs | Overlap length, quality |
| `TIMING_SYNC` | Timing | Change-points, correlations | Sampling irregularity |
| `FORMATION_STABILITY` | Formation | Spacing variance, bearings | Short windows |
| `KINEMATIC_ANOMALY` | Anomaly | Residuals, LOF-like features | Background model drift |
| `COLLECTIVE_ANOMALY` | Collective | Set features | Lookalike density |

## Appendix C — Risk factor catalogue (draft)

| Factor code | Source | Direction example |
|---|---|---|
| `BEH_PROXIMITY` | behaviour indicator | + toward elevated |
| `BEH_SIMILARITY` | behaviour indicator | + toward elevated |
| `ASSET_EXPOSURE` | context geometry | + with closing range |
| `CLASS_HYP_CONFLICT` | fusion/class | + widen band |
| `SENSOR_COVERAGE_GAP` | sensor.health | + missing_info / widen |
| `TRACK_COASTING` | track state | + widen / reduce kinematic weight |
| `KNOWN_CORRIDOR` | context | − toward false coordination |

## Appendix D — Evaluation checklist (release)

- [ ] Golden scenarios: coordinated positive, dense lookalike, dropout, coast, conflict, timing-only
- [ ] Behaviour precision/recall and FPR on lookalikes within thresholds
- [ ] 100% anomaly indicators carry feature attributions
- [ ] Risk payloads include grade, band, factors, missing_info, versions
- [ ] No binary threat field in schema
- [ ] Calibration report attached for probabilistic components
- [ ] Latency p95 within NFR after track update
- [ ] Contract test: no behaviour→integration handoff without human decision
- [ ] Copy review: no unjustified causal intent claims
- [ ] Model/policy versions recorded on assessments

## Appendix E — Glossary

| Term | Meaning |
|---|---|
| Indicator | Versioned behavioural claim with confidence; not a decision |
| Graded risk | Ordered assessment with rationale and uncertainty |
| Missing info | Material absent evidence or context, listed explicitly |
| Calibration | Match between stated probabilities and empirical frequencies |
| Sharpness | Concentration of a predictive distribution |
| Lookalike | Non-coordinated multi-object pattern that mimics swarm geometry |
| Coasting | Track propagation without fresh association; uncertainty grows |

---

## Appendix F — Extended mathematical notes

### F.1 Proximity graph persistence

Let \(d_{ij}(t)\) be distance between tracks \(i,j\) at time \(t\). Define edge \(e_{ij}(t)=1\) iff \(d_{ij}(t) \le \tau\) and both tracks pass quality gate \(q\). Persistence time:

\[
P_{ij}(t) = \int_{t-W}^{t} e_{ij}(u)\,du
\]

Emit cluster indicator if the connected component size \(\ge n_{\min}\) and \(\min_{(i,j)\in E} P_{ij}(t) \ge P_{\min}\). Confidence decreases with mean covariance trace of members and with fraction of coasting members.

### F.2 Heading correlation similarity

For heading series \(\theta_i, \theta_j\) on overlapping samples, use circular correlation or correlation of unwrapped \(\Delta\theta\) rates. Gate on minimum overlap \(L_{\min}\). Combine with mean speed ratio in \([1/\rho, \rho]\) to reject opposing traffic.

### F.3 Brier score and ECE

For probabilistic event \(o \in \{0,1\}\) and forecast \(p\):

\[
\mathrm{Brier} = \frac{1}{N}\sum (p_n - o_n)^2
\]

ECE partitions forecasts into bins \(B_k\) and averages \(|\mathrm{acc}(B_k)-\mathrm{conf}(B_k)|\) weighted by bin size. Report per slice (density, lighting, coasting fraction).

### F.4 Proper scoring and sharpness

A scoring rule \(S(F,y)\) is strictly proper if the expected score is uniquely maximised by reporting the true distribution. Calibration without sharpness yields useless hedges; sharpness without calibration yields overconfidence. Joint reporting of reliability diagrams and score values is mandatory in evaluation packs.

### F.5 Belief discounting for reliability

If modality \(m\) has reliability \(r_m \in [0,1]\), discount mass \(m_m\) toward ignorance:

\[
m'_m(A) = r_m m_m(A) \quad (A \neq \Theta),\quad m'_m(\Theta) = 1 - r_m + r_m m_m(\Theta)
\]

Export \(r_m < r_{\min}\) cases into missing_info or degraded_evidence factors rather than only burying them in maths.

---

## Appendix G — Worked offline evaluation vignette

**Scenario.** SCN-style coordinated trio vs. dense independent cluster; RF dropout on one member mid-run.

**Expected behaviour outputs.** Persistent `PROXIMITY_CLUSTER` and `TRAJECTORY_SIMILARITY` on the trio with confidence reduced after RF dropout only if RF was part of behaviour (it should not be); risk must list `MISSING_RF` after dropout; dense independent cluster may form proximity components but timing/similarity factors should remain low if scripts ensure diverse headings.

**Scoring.** Compare indicator on/off timelines to script masks with tolerance windows; compute Brier on probabilistic coordination flag; verify missing_info recall; verify UI-facing band widens after dropout without grade hallucination to HIGH solely from absence.

**Pass/fail.** Threshold file owned by DS; failures block release candidates once CI exists (simulation evaluation policy).

---

## Appendix H — Interface sketch for `behaviour.indicator.v1`

Conceptual fields (normative schemas under `/schemas` when frozen):

- `indicator_id`, `schema_version`, `policy_version`
- `type` (catalogue code)
- `track_ids[]`
- `time_window` {start, end}
- `score` (optional), `confidence`, `uncertainty`
- `features[]` {name, value, contribution}
- `stability` {persistence_s, sensitivity}
- `provenance` {service_version, code_hash}

Consumers must treat absence of a field as unknown, not zero.

## Appendix I — Interface sketch for `risk.assessment.v1`

- `assessment_id`, `schema_version`, `policy_version`, `model_version`
- `track_ids[]`, `incident_id?`
- `grade`, `uncertainty_band`
- `factors[]` {code, direction, weight, evidence_refs[]}
- `missing_info[]` {code, materiality, cue, refs[]}
- `conflicts[]`
- `recommendation_categories[]` (enum, optional, non-executing)
- `notes_for_ui` (non-causal constrained language)

## Appendix J — Operator language constraints (analytic)

Allowed: “coordination indicators present,” “elevated graded risk,” “RF association missing,” “track coasting; kinematic confidence reduced.”  
Disallowed without extraordinary evidenced identification: “hostile swarm confirmed,” “intent to attack,” “leader vehicle is X” as fact, “threat = true.”

---



## Appendix K — Architecture alternatives for behaviour and risk (mandatory exploration)

The governing constitution requires exploring multiple approaches before converging. This appendix records three end-to-end architectures for the analytic stack, with explicit trade-offs.

### K.1 Approach 1 — Streaming feature graph with rule risk (recommended MVP)

**Components.** Ring-buffer feature service; proximity graph worker; similarity worker on candidates; anomaly residual worker; risk rule engine with missingness materiality table; emitters to Kafka-compatible topics.

**Data ownership.** Behaviour owns indicator payloads; risk owns assessments; DE owns schemas and retention; ML owns nothing mandatory at MVP.

**Read path.** Operator UI reads projections from hot DB / realtime gateway fed by bus events.

**Write path.** Track updates trigger window recompute; indicators and assessments are idempotent by `(policy_version, track_set_hash, window_id)`.

**Scaling.** Horizontal scale of stateless workers with partitioned site keys; stateful window caches in Redis or embedded LRU with care for failover.

**Failure modes.** Redis eviction drops persistence state → indicator flicker; mitigate with rebuild-from-track-store on cache miss. Rule table drift across environments → enforce signed policy packs.

**When it becomes a liability.** Extremely high track counts with naive candidate generation; or sites needing rich learned collective anomalies before labels exist.

**Why it can be a bad idea.** May under-detect subtle coordination that only nonlinear embeddings catch; operationally, that is preferable to opaque over-detection in Stage 1.

**Verdict.** Best fit for Counter-Swarm Stage 1–2: matches FR explainability, versioning, and safety separation.

### K.2 Approach 2 — Batch analytic jobs with online thin alerts

**Components.** Micro-batch every \(N\) seconds materialises features in a warehouse; online path only runs coarse proximity rules; rich similarity/anomaly run near-online.

**Gains.** Easier complex joins; better for calibration jobs and model training exports.

**Losses.** Latency may miss NFR alert budgets if batch is the only path; dual paths risk inconsistency between “fast” and “rich” pictures.

**Failure modes.** Operators trust the fast path while the rich path silently disagrees; mitigate by UI labelling of provisional vs. confirmed analytic tiers—or avoid dual semantics entirely.

**When liability.** Multi-second batch under dense swarm scripts causes late incident offers.

**Verdict.** Use batch for evaluation and training exports; do not make batch the sole risk path for P0 journeys.

### K.3 Approach 3 — End-to-end learned “swarm risk” model

**Components.** Multi-agent trajectory encoder → set transformer → calibrated risk head; optional attention explanations.

**Gains.** Potential recall on complex patterns; single artefact demos well.

**Losses.** Data hunger; weak FR-BEH-002 unless attributions are engineered; calibration fragile under shift; governance burden; temptation to binary-threshold the head.

**Failure modes.** Spurious correlation with geography/time; sim overfitting; causal overclaim in saliency maps; bypass of missing-info if the model imputes silently.

**When liability.** Day-1 production ownership without twin negatives and site packs.

**Verdict.** Research track after M5 shadow mode; never sole authorisation input; always emit factors and missing_info alongside any model score.

### K.4 Comparative table

| Criterion | Approach 1 | Approach 2 | Approach 3 |
|---|---|---|---|
| Explainability | High | High (offline) | Medium–Low |
| Latency control | High | Medium | Medium |
| Label dependence | Low | Low–Medium | High |
| Calibration ops | Manageable | Strong offline | Hard |
| Safety review | Straightforward | Dual-path risk | Heavy |
| 3-year ownership | Favourable | Favourable if batch scoped | Risky early |

**Recommendation.** Approach 1 online; Approach 2 for eval/training; Approach 3 optional shadow.

---

## Appendix L — Deep dive: clustering parameter governance

### L.1 Site packs

Threshold \(\tau\), \(n_{\min}\), \(P_{\min}\), velocity compatibility \(\rho\), and quality gates differ by site geometry and traffic density. Treat them as a **policy pack** artefact:

- `site_id`, `pack_version`, `effective_from`
- numeric parameters with units
- scenario regression IDs that must pass before promotion
- signer / approver identity for audit

### L.2 Calibration of \(\tau\) without circularity

Do not tune \(\tau\) solely to maximise F1 on coordinated scripts. Jointly constrain:

- FPR on dense lookalike scenarios below bound \(f^*\)
- recall on coordinated scripts above bound \(r^*\)
- stability: small parameter perturbations should not flip indicators on golden windows (Lipschitz-like empirical test)

Plot Pareto fronts; choose operating points with commanders (PD-facilitated), not with silent DS optimisation.

### L.3 Variable density and hierarchical methods

HDBSCAN-class methods help when a single \(\tau\) fails across an airfield vs. approach corridor. Online hierarchical extraction is heavier; a pragmatic compromise is dual thresholds (tight formation vs. loose group) emitted as distinct indicator types rather than one overloaded cluster ID.

### L.4 Temporal clustering vs. snapshot clustering

Snapshot clustering at time \(t\) flickers. Persist edges; cluster the time-aggregated graph; or require component survival across \(K\) successive snapshots. Document which definition the UI means by “cluster since 12:03:10.”

---

## Appendix M — Deep dive: trajectory similarity under partial observability

### M.1 Unequal sampling and DTW windows

Radar updates may be 1 Hz while EO tracks burst higher. Resample to a common rate with uncertainty inflation for interpolated samples, or use distances designed for unequal sequences (LCSS). Always record the fraction of interpolated samples as a confidence penalty.

### M.2 Partial overlap

If two tracks co-exist for only 3 seconds, high DTW similarity is weak evidence. Enforce \(L_{\min}\) and report `overlap_s` in features. Risk should weight short-overlap similarity near zero.

### M.3 Affine and speed normalisation

Formation flying may share shape at different speeds. Separate indicators:

- `SHAPE_SIMILARITY` (time-normalised)
- `SPACE_TIME_SIMILARITY` (absolute)

Do not merge into one score without labelling. Asset-approach risk usually needs space-time, not shape-only.

### M.4 Fréchet interpretation for operators

Discrete Fréchet has an intuitive “leash” metaphor useful in explainability text: “paths remain within X m under optimal monotonic alignment.” Prefer such explanations over embedding cosine values.

### M.5 Computational budget control

Candidate generation hierarchy:

1. Spatial hash / tiles
2. Proximity graph neighbours and 2-hop
3. Optional coarse cheap similarity (heading correlation)
4. Expensive DTW/Fréchet on survivors

Load shed from step 4 first under CPU pressure; emit `DEGRADED_ANALYTICS` sensor-health-like flag into risk missing/degraded factors.

---

## Appendix N — Bayesian network sketch for graded risk (illustrative)

This is an illustrative factorisation for implementation workshops, not a claim of a unique correct model.

**Nodes (discrete).**

- \(C\): coordination_indicator_level {none, weak, strong}
- \(E\): asset_exposure {low, med, high}
- \(Q\): track_quality_aggregate {poor, ok, good}
- \(K\): class_conflict {no, yes}
- \(M\): material_missing_present {no, yes}
- \(R\): risk_grade {LOW, MODERATE, ELEVATED, HIGH}

**Example dependence.** \(R\) depends on \(C,E,Q,K,M\). \(C\) depends on behaviour features (deterministic upstream). \(M\) is partly observed from sensor health.

**CPT discipline.** Initialise from simulation histograms; freeze versions; do not silently online-learn CPTs in production without a training pipeline and shadow evaluation.

**Independence warnings.** \(Q\) and \(M\) are not independent of \(E\) (far objects have worse EO). Document correlated factors; prefer fewer joint tables over naive products when correlation is strong.

**Output.** Posterior over \(R\) displayed as grade = MAP or policy-selected quantile, with band = high-probability set (e.g., grades with cumulative mass \(\ge 0.9\)).

---

## Appendix O — Evidential example with missing RF

Frame \(\Theta = \{\mathrm{coord}, \mathrm{noncoord}\}\) for a behaviour-relevant hypothesis used inside risk (still not intent).

- Kinematic behaviour mass: \(m_k(\{\mathrm{coord}\})=0.6\), \(m_k(\Theta)=0.4\) (some ignorance remains).
- RF modality absent: \(m_{\mathrm{rf}}(\Theta)=1.0\).

Combination leaves ignorance from RF untouched; UI lists `MISSING_RF`. If instead a buggy implementation encoded missing RF as \(m(\{\mathrm{noncoord}\})=0.5, m(\{\mathrm{coord}\})=0.5\), the system would fake evidence. Contract tests should forbid fabricating balanced masses for absent modalities.

When EO later supports classification conflict, assign mass to conflict handling that widens the risk band rather than peak-picking.

---

## Appendix P — Calibration operations runbook (analytic)

1. **Collect** twin scenario runs + any reviewed operational clips with labels for the predictive claim only (e.g., “scripted coordination present”), never for unverifiable “hostile intent.”
2. **Slice** by density, coasting fraction, modality set, range.
3. **Plot** reliability diagrams; compute Brier, log score, ECE.
4. **Fit** calibrator on training split; evaluate on held-out scenarios.
5. **Register** calibrator version with base model version.
6. **Shadow** compare calibrated vs. raw for alert churn.
7. **Promote** only if slice metrics pass and churn is accepted by ops.
8. **Monitor** weekly ECE; rollback on breach.

This runbook is DS-owned; ML executes training; SE ensures registry hooks; SG reviews model cards.

---

## Appendix Q — Failure mode effects analysis (analytics FMEA excerpt)

| ID | Failure | Cause | Effect on operator | Severity | Detection | Mitigation |
|---|---|---|---|---|---|---|
| AF-01 | False coordination indicator | Lookalike density | Unnecessary incident load | 3 | Sim SCN lookalike FPR | Timing features, context, thresholds |
| AF-02 | Missed coordination | \(\tau\) too tight / ID switch | Late elevation | 4 | Sim coordinated recall | Dual thresholds, tracker quality gates |
| AF-03 | Overconfident grade | Uncalibrated model | Overtrust | 5 | ECE gate | Calibrator + UI band |
| AF-04 | Missing-info omitted | Materiality table gap | Wrong cueing | 4 | Dropout SCN | Table review + tests |
| AF-05 | Indicator flicker | No hysteresis | Distraction | 2 | UI telemetry | Enter/exit thresholds |
| AF-06 | Causal overclaim copy | Unconstrained assistant | Governance incident | 5 | Copy linter / tool allowlist | Language constraints Appendix J |
| AF-07 | Latency overrun | All-pairs DTW | Stale risk | 4 | NFR metrics | Candidate gating, load shed |
| AF-08 | Version skew | Unpinned policy | Irreproducible audit | 5 | Audit join tests | Signed packs |
| AF-09 | Coasting treated as fresh | Quality gate bug | False tightness | 4 | Coast SCN | Exclude/penalise coasting |
| AF-10 | Dual-path disagreement | Batch vs stream | Confusion | 3 | Diff monitors | Avoid dual semantics |

Severity 5 items are release blockers if unmitigated.

---

## Appendix R — Extended related work notes (honest scope)

A full related-work chapter would systematically cover maritime anomaly detection, ADS-B trajectory clustering in ATM, computer vision multi-object activity recognition, and military C2 literature on threat evaluation and weapon assignment (TEWA)—the last only at the level of **decision-support process patterns**, not effector control. This Pass 1 monograph cites landmark statistical and mining works and maps them into Counter-Swarm. Pass 2 should add a structured annotated bibliography with page-level notes, still without fabricated venues.

ATM and maritime domains supply useful negatives: lots of dense non-hostile traffic. Borrow evaluation design (lookalike stress tests) rather than borrowing threat labels.

---

## Appendix S — Statistical testing for indicator lift

When comparing policy pack A vs. B on a fixed scenario suite:

- Use paired tests on per-scenario scores (e.g., Wilcoxon signed-rank) rather than a single pooled F1.
- Control false discovery when slicing many metrics.
- Report effect sizes, not only p-values.
- Prefer pre-registered threshold files over post-hoc hunting.

For calibration comparisons, use Diebold–Mariano-style tests on proper scores where applicable, with care for dependence across overlapping windows (block bootstrap).

---

## Appendix T — Data quality contracts consumed by analytics

Behaviour and risk should hard-depend on upstream fields:

- `track.state` including `COASTING`
- covariance / uncertainty measures
- `conflict` flags from fusion
- `sensor.health` coverage polygons or sector status
- detection/track `model_version` when ML produced inputs
- observation `quality` and calibration age when present

If fields are absent, analytics must degrade via missing_info, not assume defaults that look healthy. Schema evolution follows DE ICD discipline.

---

## Appendix U — Privacy, sensitivity, and retention (analytic view)

Trajectory analytics can be sensitive even in defensive contexts. DS must:

- Prefer feature stores with retention aligned to DE policy.
- Avoid unbounded raw clip retention “for research” without SG approval.
- Separate training exports from operational hot paths.
- Scrub assistant contexts to evidence IDs rather than wholesale trajectory dumps when possible.

This is not a full threat model (see SG docs); it is an analytic data-minimisation stance.

---

## Appendix V — Worked numeric toy example (proximity + risk)

Three tracks at positions (metres ENU) at \(t\):

- T1: (0, 0), quality good
- T2: (80, 20), quality good
- T3: (90, 30), quality coasting

\(\tau = 150\) m → all pairs within τ. Persistence: T1–T2 and T2–T3 persist 10 s; T1–T3 persists 10 s. Component size 3 \(\ge n_{\min}=3\) → `PROXIMITY_CLUSTER` candidates.

Confidence penalty: one of three coasting → reduce confidence from 0.8 to 0.55 (example tempering). Similarity: heading correlation T1–T2 = 0.92, T2–T3 = 0.40 → formation claim weak; emit proximity without strong similarity factor.

Risk: exposure med; missing RF on T3 → `MISSING_RF` material; grade MODERATE with band {MODERATE, ELEVATED} rather than HIGH. Factors list proximity persistence and missing RF; not “hostile.”

This toy example is pedagogical; real systems use policy packs and calibrated tempering tables.

---

## Appendix W — Alignment to user journeys and UX principles

Journey J2 (suspected swarm) expects behaviour indicators, elevated risk with uncertainty band, evidence pack, missing-info panel. Analytics must produce the fields that make that journey true without dramatising.

UX principles call for simplifying under high load: analytics should support declutter by priority factors, not by deleting uncertainty. When the UI shows fewer tracks, risk versions and evidence IDs for hidden members must remain queryable in the incident pack.

Design tokens include uncertainty colour semantics; DS should not invent a second competing confidence encoding.

---

## Appendix X — Research ethics and defensive-only pledge

All methods are for detection, assessment, human decision support, and audit. The following are out of scope for this monograph and must not be “filled in” by later DS notes without SG escalation: effector aiming solutions, jammer control recipes, spoofing/deception playbooks, autonomous engagement policies. Simulation exists to test software, not to practise harm.

---

## Appendix Y — Pass 2 expansion backlog (word-integrity plan)

To grow toward dissertation-scale length without padding:

1. Annotated bibliography (50–80 landmark works) with 150–200 words each of critical notes.
2. Full proofs of monotonicity for the chosen combination rule with counterexamples for rejected rules.
3. Empirical twin campaign report (tables, reliability diagrams) once scenarios run in CI.
4. Human-subjects protocol with PD for uncertainty-band efficacy.
5. Site-transfer study design across two simulated geographies.
6. Formal model-checking appendix with SYS for alert policy invariants.

Each item adds substance; none invent citations.

---

## Appendix Z — Concise operational playbook for on-call DS

1. Indicator storm (too many clusters): check lookalike traffic, τ pack, hysteresis; compare to SCN baseline.
2. Missing elevations: check tracker ID switches and quality gates; review coordinated SCN recall.
3. Confidence looks “stuck” at 1.0: calibration broken or UI mapping raw scores; pull reliability report.
4. Audit cannot reproduce assessment: policy/model version skew; freeze packs.
5. Assistant invents factors: tool allowlist failure; disable assistant on risk path until fixed.
6. Latency page: enable load shed; verify degraded factor visible.

---

**End of monograph**

**Author:** Victor.I
