# RAJ-URVARA AI — Deployment, Risk & Vision Blueprint

This document is the evaluator-facing implementation blueprint for the **AI/ML-Driven Smart Fertilizer Formulation & Distribution Framework**. It explains how RAJ-URVARA moves from evaluator sandbox to a measurable 90-day Government pilot, what can fail, how failure is contained, and how the same primitives can evolve into Rajasthan's Agricultural Input Intelligence Rail.

## 1. Mission

RAJ-URVARA adds the missing intelligence loop around existing fertilizer and agriculture rails:

```text
soil / SHC → crop stage → governed nutrient decision → probabilistic demand
→ fair allocation → warehouse / dealer stock → custody proof
→ farmer / field acknowledgement → outcome learning
```

It does **not** replace iFMS/DBT, FFS, Soil Health Card, AgriStack or State systems.

## 2. Layered architecture

### Authoritative rails
- iFMS / Fertilizer DBT
- Framework for Fertilizer Sale / DRS
- Soil Health Card
- AgriStack / DCS / KDSS
- IMD / approved weather sources
- FCO / labs / COA evidence
- Raj Sewa Dwaar / approved State integration gateways

### Trust & context fabric
- **FarmGraph** temporal evidence twin
- integration adapters + schema registry
- provenance / freshness / purpose state
- event bus + derived feature store

### Decision intelligence
- **NutrientTwin + UrvaraRX** — governed formulation path
- **DemandCast 2.0** — P10/P50/P90 demand forecasting
- **FlowOpt** — fairness-constrained stock movement
- **Leakage + Quality Sentinels** — explainable human-review prioritization

### Execution and trace
- **StockPulse** physical/digital stock reconciliation
- tiered QR / mobile GPS / selected IoT
- **TraceGraph** custody event contract
- Decision Receipts and audit lineage

### Channels
- State Fertilizer Operations OS
- dealer / warehouse workflows
- Web / PWA / mobile
- **SUTRA-ID Edge** assisted offline execution

## 3. FarmGraph — innovation core

FarmGraph is a temporal evidence twin rather than another farmer database. It links the minimum permitted references and versioned facts required to explain a fertilizer decision:

```text
Farmer ref → Plot / Khasra → Crop cycle + stage → Soil / SHC version
→ Weather state → Authorized rule → Nutrient decision → Demand features
→ Stock / custody → Field / outcome signal
```

### Why this matters
- **Temporal truth:** SHC freshness, crop stage, weather and inventory change on different clocks.
- **Lineage:** every derived feature can point to source, version and timestamp.
- **Shared substrate:** formulation, forecasting, allocation and trace use one governed context.
- **Doability:** the 90-day pilot uses typed nodes/edges and deterministic feature services; graph ML is optional only after data quality and value are proven.

## 4. AI / ML release boundaries

### NutrientTwin + UrvaraRX

Numeric fertilizer decisions originate only from authorized deterministic agronomy logic:

```text
SHC source + freshness
→ State / SHC / STCR rule
→ crop-stage constraint
→ permitted-product / stock optimizer
→ 4R context
→ RAJ-NUTRI explanation
```

The RAJ-NUTRI SLM may retrieve, translate, summarize, call approved tools and explain provenance. It may **not** invent numeric fertilizer dose, invent an unapproved product, deny subsidy, mutate an official record, certify quality or enforce against a dealer.

### DemandCast 2.0
- fertilizer grade × district/geography × week target
- P10/P50/P90 uncertainty rather than a single fake-precise future
- stock-out censoring: unavailable inventory + zero sales ≠ zero latent demand
- rolling-origin validation
- district holdouts
- hierarchical reconciliation
- quantile calibration
- model registry, shadow mode, rollback and drift gates

### FlowOpt fairness
Every proposed stock movement is constrained by minimum source stock-cover, route/capacity compatibility, fertilizer grade, lead time and human authorization. A transfer that creates a new service risk elsewhere is rejected.

## 5. Physical visibility and custody

### Tiered strategy
- **Tier 0:** QR/mobile/device scans using existing operational endpoints.
- **Tier 1:** mobile GPS / geofence evidence on selected routes.
- **Tier 2:** dedicated tracker, weighbridge or sensor only where route risk/value justifies hardware.

### TraceGraph contract

```text
DISPATCH → WAREHOUSE_RECEIPT → TRANSFER → DEALER_RECEIPT
→ FFS / PoS RETAIL_REFERENCE → optional SUTRA FIELD_ACK
```

Sensitive farmer data and raw documents remain off-ledger. Multi-party events can be anchored to a permissioned DLT where its verification value is justified, or to an approved signed append-only Government journal.

## 6. SUTRA-ID Edge

Web/PWA/mobile remain primary. SUTRA is an optional assisted channel for dealers, KVKs, labs, extension/mobile camps and low-connectivity situations.

