from utils.format_dict import FormatDict
from llm.google import gemini_flash

from state.log_analyser_state import LogAnalyserState

def handle_verify_kba(state:LogAnalyserState):
    print("----------------------------------------")
    print("**verify_kba** working...")
    # print("---**input**--:")
    # print("---**response**--:")
    return {'kba_suggestion' : 'working'}    