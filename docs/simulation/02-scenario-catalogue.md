<!-- Author: Victor.I -->

# Simulation — 02 Scenario Catalogue

**Author:** Victor.I  
**Status:** Draft for review

---

## Scenario ID convention

`SCN-<domain>-<nn>` — permanent IDs.

| ID | Name | Stresses | Priority |
|---|---|---|---|
| SCN-TRK-01 | Single bird-like object | Low false interest | P0 |
| SCN-TRK-02 | Single UAV across overlapping sensors | Multi-sensor assoc | P0 |
| SCN-TRK-03 | Crossing tracks | Association ambiguity | P0 |
| SCN-SWM-01 | Coordinated trio (loose formation) | Behaviour indicators | P0 |
| SCN-SWM-02 | Dense swarm-like cluster | Alert fatigue, declutter | P0 |
| SCN-CLT-01 | High clutter / false observations | FPR, quality gates | P0 |
| SCN-MOD-01 | RF silent (modality missing) | Degraded fusion | P0 |
| SCN-CON-01 | Contradictory class evidence | Conflict UI | P0 |
| SCN-TIM-01 | Delayed obs + clock skew | Watermarks, quality flags | P0 |
| SCN-FLT-01 | Sensor death mid-run | Coverage degrade UX | P0 |
| SCN-NET-01 | Network partition + heal | Edge buffer, stale banner | P0 |
| SCN-ALT-01 | Alert storm potential | Aggregation policies | P1 |
| SCN-DEC-01 | Decision + handoff success | X04 + mock ACK | P0 |
| SCN-DEC-02 | Decision + handoff fail/DLQ | J8 journey | P0 |
| SCN-HIL-01 | Bridge stub for later HIL | Stage 7 placeholder | P2 |

---

## Scenario card template

Each scenario file (when implemented) must declare:

- seed, duration, tick rate  
- truth objects (count, scripts)  
- active sensor models  
- fault schedule  
- expected operator-visible outcomes  
- scorer thresholds  

---

## Author

Victor.I
