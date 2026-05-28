import os

from langchain_community.vectorstores import (
    Chroma
)

from config import (
    PDF_PATH,
    CHROMA_PATH
)

from src.ingestion.pdf_loader import (
    PDFLoader
)

from src.ingestion.chunking import (
    ChunkingService
)

from src.preprocessing.deduplicator import (
    Deduplicator
)

from src.embeddings.embedding_model import (
    EmbeddingModel
)


class ChromaManager:

    def __init__(self):

        self.embeddings = (
            EmbeddingModel.load()
        )

    def create_or_load_db(self):

        if os.path.exists(
            CHROMA_PATH
        ):

            return Chroma(
                persist_directory=CHROMA_PATH,
                embedding_function=self.embeddings
            )

        print(
            "Extracting PDF..."
        )

        text = (
            PDFLoader.extract_text(
                PDF_PATH
            )
        )

        print(
            text[:2000]
        )

        chunks = (
            ChunkingService
            .split_text(text)
        )

        unique_chunks = (
            Deduplicator
            .remove_duplicates(
                chunks
            )
        )

        documents = []

        for chunk in unique_chunks:

            documents.append(
                chunk
            )

        db = Chroma.from_texts(
            texts=documents,
            embedding=self.embeddings,
            persist_directory=CHROMA_PATH
        )

        print(
            "Vector DB Created"
        )

        return db