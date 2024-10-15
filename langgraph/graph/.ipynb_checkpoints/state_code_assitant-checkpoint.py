from typing import List, Dict, TypedDict, Optional


class GraphState(TypedDict):
    feedback: Optional[str] = None
    history: Optional[str] = None
    code: Optional[str] = None
    specialization: Optional[str]=None
    rating: Optional[str] = None
    iterations: Optional[int]=None
    code_compare: Optional[str]=None
    actual_code: Optional[str]=None
    code_writers: Optional[List[str]]=None
    next_implementor: Optional[str]=None
   