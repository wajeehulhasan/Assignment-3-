import numpy as np
import pandas as pd

def load():
    df = pd.read_csv("students_messy.csv")
    return df

def clean():
    df = load()
    # print(df.shape)
    print(df.info())
    print(df.describe())
    print(df.isna().sum())
    print(df[df.duplicated(keep=False)].sort_values("student_id"))
    print(df["gender"].value_counts())
    print(df["city"].value_counts())
    df["city"] = df["city"].str.strip().str.title() # # city: remove extra spaces
    print(df["city"].value_counts())
    g = df["gender"].str.strip().str.lower()
    print("g value is",g)
    df["gender"] = g.map({"m":"Male", "male":"Male", "f":"Female", "female":"Female"})
    print(df["gender"].value_counts())
    print(df["gender"].value_counts(dropna=False))
    print(df["city"].value_counts(dropna=False))
    df = df.dropna(subset = ["gender", "city"])
    print(df["gender"].value_counts(dropna=False))
    print(df["city"].value_counts(dropna=False))
    df["score"] = df["score"].str.replace("%", "")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    df["attendance"] = df["attendance"].str.replace("%", "")
    df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")
    print(df.info())

    df = df[(df["age"] >= 10) & (df["age"] <= 30)]
    df = df[(df["score"] >= 0) & (df["score"] <= 100)]
    df["attendance"] = df["attendance"].fillna(df["attendance"].median())
    print(df["attendance"].isna().sum())

    print(df.duplicated().sum())
    df = df.drop_duplicates()
    print(df.shape)
    
    df["student_name"] = df["student_name"].str.strip().str.title()
    df = df.sort_values("student_id").reset_index(drop=True)
    print(df)
    df = add_feature(df)
    print(df)
    df.to_csv("students_clean.csv", index=False)
    return df
def add_feature(df):
    df["result"] = np.where(df["score"] >= 50, "Pass", "Fail")
    df["grade"] = pd.cut(df["score"],
                         bins=[0, 49, 59, 69, 79, 100],
                         labels=["F", "D", "C", "B", "A"])
    return df
    

clean()



