<!-- Author: Victor.I -->

# Deliverable 6 — Data-Flow Architecture

**Author:** Victor.I  
**Status:** Draft for review

---

## 1. End-to-end flow

```
┌──────────────────┐
│ Physical Sensors │  (or Digital Twin)
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Sensor Adapters  │  vendor SDK / sim → candidate observation
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Data Normaliser  │  validate, CRS, time, idempotency, quality
└────────┬─────────┘
         ▼
┌──────────────────┐
│   Event Stream   │  observation.v1
└────────┬─────────┘
         │
   ┌─────┼──────────────┐
   ▼     ▼              ▼
Detect  Track/Assoc   Quality
   │     │              │
   └──┬──┴──────────────┘
      ▼
┌──────────────────┐
│  Sensor Fusion   │  fused track + evidence links
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Behaviour Engine │  coordination / anomaly indicators
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Risk Assessment  │  graded risk + missing info + version
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Decision Support │  alerts + recommended categories
└────────┬─────────┘
         ▼
   HUMAN OPERATOR
         ▼
 AUTHORISED ACTION CATEGORY
         ▼
 AUDIT / LOGGING (+ optional external handoff)
```

---

## 2. Event types (logical)

| Event | Producer | Primary consumers | Notes |
|---|---|---|---|
| `observation.v1` | Normaliser | Detection, tracking, quality, audit subsample | Canonical |
| `observation.quarantine.v1` | Normaliser | DE, SG | Invalid/suspicious |
| `detection.v1` | Detection | Tracking, UI projections | Includes model version |
| `track.update.v1` | Tracking/Fusion | Behaviour, risk, UI, audit | State estimate + cov |
| `behaviour.indicator.v1` | Behaviour | Risk, UI | Not a decision |
| `risk.assessment.v1` | Risk | Alert, UI, audit | Graded + rationale |
| `alert.v1` | Alert | UI, notify | Policy id |
| `recommendation.v1` | Decision support | UI, approval | Category enum |
| `human.decision.v1` | Approval | Audit, integration outbox | Authoritative |
| `integration.handoff.v1` | Integration | External, audit | After decision |
| `sensor.health.v1` | Adapters | UI, risk context | Coverage |
| `model.inference.v1` | Inference GW | Audit, drift monitors | Optional high-vol sample |

---

## 3. Canonical observation (conceptual)

```json
{
  "observation_id": "uuid",
  "schema_version": "1.0.0",
  "sensor_id": "string",
  "source_type": "radar|eo|ir|rf|acoustic|telemetry|other|sim",
  "timestamp_utc": "RFC3339",
  "received_at_utc": "RFC3339",
  "idempotency_key": "string",
  "location": {
    "crs": "EPSG:4326",
    "lat": 0.0,
    "lon": 0.0,
    "alt_m": null,
    "uncertainty": {}
  },
  "measurement": {},
  "confidence": 0.0,
  "quality": {},
  "provenance": {
    "adapter": "string",
    "adapter_version": "string",
    "raw_ref": "s3://..."
  },
  "metadata": {}
}
```

Normative schema files will land under `/schemas` after approval (Stage 0 keeps conceptual form here).

---

## 4. Storage flow

```
Events (bus, retention window)
        │
        ├──► Hot DB projections (tracks, alerts, incidents, decisions)
        ├──► Audit append log
        ├──► Object store (raw payloads, clips, large artifacts)
        └──► Analytics export (batch) → evaluation / DS notebooks
```

### Retention (draft)

| Store | Retention draft |
|---|---|
| Event bus | 7–30 days (env-specific) |
| Hot DB operational | 90 days online; archive after |
| Audit | Long-term (customer policy; ≥ 1 year default design) |
| Raw object store | Tiered; cost-governed |
| Model artifacts | Per registry policy |

---

## 5. Query paths (operator)

| Need | Path |
|---|---|
| Live tracks | Realtime GW ← track projections / bus |
| Evidence for track | Operator API → hot DB links → obs IDs → bus/object fetch |
| Replay | Select time range → bus replay + DB snapshots |
| Audit investigation | Audit API → immutable records |

---

## 6. ML data flow

```
Raw/sim → labeled datasets (versioned) → training pipeline
       → model registry → inference gateway → detections/classes
       → metrics to DS evaluation → drift monitors → rollback
```

Training path is offline and separated from the operational bus by design.

---

## 7. AI assistant data flow

```
Operator prompt → AI policy layer → allowlisted tools
  → Operator API / read models → grounded response + citations
  → audit of tool calls
```

Assistant **reads**; it does not directly write `human.decision.v1`.

---

## 8. Clock and ordering

- All events carry `timestamp_utc` (sensor) and `received_at_utc` (platform)  
- Stream ordering: per partition key `sensor_id` or `site_id`  
- Fusion must handle out-of-order within a bounded watermark  
- Clock skew beyond threshold → quality flag `CLOCK_SKEW`  

---

## 9. Contradictions and duplicates

| Condition | Handling |
|---|---|
| Duplicate `idempotency_key` | Drop/dedupe; metric |
| Same track, conflicting class | Keep distribution; flag `CLASS_CONFLICT` |
| Spatially incompatible assoc | Reject assoc; keep separate tracks; flag |
| Delayed obs inside watermark | Late update; possible re-eval risk |
| Delayed obs beyond watermark | Side channel / reprocessing job; mark late |

---

## Author

Victor.I
