from langchain_ollama import (
    OllamaLLM
)


class OllamaClient:

    @staticmethod
    def load():

        return OllamaLLM(
            model="gemma:2b",
            temperature=0.1,
            num_ctx=2048
        )