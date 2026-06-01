class Deduplicator:

    @staticmethod
    def remove_duplicates(
        chunks: list[str]
    ) -> list[str]:

        unique_chunks = (
            list(
                dict.fromkeys(
                    chunks
                )
            )
        )

        return unique_chunks