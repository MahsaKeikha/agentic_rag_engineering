# F35 Tools

Executable RAG tools live in [`src/tools/`](../src/tools/).

The tool layer supports ingestion/document operations, retrieval/context operations, grounding/citation evidence, and evaluation artifacts. In a provider-integrated implementation this interface is where vector stores, embedding providers, rerankers, document loaders, and evaluation backends are adapted without coupling them directly to agents.

See [`src/tools/domain_tools.py`](../src/tools/domain_tools.py).