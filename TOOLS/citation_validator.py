from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class CitationValidator:
    def validate(self, citations: Iterable[Dict[str, Any]], context: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        source_ids = {str(x.get("id")) for x in context if x.get("id") is not None}
        return [{**c, "valid": str(c.get("source_id")) in source_ids} for c in citations]
