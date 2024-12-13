"""Load and assign the Titanic passenger data file (test.csv)  to a variable. Then perform the following tasks:
a. Create a new object of class DataFrame containing the following columns from the original DataFrame with the Titanic passengers (1pt):
i. Name
ii. Age
iii. Sex
b. Then, for the new DataFrame object (created in the previous
subsection) perform the following tasks (5):
i. Give the median age of the passengers (1pt)
ii. Replace the values in the Sex column with male - 0, female - 1. (1pt)
iii. Find out how many women and how many men were on board (2pts)
iv. Knowing the date of the Titanic disaster, calculate in which year the year the passengers were born. Assign this information to the new column ‘Year of birth’ (1 point)
"""
import pandas as pd
import math

#task A
df = pd.read_csv("./11-28-Titanic/test.csv", usecols=["Name", "Age", "Sex"])

#task B i
median = df.median(axis=0, numeric_only=True)
print(median)

#task B ii
print(df["Sex"].unique())
df["Sex"]=df["Sex"].apply(lambda x: "0" if x == "male" else "1" if x == "female" else "N/A")
print(df)

#task B iii
counts = {}
data = (df["Sex"].value_counts())
print(data)
counts["men"] = data.iloc[0]
counts["women"] = data.iloc[1]
for k, v in counts.items():
    print(f"There were {v} {k} on the Titanic.")

#task B iv
#15 V 1912 –> this is 106th day of the year -> 0.29 of the year has passed
print(df["Age"].unique())
df["Year of birth"] = df["Age"].apply(lambda x: x if pd.isna(x) else 1912.29 - x)
df["Year of birth"] = df["Year of birth"].apply(lambda x: x if pd.isna(x) else math.floor(x))
print(df)
#checking if the data is more or less correct
print(df.loc[df["Age"]%1>0])#weird float ages
print(df.loc[df["Age"]%df["Age"]!=0])#the only way to filter for NaN