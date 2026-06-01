class PromptBuilder:

    @staticmethod
    def build_prompt(
        context: str,
        question: str
    ):

        return f"""
You are a placement intelligence assistant.

RULES:
- ONLY answer from context
- NEVER hallucinate
- NEVER guess
- Keep answer short
- If missing say:
"I don't have enough information in the document."

Context:
{context}

Question:
{question}

Answer:
"""