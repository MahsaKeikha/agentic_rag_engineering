# F35 Agentic RAG Engineering

Standalone multi-agent reference architecture for retrieval-augmented generation with explicit ingestion, retrieval, reranking/context, grounding/citation, and evaluation stages.

## Architecture

```text
src/
├── agents/          Ingestion, Retrieval, Context, Grounding, Evaluation agents
├── tools/           deterministic RAG evidence and record builders
├── skills/          reusable RAG reasoning procedures
├── memory/          retrieval memory
├── schemas/         RAG evidence contracts
├── prompts/         grounding principles
├── config/          grounding and citation thresholds
├── safety/          grounded-release policy
├── observability/   trace summaries
├── state.py
├── gates.py
├── orchestrator.py
├── system.py
└── run.py
```

### Agents
Ingestion Agent, Retrieval Agent, Reranking/Context Agent, Grounding and Citation Agent, Evaluation Agent, coordinated by the RAG Orchestrator.

### Skills
Ingestion planning, retrieval assessment, context selection, grounding verification, answer evaluation.

### Tools
Ingestion record, retrieval record, reranking/context record, grounding record, evaluation record.

See `docs/AGENTS_TOOLS_SKILLS.md`.

```bash
python -m src.run --example
pytest -q
```

Retrieval quality and answer quality are evaluated separately. Missing citations, insufficient grounding, absent retrieval evidence, conflicts, or failed cases block a clean release state.

**Maturity: Reference implementation.** Real deployments require corpus-specific evaluation, access controls, privacy/security review, freshness policy, provider validation, observability, and adversarial testing.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
