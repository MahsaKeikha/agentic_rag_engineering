from typing import Any
class BaseAgent:
 name="agent";responsibility="";required_skills:tuple[str,...]=();allowed_tools:tuple[str,...]=()
 def run(self,state:Any)->None:raise NotImplementedError
