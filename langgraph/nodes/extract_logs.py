import log_manager

def handle_extract_logs(state):
    print("----------------------------------------")
    print("**extract_logs** working...")
    custom_job_id_list = state.get('custom_job_id_list')
    custom_job_id_index = state.get('custom_job_id_index')
    job_id = custom_job_id_list[custom_job_id_index]     
    log_content = log_manager.get_logs_for_customjob(job_id = job_id)
    print(log_content)
    if log_content == 'Log does not exist':
        log_exist = False
    else:
        log_exist = True
    # print("---**input**--:")
    print(f"job_id:{job_id}")
    
    custom_job_id_index =  custom_job_id_index + 1 
    
    return {'log_content' : log_content,
            'log_exist' : True,
            'custom_job_id_index' : custom_job_id_index}