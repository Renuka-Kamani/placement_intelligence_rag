from src.vectordb.chroma_manager import (
    ChromaManager
)

from src.retrieval.retriever import (
    Retriever
)

from src.llm.ollama_client import (
    OllamaClient
)


class RAGPipeline:

    @staticmethod
    def build():

        db = (
            ChromaManager()
            .create_or_load_db()
        )

        retriever = (
            Retriever.get(db)
        )

        llm = (
            OllamaClient.load()
        )

        return retriever, llm