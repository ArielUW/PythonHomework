"""
1. Write a function rectangle_area that takes two arguments: the length and width of a rectangle. The function should return the area of the rectangle (1pt).
2. Write a function is_even that takes one argument: an integer. The function should return True if the number is even and False if it is odd (1pt).
3. Write a function convert_to_celsius that takes one argument: a temperature in Fahrenheit. The function should return the equivalent temperature in Celsius, using the formula (2pt):
4. Using data on the Titanic, create a function that checks whether passengers were over or under 30 years old. Pass the results to a new column in the DataFrame (2pt).
"""
import pandas as pd
import numpy as np
import random
df = pd.read_csv("./12-05-Functions/test.csv")

#task 1
def rectangleArea(length, width):
    if (type(length)==int or type(length)==float) and type(width)==int or type(width)==float:
        return 1/2*length*width
    else:
        print("Wrong data type for the length or width.")
        return None

#task 2
def isEven(num: int):
    if type(num)==int:
        if num%2==0:
            return True
        else:
            return False
    else:
        print(f'"{num}" is not an integer 😡😡')
        return None

#task 3
def convertToCelcius(farenheit):
    if type(farenheit)==int or type(farenheit)==float:
        return round(((farenheit-32)*5)/9,4)
    else:
        raise TypeError("Temperature in Farenheits should be an integer or a float.")
        #it's inconsistent with error handling in task 2, but I wantes to see how it goes
        
#task 4
def checkAge(age):
    if (type(age)==float or type(age)==int) and not pd.isna(age):
        if age > 30:
            return "Over 30 y/o"
        elif age < 30:
            return "Under 30 y/o"
        else:
            return "30 y/o"
    else:
        return np.nan

#checking stuff
if __name__=="__main__":
    #task 1
    length = random.randint(1,10)
    width = random.randint(1,10)
    area = rectangleArea(length,width)
    print(f"The rectangle with the length of {length} and the width of {width} has the area of {area}.")
    #task 2
    number = random.randint(1,100)
    if isEven(number)==None:
        pass
    elif isEven(number):
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is not even")
    #task 3
    farenheit = round(random.uniform(1.0,100.0),2)
    celcius = convertToCelcius(farenheit)
    print(f'{farenheit}°F is {celcius}°C')
    #task 4
    df["30 years old"] = df["Age"].apply(checkAge)
    mask = random.choices([True, False], k=len(df["Age"])) #quick random check
    print(df[["Age","30 years old"]].loc[mask])