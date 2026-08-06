import streamlit as st
import sqlite3
from utils.otp_manager import generate_otp
from utils.email_service import send_email
DATABASE = "database/users.db"


def show():

    st.title("🆕 Create New Account")

    st.markdown("---")

    full_name = st.text_input("Full Name")

    email = st.text_input("Email")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    st.markdown("")

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        if (
            full_name == ""
            or email == ""
            or username == ""
            or password == ""
        ):

            st.error("Please fill all fields.")
            return

        if password != confirm:

            st.error("Passwords do not match.")
            return

        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        existing = cursor.fetchone()

        if existing:

            st.error("Username already exists.")

            connection.close()

            return

        # Store registration details temporarily

        st.session_state.register_user = {

        "full_name": full_name,

        "email": email,

        "username": username,

        "password": password

}

# Generate OTP

        otp = generate_otp()

# Send Email

        send_email(

        receiver_email=email,

        subject="AI IT Support Assistant - Email Verification",

        body=f"""
        Hello{full_name},

        Your verification code is:

        {otp}

        Do not share this code with anyone.

        AI IT Support Assistant
        """

    )
        connection.close()

        st.success("OTP has been sent to your email.")

        st.session_state.page = "verify_otp"

        st.rerun()

        st.info("Return to Login and sign in.")