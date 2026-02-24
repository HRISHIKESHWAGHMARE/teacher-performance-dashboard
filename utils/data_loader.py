import pandas as pd

@staticmethod
def load_teachers(path = "data/teachers.csv"):
    df = pd.read_csv(path)
    df["teacher_id"] = df["teacher_id"].astype(str)
    return df

@staticmethod
def load_scores(path = "data/scores.csv"):
    df = pd.read_csv(path, parse_dates=["evaluation_date"])
    df["teacher_id"] = df["teacher_id"].astype(str)
    return df

@staticmethod
def load_attendance(path = "data/attendance.csv"):
    df = pd.read_csv(path)
    df["teacher_id"] = df["teacher_id"].astype(str)
    return df 

@staticmethod
def load_attrition(path = "data/attrition.csv"):
    df = pd.read_csv(path)
    df["teacher_id"] = df["teacher_id"].astype(str)
    return df

def get_master_dataset():
    # Creates a clean, joined dataset for analysis
    teachers = load_teachers()
    scores = load_scores()
    attendance = load_attendance()
    attrition = load_attrition()


    # Merge Teachers + scores 
    df = scores.merge(teachers, on="teacher_id", how="left")

    # Handle missing joins safely 
    df["section"] = df["section"].fillna("unknown")
    return df


def get_teacher_kevel_data():
    # Aggregated metrics per teacher

    df = get_master_dataset()

    agg_df = (df.groupby(["teacher_id", "teacher_name", "section"]).agg(
        avg_score = ("overall_score", "mean"),
        evaluations = ("overall_score", "count")
    ).reset_index()
    )
    return agg_df
    














