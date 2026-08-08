import streamlit as st
from utils.ticket_manager import create_ticket


def show():

    st.title("🎫 Create New Ticket")
    st.markdown("---")

    with st.form("create_ticket_form", clear_on_submit=True):

        title = st.text_input("Ticket Title")

        category = st.selectbox(
            "Category",
            [
                "Hardware",
                "Software",
                "Network",
                "Cloud",
                "Account",
                "Other"
            ]
        )

        priority = st.selectbox(
            "Priority",
            [
                "Low",
                "Medium",
                "High",
                "Critical"
            ]
        )

        description = st.text_area(
            "Describe your issue",
            height=180
        )

        submitted = st.form_submit_button(
            "📨 Submit Ticket",
            use_container_width=True
        )

    # Runs ONLY when Submit is clicked
    if submitted:

        if title.strip() == "" or description.strip() == "":

            st.error("Please fill all required fields.")

        else:

            ticket_id = create_ticket(
                username=st.session_state.username,
                title=title,
                category=category,
                priority=priority,
                description=description
            )

            st.success("✅ Ticket Created Successfully!")
            st.info(f"Your Ticket ID is: {ticket_id}")

