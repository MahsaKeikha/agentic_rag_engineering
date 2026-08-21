# F35 Agentic RAG Engineering

Standalone multi-agent reference architecture for retrieval-augmented generation with explicit ingestion, retrieval, grounding, citation, and evaluation stages.

## Agents
Ingestion Agent, Retrieval Agent, Reranking/Context Agent, Grounding and Citation Agent, Evaluation Agent, and RAG Orchestrator.

The system measures retrieval evidence separately from answer/grounding evidence and blocks release when grounding is insufficient rather than manufacturing certainty.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Real deployments require corpus-specific evaluation, access controls, privacy/security review, freshness policy, provider validation, observability, and adversarial testing.

AI Engineering Handbook Series by Mahsa Keikha: https://a.co/d/0cbZnSMi and https://a.co/d/07HnRY7H

MIT licensed.
