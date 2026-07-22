import streamlit as st

# ----------------------------
# Import Pages
# ----------------------------

from modules import dashboard
from modules import ai_chat
from modules import log_analyzer
from modules import knowledge_base
from modules import system_monitor
from modules import about
from modules import view_tickets
# ----------------------------
# Import Utilities
# ----------------------------

from utils.ai import load_llm
from utils.database import load_database

# ----------------------------
# Load CSS
# ----------------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI IT Support Assistant",
    page_icon="💻",
    layout="wide"
)

load_css()

# ----------------------------
# Session State
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Load AI & Database
# ----------------------------

llm = load_llm()
db = load_database()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.markdown("# 💻 AI IT Support Assistant")
st.sidebar.markdown("---")
st.sidebar.subheader("🟢 System Status")
st.sidebar.success("Running")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "⚙️ Modules",
    [
        "🏠 Home",
        "🤖 AI Chat",
        "📄 Log Analyzer",
        "📚 Knowledge Base",
        "🖥️ System Monitor",
        "📋 View Tickets",
        "ℹ️ About",
    ]
)

# ----------------------------
# Route Pages
# ----------------------------

if page == "🏠 Home":
    dashboard.show()

elif page == "🤖 AI Chat":
    ai_chat.show(db, llm)

elif page == "📄 Log Analyzer":
    log_analyzer.show(llm)

elif page == "📚 Knowledge Base":
    knowledge_base.show()

elif page == "🖥️ System Monitor":
    system_monitor.show()

elif page == "📋 View Tickets":
    view_tickets.show()

elif page == "ℹ️ About":
    about.show()