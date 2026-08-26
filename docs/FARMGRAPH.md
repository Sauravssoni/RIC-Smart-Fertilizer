# FarmGraph — Rajasthan Nutrient & Fertilizer Evidence Twin

FarmGraph is the common evidence substrate behind RAJ-URVARA AI. It is **not** a replacement farmer database and does not claim production access to AgriStack, Soil Health Card or Rajasthan systems.

## Purpose

FarmGraph links permitted, versioned references required to explain a fertilizer decision:

`farmer ref → plot / parcel → crop cycle → soil / SHC → weather → agronomy rule → nutrient decision → demand forecast → stock / lot → custody event → human decision → outcome`

Authoritative records remain with their source systems. The graph stores only authorized references, hashes, derived features, lineage and approved caches.

## Why a graph

A fertilizer recommendation or allocation decision is temporal. Crop stage changes, SHC freshness changes, weather changes, stock changes and policy/rule versions change. FarmGraph preserves the exact evidence path used at decision time instead of flattening these relationships into an opaque row.

## Operational uses

- **NutrientTwin / UrvaraRX** — resolves the soil, crop-stage and rule context used for a governed nutrient recommendation.
- **DemandCast** — adds plot/crop/soil/weather features while retaining source/version lineage.
- **FlowOpt** — links demand pressure to stock-cover, lead-time and source-floor constraints.
- **TraceGraph** — connects lot/custody evidence back to the operational demand and decision that caused movement.
- **Decision Receipts** — records causal factors, constraint checks, officer disposition and references.
- **Outcome learning** — allows future seasons to compare forecast, movement and agronomic outcomes without rewriting history.

## Safety boundary

FarmGraph never gives an LLM authority to invent a numeric dose, mutate an official farmer record, deny subsidy, certify fertilizer quality or automatically enforce against a dealer. Numeric agronomy must come from authorized deterministic rules/tools; consequential Government actions remain human-authorized.

## 90-day scope

The pilot implements a pragmatic temporal graph/reference model and explainable feature lineage. Graph neural networks or advanced graph ML are post-pilot options only if data volume, validation and incremental value justify them.
