from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class IngestionAgent:
    name: str = "ingestion_agent"
    responsibility: str = "Assess corpus ingestion readiness, document coverage, metadata, and chunking prerequisites."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        docs = case.get("documents", [])
        plan = skills["ingestion_planning"](case)
        audit = tools["document_loader"].inspect(docs)
        return {"agent": self.name, "plan": plan, "document_audit": audit, "ready": bool(docs)}
