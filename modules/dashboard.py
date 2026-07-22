import streamlit as st


def show():

    # ==========================================
    # Header
    # ==========================================

    st.title("💻 AI IT Support Assistant")
    st.caption("Enterprise AI Helpdesk Portal")

    st.markdown("---")

    # ==========================================
    # Welcome
    # ==========================================

    st.success("""
Welcome to the **AI IT Support Assistant**.

This platform provides AI-powered IT support, company knowledge search,
log file analysis, and live system monitoring from one place.
""")

    # ==========================================
    # Dashboard Statistics
    # ==========================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🤖 AI Status", "Online")

    with col2:
        st.metric("📚 Knowledge Files", "6")

    with col3:
        st.metric("🧠 AI Model", "Llama 3.2")

    with col4:
        st.metric("💾 Database", "Connected")

    st.markdown("---")

    # ==========================================
    # AI Assistant Status
    # ==========================================

    st.subheader("📡 AI Assistant Status")

    left, right = st.columns(2)

    with left:
        st.success("🟢 AI Model Loaded")
        st.success("🟢 Knowledge Base Connected")
        st.success("🟢 Vector Database Ready")

    with right:
        st.success("🟢 Log Analyzer Active")
        st.success("🟢 System Monitor Active")
        st.success("🟢 Ready to Assist")

    st.markdown("---")

    # ==========================================
    # Key Features
    # ==========================================

    st.subheader("🚀 Key Features")

    c1, c2 = st.columns(2)

    with c1:
        st.info("🤖 AI-powered IT Support Chat")
        st.info("📚 Company Knowledge Base Search")
        st.info("📄 AI Log File Analysis")

    with c2:
        st.info("🖥️ Live System Monitoring")
        st.info("🌐 Windows & Linux Troubleshooting")
        st.info("⚡ Fast AI Responses")

    st.markdown("---")

    # ==========================================
    # Quick Start
    # ==========================================

    st.subheader("🚀 Quick Start")

    st.info("""
**1️⃣ AI Chat**  
Ask technical questions related to Windows, Linux, networking, cloud, and IT support.

**2️⃣ Log Analyzer**  
Upload log files and receive AI-powered troubleshooting.

**3️⃣ Knowledge Base**  
Browse company documents and support manuals.

**4️⃣ System Monitor**  
Monitor CPU, RAM, Disk usage, and operating system information.
""")

    st.markdown("---")

    # ==========================================
    # Enterprise Notice
    # ==========================================

    st.subheader("📢 Enterprise Notice")

    st.warning("""
This application simulates an enterprise AI Helpdesk environment.

Responses are generated using both the company knowledge base
and an AI language model to provide accurate troubleshooting guidance.
""")

    st.markdown("---")

    # ==========================================
    # System Health
    # ==========================================

    st.subheader("📈 System Health")

    st.progress(100)

    st.success("✅ All core services are running successfully.")

    st.markdown("---")

    # ==========================================
    # Footer
    # ==========================================

    st.caption("© 2026 AI IT Support Assistant version 1.1 | Developed by Prem Kumar S")