from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RetrievalAgent:
    name: str = "retrieval_agent"
    responsibility: str = "Plan and execute evidence retrieval while preserving query and source provenance."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        queries = skills["query_decomposition"](case.get("question", ""))
        hits = tools["hybrid_retriever"].search(queries, case.get("corpus", []))
        return {"agent": self.name, "queries": queries, "hits": hits}
