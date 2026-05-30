class ChunkingService:

    @staticmethod
    def split_text(text):

        chunks = []

        lines = (
            text.split("\n")
        )

        bad_keywords = [

            "Easy Direct table lookup",
            "Hard Conflict",
            "Hop Type",
            "RAG Challenge",
            "Judges will use",
            "Question Difficulty",
            "Full synthesis",
            "Expert"

        ]

        for line in lines:

            line = line.strip()

            if len(line) < 30:
                continue

            skip = False

            for keyword in (
                bad_keywords
            ):

                if keyword in line:

                    skip = True
                    break

            if skip:
                continue

            chunks.append(
                line
            )

        return chunks