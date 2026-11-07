import pandas as pd
from pipeline import clean


def test_clean():
    clean()
    df = pd.read_csv("students_clean.csv")

    assert len(df) > 0                          # file has data
    assert df.isna().sum().sum() == 0           # no missing values
    assert df.duplicated().sum() == 0           # no duplicates
    assert df["score"].between(0, 100).all()    # score is valid
    assert df["age"].between(10, 30).all()      # age is valid
    assert set(df["gender"]) <= {"Male", "Female"}   # gender is clean