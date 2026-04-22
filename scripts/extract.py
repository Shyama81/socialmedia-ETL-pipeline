import pandas as pd
import numpy as np

def extract():
 df = pd.read_csv("data/raw.csv")

 print("missing value",df.isnull().sum())
 print("shape",df.shape)
 
 return df

