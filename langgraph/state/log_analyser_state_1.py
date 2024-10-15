from typing import List, Dict, TypedDict, Optional, Annotated,Sequence
import operator

from entities.failure_analysis_report import FailureAnalysisReport

class LogAnalyserState(TypedDict):
    #LogAnalyserState 
    pipeline_run_name: Optional[str] = None
    job_states: Optional[List[str]] = None
    kba_suggestion: Optional[str] = None
    report_generation: Optional[str] = None
    solutions: Optional[str] = None    
    #FailureAnalysisState
    # Parent
    custom_job_id_list: Optional[List[str]] = None
    custom_job_id_index: Optional[int] = None
    failure_analysis_report: Annotated[Sequence[FailureAnalysisReport], operator.add]