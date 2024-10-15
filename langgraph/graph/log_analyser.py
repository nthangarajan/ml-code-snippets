from typing import Dict, List, TypedDict, Optional

from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
from langgraph.constants import Send

from nodes.collect_custom_jobs import handle_collect_custom_jobs
from nodes.verify_kba import handle_verify_kba
from nodes.find_solution import handle_find_solution
from nodes.report_generator import handle_report_generator

from nodes.check_log_issues import handle_check_log_issues
from nodes.find_log_issues import handle_find_log_issues
from nodes.find_log_exception import handle_find_log_exception
from nodes.extract_execution_steps import handle_extract_execution_steps

from typing import List, Dict, TypedDict, Optional, Annotated,Sequence
import operator

from graph.failure_analysis import failure_analysis_workflow
import log_manager

from state.log_analyser_state import LogAnalyserState


def invoke_failure_analysis(state):
    print("**invoke_failure_analysis**...")
    custom_job_id_list = state.get('custom_job_id_list',[])
    custom_job_id_index = state.get('custom_job_id_index')
    if custom_job_id_index < len(custom_job_id_list):
        return "custom-jobs-exist"
    else:
        return "no-custom-jobs"

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
        return "exit-failure-analysis"       
    
log_analyser_workflow = StateGraph(LogAnalyserState)

log_analyser_workflow.add_node("collect_custom_jobs", handle_collect_custom_jobs)

log_analyser_workflow.add_node("check_log_issues",handle_check_log_issues)
log_analyser_workflow.add_node("find_log_issues",handle_find_log_issues) 
log_analyser_workflow.add_node("find_log_exception",handle_find_log_exception) 

log_analyser_workflow.add_node("verify_KBA",handle_verify_kba) 
log_analyser_workflow.add_node("report_generator",handle_report_generator)

log_analyser_workflow.add_edge("find_log_issues", "find_log_exception")
log_analyser_workflow.add_edge("verify_KBA", "report_generator")

log_analyser_workflow.add_conditional_edges("collect_custom_jobs",invoke_failure_analysis,{"custom-jobs-exist":"check_log_issues",
                                                                                          "no-custom-jobs":"report_generator"})

# Condition Edges
log_analyser_workflow.add_conditional_edges(
    "check_log_issues",
    should_continue_find_issues,
    { 
     "issues-exist": "find_log_issues",
     "next-job": "check_log_issues",
     "no-job"  : "report_generator",
     }
)

log_analyser_workflow.add_conditional_edges(
    "find_log_exception",
    should_continue_check_log,
    { 
     "next-job": "check_log_issues",
     "exit-failure-analysis" : "verify_KBA"
     }
)

log_analyser_workflow.set_entry_point("collect_custom_jobs")
log_analyser_workflow.set_finish_point("report_generator")

log_analyser_app = log_analyser_workflow.compile()
