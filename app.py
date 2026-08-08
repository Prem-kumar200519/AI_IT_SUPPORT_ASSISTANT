import streamlit as st

# ----------------------------
# Import Pages
# ----------------------------

from modules import dashboard
from modules import ai_chat
from modules import create_ticket
from modules import log_analyzer
from modules import knowledge_base
from modules import system_monitor
from modules import about
from modules import my_tickets
from utils.auth_database import initialize_database
from utils.ticket_database import initialize_ticket_database
from modules import login
from modules import register
from modules import verify_otp
from modules import ticket_details
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
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
# ----------------------------
# Load AI & Database
# ----------------------------

initialize_database()
initialize_ticket_database()

llm = load_llm()
db = load_database()

# ==========================================
# Sidebar
# ==========================================


if not st.session_state.logged_in:

    if st.session_state.page == "login":
        login.show()

    elif st.session_state.page == "register":
        register.show()

    elif st.session_state.page == "verify_otp":
        verify_otp.show()

else:

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

            "🎫 Create Ticket",

            "📋 My Tickets",

            "ℹ️ About",

        ]

    )

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

    elif page == "🎫 Create Ticket":
        create_ticket.show()

    elif page == "📋 My Tickets":
        my_tickets.show()

    elif st.session_state.page == "ticket_details":
        ticket_details.show()

    elif page == "ℹ️ About":
        about.show()