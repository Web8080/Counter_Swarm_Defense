<!-- Author: Victor.I -->

# Agent 7 — Security, Safety & Governance Notes

**Author:** Victor.I  
**Status:** Stage 0 research note  
**Primary artefact:** `docs/security/threat-model.md`

---

## Non-negotiables

- No autonomous destructive effects  
- Category-only external handoff  
- Tamper-evident audit on decisions  
- Least privilege services and humans  
- Model and AI governance metadata required for promotion  

## Control themes

Zero Trust tendencies: authenticate everywhere, authorise explicitly, encrypt in transit, segment networks, watch supply chain.

RBAC MVP; ABAC hooks for site/policy attributes later.

## Safety veto

SG may block releases that erode the human-approval boundary or expand integration schemas toward effector primitives.

## Operational resilience

Backup/restore drills; incident response runbooks; key rotation; dependency SLAs.

## What not to build

Shared “god” admin credentials; plaintext audit editable tables; unprotected demo endpoints in shared labs.
