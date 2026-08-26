"""Fairness-constrained stock transfer proposal. Human approval is mandatory."""
from dataclasses import dataclass

@dataclass(frozen=True)
class TransferProposal:
    quantity: float
    source_after_days: float
    approved: bool = False
    reason: str = "human approval required"

def propose_transfer(source_stock: float, source_daily_demand: float, destination_gap: float, min_source_cover_days: float = 7.0) -> TransferProposal:
    if min(source_stock, source_daily_demand, destination_gap) < 0 or source_daily_demand == 0:
        raise ValueError("invalid allocation inputs")
    protected = source_daily_demand * min_source_cover_days
    movable = max(0.0, source_stock - protected)
    qty = min(movable, destination_gap)
    after = (source_stock - qty) / source_daily_demand
    return TransferProposal(round(qty,4), round(after,4))
