<!-- Author: Victor.I -->

# Agent 1 — Product Design & Human Factors

**Author:** Victor.I  
**Status:** Stage 0 research note  
**Primary artefact:** `docs/product/executive-definition.md`

---

## Research protocol answers

| Prompt | Answer |
|---|---|
| Problem | Operators cannot build a trusted air picture from fragmented sensors without overload |
| Users | Security/sensor operators, commanders, analysts, admins |
| Inputs | Tracks, alerts, evidence, health, recommendations |
| Outputs | Wireframes, IA, UX principles, journey maps, HF metrics |
| Dependencies | Accurate APIs from SE; honest uncertainty from DS/ML |
| Failure modes | Alert fatigue; over-trust; cluttered map; faux effector UI |
| Alternatives | Thick vendor UIs; SOC-only list views — rejected as primary |
| Evidence | Public C-UAS C2 patterns; HF alert fatigue literature (synthesis) |
| Trade-offs | Richness vs clarity |
| Security | UI must not expose raw secrets; role-based views |
| Testing | Usability trials; time-to-evidence |
| Ops | Collect workload metrics; iterate policies not just pixels |

## What not to build

Chat-first C2; gamified chrome; unexplained “AI confirmed” badges.

## Published design pack

See [README.md](README.md) for the multi-document UI/UX and workflow set (`01`–`09`).

## Interface to others

PD owns information hierarchy; SE implements; SG reviews approval UX; AI assistant is secondary and dismissible.
