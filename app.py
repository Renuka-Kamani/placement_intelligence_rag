import streamlit as st

from src.services.chat_service import (
    ChatService
)

from src.services.knowledge_service import (
    KnowledgeService
)

from src.tools.rag_tool import (
    RAGTool
)


st.set_page_config(

    page_title=
    "Placement Intelligence",

    page_icon="🎓",

    layout="wide"
)


@st.cache_resource
def get_chat_service():

    return ChatService(

        knowledge_service=
        KnowledgeService(),

        rag_tool=
        RAGTool()
    )


chat_service = (
    get_chat_service()
)


if "messages" not in st.session_state:

    st.session_state.messages = []


st.markdown(

    """
    <h1 style='text-align:center'>
    🎓 Placement Intelligence Assistant
    </h1>
    """,

    unsafe_allow_html=True
)


with st.sidebar:

    st.title(
        "Chat History"
    )

    if st.button(
        "Clear Chat"
    ):

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
    "Ask anything..."
)


if question:

    st.session_state.messages.append(

        {

            "role":
            "user",

            "content":
            question
        }
    )

    with st.chat_message(
        "user"
    ):

        st.markdown(
            question
        )

    with st.spinner(
        "Thinking..."
    ):

        response = (
            chat_service
            .ask_question(
                question
            )
        )

    answer = (
        response[
            "answer"
        ]
    )

    with st.chat_message(
        "assistant"
    ):

        st.markdown(
            answer
        )

        with st.expander(
            "Source"
        ):

            st.write(
                response[
                    "context"
                ]
            )

    st.session_state.messages.append(

        {

            "role":
            "assistant",

            "content":
            answer
        }
    )