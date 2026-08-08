import streamlit as st

from utils.ticket_manager import (
    get_user_tickets,
    get_ticket_details,
    update_ticket,
    cancel_ticket
)


def show():

    st.title("📋 My Tickets")
    st.markdown("---")

    if "selected_ticket" not in st.session_state:
        st.session_state.selected_ticket = None

    if "edit_ticket" not in st.session_state:
        st.session_state.edit_ticket = False

    # ==================================================
    # TICKET DETAILS
    # ==================================================

    if st.session_state.selected_ticket:

        ticket = get_ticket_details(
            st.session_state.selected_ticket
        )

        if ticket is None:

            st.error("Ticket not found.")

            if st.button("⬅ Back"):

                st.session_state.selected_ticket = None
                st.session_state.edit_ticket = False
                st.rerun()

            return

        if st.button("⬅ Back to My Tickets"):

            st.session_state.selected_ticket = None
            st.session_state.edit_ticket = False
            st.rerun()

        st.markdown("---")

        # ===========================================
        # EDIT MODE
        # ===========================================

        if st.session_state.edit_ticket:

            st.subheader("✏ Edit Ticket")

            title = st.text_input(
                "Title",
                value=ticket[2]
            )

            category_list = [
                "Hardware",
                "Software",
                "Network",
                "Cloud",
                "Account",
                "Other"
            ]

            priority_list = [
                "Low",
                "Medium",
                "High",
                "Critical"
            ]

            category = st.selectbox(
                "Category",
                category_list,
                index=category_list.index(ticket[3])
            )

            priority = st.selectbox(
                "Priority",
                priority_list,
                index=priority_list.index(ticket[4])
            )

            description = st.text_area(
                "Description",
                value=ticket[5],
                height=180
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("💾 Save Changes"):

                    update_ticket(
                        ticket[0],
                        title,
                        category,
                        priority,
                        description
                    )

                    st.session_state.edit_ticket = False

                    st.success("Ticket Updated Successfully")

                    st.rerun()

            with col2:

                if st.button("Cancel Editing"):

                    st.session_state.edit_ticket = False

                    st.rerun()

            return

        # ===========================================
        # VIEW MODE
        # ===========================================

        st.subheader(f"🎫 {ticket[0]}")

        st.write(f"**Created By:** {ticket[1]}")
        st.write(f"**Title:** {ticket[2]}")
        st.write(f"**Category:** {ticket[3]}")
        st.write(f"**Priority:** {ticket[4]}")

        st.write("**Description:**")
        st.info(ticket[5])

        st.write(f"**Status:** {ticket[6]}")
        st.write(f"**Created At:** {ticket[7]}")

        if ticket[6] == "Open":

            col1, col2 = st.columns(2)

            with col1:

                if st.button("✏ Edit Ticket"):

                    st.session_state.edit_ticket = True
                    st.rerun()

            with col2:

                if st.button("❌ Cancel Ticket"):

                    cancel_ticket(ticket[0])

                    st.session_state.selected_ticket = None
                    st.session_state.edit_ticket = False

                    st.success("Ticket Cancelled Successfully")

                    st.rerun()

        return

    # ==================================================
    # MY TICKETS
    # ==================================================

    tickets = get_user_tickets(
        st.session_state.username
    )

    if len(tickets) == 0:

        st.info("You have not created any tickets.")

        return

    for ticket in tickets:

        st.subheader(f"🎫 {ticket[0]}")

        st.write(f"**Title:** {ticket[1]}")
        st.write(f"**Category:** {ticket[2]}")
        st.write(f"**Status:** {ticket[4]}")

        if st.button(
            "View Details",
            key=ticket[0]
        ):

            st.session_state.selected_ticket = ticket[0]
            st.rerun()

        st.markdown("---")