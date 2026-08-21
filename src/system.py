from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4
from .agents import build_agents

SYSTEM_ID, SYSTEM_NAME, VERSION = "F35", "Agentic RAG Engineering", "0.2.1"

@dataclass
class State:
    case: Dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    analyses: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Dict[str, str]] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def record(self, actor: str, event: str, artifact: Any = None) -> None:
        self.trace.append({"step": len(self.trace) + 1, "actor": actor, "event": event, "artifact": artifact})

    def rec(self, actor: str, event: str, artifact: Any = None) -> None:
        self.record(actor, event, artifact)


def run_system(case: Dict[str, Any], approve: bool = False) -> Dict[str, Any]:
    s = State(case)
    s.record("rag_orchestrator", "run started", {"system_id": SYSTEM_ID, "version": VERSION})
    for agent in build_agents():
        agent.run(s)
    for evidence in case.get("evidence", []):
        s.evidence.append({"claim": str(evidence.get("claim", "")), "source": str(evidence.get("source", "")), "status": str(evidence.get("status", "supplied"))})
    s.conflicts.extend(case.get("conflicts", []))
    blockers = bool(s.unresolved_questions or s.conflicts or s.risks)
    status = "approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    s.record("rag_orchestrator", "grounding gate evaluated", {"approve": approve, "blockers": blockers, "status": status})
    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "run_id": s.run_id,
        "domain": "rag_engineering",
        "analyses": s.analyses,
        "evidence": s.evidence,
        "unresolved_questions": s.unresolved_questions,
        "conflicts": s.conflicts,
        "risks": s.risks,
        "recommendation": "Do not release as grounded; resolve RAG blockers." if blockers else "Grounded result is ready for accountable human review.",
        "status": status,
        "trace": s.trace,
    }
