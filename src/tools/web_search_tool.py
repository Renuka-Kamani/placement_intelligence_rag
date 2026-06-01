from ddgs import DDGS


class WebSearchTool:

    def search(
        self,
        question: str
    ) -> str:

        try:

            with DDGS() as ddgs:

                results = list(

                    ddgs.text(
                        question,
                        max_results=5
                    )

                )

            if not results:

                return (
                    "No relevant web "
                    "results found."
                )

            top_result = (
                results[0]
            )

            title = (
                top_result.get(
                    "title",
                    ""
                )
            )

            body = (
                top_result.get(
                    "body",
                    ""
                )
            )

            href = (
                top_result.get(
                    "href",
                    ""
                )
            )

            return (
                f"**{title}**\n\n"
                f"{body}\n\n"
                f"Source: {href}"
            )

        except Exception as e:

            return (
                f"Web search failed: "
                f"{str(e)}"
            )