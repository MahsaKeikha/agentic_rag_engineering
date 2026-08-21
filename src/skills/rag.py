def plan_ingestion(a):return {**a,"questions":([] if all(a.values()) else ["Corpus, chunking, and index version are required"])}
def assess_retrieval(a):
 q=[] if a["retrieved"] else ["No retrieval evidence supplied"]
 r=[] if a["retrieval_metrics"] else ["Retrieval quality has not been evaluated"]
 return {**a,"questions":q,"risks":r}
def select_context(a):return {**a,"risks":([] if a["context_ids"] else ["No selected context IDs supplied"])}
def verify_grounding(a):
 q=[];r=[]
 if not a["answer"]:q.append("Generated answer is missing")
 if not a["citations"]:q.append("Citations are missing")
 if a["grounding_score"] is None or a["grounding_score"]<a["threshold"]:r.append("Grounding is below the required threshold")
 return {**a,"questions":q,"risks":r}
def evaluate_answer(a):
 r=[] if a["answer_metrics"] else ["Answer-quality evaluation is missing"]
 r.extend("Evaluation failure: "+str(x) for x in a["failure_cases"])
 return {**a,"risks":r}
SKILL_MANIFEST=["plan_ingestion","assess_retrieval","select_context","verify_grounding","evaluate_answer"]
