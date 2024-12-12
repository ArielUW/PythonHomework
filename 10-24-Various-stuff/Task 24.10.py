"""Task 24.10.2024
1. Create the following list of Strings: [“Patryk”, “Alex”, “Ian”, “Kevin”]
Then write a program that:
A. Prints out all values separately (1p),
B. Prints out second value (Alex) (1p),
C. Checks the length of a list (1p),
D. Replaces all names with a word “Tomato” (1p).
2. Create the following list of Integers: [2, 4, 8, 12, 1, 67, 31]
Then write a program which:
A. converts all two-digit numbers into any object of String type (2p),
B. Prints the lowest value (2p)."""

def tomato(l):
    for i in range(len(l)):
        l.remove(l[i])
        l.insert(i, "Tomato")
    return l

def tomato2(l):
    x = len(l)
    l.clear()
    for i in range(x):
        l.append("Tomato")
    return l

def stringConversion(l):
    for i in range(len(l)):
        if type(l[i]) is int: # the condition are nested to avoid errors
            if 9 < l[i] < 100:
                l[i] = str(l[i])
    return l

def lowestValue(l):
    try:
        for i in range(len(l)):
            l[i]=int(l[i])
        l.sort()
        return f"The lowest value on the list is {l[0]}."
    except:
        return "This list contains elements that are unconvertable into int type."

if __name__ == "__main__":
    strings = ["Patryk", "Alex", "Ian", "Kevin"]
    integers = [2, 4, 8, 12, 1, 67, 31]
    for i in range(len(strings)): # 1A
        print(strings[i])
    print(f"The second element on the list is {strings[1]}.") # 1B
    print(f"The list has {len(strings)} elements.") # 1C
    print(tomato(strings)) # 1D v1
    print(tomato2(strings)) # 1D v2
    print(stringConversion(integers)) # 2A
    # I have no idea how to print this without converting some items on the list into strings
    print(lowestValue(integers)) #2B