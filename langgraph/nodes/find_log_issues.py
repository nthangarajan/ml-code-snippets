from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_find_log_issues

def handle_find_log_issues(state):
    print("----------------------------------------")
    print("**find_log_issues** working...")
    log_content = state.get('log_content', '').strip()
    # print("---**input**--:")
    prompt = prompt_find_log_issues.format_map(FormatDict(log_content=log_content)
                                        )
    result = gemini_flash.invoke(prompt).content
    log_issues = result.strip()

    # print("---**response**--:")
    # print(f"log_issues:{log_issues}")

    return {'issues':log_issues}
