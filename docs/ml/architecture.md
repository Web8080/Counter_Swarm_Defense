<!-- Author: Victor.I -->

# Agent 4 — ML Engineering Architecture

**Author:** Victor.I  
**Status:** Stage 0 research note

---

## Pipeline

```
Raw Sensor Data → Preprocess → Detection → Features → Tracking
 → Multi-Sensor Correlation → Behaviour features → Confidence → Risk Engine
```

## Model family guidance

| Problem | Prefer first | Deep learning when |
|---|---|---|
| Kinematic tracking | Kalman / EKF / multi-hypothesis | Highly nonlinear complex scenes demand it |
| EO detection | YOLO-class / ViT detectors as justified | Labeled imagery exists |
| RF classification | Classical + shallow nets | Large corpora |
| Anomaly | Statistical / isolation / autoencoders | Residual complex patterns |

## Data

- Train / val / test splits by scenario and time  
- Synthetic twin data for rare swarms  
- Edge cases: glare, clutter, occlusions, spoof-like patterns (defensive eval)  

## Metrics

Precision, recall, F1, mAP (detectors), FPR/FNR, tracking accuracy (e.g. MOTA/IDF1), latency, throughput, calibration, robustness slices.

## Targets (draft — confirm with hardware)

| Metric | Draft |
|---|---|
| Detector latency (central) | p95 per model card |
| Track update budget | Fits NFR-LAT-002 |
| Calibration | ECE monitored |

## Lifecycle

Registry → canary → promote → monitor drift → rollback. Every operator-visible inference carries `model_version`.

## What not to build

Unversioned notebooks as prod; always-on giant models for problems classical methods solve.
