import streamlit as st


def show():

    st.title("ℹ️ About AI IT Support Assistant")
    st.caption("Enterprise AI Helpdesk Platform")

    st.markdown("---")

    # ==========================================
    # Project Overview
    # ==========================================

    st.header("📖 Project Overview")

    st.write("""
AI IT Support Assistant is an enterprise-inspired application designed to
help IT support teams troubleshoot technical issues using Artificial Intelligence.

The application combines Retrieval-Augmented Generation (RAG) with
Large Language Models (LLMs) to provide accurate and company-specific
IT support solutions.
""")

    st.markdown("---")

    # ==========================================
    # Core Features
    # ==========================================

    st.header("🚀 Core Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("🤖 AI IT Support Chat")

        st.success("📚 Company Knowledge Base")

        st.success("📄 AI Log Analyzer")

    with col2:

        st.success("🖥️ System Monitor")

        st.success("🔍 Company Knowledge Search")

        st.success("📥 Report Download")

    st.markdown("---")

    # ==========================================
    # Architecture
    # ==========================================

    st.header("🏗️ System Architecture")

    st.code("""
User
   │
   ▼
Streamlit Interface
   │
   ▼
AI Chat Module
   │
   ▼
Chroma Vector Database
   │
   ▼
Ollama (Llama 3.2)
   │
   ▼
AI Response
""")

    st.markdown("---")

    # ==========================================
    # Folder Structure
    # ==========================================

    st.header("📂 Project Structure")

    st.code("""
AI_IT_SUPPORT_ASSISTANT/

│── app.py
│── data/
│── modules/
│── utils/
│── assets/
│── chroma_db/
│── requirements.txt
│── README.md
""")

    st.markdown("---")

    # ==========================================
    # Version
    # ==========================================

    st.header("📌 Application Information")

    st.info("""
Version : 1.0

Status : Development Completed

Platform : Streamlit

AI Model : Llama 3.2

Database : ChromaDB

Knowledge Search : RAG

Deployment : Local
""")

    st.markdown("---")

    # ==========================================
    # Future Enhancements
    # ==========================================

    st.header("🚀 Future Enhancements")

    st.write("""
• Multi-user authentication

• Ticket management

• Email notifications

• Cloud deployment (AWS)

• Docker containerization

• REST API integration

• Role-based access control
""")

    st.markdown("---")

    st.success("Developed by Prem")