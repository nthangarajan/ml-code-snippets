from langchain_google_vertexai import ChatVertexAI

gemini_flash = ChatVertexAI(
    model= "gemini-1.5-flash-001",
    temperature=0,
    max_tokens=None,
    max_retries=6,
    stop=None,
    # other params...
)


gemini_pro = ChatVertexAI(
    model= "gemini-1.5-pro-001",
    temperature=0,
    max_tokens=None,
    max_retries=6,
    stop=None,
    # other params...
)
