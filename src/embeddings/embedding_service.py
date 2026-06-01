
from langchain_ollama import (
    OllamaEmbeddings
)

from src.config.settings import (
    settings
)

from src.core.logger import (
    logger
)

from src.exceptions.custom_exceptions import (
    EmbeddingError
)


class EmbeddingService:

    @staticmethod
    def load():

        try:

            logger.info(
                "Loading embedding "
                "model"
            )

            return (
                OllamaEmbeddings(
                    model=settings
                    .EMBEDDING_MODEL
                )
            )

        except Exception as e:

            logger.error(
                str(e)
            )

            raise EmbeddingError(
                "Failed to load "
                "embedding model"
            )

