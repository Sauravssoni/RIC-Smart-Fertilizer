# RAJ-URVARA AI
## Rajasthan Fertilizer Intelligence & Trust Grid

> **Evaluator Release v4 — State Fertilizer Operations Console**  
> **Right Nutrient · Right Plot · Right Time · Right Bag**

RAJ-URVARA AI is Syntheon Tech's evaluator-grade prototype for the Rajasthan Innovation Challenge problem statement **AI/ML-Driven Smart Fertilizer Formulation & Distribution Framework**.

It is not another fertilizer-booking portal. It is a governed **State intelligence, orchestration and trust control plane** designed to complement iFMS/DBT, FFS/DRS, Soil Health Card, AgriStack and approved State infrastructure:

`soil/crop truth → nutrient need → probabilistic demand → fair allocation → custody → field execution → outcome learning`

## Evaluator quick route — 90 seconds

1. Open `index.html` / `dashboard/index.html`.
2. Click **Run judge demo**.
3. Watch a synthetic Kharif stress event change Sikar DAP P90 risk.
4. DemandCast widens the uncertainty envelope.
5. Allocation Twin produces a fairness-constrained recommendation.
6. A Government officer authorizes the transfer and receives a Decision Receipt.
7. TraceGraph opens custody evidence.
8. SUTRA-ID Edge records the last-mile acknowledgement offline.
9. Reconnect: the signed event synchronizes once; a retry is duplicate-suppressed.

The interface is deliberately a **working operations console, not a pitch microsite**: district risk map, stock table, live event stream, decision workbench, warehouse reconciliation, forecast workbench, trace explorer, farmer/plot lookup and SUTRA field terminal. See `docs/OPERATIONS_CONSOLE_V4.md`.

## Rajasthan evidence

Public Government of India data for Kharif 2026 through **29 July 2026** reports for Rajasthan:

| Grade | Requirement | Availability | DBT sales | Closing stock |
|---|---:|---:|---:|---:|
| Urea | 6.71 | 11.31 | 8.05 | 3.27 LMT |
| DAP | 3.21 | 2.73 | 2.08 | 0.65 LMT |
| MOP | 0.05 | 0.15 | 0.05 | 0.10 LMT |
| NPKS | 0.77 | 1.40 | 0.68 | 0.72 LMT |

These aggregates are **not proof of leakage or a statewide shortage**. They show why planning must move beyond static State totals toward fertilizer-grade × geography × crop-stage × week intelligence.

Primary public evidence: PIB / Department of Fertilizers, 01 Apr–29 Jul 2026: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2294272

## Challenge → executable module

| Challenge gap | RAJ-URVARA response |
|---|---|
| Static historical allocation | **DemandCast** — P10/P50/P90 district × grade × week forecasts |
| No soil/crop-stage formulation intelligence | **NutrientTwin + UrvaraRX** — authorized agronomic rules + constrained product mapping |
| Limited real-time stock visibility | **Allocation Twin + StockPulse** — service-level risk and human-approved rebalancing |
| No end-to-end traceability | **TraceGraph** — tamper-evident custody events; PII stays off-ledger |
| Leakage / diversion risk | **Leakage Sentinel** — explainable human-review priority only |
| Product quality risk | **Quality Sentinel** — evidence-linked inspection prioritization only |
| Weak last-mile connectivity | **SUTRA-ID Edge + BHASHINI-ready assisted mode** |

## Core engineering principles

### DemandCast
- probabilistic P10/P50/P90 output instead of false point precision
- rolling-origin and district-holdout release gates
- hierarchy reconciliation
- stock-out censoring: zero sales during no-stock periods are not learned as zero demand
- reason-coded feature contributions and drift watches

### NutrientTwin / UrvaraRX
- source, freshness, crop and crop-stage are first-class fields
- numeric agronomic values may only originate from authorized deterministic services/rules
- RAJ-NUTRI may retrieve, call tools and explain; it cannot invent a fertilizer dose/product

### Allocation Twin
- minimum source stock-cover floor
- uncertainty-aware service-level planning
- remote/low-connectivity regions cannot be optimized away
- consequential actions require human approval or reason-coded override
- every action produces a Decision Receipt

### TraceGraph / StockPulse
- dispatch → warehouse → transfer → dealer → retail reference → field acknowledgement
- PII and raw Government documents stay off-chain
- custody proof can be anchored to permissioned DLT **or** an approved signed append-only journal
- QR/lot scans + mobile geofence evidence by default; dedicated IoT/GPS only where justified

### SUTRA-ID Edge
Optional assisted-service endpoint for low-connectivity/digital-literacy/evidence edge cases. Phone/PWA and officer/dealer web remain the primary channels. The evaluator build demonstrates signed offline queueing and idempotent synchronization.

## Integration truth standard

Every connector is explicitly one of:
- `LIVE_PUBLIC` — published non-sensitive evidence embedded in the prototype
- `CONTRACT_READY` — adapter/schema prepared; production authorization/credentials required
- `DEMO_SANDBOX` — synthetic operational values or local simulation

**No Government integration is represented as live unless it actually is.**

See `contracts/integration_status.json` and `docs/INTEGRATION_TRUTH.md`.

## 90-day impact contract

Proposed pilot gates — **targets, not achieved claims**:
- ≥10% relative WAPE improvement vs Department-agreed baseline
- P90 empirical coverage 85–95%
- ≥24h warning before stock-cover breach where data availability permits
- ≥95% required custody-event completeness
- 0 duplicate SUTRA business events after retry
- 100% auditable receipts for consequential pilot decisions

Start in **shadow mode**, measure against the baseline, then progressively enable human-approved recommendations. See `docs/PILOT_SCORECARD.md`.

## Reproducible release gate

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
node --check dashboard/app.js
```

Current evaluator release: **9/9 Python safety/engineering gates pass locally**, JavaScript syntax passes, and the v4 console has been browser-tested across its operational flows and 390 px mobile layout.

The committed tests cover deterministic nutrient safety, forecast quantile ordering, stock-out censoring, hierarchy reconciliation, allocation source-floor protection, TraceGraph tamper detection, Sentinel human-review boundaries, RAJ-NUTRI hard prohibitions and SUTRA idempotent sync.

## Repository structure

```text
.
├── index.html
├── dashboard/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── services/
│   ├── demandcast/model.py
│   ├── allocation/optimizer.py
│   ├── nutrient_engine/rules.py
│   ├── tracegraph/chain.py
│   ├── anomaly/scoring.py
│   ├── quality/sentinel.py
│   ├── nutri_slm/policy.py
│   └── sutra_edge/sync.py
├── contracts/integration_status.json
├── data/public_kharif_2026.json
├── docs/
│   ├── ARCHITECTURE.md
│   ├── INTEGRATION_TRUTH.md
│   ├── EVALUATOR_DEFENSE.md
│   ├── PILOT_SCORECARD.md
│   └── OPERATIONS_CONSOLE_V4.md
└── tests/test_release_gates.py
```

## Claim discipline

RAJ-URVARA AI is an evaluator sandbox, not a production Government service. It contains no Government secrets, Aadhaar values or real farmer PII. References to Rajasthan/GoI systems describe public evidence or proposed authorized integrations and do not imply endorsement or production access.
