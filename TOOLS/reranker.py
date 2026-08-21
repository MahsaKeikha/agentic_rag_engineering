from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class Reranker:
    def rank(self, query: str, hits: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        q = set(query.lower().split())
        ranked = []
        for hit in hits:
            text = str(hit.get("text", ""))
            score = float(hit.get("retrieval_score", 0.0)) + len(q & set(text.lower().split()))
            ranked.append({**hit, "rerank_score": score})
        return sorted(ranked, key=lambda x: x["rerank_score"], reverse=True)
