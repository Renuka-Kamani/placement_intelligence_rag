
from loguru import logger

from src.config.settings import (
    settings
)


logger.remove()

logger.add(
    "logs/app.log",
    level=settings.LOG_LEVEL,
    rotation="5 MB",
    retention="10 days"
)

