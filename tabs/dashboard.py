import streamlit as st

from dashboard_logic import (
    load_dashboard_data,
    calculate_kpis,
    performance_trend_chart,
    section_wise_performance
)


def dashboard_tab():
    st.title("Overall Performance Dashboard")

    # Load data
    df = load_dashboard_data()

    # KPIs
    kpis = calculate_kpis(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Teachers", kpis["total_teachers"])
    col2.metric("Evaluations", kpis["total_evaluations"])
    col3.metric("Avg Score", kpis["average_score"])
    col4.metric("Performance %", f'{kpis["performance_pct"]}%')

    st.divider()

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            performance_trend_chart(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            section_wise_performance(df),
            use_container_width=True
        )