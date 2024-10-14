def calculator(first_number, second_number, operator):
    # The function works for both floats and integers.
    if operator == "+":
        try:
            return first_number + second_number
        except:
            return "You somehow sneaked a non-number into my calculator 😡"
            # this will never be displayed if this file is run as a script, but I left it here in case it is imported as a package and there is a need to handle an exception (the same applies to conditions below).
    elif operator == "-":
        try:
            return first_number - second_number
        except:
            return "You somehow sneaked a non-number into my calculator 😡"
    elif operator == "*":
       try:
           return first_number * second_number
       except:
            return "You somehow sneaked a non-number into my calculator 😡"
    elif operator == "/":
        if second_number == 0:
            return "You can't divide by 0."
        else:
            try:
                return first_number / second_number
            except:
                return "You somehow sneaked a non-number into my calculator 😡"
    else:
        return "Invalid operator. I only do the following operations:\n+ (addition)\n- (subtraction)\n* (multiplication)\n/ (division)\nSorry! 💅"
        
if __name__ == "__main__":
    while True:
        while True:
            try:
                first = int(input("Type in your first integer: "))
                break
            except:
                print("The number needs to be an integer.")
        while True:
            try:
                second = int(input("Type in your second integer: "))
                break
            except:
                print("The number needs to be an integer.")
        operator = input("What operation do you want to perform? Type: + - * or / ")
        # invalid operators are handled by the function itself, so there is no need to check the input
        try:
            print(calculator(first, second, operator))
        except:
            print("Something went wrong 🤷") # for unforseen exceptions
        anwser = input("Do you want to do another operation? Type y to continue, anything else to quit. ")
        if anwser == "y":
            continue
        else:
            break