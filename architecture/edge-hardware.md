<!-- Author: Victor.I -->

# Edge and Compute Hardware Selection

**Author:** Victor.I  
**Owner:** Systems Engineering (Accountable) · Software Engineering (Responsible for packaging)  
**Status:** Proposed baseline for Stage 1–7 planning  
**Related:** `architecture/deployment.md`, `architecture/tradeoffs.md`

---

## 1. Question

Where does compute run, and should edge nodes be **Raspberry Pi** or **NVIDIA** (typically Jetson)?

This is a systems decision, not a fashion choice.

---

## 2. What systems engineers usually do in this class of product

For multi-sensor C2 / counter-UAS style platforms, the common pattern is **hybrid**:

| Tier | Typical hardware | Role |
|---|---|---|
| **Central / ops room** | x86 server or workstation (± discrete GPU) | Fusion, risk, operator console, bus, DB, audit, multi-sensor correlation |
| **Edge — vision / heavy detect** | **NVIDIA Jetson** (Orin Nano / Orin NX / AGX) or rugged GPU box | EO/IR inference close to camera; bandwidth reduction |
| **Edge — light ingest** | Industrial SBC, sometimes Raspberry Pi / CM4 | Protocol adapters, health, buffering — **not** primary ML |
| **Radar / RF front-end** | Vendor appliance or FPGA/SDR host | Often opaque; platform talks via adapter only |

Raspberry Pi alone is common in **labs and prototypes**. It is **not** what serious operational C-UAS stacks standardise on for detection/fusion under load.

NVIDIA Jetson is what most teams pick when they need **edge AI** (camera pipelines) with supported CUDA/TensorRT tooling.

---

## 3. Options compared

| Criterion | Raspberry Pi 5 / CM4 | NVIDIA Jetson Orin class | Central x86 + GPU |
|---|---|---|---|
| Cost / availability | Low / easy | Medium | Higher |
| EO detection (YOLO-class) | Marginal / constrained | Strong | Strong |
| Multi-sensor fusion site-wide | Weak | Local only | Strong |
| Ops maturity for AI | Hobby/lab leaning | Industrial edge AI norm | Datacentre/ops norm |
| Power / rugged options | Limited unless carrier board | Better ecosystem | Best in ops room |
| Maintenance | Simple OS | NVIDIA BSPs / JetPack | Standard Linux/K8s |
| Fit in our architecture | Lab adapters, IoT-like sensors | Vision edge posts | Primary platform |

---

## 4. Recommendation (baseline)

### Selected architecture: **Central x86 + optional NVIDIA edge + Pi only where justified**

```
                    CENTRAL (x86 server / workstation)
                    Compose (Stage 1) → K8s later
                    Fusion · Risk · Console · Bus · DB · Audit
                              │
              secure site network
                              │
     ┌────────────────────────┼────────────────────────┐
     ▼                        ▼                        ▼
 Jetson edge               Jetson / industrial      Light edge
 (EO/IR infer)             (optional RF host)       (Pi/CM4 OK)
 adapters + models         adapters                 adapters only
```

### Rules

1. **Stage 1 (now):** everything on one **lab x86 host** (Docker Compose) + software simulator. No Pi/Jetson required to start coding.  
2. **Vision edge (Stage 2–3+):** prefer **NVIDIA Jetson Orin Nano/NX** when real cameras arrive.  
3. **Raspberry Pi:** allowed for **lab teaching**, cheap serial/GPIO/acoustic toy sensors, or light protocol gateways — **not** the fusion brain, **not** the primary EO detector in a field trial.  
4. **Do not** pin the core platform to Pi hardware APIs.

---

## 5. Gains / losses

| Choice | Gains | Losses / risks |
|---|---|---|
| Central-first | Faster delivery, easier debug, one ops story | Needs network to edges for live sensors |
| Jetson at EO edge | Lower video bandwidth, lower detect latency | JetPack/version drift; fleet management |
| Pi as main edge AI | Cheap demos | Thermal/CPU limits, weak throughput, credibility gap in serious trials |
| Everything on Jetson cluster | Cute homogeneity | Painful to run Postgres/Kafka-class central services |

---

## 6. Stage mapping

| Stage | Compute |
|---|---|
| 0 | Docs only |
| 1 | Single x86 lab machine + Compose |
| 2–4 | Same + richer sim; optional first Jetson for camera adapter experiments |
| 5–6 | Central hardened; edge profiles documented |
| 7 HIL | Representative Jetson + vendor/test sensors |
| 8 Field | Site-approved hardware list (may add rugged PCs) |

---

## 7. Open decisions still needed from stakeholders

- Air-gapped or connected site? (Q-16)  
- Which camera/radar vendors? (Q-05)  
- Power/thermal envelope at edge posts? (Q-08)  
- Budget ceiling per edge node?

Until answered, engineering proceeds on **Compose-on-x86** and designs adapters so Jetson packaging is a deploy profile, not a rewrite.

---

## Author

Victor.I
