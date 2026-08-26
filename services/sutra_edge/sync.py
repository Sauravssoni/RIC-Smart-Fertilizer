"""Idempotent signed-queue semantics for the SUTRA evaluator demo."""
class SyncStore:
    def __init__(self): self._seen = set(); self.events = []
    def sync(self, event_id: str, payload: dict):
        if not event_id: raise ValueError("event_id required")
        if event_id in self._seen: return {"status":"ACK_DUPLICATE","created":False}
        self._seen.add(event_id); self.events.append({"event_id":event_id,"payload":payload})
        return {"status":"ACK_CREATED","created":True}
