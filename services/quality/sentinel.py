"""Quality-risk prioritization; never quality certification."""
def sampling_priority(sample_age_days: int, complaints_per_10k: float, trace_break: bool=False):
    score = (25 if sample_age_days > 90 else 10 if sample_age_days > 45 else 0) + min(45, max(0, complaints_per_10k)*8) + (30 if trace_break else 0)
    level = "HIGH" if score >= 60 else "MEDIUM" if score >= 25 else "LOW"
    return {"level": level, "score": round(score,1), "certifies_quality": False, "enforcement": False, "next_step": "AUTHORIZED_INSPECTOR_REVIEW"}
