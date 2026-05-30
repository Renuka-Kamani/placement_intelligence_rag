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

        # ------------------
        # Compare package
        # ------------------

        if (
            "compare" in q
            and "package" in q
        ):

            found = []

            for company in companies:

                if (
                    company.lower()
                    in q
                ):

                    row = (
                        df[
                            df[
                                "Company"
                            ]
                            == company
                        ]
                    )

                    package = (
                        row[
                            "Package"
                        ]
                        .values[0]
                    )

                    found.append(
                        f"{company}: "
                        f"{package} LPA"
                    )

            if found:

                return {

                    "answer":
                    ", ".join(found),

                    "context":
                    "Knowledge Base"
                }

        # ------------------
        # Compare eligibility + package
        # ------------------

        if (
            "compare" in q
            and "eligibility" in q
        ):

            found = []

            for company in companies:

                if (
                    company.lower()
                    in q
                ):

                    row = (
                        df[
                            df[
                                "Company"
                            ]
                            == company
                        ]
                    )

                    cgpa = (
                        row[
                            "CGPA"
                        ]
                        .values[0]
                    )

                    package = (
                        row[
                            "Package"
                        ]
                        .values[0]
                    )

                    found.append(

                        f"{company}: "
                        f"CGPA {cgpa}, "
                        f"Package "
                        f"{package} LPA"

                    )

            if found:

                return {

                    "answer":
                    " | ".join(found),

                    "context":
                    "Knowledge Base"
                }

        # ------------------
        # Highest package
        # ------------------

        if (
            "highest package"
            in q
            or
            "offers highest package"
            in q
        ):

            highest = (
                df.sort_values(
                    "Package",
                    ascending=False
                )
                .iloc[0]
            )

            return {

                "answer":
                f"{highest['Company']} "
                f"offers the highest "
                f"package at "
                f"{highest['Package']} "
                f"LPA.",

                "context":
                "Knowledge Base"
            }

        # ------------------
        # Lowest package
        # ------------------

        if (
            "lowest package"
            in q
        ):

            lowest = (
                df.sort_values(
                    "Package"
                )
                .iloc[0]
            )

            return {

                "answer":
                f"{lowest['Company']} "
                f"offers the lowest "
                f"package at "
                f"{lowest['Package']} "
                f"LPA.",

                "context":
                "Knowledge Base"
            }

        # ------------------
        # Python highest package
        # ------------------

        if (
            "python"
            in q
            and
            "highest package"
            in q
        ):

            filtered = (
                df[
                    df[
                        "Focus"
                    ]
                    == "Python"
                ]
            )

            highest = (
                filtered
                .sort_values(
                    "Package",
                    ascending=False
                )
                .iloc[0]
            )

            return {

                "answer":
                f"{highest['Company']} "
                f"offers the highest "
                f"package among "
                f"Python-focused "
                f"companies at "
                f"{highest['Package']} "
                f"LPA.",

                "context":
                "Knowledge Base"
            }

        # ------------------
        # High package + low CGPA
        # ------------------

        if (
            "high package" in q
            and
            "low cgpa" in q
        ):

            filtered = (
                df[
                    (
                        df["Package"]
                        > 20
                    )
                    &
                    (
                        df["CGPA"]
                        < 7
                    )
                ]
            )

            if len(filtered) > 0:

                company_names = (
                    ", ".join(
                        filtered[
                            "Company"
                        ]
                        .tolist()
                    )
                )

                return {

                    "answer":
                    f"{company_names} "
                    f"have high packages "
                    f"with low CGPA "
                    f"requirements.",

                    "context":
                    "Knowledge Base"
                }

        # ------------------
        # Direct company lookup
        # ------------------

        for company in companies:

            if (
                company.lower()
                in q
            ):

                row = (
                    df[
                        df[
                            "Company"
                        ]
                        == company
                    ]
                )

                # Package
                if (
                    "package"
                    in q
                ):

                    package = (
                        row[
                            "Package"
                        ]
                        .values[0]
                    )

                    return {

                        "answer":
                        f"{company} "
                        f"offers "
                        f"{package} "
                        f"LPA.",

                        "context":
                        "Knowledge Base"
                    }

                # CGPA
                if (
                    "cgpa"
                    in q
                ):

                    cgpa = (
                        row[
                            "CGPA"
                        ]
                        .values[0]
                    )

                    return {

                        "answer":
                        f"{company} "
                        f"requires "
                        f"{cgpa} CGPA.",

                        "context":
                        "Knowledge Base"
                    }

                # Backlogs
                if (
                    "backlog"
                    in q
                ):

                    backlogs = (
                        row[
                            "Backlogs"
                        ]
                        .values[0]
                    )

                    if (
                        backlogs > 0
                    ):

                        return {

                            "answer":
                            f"Yes, "
                            f"{company} "
                            f"allows "
                            f"{backlogs} "
                            f"backlog(s).",

                            "context":
                            "Knowledge Base"
                        }

                    return {

                        "answer":
                        f"No, "
                        f"{company} "
                        f"does not allow "
                        f"backlogs.",

                        "context":
                        "Knowledge Base"
                    }

                # Technology focus
                if (
                    "technology"
                    in q
                    or
                    "focus"
                    in q
                ):

                    focus = (
                        row[
                            "Focus"
                        ]
                        .values[0]
                    )

                    return {

                        "answer":
                        f"{company} "
                        f"focuses on "
                        f"{focus}.",

                        "context":
                        "Knowledge Base"
                    }

        # ------------------
        # Fallback RAG
        # ------------------

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