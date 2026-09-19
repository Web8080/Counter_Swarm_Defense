<!-- Author: Victor.I -->

# Deliverable 11 — Digital Twin / Simulation Architecture

**Author:** Victor.I  
**Status:** Draft for review  
**Goal:** Develop and validate the full software platform without operational hardware or harmful effects

---

## 1. Purpose

The digital twin provides a controlled world model that emits synthetic sensor observations (and faults) into the **same adapter contracts** as real sensors.

```
SIMULATED ENVIRONMENT
        │
        ▼
Synthetic Objects (truth state)
        │
        ▼
Sensor Models (physics/noise abstractions)
        │
        ▼
Synthetic Observations (+ faults)
        │
        ▼
Real Platform (normaliser → fusion → risk → UI)
        │
        ▼
Evaluation vs Truth (offline)
```

---

## 2. Components

| Component | Role |
|---|---|
| **Scenario director** | Loads scenarios; time control; seed |
| **Truth engine** | Object kinematics, swarm scripts, environment flags |
| **Sensor models** | Radar/EO/RF/acoustic abstractions with FOV, rate, noise, bias |
| **Fault injector** | Drop, delay, duplicate, corrupt, contradict, sensor death, link loss |
| **Sim adapters** | Publish candidate observations like real adapters |
| **Mock external system** | Receives category handoffs; returns canned acks/failures |
| **Scorer** | Compares tracks/risk to truth for metrics |
| **Recorder** | Saves scenario run bundles for regression |

---

## 3. Scenario classes (must-have suite)

1. Single non-threatening object (bird-like)  
2. Single UAV-like track across overlapping sensors  
3. Crossing tracks (association stress)  
4. Coordinated multi-object “swarm-like” patterns  
5. High clutter / false observations  
6. Missing modality (RF silent)  
7. Contradictory class evidence  
8. Delayed observations / clock skew  
9. Sensor failure mid-run  
10. Network partition and heal  
11. Alert storm potential (tuning)  
12. Operator decision + handoff success/fail  

---

## 4. Truth vs estimate

Truth stays inside the twin and scorer — **never shown as live fact to operators in a way that trains over-trust** during human-factors trials (optional instructor view is separate and role-gated).

---

## 5. Interfaces

- Sim adapters implement ICD-01/15  
- Mock external implements ICD-11  
- Scorer reads platform export + truth store (lab only)

---

## 6. Non-goals

- Photoreal battlefield rendering as a hard dependency  
- Classified threat libraries in public repo  
- Real RF transmission  

Abstract kinematics + statistical sensor models are enough for architecture proof.

---

## 7. Validation use

| Stage | Twin role |
|---|---|
| Stage 1 | Prove bus→UI path |
| Stage 3–4 | ML and fusion metrics |
| Stage 5 | UX workload studies |
| Stage 6–7 | Chaos + HIL bridge (hybrid truth) |

---

## Author

Victor.I
