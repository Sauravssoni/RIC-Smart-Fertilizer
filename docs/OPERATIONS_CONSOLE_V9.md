# Operations Console v9 — Evaluator Runbook

The evaluator UI is designed as a **State operations system**, not a pitch microsite. Navigation is workspace-based across the top; there is no numbered walkthrough sidebar.

## Workspaces

- **Command Centre** — 41-district analytical service-risk layer, statewide KPIs, district nutrient-demand/stock table, live event stream and human decision workbench.
- **FarmGraph** — temporal evidence lineage from farmer/plot/crop/SHC/weather through demand, stock, decision and custody evidence.
- **Formulation** — 12-parameter SHC-compatible NutrientTwin and governed UrvaraRX path.
- **DemandCast** — P10/P50/P90 scenario workbench, stock-out censoring and release gates.
- **Supply Network** — StockPulse reconciliation, FlowOpt transfer queue and GPS/geofence exception simulation.
- **Trace & Quality** — TraceGraph custody chain plus Leakage/Quality Sentinel human-review prioritization.
- **SUTRA Edge** — vernacular/offline assisted workflow, signed queue, reconnect and duplicate-safe sync.
- **Pilot & Vision** — 90-day impact contract and 2026–2030 scale path.
- **Governance** — integration truth states, model policy and human-authority controls.

## 90-second jury mission

1. Open the State Command Centre and select a district under P90 service-level pressure.
2. Inspect FarmGraph causal evidence: crop stage, SHC context, weather and stock state.
3. DemandCast widens the forecast envelope; FlowOpt proposes a transfer subject to source-stock floors and lead-time constraints.
4. Officer authorizes the transfer; a Decision Receipt is generated.
5. TraceGraph opens custody events and StockPulse monitors movement.
6. SUTRA captures a signed field/dealer acknowledgement while offline.
7. Reconnect; the event syncs idempotently. Retry the same event and demonstrate duplicate suppression.
8. Close on the 90-day impact contract: forecast improvement, calibrated uncertainty, custody completeness, warning lead-time and auditable decisions.

## Claim discipline

District-level risk, stock and FarmGraph values in the public evaluator build are synthetic unless explicitly marked `LIVE_PUBLIC`. Government integrations remain `CONTRACT_READY` until authorized credentials/approvals exist. The UI must never imply production access to Rajasthan systems.
