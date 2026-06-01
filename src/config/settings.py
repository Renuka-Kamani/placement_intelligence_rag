
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(
    BaseSettings
):

    OLLAMA_MODEL: str
    EMBEDDING_MODEL: str

    PDF_PATH: str
    CHROMA_PATH: str

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    LOG_LEVEL: str = "INFO"

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore"
        )
    )
settings = Settings()

