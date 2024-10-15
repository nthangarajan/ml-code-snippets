from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from graph.state_code_assitant import GraphState

from nodes.handle_coder import handle_coder
from nodes.handle_reviewer import handle_reviewer
from nodes.handle_result import handle_result
from nodes.pair_programmer import pair_programmer
from nodes.handle_exception import handle_exception
from nodes.handle_logger import handle_logger


load_dotenv()


from prompts.handle_reviewer import classify_feedback
from llm.google import gemini_flash

def deployment_ready(state):
    deployment_ready = 1 if 'yes' in gemini_flash.invoke(classify_feedback.format(state.get('code'),state.get('feedback'))) else 0
    total_iterations = 1 if state.get('iterations')> 1 else 0
    return "handle_result" if  deployment_ready or total_iterations else "handle_coder" 

code_writers = ['*Exception Handler Writer*','*Logging Writer*']

conditional_map = {k: k for k in code_writers}
conditional_map["CODE_REVIEWER"] = 'CODE_REVIEWER'
print(conditional_map)

def function_1(state):
    next_step = state['next_implementor'].strip()
    print(next_step)
    return next_step

workflow = StateGraph(GraphState)
workflow.add_node("pair_programmer", pair_programmer)
   
workflow.add_node("*Exception Handler Writer*",handle_exception)
workflow.add_node("*Logging Writer*",handle_logger)

for member in code_writers:
    # We want our workers to ALWAYS "report back" to the supervisor when done
    workflow.add_edge(member, "pair_programmer")

workflow.add_node("CODE_REVIEWER",handle_reviewer)
workflow.add_node("handle_coder",handle_coder)
workflow.add_node("handle_result",handle_result)

workflow.add_edge('handle_coder', "CODE_REVIEWER")

workflow.add_conditional_edges(
    "CODE_REVIEWER",
    deployment_ready,
    {
        "handle_result": "handle_result",
        "handle_coder": "handle_coder"
    }
)

workflow.add_conditional_edges("pair_programmer", function_1, conditional_map)
workflow.set_entry_point("pair_programmer")

workflow.add_edge('handle_result', END)
app = workflow.compile()