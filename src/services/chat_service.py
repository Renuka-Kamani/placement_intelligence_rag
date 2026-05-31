
from src.services.knowledge_service import (
    KnowledgeService
)

from src.rag.rag_pipeline import (
    RAGPipeline
)

from src.llm.prompt_builder import (
    PromptBuilder
)


class ChatService:

    @staticmethod
    def ask_question(question):

        q = question.lower()

        df = (
            KnowledgeService
            .load_company_data()
        )

        companies = list(
            df["Company"]
        )

        mentioned = []

        for company in companies:

            if (
                company.lower()
                in q
            ):

                mentioned.append(
                    company
                )

        # -------------------
        # Top / highest
        # -------------------

        if (
            "highest package"
            in q
            or
            "top company"
            in q
        ):

            top = (
                df.sort_values(
                    "Package",
                    ascending=False
                )
                .iloc[0]
            )

            return {

                "answer":
                f"{top['Company']} "
                f"offers the highest "
                f"package at "
                f"{top['Package']} LPA.",

                "context":
                "Knowledge Base"
            }

        # -------------------
        # Top 3
        # -------------------

        if (
            "top 3"
            in q
            and
            "package"
            in q
        ):

            top3 = (
                df.sort_values(
                    "Package",
                    ascending=False
                )
                .head(3)
            )

            result = []

            for _, row in (
                top3.iterrows()
            ):

                result.append(

                    f"{row['Company']} "
                    f"({row['Package']} LPA)"

                )

            return {

                "answer":
                ", ".join(
                    result
                ),

                "context":
                "Knowledge Base"
            }

        # -------------------
        # Company-specific
        # -------------------

        if len(mentioned):

            responses = []

            for company in mentioned:

                row = (
                    df[
                        df[
                            "Company"
                        ]
                        == company
                    ]
                    .iloc[0]
                )

                if (
                    "package"
                    in q
                ):

                    responses.append(
                        f"{company}: "
                        f"{row['Package']} LPA"
                    )

                elif (
                    "cgpa"
                    in q
                ):

                    responses.append(
                        f"{company}: "
                        f"{row['CGPA']} CGPA"
                    )

                elif (
                    "backlog"
                    in q
                ):

                    responses.append(
                        f"{company}: "
                        f"{row['Backlogs']} backlog(s)"
                    )

                elif (
                    "focus"
                    in q
                    or
                    "technology"
                    in q
                ):

                    responses.append(
                        f"{company}: "
                        f"{row['Focus']}"
                    )

                elif (
                    "eligibility"
                    in q
                    or
                    "criteria"
                    in q
                ):

                    responses.append(

                        f"{company}: "
                        f"CGPA "
                        f"{row['CGPA']}, "
                        f"Backlogs "
                        f"{row['Backlogs']}"

                    )

            if responses:

                return {

                    "answer":
                    " | ".join(
                        responses
                    ),

                    "context":
                    "Knowledge Base"
                }

        # -------------------
        # fallback rag
        # -------------------

        retriever, llm = (
            RAGPipeline.build()
        )

        docs = retriever.invoke(
            question
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = (
            PromptBuilder
            .build_prompt(
                context,
                question
            )
        )

        response = (
            llm.invoke(
                prompt
            )
        )

        return {

            "answer":
            response,

            "context":
            context
        }

