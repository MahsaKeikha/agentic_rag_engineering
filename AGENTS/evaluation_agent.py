from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RAGEvaluationAgent:
    name: str = "rag_evaluation_agent"
    responsibility: str = "Evaluate retrieval quality, grounding, citation integrity, and answer readiness separately."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        metrics = tools["evaluation_tool"].score(case)
        decision = skills["rag_evaluation"](metrics)
        return {"agent": self.name, "metrics": metrics, "decision": decision}
