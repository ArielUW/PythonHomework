"""Create a Kaggle (https://www.kaggle.com) account and download test.csv 
from the https://www.kaggle.com/competitions/titanic dataset (1p):
Upload the dataset to colab and load it into a variable (1p). Then:
display the first 5 rows (1p)
display the last 20 rows (1p)
display basic information about this dataset (1p)"""
import numpy as np
import pandas as pd
import matplotlib as plt
import os
cwd = os.getcwd()
print(cwd)
df = pd.read_csv("./11-21-Pandas/test.csv")

print(df[:5])
print(df[-20:])
print(df.info())