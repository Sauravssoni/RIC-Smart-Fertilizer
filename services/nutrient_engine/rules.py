"""Guarded nutrient-risk primitives for the evaluator sandbox.
No fertilizer dose is generated here. Production numeric values must come
from authorized SHC/STCR/Department rules and permitted-product constraints.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class NutrientRisk:
    level: str
    score: int
    reasons: tuple[str, ...]
    generates_dose: bool = False

def assess(n: float, p: float, k: float, organic_c: float) -> NutrientRisk:
    vals = (n, p, k, organic_c)
    if any(v is None or not isinstance(v, (int, float)) for v in vals):
        raise ValueError("numeric indicators required")
    reasons: list[str] = []
    score = 0
    if n < 40: score += 3; reasons.append("N indicator low")
    elif n < 60: score += 1; reasons.append("N indicator moderate")
    if p < 35: score += 2; reasons.append("P indicator low")
    if k < 45: score += 2; reasons.append("K indicator low")
    if organic_c < 0.5: score += 2; reasons.append("organic carbon indicator low")
    level = "HIGH" if score >= 6 else "MEDIUM" if score >= 3 else "LOW"
    return NutrientRisk(level, score, tuple(reasons))
