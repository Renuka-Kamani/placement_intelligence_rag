class PromptBuilder:

    @staticmethod
    def build_prompt(
        context,
        question
    ):

        return f"""
You are a strict extraction system.

RULES:
- ONLY answer from context
- NEVER explain
- NEVER guess
- Return exact values
- Keep answer under one sentence
- If missing:
"I don't have enough information in the document."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""