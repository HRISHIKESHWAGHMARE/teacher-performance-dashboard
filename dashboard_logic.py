import pandas as pd
import plotly.express as px

from utils.data_loader import get_master_dataset
from utils.metrics import (
    total_teachers,
    total_evaluation,
    average_score,
    performance_percentage
)


def load_dashboard_data():
    """
    Loads and prepares data required for dashboard
    """
    df = get_master_dataset()
    return df


def calculate_kpis(df):
    """
    Returns all KPI values as a dictionary
    """
    return {
        "total_teachers": total_teachers(df),
        "total_evaluations": total_evaluation(df),
        "average_score": average_score(df),
        "performance_pct": performance_percentage(df)
    }


def performance_trend_chart(df):
    """
    Returns Plotly figure for performance trend
    """
    trend_df = (
        df.groupby("evaluation_date")
        .agg(avg_score=("overall_score", "mean"))
        .reset_index()
    )

    fig = px.line(
        trend_df,
        x="evaluation_date",
        y="avg_score",
        title="Average Performance Trend"
    )

    return fig


def section_wise_performance(df):
    """
    Returns section-wise average performance chart
    """
    section_df = (
        df.groupby("section")
        .agg(avg_score=("overall_score", "mean"))
        .reset_index()
    )

    fig = px.bar(
        section_df,
        x="section",
        y="avg_score",
        title="Section-wise Performance"
    )

    return fig

if __name__ == "__main__":
    df = load_dashboard_data
    print(calculate_kpis(df))