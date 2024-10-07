import string

firstString = "I love programming classes."
secondString = "Black is my favourite colour, unfortunately the colour black washes out of my clothes."

def firstTaskA (text):
    x = text.find('ing')
    y = text.find('ses')
    return text[x:y]

def negativeIndex (text):
    text = text + ":3"
    return text[0:-2]

def everyThird (text):
    chars = []
    index = 1
    while index < len(text):
        chars.append(text[index])
        index+=3
    return chars

def capitalInitials (text):
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

def initialC (text):
    if text[0] == "C":
        return True
    else:
        return False

def replaceBlack (text, colour="blue"):
    text = text.replace("Black", colour.capitalize())
    text = text.replace("black", colour.lower())
    return text

def replaceBlackSilly (text, colour="lue"):
    ### I did this one for fun, it only works for blue. I know you probably wanted us to do something with RegEx, but I couldn't help myself
    ### Please note that it *does* meet your requirement, as there was no restriction for the colour choice!
    return text.replace("lack", colour)

if __name__ == "__main__":
    print("\n\t\t📚 ARIEL'S FIRST HOMEWORK 🎉")
    print("\n### Task 1a ###")
    print((firstTaskA(firstString)))
    print("\n\n### Task 1b ###")
    print((negativeIndex(firstString)))
    print("\n\n### Task 1c ###")
    for i in everyThird(firstString):
        print(i)
    print("\n\n### Task 2a ###")
    if capitalInitials(secondString):
        print("All the words begin with a capital letter.")
    else:
        print("Not all the words begin with a capital letter.")
    print("\n\n### Task 2b ###")
    if initialC(secondString):
        print("The string begins with a capital C.")
    else:
        print("The string doesn't begin with a capital C.")
    print("\n\n### Task 2c ###")
    print(replaceBlack(secondString, "yellow"))
    print("\n\n### Task 2d ###")
    print(replaceBlackSilly(secondString))
    print("\n\t\t👋\n")
