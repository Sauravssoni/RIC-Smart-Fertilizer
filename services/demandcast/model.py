"""Small deterministic primitives illustrating DemandCast release logic."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Forecast:
    p10: float
    p50: float
    p90: float

def forecast(base: float, crop_area_change_pct: float = 0, weather_pct: float = 0, high_service: bool = False) -> Forecast:
    if base < 0: raise ValueError("base demand cannot be negative")
    median = max(0.0, base * (1 + crop_area_change_pct/100) * (1 + max(-0.2, min(0.2, weather_pct*0.003))))
    spread = 0.16 if high_service else 0.12
    return Forecast(round(max(0, median*(1-spread)),4), round(median,4), round(median*(1+spread),4))

def latent_demand_observation(sales: float, closing_stock: float, stockout_flag: bool) -> dict:
    """Do not encode a stock-out as evidence that latent demand was zero."""
    if sales < 0 or closing_stock < 0: raise ValueError("sales/stock cannot be negative")
    return {"sales": sales, "closing_stock": closing_stock, "censored": bool(stockout_flag), "usable_as_zero_demand": not stockout_flag}

def reconcile(children: list[float]) -> float:
    if any(x < 0 for x in children): raise ValueError("negative child demand")
    return round(sum(children), 6)
