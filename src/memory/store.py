class RetrievalMemory:
 def __init__(self):self.turns=[]
 def add(self,query,context_ids):self.turns.append({"query":query,"context_ids":list(context_ids)})
 def snapshot(self):return list(self.turns)
