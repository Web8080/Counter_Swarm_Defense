<!-- Author: Victor.I -->

# Simulation — 01 Overview

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Why simulation first

The platform must be developed and tested without operational sensors and without any ability to cause physical harm. The digital twin generates synthetic worlds; **sim adapters** publish observations through the **same contracts** as real adapters. The rest of the stack (bus → fusion → risk → operator console) is the real software under test.

```
Truth world  →  Sensor models  →  Faults  →  Sim adapters
                                                │
                                                ▼
                                    Real Counter-Swarm platform
                                                │
                                                ▼
                                    Operator console (X01…)
                                    + offline scorer vs truth
```

---

## 2. What is simulated

| Layer | Simulated? |
|---|---|
| Object kinematics / swarm scripts | Yes |
| Radar / EO / RF / acoustic observation streams | Yes (abstract models) |
| Noise, bias, clutter, false plots | Yes |
| Sensor dropouts, delay, duplicate, corrupt | Yes |
| Network partition edge↔central | Yes (fault injector) |
| External handoff responses | Yes (mock external) |
| Operator UI | Real UI against sim data |
| Weapons / jammers / kinetic effects | **Never** — only abstract categories |

---

## 3. Environments

| Env | Sim allowed | Truth overlay |
|---|---|---|
| LAB | Yes | Instructor-only |
| STAGING | Yes (gated) | No by default |
| OPS | Build-flag off | Never |

---

## 4. Safety

Simulation must not unlock real integration endpoints. LAB badge is mandatory on S01. Category handoffs in sim go only to the mock external system.

---

## Author

Victor.I
