# RAJ-URVARA AI — Architecture

`Observe → Infer → Plan → Execute → Verify → Learn`

1. **NutrientTwin**: versioned plot nutrient context; production values from authorized SHC/STCR/Department rules.
2. **UrvaraRX**: constrained permitted-product and stock optimization. The SLM never creates dose/product values.
3. **DemandCast**: district × grade × week P10/P50/P90 planning with stock-out censoring and hierarchy reconciliation.
4. **Allocation Twin**: human-approved rebalancing with minimum stock-cover fairness floors.
5. **TraceGraph / StockPulse**: custody state transitions and evidence hashes; PII/raw evidence stays off-ledger.
6. **Leakage + Quality Sentinel**: investigation/inspection prioritization only.
7. **SUTRA-ID Edge**: optional voice-first/offline assisted channel with signed, idempotent sync.

## Deployment principle
Federated-by-default. Existing GoI/Rajasthan systems remain systems of record. RAJ-URVARA is the decision, orchestration and trust layer around them.
