from typing import List

def query_decomposition(question: str) -> List[str]:
    question = question.strip()
    if not question:
        return []
    parts = [p.strip() for p in question.replace("?", ".").split(".") if p.strip()]
    return parts or [question]
