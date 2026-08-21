from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

@dataclass
class HybridRetriever:
    top_k: int = 8

    def search(self, queries: Iterable[str], corpus: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        terms = {t.lower() for q in queries for t in q.split() if t.strip()}
        scored = []
        for item in corpus:
            text = str(item.get("text", ""))
            tokens = set(text.lower().split())
            score = len(terms & tokens)
            if score:
                scored.append({**item, "retrieval_score": float(score)})
        return sorted(scored, key=lambda x: x["retrieval_score"], reverse=True)[:self.top_k]
