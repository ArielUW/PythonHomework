"""
Write a lambda function to calculate the cube of a number over a [1,2,3,4].
Use filter and a lambda function to extract all numbers divisible by 3 from a list: [1, 2, 3, 4, 5, 6, 7, 8, 9].
Create a Pandas Series of integers from 1 to 10. Use a lambda function with .apply() to create a new Series where all values greater than 5 are squared.
Create a DataFrame with columns Name, Age, and City. Use a lambda function with .apply() to create a new column indicating whether a person is a minor (Age < 18)."""
import pandas as pd
import random

#ex 1
numbers = [1,2,3,4]
cubes = list(map(lambda x: x**3, numbers))
print(cubes)

#ex 2
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
extracted = list(filter(lambda x: x % 3 == 0, numbers2))
print(extracted)

#ex 3
data = pd.Series(range(1,11))
new_data = data.apply(lambda x: x**2 if x > 5 else x)
print(new_data)

#ex 4
names = ["Jana", "Pèire", "Augustin", "Gizem", "Alexei","Aphrodisios", "Tihomir", "Željko", "Apollonides", "Haruna"]
ages = [random.randrange(1, 60, 1) for i in range(10)]
cities = random.choices(["Paris", "London", "Warsaw"], k=10)

print(len(names))
print(len(ages))
print(len(cities))
print(names)
print(ages)
print(cities)

df = pd.DataFrame({"Name": names, "Age": ages, "City": cities})
df["Minor"] = df["Age"].apply(lambda x: "yes" if x < 18 else "no")
print(df)