from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"AGENTS": ["ingestion_agent.py", "retrieval_agent.py", "reranking_agent.py", "grounding_agent.py", "citation_agent.py", "evaluation_agent.py"], "TOOLS": ["document_loader.py", "chunker.py", "hybrid_retriever.py", "reranker.py", "citation_validator.py", "evaluation_tool.py"], "SKILLS": ["ingestion_planning.py", "query_decomposition.py", "context_selection.py", "grounding_analysis.py", "citation_verification.py", "rag_evaluation.py"]}
def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")
