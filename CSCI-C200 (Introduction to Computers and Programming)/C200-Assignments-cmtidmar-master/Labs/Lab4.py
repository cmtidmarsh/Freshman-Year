def stringPractice():
    """
    Document string
    Describing the function
    """
    myString = "the lost tomato"
    print(myString)
    print(myString[4:9]) #Doing a substring from index 4 up to index 9 (not including)
    print(myString[2]) #Gets the value at index 2
    # myString[2] = "y" #Strings are immutable, you can't change them
    myString = "thy" + myString[3:]
    print(myString)

#stringPractice()

def listPractice():
    """
    Practicing with lists
    """

    exp = ["a", "b", "c", "d", "e"]
    print(exp)
    print(exp[3]) #Prints the value at the location in the list
    # Examples of slicing
    print(exp[1:4])
    print(exp[2:2])
    print(exp[4:1])
    print(exp) #The lines above it are not modified the original list, just taking substrings

    #Modify the list
    exp[2] = "Fisher"
    print(exp)
    #Expanding the list
    exp = exp + [1, 2, 3]
    print(exp)
    exp += []
    print(exp)
    exp += [[]]
    print(exp)
#listPractice()


def tuplePractice():
    myTuple = (1, 2, 3)
    print(myTuple)
    #Slicing
    print(myTuple[1:2])
    print(len(myTuple[1:2]))
    #reassigning
    # myTuple[1] = 5 #Tuples are immutable
    print(myTuple[1])
    myTuple += (4,)
    print(myTuple)


#tuplePractice()

def types():
    """
    Showing the conversion of one type to another
    """

    #type() #Gives the type of the item in python
    myList = [10, 11, 12, 13, 14, 15]
    myString = "QWERTY"
    myTuple = (0, 9, 8, 7, 6)
    print(type(myList), type(myString), type(myTuple))
    print(str(type(myList)) + str(type(myString)) + str(type(myTuple)))
    newList = list(myString)
    print(newList)
    newTuple = tuple(myList)
    print(newTuple)
    v1 = 100
    print(type(v1))
    print(type(None))

#types()

def conditionals(item):
    """
    Given an item, return the type

    """
    #return type(item)

    if type(item) == int:
        return int
    if type(item) == list:
        return list
    if type(item) == float:
        return float
    return "unknown"

# print(conditionals(1))
# print(conditionals([1, 2, 3]))
# print(conditionals(1.2))

def whatDrink(age):
    if age < 21:
        print("Here is a juice box")
    elif age >= 21 and age <= 30:
        print("You can have a beer")
    elif age > 30 and age <= 40:
        print("You can have expensive wine")
    elif age > 40 and age <= 50:
        print("What might be good for you")
    elif age > 50:
        print("Oh, you're still here?")
    else:
        print("Umm, have some some air")

whatDrink(21)
whatDrink(11)
whatDrink(31)
