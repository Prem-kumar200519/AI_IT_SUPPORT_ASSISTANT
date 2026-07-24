import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()


def load_database():
    """
    Load the Chroma Vector Database.
    """

    ollama_host = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url=ollama_host
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db
    return db