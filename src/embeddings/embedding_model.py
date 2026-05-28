from langchain_ollama import (
    OllamaEmbeddings
)

from config import (
    EMBED_MODEL
)


class EmbeddingModel:

    @staticmethod
    def load():

        return OllamaEmbeddings(
            model=EMBED_MODEL
        )