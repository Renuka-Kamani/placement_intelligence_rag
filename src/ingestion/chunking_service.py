from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class ChunkingService:

    @staticmethod
    def split_text(
        text: str
    ) -> list[str]:

        splitter = (
            RecursiveCharacterTextSplitter(

                chunk_size=500,

                chunk_overlap=100
            )
        )

        chunks = (
            splitter
            .split_text(
                text
            )
        )

        return chunks