"""
Author: tnagarethina@micron.com
Summary: This library provides the functions to:
1. get_project_id()
2. get_ml_default_bucket_name()
3. get_service_account()
and False if it is stopped or failed.
"""

import http.client as httplib

def get_project_number():
    """
    Summary:
        get project_id from google cloud platform
    Returns:
        _type_: _description_
    """    
    project_id_uri = '/computeMetadata/v1/project/numeric-project-id'
    
    conn = httplib.HTTPConnection('metadata.google.internal')
    conn.request('GET', project_id_uri, None, {'Metadata-Flavor': 'Google'})
    response = conn.getresponse()
    metadata_request = response.read()
    project_number = metadata_request.decode('cp437')
    conn.close()
    return project_number

def get_project_id():
    """
    Summary:
        get project_id from google cloud platform
    Returns:
        _type_: _description_
    """    
    project_id_uri = '/computeMetadata/v1/project/project-id'
    
    conn = httplib.HTTPConnection('metadata.google.internal')
    conn.request('GET', project_id_uri, None, {'Metadata-Flavor': 'Google'})
    response = conn.getresponse()
    metadata_request = response.read()    
    project_id = metadata_request.decode('cp437')
    conn.close()
    
    return project_id

def get_ml_default_bucket_name():
    """
    Summary:
        get default ml bucket name from google cloud storage
        Exxample: gdw-dev-fdis-ml-default
    Returns:
        string : default ml bucket name from google cloud storage
    """
    project_id = get_project_id()
    return f"{project_id}-ml-default"

def get_service_account():
    """
    Summary:
        get service account of google cloud platform
    Returns:
        string: service account
    """
    project_id = get_project_id()
    return f"shared-service-account@{project_id}.iam.gserviceaccount.com"

def get_env_from_project_id(project_id: str = '',
                            default_env: str ='dev')->str:
    if len(project_id) > 0:
        split_list = project_id.split('-')
        if (len(split_list) >= 2):
            return split_list[1] if (len(split_list[1]) > 0) else default_env
        else:
            return default_env
    else:
        default_env