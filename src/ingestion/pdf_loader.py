import pdfplumber
import pandas as pd


class PDFLoader:

    @staticmethod
    def extract_text(pdf_path):

        text_chunks = []

        with pdfplumber.open(
            pdf_path
        ) as pdf:

            for page in pdf.pages:

                # Extract normal text
                text = (
                    page.extract_text()
                )

                if text:

                    text_chunks.append(
                        text
                    )

                # Extract tables
                tables = (
                    page.extract_tables()
                )

                for table in tables:

                    try:

                        df = pd.DataFrame(
                            table[1:],
                            columns=table[0]
                        )

                        for _, row in (
                            df.iterrows()
                        ):

                            row_text = (
                                " | ".join(
                                    [
                                        f"{col}: {row[col]}"
                                        for col in df.columns
                                    ]
                                )
                            )

                            text_chunks.append(
                                row_text
                            )

                    except:

                        continue

        return "\n".join(
            text_chunks
        )