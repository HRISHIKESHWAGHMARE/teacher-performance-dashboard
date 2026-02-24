import pandas as pd
import streamlit as st

def teacher_tab():
    st.title("Teacher Performance")

    teachers = pd.read_csv("data/teachers.csv")
    scores = pd.read_csv("data/scores.csv")

    teacher = st.selectbox("Select Teacher", teachers["teacher_name"])

    teacher_id = teachers.loc[teachers["teacher_name"] == teacher,
                              "teacher_id"].values[0]
    
    t_score = scores[scores["teacher_id"] == teacher_id]

    st.subheader("Overall Score")
    st.progress(int(t_score["overall_score"].iloc[0])/ 100)

    st.subheader("Score Breakdown")
    st.dataframe(t_score)