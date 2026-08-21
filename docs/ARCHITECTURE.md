# Architecture

`corpus/query -> RAG Orchestrator -> Ingestion -> Retrieval -> Reranking/Context -> Grounding/Citation -> Evaluation -> grounding gate`

Retrieval quality and answer quality are evaluated separately. Missing citations, insufficient grounding, absent retrieval evidence or failed cases prevent a clean release state.
