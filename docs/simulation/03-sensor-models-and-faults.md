<!-- Author: Victor.I -->

# Simulation — 03 Sensor Models and Faults

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Sensor model abstractions

Models are statistical / geometric — not full physics engines for Stage 1.

| Model | Emits | Key parameters |
|---|---|---|
| Radar-like | Range-bearing / geo plots, rate, SNR | FOV, max range, noise σ, Pd, Pfa |
| EO/IR-like | Detections with class hints, pixels optional | FOV cone, lighting factor, latency |
| RF-like | Emitter hits / bearings | silence probability, spoof rate (defensive test) |
| Acoustic-like | Coarse bearings | short range, high noise |

All outputs become **candidate observations** for sim adapters → normaliser.

---

## 2. Fault injector catalogue

| Fault | Effect on stream | UI expectation |
|---|---|---|
| DROP | Missing obs | Coast / coverage hole |
| DELAY | Late timestamps | Late/watermark behaviour |
| DUPLICATE | Re-sent ids/keys | Dedup metrics |
| CORRUPT | Invalid payload | Quarantine |
| CONTRADICT | Conflicting class/geo | Conflict strip on X03 |
| SENSOR_DEATH | Heartbeat stop | X05 + hatch |
| LINK_LOSS | Edge buffer | D3 stale banner when applicable |
| BIAS_STEP | Systematic geo offset | Cross-sensor residual |

---

## 3. Scheduling

Faults are timeline events in the scenario JSON, e.g. `t=45s SENSOR_DEATH RF-02`.

---

## Author

Victor.I
