from src.rag.rag_pipeline import (
    RAGPipeline
)

from src.llm.prompt_builder import (
    PromptBuilder
)


class RAGTool:

    def run(
        self,
        question: str
    ):

        retriever, llm = (
            RAGPipeline
            .build()
        )

        docs = (
            retriever.invoke(
                question
            )
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

        answer = (

            response.content

            if hasattr(
                response,
                "content"
            )

            else str(
                response
            )
        )

        return {

            "answer":
            answer,

            "context":
            context
        }