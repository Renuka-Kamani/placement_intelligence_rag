import streamlit as st

from src.rag.pipeline import (
    RAGPipeline
)


st.set_page_config(
    page_title="Placement Intelligence Assistant",
    layout="wide"
)

st.title(
    "Placement Intelligence Assistant"
)


# Store chat history
if "messages" not in st.session_state:

    st.session_state.messages = []


# Show previous chats
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# User input
question = st.chat_input(
    "Ask a placement-related question"
)


if question:

    # Show user message
    with st.chat_message(
        "user"
    ):

        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner(
        "Thinking..."
    ):

        try:

            retriever, llm = (
                RAGPipeline.build()
            )

            # Retrieve relevant docs
            docs = retriever.invoke(
                question
            )

            # Limit context size
            context = "\n\n".join(
                [
                    doc.page_content[:400]
                    for doc in docs
                ]
            )

            # Small prompt for low RAM laptop
            prompt = f"""
You are a Placement Intelligence Assistant.

Rules:
1. Answer ONLY from context.
2. Give exact values if present.
3. If rounds exist, list them clearly.
4. If answer is not found say:
"I don't have enough information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

            response = llm.invoke(
                prompt
            )

            answer = (
                response.content
            )

        except Exception as e:

            answer = (
                f"Error: {str(e)}"
            )

    # Show assistant response
    with st.chat_message(
        "assistant"
    ):

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Debug section
    with st.expander(
        "Retrieved Context"
    ):

        st.write(context)