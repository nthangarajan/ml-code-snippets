from typing import Union, List

class FormatDict(dict):
    def __missing__(self, key):
        return '{' + str(key) + '}'
    
import inspect

def get_source_code(function_name):
    # Get the source code of the function
    return inspect.getsource(function_name)

def get_source_code_from_file(file_name):
    with open(file_name) as f:
        contents = f.read()
        return contents

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