from src.router.intent_router import (
    IntentRouter
)

from src.tools.rag_tool import (
    RAGTool
)

from src.tools.web_search_tool import (
    WebSearchTool
)


class ChatService:

    def __init__(

        self,

        knowledge_service,

        rag_tool

    ):

        self.knowledge = (
            knowledge_service
        )

        self.rag_tool = (
            rag_tool
        )

        self.web_tool = (
            WebSearchTool()
        )

    def ask_question(
        self,
        question: str
    ):

        intent = (
            IntentRouter
            .detect_intent(
                question
            )
        )

        if intent == (
            "mysql"
        ):

            result = (
                self
                .handle_sql_query(
                    question
                )
            )

            if (
                "don't have"
                not in
                result[
                    "answer"
                ].lower()
            ):

                return result

        elif intent == (
            "web"
        ):

            answer = (
                self.web_tool
                .search(
                    question
                )
            )

            return {

                "answer":
                answer,

                "context":
                "Web Search"
            }

        result = (
            self.rag_tool
            .run(
                question
            )
        )

        if (

            "don't have enough"
            in result[
                "answer"
            ].lower()

        ):

            answer = (
                self.web_tool
                .search(
                    question
                )
            )

            return {

                "answer":
                answer,

                "context":
                "Web Fallback"
            }

        return result

    def handle_sql_query(
        self,
        question
    ):

        q = (
            question
            .lower()
        )

        df = (
            self
            .knowledge
            .get_dataframe()
        )

        # highest package

        if (
            "highest package"
            in q
        ):

            row = (
                df
                .sort_values(
                    "package_lpa",
                    ascending=False
                )
                .iloc[0]
            )

            return {

                "answer":
                f"{row['company_name']} "
                f"offers the "
                f"highest package "
                f"at "
                f"{row['package_lpa']} "
                f"LPA.",

                "context":
                "MySQL"
            }

        # company lookup

        for company in (
            df[
                "company_name"
            ]
        ):

            if (
                company.lower()
                in q
            ):

                row = (
                    df[
                        df[
                            "company_name"
                        ]
                        ==
                        company
                    ]
                    .iloc[0]
                )

                if (
                    "package"
                    in q
                ):

                    return {

                        "answer":
                        f"{company} "
                        f"offers "
                        f"{row['package_lpa']} "
                        f"LPA.",

                        "context":
                        "MySQL"
                    }

                if (

                    "eligibility"
                    in q

                    or

                    "cgpa"
                    in q

                ):

                    return {

                        "answer":
                        f"{company} "
                        f"requires "
                        f"{row['cgpa']} "
                        f"CGPA and "
                        f"allows "
                        f"{row['backlogs']} "
                        f"backlogs.",

                        "context":
                        "MySQL"
                    }

        return {

            "answer":
            "I don't have "
            "enough information.",

            "context":
            "MySQL"
        }