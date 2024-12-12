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

df = pd.read_csv("test.csv", usecols=["Name", "Age", "Sex"])