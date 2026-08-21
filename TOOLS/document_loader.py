from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class DocumentLoader:
    def inspect(self, documents: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
        docs = list(documents)
        missing_ids = [i for i, d in enumerate(docs) if not d.get("id")]
        return {"count": len(docs), "missing_ids": missing_ids, "ready": bool(docs) and not missing_ids}
