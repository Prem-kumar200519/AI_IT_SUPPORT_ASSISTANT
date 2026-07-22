from langchain_ollama import ChatOllama


def load_llm():
    """
    Load the Ollama language model.
    """

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    return llm