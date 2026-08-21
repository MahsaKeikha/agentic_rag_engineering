from typing import Any, Dict, Iterable, List

def context_selection(ranked: Iterable[Dict[str, Any]], budget: int = 5) -> List[Dict[str, Any]]:
    return list(ranked)[:max(1, int(budget))]
