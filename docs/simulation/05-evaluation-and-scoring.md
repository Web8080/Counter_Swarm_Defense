<!-- Author: Victor.I -->

# Simulation — 05 Evaluation and Scoring

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. Truth vs estimate

Truth stays in the twin. Scorer compares offline (or instructor live):

| Metric family | Examples |
|---|---|
| Detection | Precision/recall vs truth objects |
| Tracking | ID switches, fragmentation, MOTA/IDF1-like |
| Latency | Truth event → operator-visible track |
| Fusion | Correct multi-sensor association rate |
| Risk/UI | Alert tier appropriateness (scripted expectations) |
| Decision path | Decision recorded; handoff ACK/FAIL as scripted |

---

## 2. Regression

Nightly: P0 scenarios must pass threshold file. Failures block release candidates once Stage 1+ CI exists.

---

## 3. What scoring is not

Scorer output is **not** shown as live “confirmed threat” on the operator console.

---

## Author

Victor.I
