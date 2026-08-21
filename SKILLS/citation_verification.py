from typing import Any, Dict, Iterable

def citation_verification(citations: Iterable[Dict[str, Any]]) -> bool:
    items = list(citations)
    return bool(items) and all(bool(x.get("valid")) for x in items)
