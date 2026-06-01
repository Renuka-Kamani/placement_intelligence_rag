
from langchain_ollama import (
    ChatOllama
)

from src.config.settings import (
    settings
)

from src.core.logger import (
    logger
)

from src.exceptions.custom_exceptions import (
    OllamaConnectionError
)


class OllamaClient:

    @staticmethod
    def load():

        try:

            logger.info(
                "Loading Ollama "
                "model"
            )

            return ChatOllama(
                model=settings
                .OLLAMA_MODEL
            )

        except Exception as e:

            logger.error(
                str(e)
            )

            raise (
                OllamaConnectionError(
                    "Ollama model "
                    "not available."
                )
            )

