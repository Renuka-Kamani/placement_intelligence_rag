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

from src.ingestion.chunking_service import (
    ChunkingService
)

from src.preprocessing.deduplicator import (
    Deduplicator
)

from src.embeddings.embedding_service import (
    EmbeddingModel
)


class ChromaManager:

    def __init__(self):

        self.embeddings = (
            EmbeddingModel.load()
        )

    def create_or_load_db(self):

        # Load existing database
        if os.path.exists(
            CHROMA_PATH
        ):

            print(
                "Loading existing ChromaDB..."
            )

            return Chroma(
                persist_directory=CHROMA_PATH,
                embedding_function=self.embeddings
            )

        print(
            "Extracting PDF..."
        )

        # Extract text
        text = (
            PDFLoader.extract_text(
                PDF_PATH
            )
        )

        print(
            "Chunking document..."
        )

        # Split into chunks
        chunks = (
            ChunkingService
            .split_text(text)
        )

        print(
            "Removing duplicate chunks..."
        )

        # Remove duplicates
        unique_chunks = (
            Deduplicator
            .remove_duplicates(
                chunks
            )
        )

        print(
            "Creating Vector Database..."
        )

        # Create vector database
        db = Chroma.from_texts(
            texts=unique_chunks,
            embedding=self.embeddings,
            persist_directory=CHROMA_PATH
        )

        print(
            "Vector DB Created Successfully"
        )

        return db