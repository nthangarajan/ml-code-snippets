from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from graph.state import GraphState

from nodes.handle_coder import handle_coder
from nodes.handle_reviewer import handle_reviewer
from nodes.handle_result import handle_result


load_dotenv()


from prompts.handle_reviewer import classify_feedback
from llm.google import gemini_flash

def deployment_ready(state):
    deployment_ready = 1 if 'yes' in gemini_flash.invoke(classify_feedback.format(state.get('code'),state.get('feedback'))) else 0
    total_iterations = 1 if state.get('iterations')> 5 else 0
    return "handle_result" if  deployment_ready or total_iterations else "handle_coder" 


workflow = StateGraph(GraphState)
workflow.add_node("handle_reviewer",handle_reviewer)
workflow.add_node("handle_coder",handle_coder)
workflow.add_node("handle_result",handle_result)
workflow.add_conditional_edges(
    "handle_reviewer",
    deployment_ready,
    {
        "handle_result": "handle_result",
        "handle_coder": "handle_coder"
    }
)

workflow.set_entry_point("handle_reviewer")
workflow.add_edge('handle_coder', "handle_reviewer")
workflow.add_edge('handle_result', END)

app = workflow.compile()