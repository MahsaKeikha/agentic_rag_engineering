# F35 Agents

Executable specialists live in [`src/agents/`](../src/agents/).

## Agent team
- Ingestion Agent
- Retrieval Agent
- Reranking & Context Agent
- Grounding & Citation Agent
- RAG Evaluation Agent
- RAG Orchestrator

The agents separate corpus preparation, retrieval, context construction, grounded synthesis/citation, and evaluation. See [`src/agents/team.py`](../src/agents/team.py).