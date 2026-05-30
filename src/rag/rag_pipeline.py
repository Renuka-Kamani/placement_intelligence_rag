from src.vectordb.chroma_manager import (
    ChromaManager
)

from src.retrieval.retriever_service import (
    Retriever
)

from src.llm.ollama_client import (
    OllamaClient
)


class RAGPipeline:

    @staticmethod
    def build():

        # Create or load vector DB
        db = (
            ChromaManager()
            .create_or_load_db()
        )

        # Create retriever
        retriever = (
            Retriever.get(
                db
            )
        )

        # Load local LLM
        llm = (
            OllamaClient.load()
        )

        return (
            retriever,
            llm
        )