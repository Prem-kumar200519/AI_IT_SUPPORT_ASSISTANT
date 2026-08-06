import random
import streamlit as st


def generate_otp():
    """
    Generate a random 6-digit OTP.
    """

    otp = str(random.randint(100000, 999999))

    st.session_state.generated_otp = otp

    return otp


def verify_otp(user_otp):
    """
    Verify the entered OTP.
    """

    return (
        user_otp ==
        st.session_state.get("generated_otp")
    )