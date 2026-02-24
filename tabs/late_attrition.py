import pandas as pd
import streamlit as st
import plotly.express as px 

def late_attrition_tab():
    st.title("Late Count & Attrition")

    attendance = pd.read_csv("data/attendance.csv")
    attrition = pd.read_csv("data/attrition.csv")

    fig = px.line(attendance, x="month", y = "late_count",
                  color = "teacher_id", title="Late Attendance Trend")
    
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Attrition Details")
    st.dataframe(attrition)