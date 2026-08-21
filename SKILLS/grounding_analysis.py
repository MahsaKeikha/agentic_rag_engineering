from typing import Any, Dict, Iterable, List

def grounding_analysis(claims: Iterable[Dict[str, Any]], context: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    corpus = " ".join(str(x.get("text", "")).lower() for x in context)
    results = []
    for claim in claims:
        text = str(claim.get("text", ""))
        tokens = [t for t in text.lower().split() if len(t) > 3]
        supported = bool(tokens) and sum(1 for t in tokens if t in corpus) / len(tokens) >= 0.5
        results.append({"claim": text, "supported": supported})
    return results
