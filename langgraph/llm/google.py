from langchain_google_vertexai import ChatVertexAI

gemini_flash = ChatVertexAI(
    model= "gemini-1.5-flash-001",
    temperature=1,
    max_tokens=8192,
    max_retries=6,
    stop=None,
    # other params...
)


gemini_pro = ChatVertexAI(
    model= "gemini-1.5-pro-001",
    temperature=1,
    max_tokens=8192,
    max_retries=6,
    stop=None,
    # other params...
)

from vertexai.generative_models import GenerationConfig

gemini_flash_json = ChatVertexAI(
    model="gemini-pro",
    response_mime_type="application/json",
    temperature=1,
    max_tokens=8192,
    max_retries=6,
    stop=None,
    # other params...
    )   
