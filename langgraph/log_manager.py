import pandas as pd
from datetime import datetime, timedelta
from datetime import date 
from pytz import timezone

from google.cloud.logging import DESCENDING,ASCENDING, Client

from utils import gcp_utils

def get_job_ids_from_log_entries(log_query:str):
    project_id = gcp_utils.get_project_id()

    client = Client(project = project_id)
    job_id_list = []
    for entry in client.list_entries(filter_=log_query,
                                        order_by=DESCENDING, 
                                        page_size=1000):
        job_id = entry.resource.labels['job_id']
        job_id_list.append(job_id)

    return job_id_list

def get_df_logging_entries(log_query:str):
    project_id = gcp_utils.get_project_id()
    
    client = Client(project = project_id)
    df_log = pd.DataFrame()
    # for entry in client.list_entries(filter_=log_query,order_by=DESCENDING, page_size=1000):
    for entry in client.list_entries(filter_=log_query,order_by=ASCENDING, page_size=1000):        
        payload = entry.payload
        if type(payload) == dict:
            timestamp = entry.timestamp.isoformat()
            resource = entry.resource.labels
            severity= entry.severity
            job_id = entry.resource.labels['job_id']
            new_row = pd.DataFrame({
                'job_id' : job_id,
                # 'timestamp': timestamp,
                'severity': severity,
                'payload': payload['message']
             }, index=[0])
            df_log = pd.concat([df_log,new_row]).reset_index(drop=True)
    return df_log

def get_current_time():
    # tz = timezone('Asia/Singapore')
    # current_time = datetime.now(tz)
    current_time = datetime.now()    
    return current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

def get_back_time(back_hours:int = 0,
                  back_days:int = 0
                  ):
    current_time = datetime.now()
    back_time = (current_time - timedelta(hours=back_hours,days = back_days))
    return back_time.strftime("%Y-%m-%dT%H:%M:%SZ")

def get_log_query_from_resouce_type(resource_type:str,
                                    jsonPayload_message:str,
                                    start_datetime:datetime,
                                    end_datetime:datetime):
                                           
    log_query =f"""resource.type="{resource_type}"
    jsonPayload.message=~"{jsonPayload_message}"
    timestamp>="{start_datetime}" AND timestamp <= "{end_datetime}"
    """
    return log_query

def get_log_query_for_customjob(job_id:str):
    back_days = 30
    start_datetime = get_back_time(back_days = back_days)
    end_datetime = get_current_time()                                           
    log_query = f"""
    resource.type= "ml_job"
    resource.labels.job_id={job_id}
    timestamp>="{start_datetime}" AND timestamp <= "{end_datetime}"
    severity>=DEFAULT
    """
    return log_query


def get_logs_for_customjob(job_id:str):
    log_query = get_log_query_for_customjob(job_id = job_id)

    df_log_entries = get_df_logging_entries(log_query = log_query)
    if df_log_entries.empty:
        return 'Log does not exist'
    log_list = df_log_entries['payload'].tolist()
    filter_log_list  = []
    [filter_log_list.append(x) for x in log_list if x not in filter_log_list]
    log_content =  "\n".join(filter_log_list)
    return log_content


