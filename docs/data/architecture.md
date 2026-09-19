<!-- Author: Victor.I -->

# Agent 5 — Data Engineering Architecture

**Author:** Victor.I  
**Status:** Stage 0 research note  
**See also:** `architecture/data-flow.md`

---

## Design assumptions

Heterogeneous rates, clocks, CRS, missing/duplicated/contradictory observations, flaky sensors.

## Path

```
Sensor → Adapter → Normalisation → Validation → Event Bus → Processing → Storage
```

## Stores

| Tier | Tech (proposed) | Role |
|---|---|---|
| Hot | Postgres+PostGIS | Tracks, incidents, config |
| Stream | Kafka API bus | Events + replay window |
| Cold | S3 API | Raw, models, bundles |
| Analytic | Export / later OLAP | DS evaluation |

## Quality checks

Schema validity, range checks, CRS presence, timestamp monotonicity per sensor, rate anomalies, required field completeness, quarantine topic.

## Lineage

`observation_id` → detection/track evidence arrays → risk → decision. Persist model versions on derived events.

## Schema evolution

Registry compatibility BACKWARD within major; expand/contract migrations for DB.

## What not to build

Unbounded raw topic without retention; PII in clear logs; coupling risk rules into ingest.
