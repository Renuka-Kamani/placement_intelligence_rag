from src.rag.rag_pipeline import (
    RAGPipeline
)

from src.llm.prompt_builder import (
    PromptBuilder
)


class ChatService:

    @staticmethod
    def ask_question(
        question
    ):

        retriever, llm = (
            RAGPipeline.build()
        )

        docs = retriever.invoke(
            question
        )

        context = "\n\n".join(
            [
                doc.page_content[:400]
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