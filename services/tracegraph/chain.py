"""Minimal tamper-evident custody chain; sensitive evidence stays off-ledger."""
import hashlib, json

def digest(event: dict, previous_hash: str = "GENESIS") -> str:
    safe = {k:v for k,v in event.items() if k not in {"aadhaar","farmer_name","raw_document","photo"}}
    payload = json.dumps({"previous": previous_hash, "event": safe}, sort_keys=True, separators=(",",":"))
    return hashlib.sha256(payload.encode()).hexdigest()

def append(chain: list[dict], event: dict) -> dict:
    prev = chain[-1]["hash"] if chain else "GENESIS"
    item = {"event": event, "previous_hash": prev, "hash": digest(event, prev)}
    chain.append(item); return item

def verify(chain: list[dict]) -> bool:
    prev = "GENESIS"
    for item in chain:
        if item.get("previous_hash") != prev or item.get("hash") != digest(item.get("event", {}), prev): return False
        prev = item["hash"]
    return True
