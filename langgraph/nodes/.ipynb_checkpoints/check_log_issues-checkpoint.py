from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_check_logs_issues
import log_manager

def handle_check_log_issues(state):
    print("----------------------------------------")
    print("**check_log_issues** working...")
    custom_job_id_list = state.get('custom_job_id_list')
    custom_job_id_index = state.get('custom_job_id_index')
    job_id = custom_job_id_list[custom_job_id_index]     
    log_content = log_manager.get_logs_for_customjob(job_id = job_id)
    # print("---**input**--:")
    print(f"job_id:{job_id}")

    prompt = prompt_check_logs_issues.format_map(FormatDict(log_content=log_content)
                                        )
    # print(prompt)
    result = gemini_flash.invoke(prompt).content
    result = result.upper().strip()
    if result == 'YES':
        issues_exist = True
    elif result == 'NO':
        issues_exist = False
    else:
        issues_exist = False
        
    print("---**response**--:")
    print(f"issues_exist:{issues_exist}")
    
    custom_job_id_index =  custom_job_id_index + 1 
    
    return {'job_id': job_id, 
            'custom_job_id_index':custom_job_id_index,
            'log_content' : log_content , 
            'issues_exist': issues_exist}
