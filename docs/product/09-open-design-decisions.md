<!-- Author: Victor.I -->

# Product Design — 09 Open Design Decisions

**Author:** Victor.I  
**Status:** Draft for review

---

## Blocking (resolve before Stage 5 UI build)

| ID | Decision | Options | Why blocking |
|---|---|---|---|
| D-UI-01 | Single accent colour | Teal (`#2BB3A3`) vs Amber | Affects selection + recommendation chrome |
| D-UI-02 | Dual-control categories | Which categories need two approvers | Changes I02 flows |
| D-UI-03 | Auto-open incidents | On behaviour flag vs risk threshold vs manual only | I01 entry volume |
| D-UI-04 | Sound for T3 | On / off / user preference | HF + site rules |
| D-UI-05 | Assistant in MVP | Include P2 early vs defer | Nav IA + security review |
| D-UI-06 | Map basemap | Offline tiles vs online provider | Air-gap deploy |

---

## Non-blocking (can iterate)

| ID | Decision | Default for now |
|---|---|---|
| D-UI-07 | Font pair final licensing | IBM Plex proposed |
| D-UI-08 | Keyboard shortcut set | Defer detailed map |
| D-UI-09 | Mobile operator mode | P2 |
| D-UI-10 | Truth overlay for training | Instructor-only in lab |
| D-UI-11 | Export formats for AAR | JSON first, PDF later |

---

## Dependencies on CONOPS (from Deliverable 17)

Q-01 categories, Q-02 paging, Q-03 dual-control, Q-04 instructor truth — all feed this file when answered.

---

## Approval

Product + Security sign-off on blocking items unlocks high-fidelity visuals and frontend implementation.

---

## Author

Victor.I
