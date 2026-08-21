from typing import Any, Dict

def ingestion_planning(case: Dict[str, Any]) -> Dict[str, Any]:
    docs = case.get("documents", [])
    return {
        "document_count": len(docs),
        "require_metadata": True,
        "require_stable_ids": True,
        "chunking_strategy": case.get("chunking_strategy", "bounded_overlap"),
    }
