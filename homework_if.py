#MEDIUM

#1 Check if the user entered an even number.

#2 Check if the user has entered an odd number

#3. check if the sum of the two numbers entered by the user is an even number

#4. Check if the password entered by the user meets the following conditions
  # - at least one lowercase and one uppercase letter
  # - at least one digit
  # - at least one special character
  # - at least 3 characters in length
  # - a maximum of 18 characters in length
import string

def isEven(number):
    if number%2==0:
        return True
    else:
        return False
    
def checkPassword(password):
    for w in string.whitespace:
        if w in password:
            password = password.translate({ord(char): None for char in string.whitespace})
            print(f"Your password can't contain any white characters. They were removed from your password, which looks like this:\n{password}")
            break
    def checkLength(password):
        if len(password)<3:
            print("The password is too short.")
            return 1
        elif len(password)>18:
            print("The password is too long.")
            return 1
        else:
            return 0
    def noSpecChars(password):
        if password.isalnum():
            print("Your password doesn't containt any special characters")
            return 1
        else:
            return 0
    def noLetters(password):
        no_upper = True
        no_lower = True
        for i in password:
            if i.isupper():
                no_upper = False
                break
        for i in password:
            if i.islower():
                no_lower  = False
                break
        if no_upper and no_lower:
            print("Your password dosen't contain neither lower nor upper case letter.")
            return 1
        elif no_upper:
            print("Your password doesn't contain any upper case letter.")
            return 1
        elif no_lower:
            print("Your password doesn't contain any lower case letter.")
            return 1
        else:
            return 0
    def noDigits(password):
        no_digit = True
        for i in password:
            if i.isdigit():
                no_digit = False
                break
        if no_digit:
            print("Your password doesn't contain any digit.")
            return 1
        else:
            return 0
    somethingWrong = checkLength(password)
    somethingWrong += noLetters(password)
    somethingWrong += noDigits(password)
    somethingWrong += noSpecChars(password)
    if somethingWrong:
        return 1
    else:
        print("Great password, ok byeee! :3 💖")
        return 0

if __name__ == "__main__":    
    while True:
        first_number = input("Enter a number: ")
        try:
            first_number = int(first_number)
            if isEven(first_number):
                print("You have entered an even number.")
            else:
                print("You haven't entered an even number, but that's ok.")
            break
        except:
            print("The number needs to be expressed by digits only.")
            continue
    while True:
        second_number = input("Enter another number: ")
        try:
            second_number = int(second_number)
            if not isEven(second_number):
                print("You have entered an odd number.")
            else:
                print("You haven't entered an odd number, but that's ok.")
            break
        except:
            print("The number needs to be expressed by digits only.")
            continue    
    if isEven(first_number+second_number):
        print("The sum of the numbers you've entered is even.")
    else:
        print("The sum of the numbers you've entered is odd.")
    password = input("Pick a password: ")
    while checkPassword(password):
        password = input("Pick a different password: ")
        if not password:
            print("Bye~~ ✨")
            break
        else:
            continue