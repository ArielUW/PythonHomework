def passwordVerification (password1, password2):
    if password1 == password2:
        return True
    else:
        return False

def phoneVerification (phoneNumber):
    if len(phoneNumber) < 9:
        return "Your phone number is too short."
    elif len(phoneNumber) > 9:
        return "Your phone number is too long."
    elif not phoneNumber.isdigit():
        return "Your phone number must be digits only."
    else:
        return 0

if __name__ == "__main__":
    name = input("What is your name? ")
    lastName = input("What is your last name? ")
    while True:
        try:
            age = int(input("What is your age? (in years) "))
            # here should be some additional verification if the number is probable (i.e. under ~120)
            break
        except:
            print("Age must be an integer!")
    while True:
        password = input("Password: ")
        password2 = input("Repeat password: ")
        if passwordVerification(password, password2):
            break
        else:
            print("You typed a different password the second type, try again")
    while True:
        phoneNumber = input("What is your phone nummber? (format: DDDDDDDDD) ")
        if phoneVerification(phoneNumber):
            print(phoneVerification(phoneNumber))
        else:
            break
    print(f"Here is the summary of your data:\nName: {name}\nLast name: {lastName}\nAge: {age}\nPhone number: {phoneNumber}")