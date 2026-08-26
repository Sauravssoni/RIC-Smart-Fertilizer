# RAJ-URVARA AI — 90-Day Pilot Scorecard

The pilot is designed to prove decision quality and operational usability before any statewide automation. No KPI requires autonomous allocation, subsidy denial or agronomic prescription by an LLM.

## Pilot design
Use three contrasting agro-logistics archetypes selected with the Department (for example: dryland/western, irrigated/northern-eastern, and southern/tribal-hilly). Final districts are chosen jointly after data-access and operational-readiness review.

### Days 0–15 — Baseline & contracts
- Freeze authoritative source definitions and integration contracts.
- Establish historical baseline by grade × district/block × week.
- Define SHC/crop/weather freshness rules and model-card acceptance thresholds.
- Map warehouse/dealer event states and human approval roles.

### Days 16–35 — Shadow intelligence
- Run DemandCast in shadow mode against existing planning.
- Create NutrientTwin/UrvaraRX only from authorized agronomic sources.
- Measure P10/P50/P90 calibration and stock-out censoring behavior.
- No operational stock movement is executed from AI output.

### Days 36–60 — Human-in-the-loop operations
- Activate Allocation Twin recommendations with officer approval.
- Pilot TraceGraph/StockPulse on selected routes/lots.
- Use Leakage and Quality Sentinel only as review queues.
- Pilot SUTRA assisted workflows at a small number of authorized field/service points.

### Days 61–75 — Stress & failure testing
- Missing API / delayed data / stale SHC / connectivity outage drills.
- Duplicate SUTRA sync and conflict tests.
- Trace-tamper and rollback tests.
- Fairness-floor and override testing.

### Days 76–90 — UAT, impact readout & scale plan
- Compare against baseline and simple seasonal forecasting benchmarks.
- Department UAT and operator training.
- Security/privacy/observability review.
- Statewide rollout economics and phased integration plan.

## Release KPIs
| KPI | Pilot target / acceptance concept |
|---|---|
| Demand forecast quality | Beat agreed seasonal/simple baseline on WAPE/MAE at grade × geography × week |
| Quantile calibration | P90 coverage close to nominal target; calibration reported, never hidden |
| Stock-out handling | Stock-out periods flagged as censored rather than interpreted as zero demand |
| Service level | Reduction in simulated/observed low-stock-cover days without degrading protected source floors |
| Emergency rebalancing | Fewer late emergency transfers or earlier warning lead time versus baseline |
| Trace completeness | >95% required pilot custody transitions carrying valid event/evidence references |
| Trace integrity | 100% deliberate tamper tests detected by the pilot verification gate |
| Exception resolution | Median time from alert → human disposition measured and improved during pilot |
| Quality workflow | Sampling priority produces officer queue only; zero automatic certification/enforcement |
| AI safety | Zero unsupported numeric fertilizer dose/product outputs in red-team evaluation set |
| SUTRA resilience | Duplicate-safe sync; signed offline events recover after reconnect; no duplicate state mutation |
| User acceptance | Officer/dealer/field-user task completion and explainability rating captured in UAT |

## Scale economics principle
QR/mobile event capture first. Dedicated IoT/GPS devices only where route risk, consignment value or operational criticality justifies them. Reuse iFMS/DBT/FFS/SHC/AgriStack/BHASHINI/Rajasthan infrastructure wherever authorized; do not rebuild systems of record.
