<!-- Author: Victor.I -->

# Deliverable 15 — Repository Structure

**Author:** Victor.I  
**Status:** Draft for review  
**Note:** Folders below are reserved; application code remains empty until architecture approval

---

## 1. Target tree

```
/
├── README.md
├── LICENSE                          # TBD by owner
├── .gitignore
├── docs/
│   ├── product/
│   ├── software/
│   ├── ai/
│   ├── ml/
│   ├── data/
│   ├── data-science/
│   ├── security/
│   └── systems/
├── architecture/
│   ├── system.md
│   ├── interfaces.md
│   ├── data-flow.md
│   ├── deployment.md
│   ├── failure-modes.md
│   ├── tradeoffs.md
│   └── dependencies.md
├── schemas/                         # canonical event/API schemas (post-approval)
├── api/                             # OpenAPI specs
├── models/                          # model cards, eval reports (weights via registry)
├── simulation/                      # twin scenarios & engine (post-approval)
├── tests/                           # cross-cutting contract/chaos fixtures
├── infrastructure/                  # compose, k8s, terraform
├── frontend/                        # operator console
├── backend/                         # services
└── .github/                         # CI workflows (post-approval)
```

---

## 2. Mapping to agents

| Path | Primary owner |
|---|---|
| `docs/product` | Agent 1 |
| `docs/software`, `backend`, `frontend`, `api` | Agent 2 |
| `docs/ai` | Agent 3 |
| `docs/ml`, `models` | Agent 4 |
| `docs/data`, `schemas` | Agent 5 |
| `docs/data-science` | Agent 6 |
| `docs/security` | Agent 7 |
| `docs/systems`, `architecture`, `simulation`, `infrastructure` | Agent 8 (+ SE for infra impl) |

---

## 3. Stage 0 contents

Documentation only under `docs/`, `architecture/`, and root `README.md`. Placeholder directories may exist empty.

---

## 4. `.gitignore` expectations (when coding starts)

Exclude: `.env`, secrets, `node_modules`, venv, model weight binaries (unless LFS policy set), local data dumps, IDE junk, system logs.

---

## Author

Victor.I
