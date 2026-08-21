from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class CitationAgent:
    name: str = "citation_agent"
    responsibility: str = "Verify citation presence, source linkage, and claim-to-source traceability."

    def run(self, case: Dict[str, Any], tools: Dict[str, Any], skills: Dict[str, Any]) -> Dict[str, Any]:
        citations = case.get("citations", [])
        checked = tools["citation_validator"].validate(citations, case.get("context", []))
        return {"agent": self.name, "citations": checked, "valid": skills["citation_verification"](checked)}
