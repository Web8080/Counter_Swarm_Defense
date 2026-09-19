<!-- Author: Victor.I -->

# Simulation — 04 Simulation UI and Operator Loop

**Author:** Victor.I  
**Status:** Draft for review  
**Screens:** S01 Sim director, S02 Scenario library; operator still uses X01…

---

## 1. Dual-console lab layout

```
┌─────────────────────────────┐    ┌─────────────────────────────┐
│ S01 SIM DIRECTOR  [LAB]     │    │ X01 OPERATOR CONSOLE        │
│ Scenario · seed · faults    │───►│ Real UI, sim observations   │
│ Start/Pause/Inject          │    │ No "fake" weapon controls   │
│ Truth overlay (instructor)  │    │                             │
└─────────────────────────────┘    └─────────────────────────────┘
```

Instructor may see truth; operators under test should **not** by default (HF validity).

---

## 2. S01 responsibilities

- Load scenario from catalogue  
- Control time (start/pause/speed)  
- Toggle fault injectors  
- Show connection to bus (“observations flowing”)  
- Never exposed in OPS builds  

---

## 3. Operator loop under simulation

Identical to production journeys J1–J8. Success criterion: operator cannot tell sim vs live at the schema boundary (except LAB chrome on the director, not on X01 unless env badge configured).

---

## 4. Mock external panel (lab)

Shows category handoffs received, ACK/FAIL scripted responses — proves ICD-11 without real effectors.

---

## Author

Victor.I
