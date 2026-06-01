import streamlit as st

from src.services.chat_service import (
    ChatService
)

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Placement Intelligence Assistant",
    page_icon="🎓",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

.user-box {
    background: #1f2937;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.bot-box {
    background: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 4px solid #00ADB5;
}

.big-title {
    font-size: 38px;
    font-weight: bold;
    color: white;
}

.subtitle {
    color: #9CA3AF;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.subheader("Supported Features")

    st.markdown("""
    ✅ Package Queries  
    ✅ Eligibility Queries  
    ✅ Company Comparison  
    ✅ Multi-hop Reasoning  
    ✅ Ranking Queries  
    ✅ Document Retrieval  
    """)

    st.markdown("---")

    st.subheader("Quick Questions")

    sample_questions = [

        "What is package offered by Google?",

        "Compare Google and Microsoft package",

        "Which company offers highest package?",

        "Which company using Python offers highest package?",

        "Eligibility criteria for Amazon"

    ]

# -------------------------
# Header
# -------------------------

st.markdown(
    '<div class="big-title">'
    '🎓 Placement Intelligence Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Hybrid RAG + Knowledge Base Placement Assistant'
    '</div>',
    unsafe_allow_html=True
)

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# -------------------------
# Display Chat
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# -------------------------
# Input
# -------------------------

prompt = st.chat_input(
    "Ask placement-related questions..."
)

# -------------------------
# Process Query
# -------------------------

if prompt:

    st.session_state.messages.append({

        "role": "user",

        "content": prompt
    })

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            response = (
                ChatService
                .ask_question(prompt)
            )

            answer = (
                response[
                    "answer"
                ]
            )

            context = (
                response[
                    "context"
                ]
            )

            st.markdown(answer)

            with st.expander(
                "Retrieved Context"
            ):

                st.write(
                    context
                )

    st.session_state.messages.append({

        "role": "assistant",

        "content": answer
    })