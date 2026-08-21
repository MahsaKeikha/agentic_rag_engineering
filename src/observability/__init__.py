def trace_summary(trace):return {"steps":len(trace),"actors":sorted({e.get("actor") for e in trace if e.get("actor")})}
