<!-- Author: Victor.I -->

# Deliverable 8 — Threat Model

**Author:** Victor.I  
**Status:** Draft for review  
**Method:** STRIDE-oriented boundary analysis + abuse cases  
**Scope:** Software platform and integrations; excludes physical base defence CONOPS details

---

## 1. Assets

| Asset | Sensitivity |
|---|---|
| Live air picture / tracks | High (operational) |
| Raw sensor media | High (privacy + ops) |
| Model weights & features | High (IP + attack surface) |
| Audit logs | High (integrity) |
| Credentials / tokens / mTLS keys | Critical |
| Operator decisions / categories | High |
| External integration endpoints | Critical |
| User PII (accounts) | Medium–High |

---

## 2. Trust boundaries

```
External attacker / internet
        ↓
API Gateway / Exposure edge
        ↓
Identity (IdP)
        ↓
Operator / Integration APIs
        ↓
Service mesh (internal)
        ↓
Sensor ingestion (edge)
        ↓
Event stream
        ↓
ML inference
        ↓
Decision support
        ↓
Operator (human)
        ↓
External authorised systems
```

Also: CI/CD, artifact registries, admin laptops, sim lab vs ops enclave.

---

## 3. Adversaries

| Adversary | Capability |
|---|---|
| External network attacker | Scan, credential stuff, API abuse |
| Malicious insider (operator) | Misuse UI, exfil via screens, false decisions |
| Compromised sensor/adapter | Inject false observations |
| Supply-chain attacker | Malicious dependency/model |
| Prompt injector | Manipulate AI assistant tools |
| Physical thief of edge box | Offline attacks on disk |

---

## 4. STRIDE summary (selected)

| Boundary | Spoofing | Tampering | Repudiation | Info disclosure | DoS | Elevation |
|---|---|---|---|---|---|---|
| API gateway | Stolen tokens | Body tamper | Weak logs | Verbose errors | Flood | PrivEsc via IDOR |
| Ingest | Fake sensor | Crafted payloads | Untracked inject | Raw leak | Event flood | Adapter escape |
| Event bus | Rogue producer | Message alter | — | Topic ACL fail | Overwhelm | Cross-tenant read |
| ML | — | Poisoning/adversarial | — | Model steal | Slow infer | — |
| AI assistant | — | Prompt inject | Unaudited tools | Data exfil via tools | — | Tool privilege |
| Approval | Session hijack | Decision rewrite | Missing audit | — | Lock users out | Role forge |
| Integration | Endpoint spoof | Handoff alter | — | Category leak | Retry storm | Extra categories |

---

## 5. Abuse cases and controls

### TM-01 — False track injection via compromised adapter

- **Impact:** Operator misled; wrongful escalation  
- **Controls:** mTLS device identity; signed adapter builds; anomaly on sensor baseline; multi-sensor corroboration weighting; audit of obs provenance; rate limits  

### TM-02 — Alert flooding DoS

- **Impact:** Fatigue / missed real events  
- **Controls:** Ingest quotas; quality gates; alert aggregation; backpressure; circuit breakers  

### TM-03 — Privilege escalation to approve high categories

- **Impact:** Improper external handoff  
- **Controls:** RBAC; optional dual-control; short-lived tokens; approval permission separate from view; session binding  

### TM-04 — Silent audit deletion

- **Impact:** Cover-up  
- **Controls:** Append-only storage; hash chain; separate audit role; alerts on audit write failure  

### TM-05 — Model poisoning / adversarial patches

- **Impact:** Missed detections or spoofed classes  
- **Controls:** Training data provenance; eval gates; drift monitors; canary; human evidence review norms  

### TM-06 — Prompt injection → tool exfiltration

- **Impact:** Sensitive track dump via assistant  
- **Controls:** Allowlisted tools; argument schemas; output filtering; no raw SQL tools; per-tool AuthZ; audit tool calls; disable assistant in high-classification modes if required  

### TM-07 — Supply chain compromise

- **Impact:** Backdoor in platform  
- **Controls:** Lockfiles; provenance attestations; image signing; vuln scanning; minimal base images; private registry  

### TM-08 — Integration API misuse as pseudo-weapon control

- **Impact:** Safety boundary erosion  
- **Controls:** Category enum only; schema deny unknown fields; legal/process controls; separate network zone; SG veto on expanding schema toward effector params  

---

## 6. Security control baseline

| Control | Requirement |
|---|---|
| Authentication | OIDC for users; mTLS for services |
| Authorisation | RBAC MVP; ABAC-ready |
| Encryption | TLS in transit; at-rest for DB/object |
| Secrets | KMS/vault; never in git |
| Network | Segmentation edge/control/data; deny by default |
| Audit | Tamper-evident; complete decision chain |
| SDLC | SAST/DAST dependency scan; signed artifacts |
| Runtime | Least privilege; read-only roots where possible |
| AI | Policy gateway; injection tests |
| ML | Model cards; version pin; rollback |
| Resilience | Rate limits; backpressure; chaos tests |

---

## 7. AI / ML governance requirements

Each production model must record:

- Owner, version, training provenance, evaluation results  
- Intended use and limitations  
- Known failure modes  
- Monitoring and rollback procedure  

LLM features inherit the same ownership and an additional tool-permission manifest.

---

## 8. Residual risks (accepted only with sign-off)

| Risk | Residual | Treatment |
|---|---|---|
| Determined insider with physical access | Medium | Process + monitoring |
| Novel adversarial ML | Medium | Defence-in-depth + human evidence |
| Zero-day in dependency | Medium | Patch SLAs |
| Operator over-trust in AI labels | Medium | UX epistemic honesty + training |

---

## 9. Threat model maintenance

Revisit on: new external integration, new sensor class, enabling AI tools, moving to field test (Stage 8), major architecture change.

---

## Author

Victor.I
