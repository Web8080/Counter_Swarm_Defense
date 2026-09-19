<!-- Author: Victor.I -->

# Agent 2 — Software Engineering Architecture Notes

**Author:** Victor.I  
**Status:** Stage 0 research note  
**Reconciled in:** `architecture/system.md`, `architecture/tradeoffs.md`

---

## Research protocol answers

| Prompt | Answer |
|---|---|
| Problem | Need production-grade modular services with clear contracts |
| Users | Operators (via UI), integrators, other services |
| Inputs | Events, user commands, configs |
| Outputs | APIs, services, CI/CD design, observability hooks |
| Dependencies | Schemas (DE), IAM (SG), models (ML) behind gateways |
| Failure modes | Cascading outages; chatty monoliths; undocumented coupling |
| Alternatives | Monolith vs fine microservices vs modular services — **modular event-driven selected** |
| Evidence | Standard C2/SOC platform patterns; team operability |
| Trade-offs | Dual REST/gRPC cost vs clarity |
| Security | Gateway authz; no trust of client input; SSRF guards on integrations |
| Testing | Contract + integration + chaos |
| Ops | SLIs/SLOs; runbooks; versioned deploys |

## Service design rules

1. One writable datastore owner per entity  
2. Outbox for integration side effects  
3. Idempotent consumers  
4. OpenAPI for external; schema registry for events  

## What not to build

Custom orchestrators; effector drivers; hand-rolled crypto.
