from typing import Dict

def rag_evaluation(metrics: Dict[str, float], threshold: float = 0.8) -> Dict[str, object]:
    failed = [name for name, value in metrics.items() if value < threshold]
    return {"pass": not failed, "failed_metrics": failed, "threshold": threshold}
