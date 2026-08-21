from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RerankingAgent:
    name: str = "reranking_agent"
    responsibility: str = "Rank retrieved evidence and construct a bounded context set."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        hits = case.get("retrieved_hits", [])
        ranked = tools["reranker"].rank(case.get("question", ""), hits)
        selected = skills["context_selection"](ranked, case.get("context_budget", 5))
        return {"agent": self.name, "ranked": ranked, "selected_context": selected}
