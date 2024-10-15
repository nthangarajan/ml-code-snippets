from typing import Annotated,Sequence,Literal

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langchain_core.tools import tool

from tavily import TavilyClient

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool


@tool
def wikipedia_tool(input: Annotated[str,"The query which is passed to search in wikipedia"],):
    """Use this tool when the user need a short description about any topic.
    """
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
    wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki_tool.run(input)+ "\n\nIf you have completed all tasks, respond with FINAL ANSWER."

@tool
def Tavily_tool(input: Annotated[str,"The query which is passed to search in internet using tavil tool"],):
    """use this tool only when the user tells to search from internet or from websites.
    """
    tavily = TavilyClient(api_key="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")
    query = input
    response = tavily.search(query)
    if response["results"][0]:
        result=response["results"][0]
        return(result.get("content"))+ "\n\nIf you have completed all tasks, respond with FINAL ANSWER."
    
@tool
def python_repl(
    code: Annotated[str, "The python code to execute to generate your output."],):
    """Use this to execute python code. If you want to see the output,
    you should print it out with `print(...)` or you could also use pandas,matplotib,numpy. This is visible to the user.
    """
    try:
        repl = PythonREPLTool()
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Successfully executed:\n```python\n{code}\n```\nStdout: {result}"
    return (
        result_str+ "\n\nIf you have completed all tasks, respond with FINAL ANSWER."
    )    