```text
voice / scan
→ verified plot / SHC / lot context
→ authorized tool
→ grounded explanation
→ human confirmation
→ signed local business event
→ offline queue
→ reconnect
→ idempotent synchronization
```

The evaluator demo intentionally retries the same event to prove duplicate suppression.

## 7. Predictable failure modes and containment

| Failure | Automatic containment | Safe operational fallback |
|---|---|---|
| Stale / missing SHC | lower certainty; block unsupported formulation | retest / authorized fallback rule |
| Forecast drift / poor P90 calibration | freeze recommendation-capable version | rollback to accepted baseline/model |
| Government API unavailable | queue signed request; preserve connector state | offline PWA/SUTRA + later reconciliation |
| Stock sensor / GPS mismatch | create evidence conflict, not accusation | physical verification / officer review |
| DLT unavailable | persist signed append-only events | anchor later; operations continue |
| Connectivity failure | local idempotent event queue | retry safely; suppress duplicates |
| Prompt injection / unsupported ask | schema/tool gate + abstention | source-backed rule / officer escalation |
| Sparse or biased history | widen uncertainty; hierarchical baseline | shadow mode / manual baseline |
| Dealer adoption friction | minimize additional capture; reuse QR/PoS references | assisted mobile/SUTRA workflow |
| Remote-district starvation risk | hard minimum stock-cover/service floor | officer override with reason receipt |

## 8. Security and governance

- RBAC/ABAC and least privilege
- purpose limitation and data minimization
- no raw Aadhaar in analytics; no farmer PII on DLT
- TLS and State-approved encryption/KMS
- model/rule registry with acceptance gates and rollback
- consequential recommendation ≠ Government decision
- human authorization + Decision Receipt
- data freshness, connector health, model calibration, sync lag and exception SLA observability
- recommendation freeze / kill switch / incident runbook

### Decision Receipt
Required fields for consequential pilot actions:

`decision_id · actor/role · source versions · FarmGraph feature snapshot · model/rule version · recommendation · uncertainty · fairness/stock-floor checks · approve/override/defer · reason code · linked trace event · receipt hash`

## 9. 90-day pilot

| Window | Mission | Exit evidence |
|---|---|---|
| Days 0–15 | baseline, data contracts, pilot archetypes, security/privacy review | signed inception + truth registry + KPI baseline |
| Days 16–35 | FarmGraph + NutrientTwin + DemandCast in shadow mode | shadow dashboard + model card + baseline comparison |
| Days 36–65 | controlled FlowOpt / TraceGraph / QR-GPS / SUTRA workflows | Decision Receipts + custody + field evidence |
| Days 66–90 | UAT, red-team, rollback drills, officer training, handover | acceptance report + deployment package + scale/no-scale decision |

### Proposed acceptance gates — not pre-claimed results
- ≥10% relative WAPE improvement against Department-agreed baseline
- P90 empirical coverage 85–95%
- ≥24 h selected stock-cover warning where data permits
- ≥95% required custody-event completeness on selected routes
- 0 duplicate SUTRA business events
- 100% consequential recommendations receipt-linked
- 0 unsupported numeric dose/product generation by SLM on approved safety set

## 10. Vision 2030

### 2026 — Smart Fertilizer Pilot
Prove FarmGraph, DemandCast, governed formulation, fair stock orchestration, selected trace/GPS and SUTRA last-mile execution.

### 2027 — State Fertilizer Operating Layer
Scale approved modules, ModelOps, warehouse/dealer coverage, State integrations and audit receipts.

### 2028–29 — Agricultural Input Trust Rail
Reuse the primitives for micronutrients, seeds/input logistics, quality surveillance, extension workflows and FPO service planning.

### 2030 — Rajasthan Agricultural Digital Twin
A State-owned temporal crop/soil/input/outcome intelligence layer for policy simulation, resilience planning and authorized ecosystem innovation — without monetizing farmer PII.

## 11. Commercial and procurement logic

**Proposed 90-day pilot: ₹79.50 lakh.** Statewide cost is intentionally not guessed before pilot evidence establishes data readiness, integration complexity and hardware tiering.

The Government pays for implementation, integration, model/operations hardening, field enablement, training and O&M — not for access to farmer data.

Balanced-use analytics may support PM-PRANAM planning, but no fiscal incentive is treated as guaranteed revenue.

## 12. Claim discipline

- `LIVE_PUBLIC` — directly cited public Government aggregate/evidence
- `CONTRACT_READY` — adapter defined; production credentials/approval required
- `DEMO_SANDBOX` — synthetic operational signal used to demonstrate end-to-end behavior
- pilot KPIs are proposed acceptance targets, not achieved results
- no Government integration is labelled live without authorization

## Evaluator path

**README → Operations OS → FarmGraph → Formulation/DemandCast → 90-day pilot → Governance → release tests**

Canonical repository: https://github.com/Sauravssoni/RIC-Smart-Fertilizer
