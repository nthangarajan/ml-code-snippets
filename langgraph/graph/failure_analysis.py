from typing import List, Dict, TypedDict, Optional, Annotated,Sequence
import operator


from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph

from nodes.check_log_issues import handle_check_log_issues
from nodes.find_log_issues import handle_find_log_issues
from nodes.find_log_exception import handle_find_log_exception
from nodes.extract_execution_steps import handle_extract_execution_steps

from state.failure_analysis_state import FailureAnalysisState

def should_continue_find_issues(state):
    # print("----------------------------------------")
    # print("**should_continue_issues_finder** condition...")
    issues_exist = state["issues_exist"]
    
    if issues_exist == True:
        return "issues-exist"
    else:
        custom_job_id_list = state.get('custom_job_id_list')
        custom_job_id_index = state.get('custom_job_id_index')
        if custom_job_id_index < len(custom_job_id_list):
            return "next-job"
        else:
            return "no-job"                

def should_continue_check_log(state):
    # print("----------------------------------------")
    # print("**should_continue_check_log** condition...")
    custom_job_id_list = state.get('custom_job_id_list')
    custom_job_id_index = state.get('custom_job_id_index')
    
    if custom_job_id_index < len(custom_job_id_list):
        return "next-job"
    else:
        return "exit"    
    
failure_analysis_workflow = StateGraph(FailureAnalysisState)

failure_analysis_workflow.add_node("check_log_issues",handle_check_log_issues)
failure_analysis_workflow.add_node("find_log_issues",handle_find_log_issues) 
failure_analysis_workflow.add_node("find_log_exception",handle_find_log_exception) 

#Normal Edges
failure_analysis_workflow.set_entry_point("check_log_issues")
failure_analysis_workflow.add_edge("find_log_issues", "find_log_exception")

# Condition Edges
failure_analysis_workflow.add_conditional_edges(
    "check_log_issues",
    should_continue_find_issues,
    { 
     "issues-exist": "find_log_issues",
     "next-job": "check_log_issues",
     "no-job"  : END,
     }
)

failure_analysis_workflow.add_conditional_edges(
    "find_log_exception",
    should_continue_check_log,
    { 
     "next-job": "check_log_issues",
     "exit" : END
     }
)

failure_analysis_graph = failure_analysis_workflow.compile()
