"""Explainable prioritization only; never automatic denial/enforcement."""
def review_priority(volume_ratio=1.0, route_deviation=False, repeated_pattern=False, stock_mismatch=False, identity_conflict=False):
    score, reasons = 0, []
    if volume_ratio > 2: score += 30; reasons.append("volume above reference pattern")
    if route_deviation: score += 22; reasons.append("route/geofence deviation")
    if repeated_pattern: score += 18; reasons.append("rapid repeated pattern")
    if stock_mismatch: score += 30; reasons.append("digital/physical stock mismatch")
    if identity_conflict: score += 18; reasons.append("entitlement/land-reference conflict")
    score = min(100, score)
    return {"score": score, "reasons": reasons, "action": "HUMAN_REVIEW" if score >= 35 else "MONITOR", "automatic_denial": False}
