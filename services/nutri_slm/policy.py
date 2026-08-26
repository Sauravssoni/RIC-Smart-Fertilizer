"""Hard policy boundary for the RAJ-NUTRI explanation/tool layer."""
PROHIBITED = {"generate_dose","invent_product","deny_subsidy","enforce_quality","mutate_official_record"}
ALLOWED = {"retrieve_shc","retrieve_crop","retrieve_stock","retrieve_trace","explain_authorized_result"}

def authorize(tool_name: str) -> bool:
    if tool_name in PROHIBITED: return False
    return tool_name in ALLOWED
