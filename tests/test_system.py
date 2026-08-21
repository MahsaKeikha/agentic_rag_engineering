from src.system import run_system
def case():return {"corpus":"c","chunking":"x","index_version":"1","query":"q","retrieved":[{"id":"d"}],"retrieval_metrics":{"recall":1},"reranking":"r","context_ids":["d"],"answer":"a","citations":["d"],"grounding_score":0.9,"grounding_threshold":0.8,"answer_metrics":{"faithfulness":1},"failure_cases":[]}
def test_clean_waits():assert run_system(case())["status"]=="awaiting_human_approval"
def test_clean_approval():assert run_system(case(),True)["status"]=="approved_for_human_follow_through"
def test_low_grounding_blocks():
 c=case();c["grounding_score"]=0.2;assert run_system(c,True)["status"]=="blocked"
def test_missing_citations_blocks():
 c=case();c["citations"]=[];assert run_system(c,True)["status"]=="blocked"
