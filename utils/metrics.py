import pandas as pd

def total_teachers(df):
    return df["teacher_id"].nunique()

def total_evaluation(df):
    return len(df)

def average_score(df):
    return round(df["overall_score"].mean(),2)

def performance_percentage(df, benchmark = 75):
    # % of evaluations meeting benchmark score

    return round((df["overall_score"] >= benchmark).mean()*100, 2)

def teacher_rankings(df):
    # Rank teachers by average score

    rankings = (df.groupby(["teacher_id", "teacher_name"])
                .agg(avg_score = ("overall_score", "mean"))
                .reset_index()
                .sort_values("avg_score", ascending = False))
    
    rankings['rank'] = range(1, len(rankings) + 1)
    return rankings

def attrition_risk_flag(attrition_df):
    # Flag high attrition risk teachers

    attrition_df["risk_level"] = attrition_df["attrition_score"].apply(
        lambda x: "High" if x >= 3.5 else "Medium" if x >= 2 else "Low"
    )
    return attrition_df