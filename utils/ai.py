import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def load_llm():

    ollama_host = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
        base_url=ollama_host
    )

    return llm