from langchain_ollama import (
    OllamaEmbeddings
)


class EmbeddingModel:

    @staticmethod
    def load():

        return OllamaEmbeddings(
            model="nomic-embed-text"
        )