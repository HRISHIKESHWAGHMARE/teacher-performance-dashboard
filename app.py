import streamlit as st
from auth.login import login
from tabs.dashboard import dashboard_tab
from tabs.teacher import teacher_tab
from tabs.late_attrition import late_attrition_tab

# Page Config
st.set_page_config(page_title="Teacher Performance Dashboard", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to",
            ["Dashboard", "Teacher", "Late Count & Attrition", "Logout"])
    
    if page == "Dashboard":
        dashboard_tab()
    elif page == "Teacher":
        teacher_tab()
    else:
        late_attrition_tab()

        
    # elif page == "Late Count & Attrition":
    #     late_attrition_tab()
    # else:
    #     st.session_state.logged_in = False
    #     st.rerun()