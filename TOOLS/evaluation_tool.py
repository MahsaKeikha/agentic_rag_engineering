from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RAGEvaluationTool:
    def score(self, case: Dict[str, Any]) -> Dict[str, float]:
        retrieved = case.get("retrieved_hits", [])
        citations = case.get("citations", [])
        grounded = case.get("grounding", [])
        return {
            "retrieval_coverage": min(1.0, len(retrieved) / max(1, int(case.get("expected_hits", 1)))),
            "citation_validity": sum(1 for c in citations if c.get("valid")) / max(1, len(citations)),
            "grounding_rate": sum(1 for g in grounded if g.get("supported")) / max(1, len(grounded)),
        }
