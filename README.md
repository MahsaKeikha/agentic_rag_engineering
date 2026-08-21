# F35 Agentic RAG Engineering

Standalone multi-agent reference architecture for retrieval-augmented generation with explicit ingestion, retrieval, grounding, citation, and evaluation stages.

## Agent team

- Ingestion Agent
- Retrieval Agent
- Reranking and Context Agent
- Grounding and Citation Agent
- Evaluation Agent
- RAG Orchestrator

The **actual specialist agent implementations live in [`src/agents.py`](src/agents.py)**. Shared state, evidence tracking, orchestration, and grounding gates live in [`src/system.py`](src/system.py). Agent-composition and workflow tests live under [`tests/`](tests/).

## Architecture

```text
Corpus / query
   ↓
Ingestion Agent
   ↓
Retrieval Agent
   ↓
Reranking / Context Agent
   ↓
Grounding / Citation Agent
   ↓
Evaluation Agent
   ↓
RAG Orchestrator / Grounding Gate
```

The system evaluates retrieval evidence separately from answer and grounding evidence. It blocks a clean release when retrieval quality, citations, grounding, or answer-quality evidence is insufficient rather than manufacturing certainty.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Real deployments require corpus-specific evaluation, access controls, privacy/security review, freshness policy, provider validation, observability, and adversarial testing.

## AI Engineering Handbook Series

By Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.
