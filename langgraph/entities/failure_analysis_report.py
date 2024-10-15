from typing import List, TypedDict, Optional, Annotated, Dict
import pandas as pd

from pydantic import BaseModel

class FailureAnalysisReport(BaseModel):
    job_id: Optional[str] = None
    log_content: Optional[str] = None
    issues_exist: Optional[bool] = None
    issues: Optional[str] = None
    exceptions: Optional[str] = None
    execution_steps: Optional[str] = None