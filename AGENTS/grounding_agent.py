from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class GroundingAgent:
    name: str = "grounding_agent"
    responsibility: str = "Check whether proposed answer claims are supported by selected context."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        claims = case.get("claims", [])
        context = case.get("context", [])
        assessment = skills["grounding_analysis"](claims, context)
        return {"agent": self.name, "grounding": assessment, "supported": all(x.get("supported", False) for x in assessment) if assessment else False}
