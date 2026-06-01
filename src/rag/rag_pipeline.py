from src.vectordb.chroma_manager import (
    ChromaManager
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
            db.as_retriever(
                search_kwargs={
                    "k": 5
                }
            )
        )

        llm = (
            OllamaClient
            .load()
        )

        return (
            retriever,
            llm
        )