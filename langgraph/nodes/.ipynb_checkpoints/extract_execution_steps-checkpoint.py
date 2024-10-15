from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_extract_execution_step
from entities.failure_analysis_report import FailureAnalysisReport

from state.failure_analysis_state import FailureAnalysisState

def handle_extract_execution_steps(state:FailureAnalysisState):
    print("----------------------------------------")
    print("**extract_execution_steps** working...")
    job_id = state.get('job_id')
    log_content = state.get('log_content', '').strip()
    issues_exist = state.get('issues_exist')
    issues = state.get('issues')
    exceptions = state.get('exceptions')

    # print("---**input**--:")
    prompt = prompt_extract_execution_step.format_map(FormatDict(log_content=log_content)
                                        )
    result = gemini_flash.invoke(prompt).content
    execution_steps = result.strip()

    # print("---**response**--:")
    # print(f"execution_steps:{execution_steps}")
    failure_analysis_report  = FailureAnalysisReport(job_id = job_id,
                                             log_content = log_content,
                                             issues_exist = issues_exist,
                                             issues = issues,
                                             exceptions = exceptions,
                                             execution_steps = execution_steps
                                             )
    
    return {'failure_analysis_report': [failure_analysis_report]}
