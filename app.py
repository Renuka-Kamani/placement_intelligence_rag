import streamlit as st

from src.services.chat_service import (
    ChatService
)


st.set_page_config(
    page_title="Placement Intelligence Assistant",
    layout="wide"
)

st.title(
    "Placement Intelligence Assistant"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in (
    st.session_state.messages
):

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


question = st.chat_input(
    "Ask a placement-related question"
)


if question:

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

        result = (
            ChatService
            .ask_question(
                question
            )
        )

        answer = (
            result["answer"]
        )

        context = (
            result["context"]
        )

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

    with st.expander(
        "Retrieved Context"
    ):

        st.write(context)