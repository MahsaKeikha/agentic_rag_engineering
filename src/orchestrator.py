from .agents import build_agents
from .gates import evaluate_grounding_gate
from .state import RunState
SYSTEM_ID,SYSTEM_NAME,VERSION="F35","Agentic RAG Engineering","0.2.0"
def run_system(case,approve=False):
 s=RunState(case);s.record("rag_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
 for a in build_agents():a.run(s)
 for e in case.get("evidence",[]):s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
 s.conflicts.extend(case.get("conflicts",[]));status=evaluate_grounding_gate(s,approve);s.record("rag_orchestrator","grounding gate evaluated",{"approve":approve,"status":status})
 return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"rag_engineering","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Do not release as grounded; resolve RAG blockers." if status=="blocked" else "Grounded result is ready for accountable human review.","status":status,"trace":s.trace}
