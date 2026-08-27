# Evidence & Claim Register

RAJ-URVARA is intentionally conservative about what is public, simulated, integration-ready and independently validated.

| Claim / component | State | Evidence / boundary |
|---|---|---|
| Rajasthan Kharif 2026 fertilizer position | `LIVE_PUBLIC` | Government of India / PIB public aggregate snapshot used in proposal and dashboard. Aggregate values are not interpreted as proof of local shortage or leakage. |
| Soil Health Card parameter structure | `LIVE_PUBLIC` | Official Soil Health Card API/integration guidance; production data remains authorization-dependent. |
| District risk, warehouse, dealer, plot and farmer records in evaluator console | `DEMO_SANDBOX` | Synthetic records constructed to exercise the closed-loop workflow. |
| iFMS / DBT | `CONTRACT_READY` | Existing national fertilizer transaction/movement rail; no production credentials represented as held. |
| FFS / DRS | `CONTRACT_READY` | Existing fertilizer application/retail/dispute rail; adapter requires authorization. |
| AgriStack / DCS / KDSS | `CONTRACT_READY` | Farmer/plot/crop context is consumed only through approved interfaces. |
| IMD / approved weather | `CONTRACT_READY` | Production weather connector requires approved source/interface. |
| Raj Sewa Dwaar / State APIs | `CONTRACT_READY` | Preferred State integration gateway; no unauthorized API use. |
| FCO / laboratory / COA evidence | `CONTRACT_READY` | Quality Sentinel only prioritizes authorized inspection. |
| FarmGraph | `LOCAL_PROOF / DEMO` | Typed temporal evidence and lineage architecture; authoritative systems remain authoritative. |
| DemandCast | `SHADOW / DEMO` | Probabilistic forecasting workflow and release gates demonstrated; pilot improvement targets are not claimed as achieved. |
| RAJ-NUTRI | `SANDBOX` | Tool-using explanation policy with explicit prohibition on invented numeric agronomic recommendations. |
| TraceGraph | `LOCAL_PROOF / DEMO` | Tamper-evident event chain and PII-exclusion model demonstrated. Production DLT is optional and governance-dependent. |
| SUTRA-ID Edge capability | `TECHNICAL EXECUTION PROOF` | Offline voice/scan/human-confirmation/signed-event/idempotent-sync pattern; not represented here as a Smart Fertilizer production deployment. |
| VYOM Trade Ledger | `DOCUMENTED PROGRAM MILESTONE` | MeitY/C-DAC Blockchain India Challenge Proof-of-Concept progression; transferable relevance is permissioned traceability and governed state. |
| Nyaya Saarthi | `DOCUMENTED PROGRAM MILESTONE` | IndiaAI evaluation/Stage-2/Pilot progression supported by applicant evidence; transferable relevance is human-authority, evidence-linked AI workflow design. |

## Explicit non-claims

RAJ-URVARA does not claim that:
- district sandbox figures are current Government operating data;
- the State presently has a fertilizer shortage or leakage problem merely because grade-level public aggregates differ;
- Government APIs are live without credentials/authorization;
- a blockchain is mandatory for every trace event;
- AI is authorized to prescribe fertilizer autonomously;
- anomaly scoring can deny a farmer, accuse a dealer or trigger enforcement;
- proposed pilot KPIs have already been achieved;
- the INR 79.50 lakh pilot ask is a statewide rollout price.

This register is part of the evaluator release contract: impressive functionality must remain inspectably truthful.
