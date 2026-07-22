import streamlit as st
import time
import json
import streamlit.components.v1 as components


def show(db, llm):

    st.title("🤖 AI IT Support Chat")

    st.caption(
        "Ask questions related to Windows, Linux, Networking, Cloud, and Company Knowledge."
    )

    # ==========================================
    # Session State
    # ==========================================

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "last_response" not in st.session_state:
        st.session_state.last_response = ""

    if "last_issue" not in st.session_state:
        st.session_state.last_issue = ""

    if "response_time" not in st.session_state:
        st.session_state.response_time = 0

    # ==========================================
    # Top Controls
    # ==========================================

    col1, col2, col3 = st.columns([1,1,2])

    with col1:

        if st.button(
            "🗑️ Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []
            st.session_state.last_response = ""
            st.session_state.last_issue = ""

            st.rerun()

    with col2:

        chat_history = ""

        for msg in st.session_state.messages:

            chat_history += (
                f"{msg['role'].upper()}:\n"
            )

            chat_history += (
                msg["content"] + "\n\n"
            )

        st.download_button(

            "📄 Export Chat",

            data=chat_history,

            file_name="chat_history.txt",

            mime="text/plain",

            use_container_width=True

        )

    with col3:

        total_questions = len(

            [
                m
                for m in st.session_state.messages
                if m["role"] == "user"
            ]

        )

        st.info(
            f"💬 Total Questions : {total_questions}"
        )

    st.divider()

    # ==========================================
    # Chat History
    # ==========================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(
                message["content"]
            )

    # ==========================================
    # User Input
    # ==========================================

    question = st.chat_input(
        "Ask your IT support question..."
    )

    if question:

        st.session_state.last_issue = question

        st.session_state.messages.append(
            {
                "role":"user",
                "content":question
            }
        )

        with st.chat_message("user"):

            st.write(question)

        results = db.similarity_search(
            question,
            k=2
        )

        context = ""

        for doc in results:

            context += (
                doc.page_content + "\n"
            )

        prompt = f"""
You are an Enterprise AI IT Support Assistant.

Rules:

- Use company knowledge whenever available.
- Otherwise answer using IT Support knowledge.
- Keep answers professional.
- Give step-by-step troubleshooting.

Knowledge:

{context}

Question:

{question}
"""

        start = time.time()

        with st.spinner(
            "🤖 AI is analyzing..."
        ):

            response = llm.invoke(prompt)

        end = time.time()

        st.session_state.response_time = (
            end-start
        )

        st.session_state.last_response = (
            response.content
        )

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":response.content
            }
        )

        st.rerun()

# ==========================================
# Latest AI Response
# ==========================================

    if st.session_state.last_response != "":
        
        st.divider()

        st.subheader("🤖 Latest AI Response")

        st.write(
        st.session_state.last_response
    )

        st.caption(
        f"⏱️ Response Time : {st.session_state.response_time:.2f} seconds"
    )

    # ==========================================
    # Action Buttons
    # ==========================================

    col1, col2 = st.columns(2)

    # ---------------- Copy Response ----------------

    with col1:

        safe_text = (
            st.session_state.last_response
            .replace("\\", "\\\\")
            .replace("`", "\\`")
            .replace("${", "\\${")
        )

        components.html(
            f"""
            <button
                onclick="navigator.clipboard.writeText(`{safe_text}`);this.innerHTML='✅ Copied!';setTimeout(()=>this.innerHTML='📋 Copy Response',1500);"
                style="
                    width:100%;
                    background:#0E7490;
                    color:white;
                    border:none;
                    padding:10px;
                    border-radius:8px;
                    font-size:15px;
                    font-weight:bold;
                    cursor:pointer;
                ">
                📋 Copy Response
            </button>
            """,
            height=55,
        )

    # ---------------- Create Ticket ----------------

    with col2:

        if st.button(
            "🎫 Create Support Ticket",
            use_container_width=True
        ):

            st.session_state["ticket_issue"] = (
                st.session_state.last_issue
            )

            st.success("✅ Issue sent to Ticket System.")

            st.info("📋 Open 'View Tickets' from the sidebar to view or manage your ticket.")