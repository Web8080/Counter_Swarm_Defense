<!-- Author: Victor.I -->

# Product Design — 06 UX Principles and Visual Language

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. North-star UX statement

The console must make an overloaded human **correctly sceptical and correctly fast**: sceptical of unverified inference, fast at finding evidence and recording an accountable decision.

---

## 2. Ten principles

1. **Epistemic honesty** — Inference never wears the clothes of fact.  
2. **Map is the truth surface** — Lists support the map; they do not replace it.  
3. **Priority is a scarce resource** — Every alert must earn its tier.  
4. **One primary selection** — One track/incident in focus; prevent split-brain panels.  
5. **Degrade in public** — Capability loss is visible in chrome.  
6. **Language of categories** — Never mimic weapon control affordances.  
7. **Progressive disclosure** — Summary first; evidence on demand.  
8. **Calm urgency** — T3 is assertive, not theatrical.  
9. **Audit without choreography** — Material acts log themselves.  
10. **Assistant is optional** — Core path works if AI is off.

---

## 3. Epistemic visual language

| Layer | Visual treatment (intent) | Example copy |
|---|---|---|
| Observation | Solid, neutral, “measured” | “Obs from RDR-1 at 12:01:02Z” |
| Inference | Hatched / labelled badge “INFERENCE” | “Class UAV p=0.72 (det-v3.2)” |
| Prediction | Dashed geometry on map | “60s envelope (kinematic)” |
| Recommendation | Policy chip, not alarm colour alone | “Rec: HEIGHTEN_MONITORING (P-12)” |
| Decision | High-contrast confirmed stamp + actor | “Decided by j.smith 12:04:11Z” |

**Forbidden:** green checkmarks on model class labels that imply ground truth.

---

## 4. Colour intent (operational — not marketing)

Direction: night-operable tactical console. Avoid purple-gradient SaaS clichés and warm “lifestyle” cream themes.

| Token role | Intent |
|---|---|
| Canvas | Dark cool neutral map background |
| Track default | Light neutral |
| Selected | Clear accent (teal or amber — pick one system accent) |
| T3 alert | Strong warm danger |
| T2 | Amber attention |
| T1 | Cool info |
| Degraded/coverage | Violet-grey hatch reserved for *system* impairment only (not “brand purple UI”) |
| Inference badge | Distinct from alert colours |

Exact hex values live in `08-design-tokens.md`.

---

## 5. Typography

- **UI sans:** readable geometric or humanist sans suited to dense data (not Inter-as-default if a project font is chosen — document choice in tokens).  
- **Mono:** track IDs, timestamps, sensor IDs.  
- **Display:** restrained; brand in shell only — do not let marketing headlines overpower the operational canvas.

---

## 6. Motion

Use 2–3 purposeful motions only:

1. Alert row insert (short)  
2. Map selection focus easing  
3. Degraded banner slide-in  

Avoid continuous glow pulses on tracks (noise + epilepsy risk). Prediction envelopes may animate slowly if toggled on.

---

## 7. Density modes

| Mode | Use |
|---|---|
| Standard | Default ops |
| Simplify | High load / swarm — T2+/T3 + incident tracks only |
| Analysis | Analyst — more raw obs layers available |

---

## 8. Accessibility

- WCAG 2.2 AA contrast for text/chips  
- Tier not by colour alone (icons + labels)  
- Keyboard path for acknowledge and decide  
- Reduced-motion respects OS setting  

---

## 9. Anti-patterns (explicit)

- Dashboard stat cards in the first viewport  
- Floating promo badges on the map  
- “AI confirmed threat” banners  
- Single-click irreversible external notify without confirm  
- Card-soup replacing the map  

---

## Author

Victor.I
