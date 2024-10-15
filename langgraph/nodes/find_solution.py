from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_find_solution

def handle_find_solution(state):
    print("----------------------------------------")
    print("**find_solution** working...")
    pipeline_run_name = state.get('pipeline_run_name', '').strip()
    custom_job_id_list = state.get('custom_job_id_list')
    custom_job_id_index = state.get('custom_job_id_index')
    job_id = custom_job_id_list[custom_job_id_index]

    log_issues = state.get('log_issues')
    exception_info = state.get('exception_info')
    
    issues_exist = state.get('issues_exist', '')
    # print("---**input**--:")
    # print(f"issues_exist:{issues_exist}")
    
    solutions = f"pipeline_run_name : {pipeline_run_name}" + "\n"
    solutions = solutions + f"job_id : {job_id}" + "\n"
    
    if issues_exist == False:
        solutions = solutions + 'No issues' + "\n" 
    else:
        prompt = prompt_find_solution.format_map(FormatDict(log_issues=log_issues,
                                                               exception_info = exception_info
                                                               )
                                            )
        result = gemini_flash.invoke(prompt).content
        solutions =  solutions + result.strip()        
            
    # print("---**response**--:")
    # print(f"report_generation:{report_generation}")
    
    return {'solutions': solutions}