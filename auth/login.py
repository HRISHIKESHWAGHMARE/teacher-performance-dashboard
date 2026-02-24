import streamlit as st

USERS = {"admin":{"password":"admin123", "role":"Admin"},
         "teacher":{"password":"teacher123", "role":"Teacher"}}

def login():
    st.title("myNalanda Login")

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        user = USERS.get(username)

        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")