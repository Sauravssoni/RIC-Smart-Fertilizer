# RAJ-URVARA AI — Evaluator Defense

## Why not just use iFMS / DBT?
iFMS already tracks subsidized-fertilizer movement and DBT sales; RAJ-URVARA does not replace it. The missing layer in the challenge is predictive and agronomic intelligence: soil/crop/weather-aware demand, uncertainty, fair reallocation, exception reasoning, custody evidence and outcome learning. iFMS becomes an authoritative input/output rail.

## Why DLT at all?
Only tamper-evident custody transitions and evidence hashes belong on a permissioned event plane. Farmer PII, Aadhaar values, raw documents and continuous GPS do not. If the Department determines that a signed append-only journal meets the governance requirement better than DLT, TraceGraph can use that backend without changing the domain/event model. The architecture is not blockchain-dependent.

## Can an SLM safely prescribe fertilizer?
It does not. Numeric agronomic values must originate from authorized SHC/STCR/Department rules and permitted-product constraints. RAJ-NUTRI may retrieve, call approved tools, explain and translate. `generate_dose` and `invent_product` are hard-prohibited actions and are covered by the committed release tests.

## What if a Soil Health Card is stale or missing?
NutrientTwin carries source, test date/version and freshness status. Missing/stale inputs lower confidence and route the user toward re-testing or an authorized extension workflow rather than creating false precision.

## Why SUTRA-ID Edge?
It is optional. Web/mobile remain primary. SUTRA is for assisted, low-connectivity and field-evidence workflows where voice, local processing and signed offline sync materially improve last-mile execution. No statewide hardware dependency is created.

## How do you avoid starving remote districts?
Allocation Twin treats minimum source/destination stock-cover and service-level floors as constraints, not after-the-fact dashboard metrics. Recommendations remain human-approved and every override carries a reason code.

## Does Leakage Sentinel accuse dealers or deny subsidy?
No. It creates explainable human-review priority only. `automatic_denial=false` is an explicit release gate.

## Does Quality Sentinel certify fertilizer?
No. It links custody/COA/lab/sample signals to inspection priority. Certification and enforcement remain with the legally authorized authority.

## What if Government APIs are unavailable during the pilot?
Every connector is truth-labelled: `LIVE_PUBLIC`, `CONTRACT_READY` or `DEMO_SANDBOX`. The pilot can validate schemas, replay authorized extracts/synthetic fixtures, measure model/UX behavior and switch to production credentials without re-architecting the platform.

## What is real today?
A functional evaluator command centre; deterministic nutrient-risk service; probabilistic demand primitives; fair allocation proposal; tamper-evident trace chain; Leakage/Quality guardrails; SLM policy boundary; SUTRA idempotent sync; reproducible release tests; and public Rajasthan Kharif-2026 fertilizer evidence. Production Government connectors require authorization.

## Primary evidence anchors
- PIB / Department of Fertilizers, Kharif 2026 state-wise requirement, availability, DBT sales and closing stock: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2294272
- Soil Health Card API integration guidance: https://soilhealth.dac.gov.in/files/SHC_API_Integration_Guidelines.pdf
- Rajasthan Innovation Challenge listing: https://change.rajasthan.gov.in/challenges/startup
