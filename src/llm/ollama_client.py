from langchain_ollama import (
    OllamaLLM
)


class OllamaClient:

    @staticmethod
    def load():

        return OllamaLLM(
            model="tinyllama"
        )