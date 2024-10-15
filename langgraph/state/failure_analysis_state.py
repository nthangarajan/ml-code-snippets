from typing import List, Dict, TypedDict, Optional, Annotated,Sequence
import operator

from entities.failure_analysis_report import FailureAnalysisReport

# Failure Analysis Sub-graph
class FailureAnalysisState(TypedDict):
    job_id: Optional[str] = None
    log_exist: Optional[bool] = None
    log_content: Optional[str] = None
    issues_exist: Optional[bool] = None
    issues: Optional[str] = None
    exceptions: Optional[str] = None
    execution_steps: Optional[str] = None
    # Parent
    custom_job_id_list: Optional[List[str]] = None
    custom_job_id_index: Optional[int] = None
    failure_analysis_report: Annotated[Sequence[FailureAnalysisReport], operator.add]
