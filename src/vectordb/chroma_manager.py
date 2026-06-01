
import os

from langchain_community.vectorstores import (
    Chroma
)

from src.config.settings import (
    settings
)

from src.core.logger import (
    logger
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
    EmbeddingService
)

from src.exceptions.custom_exceptions import (
    ChromaDBError
)


class ChromaManager:

    def __init__(self):

        self.embeddings = (
            EmbeddingService
            .load()
        )

    def create_or_load_db(self):

        try:

            if os.path.exists(
                settings
                .CHROMA_PATH
            ):

                logger.info(
                    "Loading "
                    "existing "
                    "ChromaDB"
                )

                return Chroma(

                    persist_directory=
                    settings
                    .CHROMA_PATH,

                    embedding_function=
                    self.embeddings
                )

            logger.info(
                "Creating "
                "new ChromaDB"
            )

            text = (
                PDFLoader
                .extract_text(
                    settings
                    .PDF_PATH
                )
            )

            chunks = (
                ChunkingService
                .split_text(
                    text
                )
            )

            chunks = (
                Deduplicator
                .remove_duplicates(
                    chunks
                )
            )

            db = (
                Chroma
                .from_texts(

                    texts=chunks,

                    embedding=
                    self.embeddings,

                    persist_directory=
                    settings
                    .CHROMA_PATH
                )
            )

            logger.info(
                "ChromaDB "
                "created"
            )

            return db

        except Exception as e:

            logger.error(
                str(e)
            )

            raise (
                ChromaDBError(
                    "Failed to "
                    "create/load "
                    "ChromaDB"
                )
            )

