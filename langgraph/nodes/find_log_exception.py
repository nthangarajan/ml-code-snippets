from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_find_log_exception
from state.failure_analysis_state import FailureAnalysisState
from entities.failure_analysis_report import FailureAnalysisReport

def handle_find_log_exception(state:FailureAnalysisState):
    print("----------------------------------------")
    print("**find_log_exception** working...")
    log_content = state.get('log_content', '').strip()

    job_id = state.get('job_id')
    issues_exist = state.get('issues_exist')
    issues = state.get('issues')
    # print("---**input**--:")
    prompt = prompt_find_log_exception.format_map(FormatDict(log_content=log_content)
                                        )
    result = gemini_flash.invoke(prompt).content
    exceptions = result.strip()
    print("---**response**--:")
    print(exceptions)
    failure_analysis_report  = FailureAnalysisReport(job_id = job_id,
                                             log_content = log_content,
                                             issues_exist = issues_exist,
                                             issues = issues,
                                             exceptions = exceptions,
                                             execution_steps = ''
                                             )
    
    return {'failure_analysis_report': [failure_analysis_report]}
