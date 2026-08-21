import argparse,json
from .system import run_system
EXAMPLE={"corpus":"handbook-fixture","chunking":"semantic-800","index_version":"v1","query":"What does the supplied policy require?","retrieved":[{"id":"d1","text":"Approval is required."}],"retrieval_metrics":{"recall_at_5":1.0},"reranking":"fixture","context_ids":["d1"],"answer":"The supplied policy states that approval is required.","citations":["d1"],"grounding_score":0.98,"grounding_threshold":0.8,"answer_metrics":{"faithfulness":1.0},"failure_cases":[],"evidence":[{"claim":"approval required","source":"d1","status":"supplied"}]}
def main():
 p=argparse.ArgumentParser();p.add_argument("--example",action="store_true");p.add_argument("--approve",action="store_true");a=p.parse_args();print(json.dumps(run_system(EXAMPLE if a.example else {},a.approve),indent=2))
if __name__=="__main__":main()
