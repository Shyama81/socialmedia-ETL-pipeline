import pandas as pd
import numpy as np

def transform(df):
 df = pd.read_csv("data/raw.csv")
 print(df.dtypes)


 df["gender"] = df["gender"].astype("category")
 df["platform_usage"] = df["platform_usage"].astype("category")
 df["social_interaction_level"] = df["social_interaction_level"].astype("category")

 df["screen_to_sleep_ratio"] = df["daily_social_media_hours"]/df["sleep_hours"].replace(0,1)

 df["high_social_media_user"] = df["daily_social_media_hours"]>5

 # Sleep category
 def sleep_category(hours):
    if(hours)<5:
        return "low"
    elif hours <=8:
        return "average"
    else: return "high"

 df["sleep_category"] = df["sleep_hours"].apply(sleep_category)

# mental health risk score
 df["risk_score"] = (
    df["stress_level"]+
    df["anxiety_level"]+
    df["addiction_level"]+
    df["depression_label"]
 )
 # Agregation
 result = df.groupby("gender")["stress_level"].mean()
 print(result)
 results = df.groupby("gender")["daily_social_media_hours"].mean()
 print(results)

 # column re-naming
 df.columns = df.columns.str.lower().str.replace(" ", "_")

 # Encoding categorial data (converting categorical to numeric )
 df = pd.get_dummies(df, columns=["gender","platform_usage","social_interaction_level"])


 # creating analytics ready dataset
 df.to_parquet("data/cleaned_data")

 return df



