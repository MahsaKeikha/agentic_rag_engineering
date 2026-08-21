# F35 Agentic RAG Engineering

Standalone multi-agent reference architecture for retrieval-augmented generation with explicit ingestion, retrieval, reranking/context, grounding/citation, and evaluation stages.

## Repository map

```text
.github/workflows/tests.yml
src/agents.py
src/state.py
src/gates.py
src/orchestrator.py
src/system.py
src/run.py
evals/evaluator.py
examples/rag_case.json
benchmarks/README.md
docs/ARCHITECTURE.md
tests/
SECURITY.md
CONTRIBUTING.md
CITATION.cff
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
pyproject.toml
```

## Multi-agent team
Ingestion Agent, Retrieval Agent, Reranking/Context Agent, Grounding and Citation Agent, Evaluation Agent, and RAG Orchestrator.

```bash
python -m src.run --example
pytest -q
```

Retrieval quality and answer quality are evaluated separately. Missing citations, insufficient grounding, absent retrieval evidence, conflicts, or failed cases block a clean release state.

**Maturity: Reference implementation.** Real deployments require corpus-specific evaluation, access controls, privacy/security review, freshness policy, provider validation, observability, and adversarial testing.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
