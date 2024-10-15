from langchain_groq import ChatGroq

llama3 = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key="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" # Optional if not set as an environment variable
)

gemma = ChatGroq(
    temperature=0,
    model="gemma-7b-it",
    api_key="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" # Optional if not set as an environment variable
)

