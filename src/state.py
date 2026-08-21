from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4
@dataclass
class RunState:
    case: Dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    analyses: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Dict[str, str]] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)
    def record(self, actor, event, artifact=None): self.trace.append({"step":len(self.trace)+1,"actor":actor,"event":event,"artifact":artifact})
