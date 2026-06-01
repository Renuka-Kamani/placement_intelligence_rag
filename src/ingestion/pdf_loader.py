
import os
import fitz

from src.core.logger import (
    logger
)

from src.exceptions.custom_exceptions import (
    PDFNotFoundError
)


class PDFLoader:

    @staticmethod
    def extract_text(
        pdf_path: str
    ) -> str:

        try:

            if not os.path.exists(
                pdf_path
            ):

                raise PDFNotFoundError(
                    f"PDF not found: "
                    f"{pdf_path}"
                )

            logger.info(
                f"Loading PDF: "
                f"{pdf_path}"
            )

            doc = fitz.open(
                pdf_path
            )

            text = ""

            for page in doc:

                text += (
                    page.get_text()
                )

            logger.info(
                "PDF extraction "
                "completed"
            )

            return text

        except Exception as e:

            logger.error(
                str(e)
            )

            raise

