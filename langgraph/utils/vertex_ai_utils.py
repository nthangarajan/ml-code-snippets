from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta
from typing import Union, List

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic import JobState

from utils import gcp_utils

def dict_to_labels_filter(labels: dict) -> Union[str, None]:
    """
    Convert dict labels to a specific format e.g. "{k1}={v1} AND {k2}={v2} AND {k3}={v3}"
    This format is supported by Vertex AI PipelineJob, Vertex AI CustomJob for now
    If there are multiple labels, they are chained together with a space, 
    e.g. "{k1}={v1} AND {k2}={v2}" and so on..

    Args:
        labels (`dict`): Labels to be converted to GCP format
    """
    if not labels:
        return None
    label_filter = [f"labels.{k}={labels[k]}" for k in labels]
    return " AND ".join(label_filter)

def list_to_state_filter(job_states:List[str]) -> Union[str, None]:
    if not job_states:
        return None
    state_filter = [f'state="{job_state}"' for job_state in job_states]
    return "(" + " OR ".join(state_filter) + ")"

def get_pipeline_job(pipeline_run_name:str,
                     location = 'us-west1'):
    project_number = gcp_utils.get_project_number()
    project_id = gcp_utils.get_project_id()
    
    aiplatform.init(project=project_id, location= location)

    resource_name = f'projects/{project_number}/locations/{location}/pipelineJobs/{pipeline_run_name}'
    try:
        pipeline_job = aiplatform.PipelineJob.get(resource_name)
        return pipeline_job
    except Exception as error:
        raise ValueError("Invalid pipeline_run_name")

def get_custom_job_id_list(pipeline_run_name:str,
                          back_days : int = 60,
                          job_states:List[str] = [],
                          location = 'us-west1'):
    
    pipeline_job = get_pipeline_job (pipeline_run_name = pipeline_run_name)
    vertex_ai_pipelines_run_billing_id = pipeline_job.labels['vertex-ai-pipelines-run-billing-id']
    
    project_id = gcp_utils.get_project_id()
    aiplatform.init(project=project_id, location= location)
    # back_datetime= datetime.datetime.now() - relativedelta(minutes=max_threshold_minutues)
    back_datetime= datetime.datetime.now() - relativedelta(days=back_days)
    
    create_time_filter = f'createTime>="{back_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")}"' 
    update_time_filter = f'updateTime>"{back_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")}"' 
    end_time_filter = f'endTime>"{back_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")}"'
    if len(job_states) == 0:
        state_filter = None
    else:
        state_filter = list_to_state_filter(job_states)
    order_by_condition = 'create_time desc'
    
    dict_labels = {'vertex-ai-pipelines-run-billing-id' : vertex_ai_pipelines_run_billing_id}
    labels_filter = dict_to_labels_filter(dict_labels)
    
    if state_filter is None:    
        filter_condition=f"({create_time_filter} AND {labels_filter})"
    else:
        filter_condition=f"({create_time_filter} AND {labels_filter} AND {state_filter})"
        
    # print(filter_condition)
    custom_jobs = aiplatform.CustomJob.list(filter=filter_condition,
                                               order_by=order_by_condition)
    custom_job_id_list = []
    for custom_job in custom_jobs:
        custom_job_id_list.append(custom_job.name)
    return custom_job_id_list    