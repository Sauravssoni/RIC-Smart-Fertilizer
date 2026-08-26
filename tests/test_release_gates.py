import unittest
from services.nutrient_engine.rules import assess
from services.demandcast.model import forecast, latent_demand_observation, reconcile
from services.allocation.optimizer import propose_transfer
from services.tracegraph.chain import append, verify
from services.anomaly.scoring import review_priority
from services.quality.sentinel import sampling_priority
from services.nutri_slm.policy import authorize
from services.sutra_edge.sync import SyncStore

class ReleaseGates(unittest.TestCase):
    def test_01_nutrient_engine_never_generates_dose(self): self.assertFalse(assess(28,24,38,.38).generates_dose)
    def test_02_forecast_quantiles_are_monotonic(self):
        f=forecast(1.0,12,18,True); self.assertLessEqual(f.p10,f.p50); self.assertLessEqual(f.p50,f.p90)
    def test_03_stockout_is_censored_not_zero_demand(self): self.assertFalse(latent_demand_observation(0,0,True)["usable_as_zero_demand"])
    def test_04_hierarchy_reconciles(self): self.assertEqual(reconcile([.2,.3,.5]),1.0)
    def test_05_allocation_preserves_source_floor_and_requires_human(self):
        p=propose_transfer(20,2,10,7); self.assertGreaterEqual(p.source_after_days,7); self.assertFalse(p.approved)
    def test_06_trace_chain_detects_tampering(self):
        c=[]; append(c,{"state":"dispatch","batch":"A"}); append(c,{"state":"receipt","batch":"A"}); self.assertTrue(verify(c)); c[0]["event"]["state"]="tampered"; self.assertFalse(verify(c))
    def test_07_sentinel_never_auto_denies_or_enforces(self):
        a=review_priority(2.5,True,False,True,False); q=sampling_priority(100,4,True); self.assertFalse(a["automatic_denial"]); self.assertFalse(q["enforcement"]); self.assertFalse(q["certifies_quality"])
    def test_08_slm_hard_prohibition(self): self.assertFalse(authorize("generate_dose")); self.assertTrue(authorize("explain_authorized_result"))
    def test_09_sutra_sync_is_idempotent(self):
        s=SyncStore(); self.assertTrue(s.sync("evt-1",{"x":1})["created"]); self.assertFalse(s.sync("evt-1",{"x":1})["created"]); self.assertEqual(len(s.events),1)

if __name__ == '__main__': unittest.main()
