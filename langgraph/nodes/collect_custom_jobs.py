import log_manager
from utils import vertex_ai_utils

def handle_collect_custom_jobs(state):
    print("----------------------------------------")
    print("**collect_custom_jobs** working...")
    pipeline_run_name = state.get('pipeline_run_name', '').strip()
    job_states = state.get('job_states', '')
    # print("---**input**--:")
    # print(f"pipeline_run_name:{pipeline_run_name}")
    # print(f"job_states:{job_states}")
    custom_job_id_list = vertex_ai_utils.get_custom_job_id_list(pipeline_run_name = pipeline_run_name,
                                                                job_states = job_states)
    # print("---**response**--:")
    print(f"pipeline_run_name:{pipeline_run_name}")
    print(f"custom_job_id_list:{custom_job_id_list}")
    print(f"custom_job_id_index:{0}")

    return {'pipeline_run_name':pipeline_run_name, 
            'custom_job_id_list':custom_job_id_list,
            'custom_job_id_index' : 0,
            }