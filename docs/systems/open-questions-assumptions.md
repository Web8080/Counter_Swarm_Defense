<!-- Author: Victor.I -->

# Deliverable 17 — Open Questions and Assumptions

**Author:** Victor.I  
**Status:** Draft for review — **must be resolved or explicitly accepted before implementation priorities solidify**

---

## 1. Assumptions (working)

| ID | Assumption | If wrong |
|---|---|---|
| A-01 | Simulation-first delivery is acceptable to stakeholders | Hardware pressure may force earlier HIL — still keep safety mocks |
| A-02 | Single site / single security domain for MVP | Need tenant isolation earlier → identity & data model change |
| A-03 | OIDC IdP available | Must select/deploy Keycloak or equivalent |
| A-04 | Operators accept web console | May need hardened/air-gapped browser policy or native later |
| A-05 | Kafka API bus is acceptable on customer network | May force alternate messaging — keep ICD stable |
| A-06 | External systems accept abstract categories | Integration redesign with SG if they demand effector params (likely reject) |
| A-07 | English-first UI | I18n schedule needed |
| A-08 | Draft latency NFRs are directionally correct | Resize infrastructure / edge inference |
| A-09 | Classical tracking sufficient for Stage 1 proof | Bring ML tracking forward |
| A-10 | No classified data in this GitHub repo | Separate enclave repos/processes required |
| A-11 | Author name Victor.I in project markdown/scripts per project convention | — |

---

## 2. Open questions

### Product / CONOPS

| ID | Question | Owner |
|---|---|---|
| Q-01 | What sites, threat profiles, and rules of engagement constrain categories? | Customer + SYS + SG |
| Q-02 | Which alert tiers page humans 24/7? | PD + Customer |
| Q-03 | Dual-control required for which categories? | SG + Customer |
| Q-04 | Instructor/truth view allowed in training? | PD + SG |

### Sensing / integration

| ID | Question | Owner |
|---|---|---|
| Q-05 | Which real sensor vendors are in-scope for Stage 2–7? | SYS + Customer |
| Q-06 | Coordinate reference systems and site surveys? | DE + SYS |
| Q-07 | Time sync architecture (NTP vs PTP)? | SYS |
| Q-08 | Edge compute hardware standards? | SYS |

### Data / retention / privacy

| ID | Question | Owner |
|---|---|---|
| Q-09 | Retention periods for raw EO imagery? | SG + Legal + Customer |
| Q-10 | Are camera feeds subject to privacy regimes? | SG |
| Q-11 | Cross-border data movement restrictions? | SG |

### ML / AI

| ID | Question | Owner |
|---|---|---|
| Q-12 | Is labeled training data available or only synthetic? | ML + DS |
| Q-13 | Is an LLM assistant desired in MVP or deferred? | PD + SG |
| Q-14 | Private model hosting constraints? | SG + ML |

### Security / deployment

| ID | Question | Owner |
|---|---|---|
| Q-15 | Target accreditation / assurance regime? | SG |
| Q-16 | Air-gapped deploy required? | SYS + SG |
| Q-17 | GitHub `web8080` org/user visibility (public vs private)? | Owner |
| Q-18 | Export control review needed before publishing docs? | SG + Legal |

### Engineering

| ID | Question | Owner |
|---|---|---|
| Q-19 | Confirm Redpanda vs managed Kafka | SE + SYS |
| Q-20 | GPU availability in lab? | ML + SYS |
| Q-21 | Team skill mix (Go vs Python adapters)? | SE |

---

## 3. Risks of unanswered questions

Unresolved Q-01/Q-05/Q-09/Q-15/Q-18 can invalidate schema fields, deploy topology, or even the legality of a public repo push.

**Recommendation:** Answer Q-17 and Q-18 before any GitHub publication; answer Q-01 and Q-05 before Stage 2.

---

## 4. Document approval checklist

- [ ] Deliverable 1 Product / UX  
- [ ] Deliverable 2 Requirements  
- [ ] Deliverable 3 Agent matrix  
- [ ] Deliverable 4–7 Architecture / ICD / data-flow / deps  
- [ ] Deliverable 8 Threat model  
- [ ] Deliverable 9 FMEA  
- [ ] Deliverable 10 Tech matrix  
- [ ] Deliverable 11–14 Twin, roadmap, tests, deploy  
- [ ] Deliverable 15–16 Structure + README  
- [ ] This open-questions register reviewed  

Upon approval: create/push GitHub repo under `web8080` as directed, then begin Stage 1.

---

## Author

Victor.I
