import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from utils.gemini_ai import GeminiLLM

load_dotenv()


def load_llm():

    provider = os.getenv("AI_PROVIDER", "ollama").lower()

    if provider == "ollama":

        print("✅ Using Ollama")

        return ChatOllama(
            model="llama3.2",
            temperature=0
        )

    elif provider == "gemini":

        print("✅ Using Gemini")

        return GeminiLLM()

    else:

        raise ValueError(
            "AI_PROVIDER must be either 'ollama' or 'gemini'"
        )