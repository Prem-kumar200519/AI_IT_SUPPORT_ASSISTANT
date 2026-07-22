import streamlit as st
import json
import os
from datetime import datetime

TICKET_FILE = "tickets.json"


def load_tickets():

    if not os.path.exists(TICKET_FILE):
        return []

    with open(TICKET_FILE, "r") as f:
        return json.load(f)


def save_tickets(tickets):

    try:

        with open(TICKET_FILE, "w", encoding="utf-8") as f:

            json.dump(
                tickets,
                f,
                indent=4
            )

        return True

    except Exception as e:

        st.error(f"Error Saving Ticket: {e}")

        return False


def generate_ticket_number(tickets):

    if len(tickets) == 0:
        return "INC-1001"

    last = tickets[-1]["ticket_id"]

    number = int(last.split("-")[1])

    return f"INC-{number+1}"


def show():

    st.title("🎫 Create Support Ticket")

    st.caption(
        "Create an IT incident ticket."
    )

    tickets = load_tickets()

    issue = st.text_input(
        "Issue",
        value=st.session_state.get(
            "last_issue",
            ""
        )
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

    department = st.selectbox(
        "Department",
        [
            "IT Support",
            "Network",
            "Cloud",
            "Security",
            "System Administration"
        ]
    )

    description = st.text_area(
        "Additional Description"
    )

    if st.button(
        "🎫 Create Ticket",
        use_container_width=True
    ):

        ticket = {

            "ticket_id":
                generate_ticket_number(
                    tickets
                ),

            "issue":
                issue,

            "description":
                description,

            "priority":
                priority,

            "department":
                department,

            "status":
                "Open",

            "created_date":
                datetime.now().strftime("%d-%b-%Y"),

            "created_time":
                datetime.now().strftime("%I:%M %p")
        }
        
        tickets.append(ticket)

        if save_tickets(tickets):
            st.success(
        f"✅ Ticket {ticket['ticket_id']} created successfully!"
        )

        st.json(ticket)