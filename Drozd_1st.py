import string
import re

# hello

def firstTaskA (text): # anwser for Task 1a
    x = text.find('ing')
    y = text.find('ses')
    return text[x:y]

def negativeIndex (text): # anwser for Task 1b
    # correct: text[-len(text):]
    text = text + ":3"
    return text[0:-2]

def everyThird (text): # anwser for Task 1c
    # correct: text[1:len(text):3]
    chars = []
    index = 1
    while index < len(text):
        chars.append(text[index])
        index+=3
    return chars

def capitalInitials (text): # anwser for Task 2a
    # correct: text.istitle()
    #text = text.title() # for testing
    normalisedText = text.translate(str.maketrans('', '',string.punctuation))
    words = normalisedText.split(" ")
    flag = True
    for w in words:
        if w[0].isupper():
            continue
        else:
            flag = False
            break
    return flag

def initialC (text): # anwser for Task 2b
    if text[0] == "C":
        return True
    else:
        return False

def replaceBlack (text, colour="blue"): # anwser for Task 2c
    text = text.replace("Black", colour.capitalize())
    text = text.replace("black", colour.lower())
    return text

def replaceBlackSilly (text, colour="lue"): # silly anwser for Task 2d
    ### I did this one for fun, it only works for blue. I know you probably wanted us to do something with RegEx, but I couldn't help myself. It *does* meet your requirement, as there was no restriction for the colour choice!
    return text.replace("lack", colour)

def replaceColour (text, newColour="beige", orgColour="black"): # serious anwser for Task 2d
    ### I coundn't think of a way to make it contain exactly one meaningful instance of using the replace() method, so I ended up using a different design all together.
    def cases(match):
        colour = match.group()
        if colour.islower(): return newColour.lower()
        if colour.istitle(): return newColour.title()
        if colour.isupper(): return newColour.upper()
        return newColour
    return re.sub(orgColour, cases, text, flags=re.I)

if __name__ == "__main__":
    firstString = "I love programming classes."
    secondString = "Black is my favourite colour, unfortunately the colour black washes out of my clothes."
    print("\n\t\t📚📚📚📚📚📚📚📚📚📚📚\n\t\t📚 ARIEL'S HOMEWORK 📚\n\t\t📚📚📚📚📚📚📚📚📚📚📚")
    print("\n### Task 1a ###")
    print((firstTaskA(firstString)))
    print("\n\n### Task 1b ###")
    print((negativeIndex(firstString)))
    print("\n\n### Task 1c ###")
    for i in everyThird(firstString):
        print(i)
    print("\n\n### Task 2a ###")
    if capitalInitials(secondString):
        print("All the words in the default string begin with a capital letter.")
    else:
        print("Not all the words in the default string begin with a capital letter.")
    while True:
        anwser = input("\nDo you want to check another string?\n(type y to agree, anything else to decline): ")
        if anwser == "y":
            newString = input("Type in your string: ")
            if capitalInitials(newString):
                print("All words in your string begin with capital letters.")
            else:
                print("Not all words in your string begin with capital letters.")
        else:
            print("Ok 😔")
            break
    print("\n\n### Task 2b ###")
    if initialC(secondString):
        print("The default string begins with a capital C.")
    else:
        print("The default string doesn't begin with a capital C.")
    while True:
        anwser = input("\nDo you want to check another string?\n(type y to agree, anything else to decline): ")
        if anwser == "y":
            newString = input("Type in your string: ")
            if initialC(newString):
                print("Your string begins with a capital C.")
            else:
                print("Your string doesn't begin with a capital C.")
        else:
            print("Ok 😔")
            break
    print("\n\n### Task 2c ###")
    print(replaceBlack(secondString, "yellow"))
    while True:
        anwser = input("\nDo you want to replace it with another colour?\n(type y to agree, anything else to decline): ")
        if anwser == "y":
            newColour = input("Type in your colour: ")
            print(replaceBlack(secondString, newColour))
        else:
            print("Ok 😔")
            break
    print("\n\n### Task 2d ###")
    print(replaceBlackSilly(secondString))
    print(replaceColour(secondString))
    while True:
        anwser = input("\nDo you want to replace it with another colour?\n(type y to agree, anything else to decline): ")
        if anwser == "y":
            colour = input("Type in your colour: ")
            print(replaceColour(secondString, colour))
        else:
            print("Ok 😔")
            break
    print("\n\t\tThis is all, bye-bye! 👋\n")
