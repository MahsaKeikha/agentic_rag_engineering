def evaluate_result(r):
 a=r.get("analyses",{});return {"ingestion_present":"ingestion" in a,"retrieval_present":"retrieval" in a,"context_present":"context_reranking" in a,"grounding_present":"grounding_citation" in a,"answer_eval_present":"evaluation" in a,"blocked":r.get("status")=="blocked","trace_steps":len(r.get("trace",[]))}
