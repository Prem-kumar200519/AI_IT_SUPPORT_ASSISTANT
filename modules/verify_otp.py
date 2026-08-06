import sqlite3
import streamlit as st

from utils.otp_manager import verify_otp

DATABASE = "database/users.db"


def show():

    st.title("📧 Email Verification")

    st.write("A 6-digit OTP has been sent to your email.")

    otp = st.text_input("Enter OTP")

    if st.button("✅ Verify OTP"):

        if verify_otp(otp):

            user = st.session_state.register_user

            connection = sqlite3.connect(DATABASE)

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO users(
                    full_name,
                    email,
                    username,
                    password,
                    role,
                    status
                )

                VALUES(?,?,?,?,?,?)
                """,
                (
                    user["full_name"],
                    user["email"],
                    user["username"],
                    user["password"],
                    "Employee",
                    "Active"
                )
            )

            connection.commit()
            connection.close()

            # Clear temporary registration data
            del st.session_state.register_user
            del st.session_state.generated_otp

            st.success("✅ Registration Successful!")

            st.info("Please login using your Username and Password.")

            # Go back to Login Page
            st.session_state.page = "login"

            st.rerun()

        else:

            st.error("❌ Invalid OTP")