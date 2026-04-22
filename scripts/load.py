from sqlalchemy import create_engine
import pandas as pd
df = pd.read_parquet("data/cleaned_data")
engine = create_engine("postgresql://postgres:shyama123@localhost:5432/postgres")
df.to_sql("teen_health", engine, if_exists= "replace", index= False )
df_check = pd.read_sql("SELECT * FROM teen_health ", engine)
print(df_check)
print(df.shape)
print(df.isnull().sum())
print(df.describe())
