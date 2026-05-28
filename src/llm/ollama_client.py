from langchain_ollama import (
    ChatOllama
)

from config import (
    LLM_MODEL
)


class OllamaClient:

    @staticmethod
    def load():

        return ChatOllama(
            model=LLM_MODEL,
            temperature=0
        )