import streamlit as st

from utils.login_manager import login_user


def show():

    st.title("💻 AI IT Support Assistant")
    st.subheader("Enterprise AI Helpdesk")

    st.markdown("---")

    st.success(
        "Welcome to AI IT Support Assistant v1.2"
    )

    st.write("Please login to continue.")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:

        login = st.button(
            "🔑 Login",
            use_container_width=True
        )

    with col2:

        register = st.button(
            "🆕 Register",
            use_container_width=True
        )

    # -------------------------
    # LOGIN
    # -------------------------

    if login:

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.username = user[0]

            st.session_state.role = user[1]

            st.session_state.full_name = user[2]

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Username or Password")

    # -------------------------
    # REGISTER
    # -------------------------

    if register:

        st.session_state.page = "register"

        st.rerun()