from typing import Dict, List, TypedDict, Optional

from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
from langgraph.constants import Send

from nodes.collect_custom_jobs import handle_collect_custom_jobs
from nodes.verify_kba import handle_verify_kba
from nodes.find_solution import handle_find_solution
from nodes.report_generator import handle_report_generator


from typing import List, Dict, TypedDict, Optional, Annotated,Sequence
import operator

from graph.failure_analysis import failure_analysis_workflow
import log_manager

from state.log_analyser_state import LogAnalyserState


def invoke_failure_analysis(state):
    print("**invoke_failure_analysis**...")
    custom_job_id_list = state.get('custom_job_id_list',[])
    custom_job_id_index = state.get('custom_job_id_list')
    if custom_job_id_index < len(custom_job_id_list):
        return "failure_analysis"
    else:
        return "report_generator"
    
log_analyser_workflow = StateGraph(LogAnalyserState)

def test1(state):
    pass

log_analyser_workflow.add_node("collect_custom_jobs", handle_collect_custom_jobs)
log_analyser_workflow.add_node("failure_analysis",failure_analysis_workflow.compile())
# log_analyser_workflow.add_node("failure_analysis",test1)
log_analyser_workflow.add_node("verify_KBA",handle_verify_kba) 
log_analyser_workflow.add_node("report_generator",handle_report_generator)

# log_analyser_workflow.add_edge("collect_custom_jobs", "failure_analysis")
log_analyser_workflow.add_edge("failure_analysis", "verify_KBA")
log_analyser_workflow.add_edge("verify_KBA", "report_generator")

log_analyser_workflow.add_conditional_edges("collect_custom_jobs",invoke_failure_analysis,{"failure_analysis":"failure_analysis",
                                                                                          "report_generator":"report_generator"})

log_analyser_workflow.set_entry_point("collect_custom_jobs")
log_analyser_workflow.set_finish_point("report_generator")

log_analyser_app = log_analyser_workflow.compile()
