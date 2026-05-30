from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


class ChunkingService:

    @staticmethod
    def split_text(text):

        splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=250,
                chunk_overlap=50,
                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " "
                ]
            )
        )

        chunks = (
            splitter.split_text(
                text
            )
        )

        # Remove very large chunks
        filtered_chunks = []

        for chunk in chunks:

            if len(chunk) < 800:

                filtered_chunks.append(
                    chunk
                )

        return filtered_chunks