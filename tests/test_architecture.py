from src.agents import AGENT_MANIFEST,build_agents
from src.orchestrator import run_system
def test_team():
 a=build_agents();assert len(a)==5 and len({x.name for x in a})==5 and all(x["responsibility"] for x in AGENT_MANIFEST)
def test_orchestrator_trace():
 assert run_system({})["trace"][0]["actor"]=="rag_orchestrator"
