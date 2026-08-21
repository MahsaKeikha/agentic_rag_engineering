def ingestion_record(c):return {"corpus":c.get("corpus"),"chunking":c.get("chunking"),"index_version":c.get("index_version")}
def retrieval_record(c):return {"query":c.get("query"),"retrieved":c.get("retrieved",[]),"retrieval_metrics":c.get("retrieval_metrics",{})}
def rerank_record(c):return {"reranking":c.get("reranking"),"context_ids":c.get("context_ids",[])}
def grounding_record(c):return {"answer":c.get("answer"),"citations":c.get("citations",[]),"grounding_score":c.get("grounding_score"),"threshold":c.get("grounding_threshold",0.8)}
def evaluation_record(c):return {"answer_metrics":c.get("answer_metrics",{}),"failure_cases":c.get("failure_cases",[])}
TOOL_MANIFEST=[{"name":n,"side_effects":False} for n in ("ingestion_record","retrieval_record","rerank_record","grounding_record","evaluation_record")]
