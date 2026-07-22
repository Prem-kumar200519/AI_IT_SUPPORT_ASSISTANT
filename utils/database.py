from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def load_database():
    """
    Load the Chroma vector database.
    """

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db