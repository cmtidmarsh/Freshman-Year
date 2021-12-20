def myRemoveList(x, lst):
    """
    Remove every occurence of `x` in `lst` and return a list 
    that has all the contents of `cont` that are not `x`

    Not allowed to use a loop.
    
    UPDATE: CAN USE LOOP
    """

    for i in lst:
        if i == x:
            lst.remove(x)
            return [lst]

def myRemoveString(x, string):
    """
    Remove every occurence of `x` in `string` and return a list 
    that has all the contents of `cont` that are not `x`

    Not allowed to use a loop.
    """
    return string.replace(x,"")


def myReplaceList(old, new, cont):
    """
    Return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`
    """
    for i in cont:
        if i == old:
            cont[cont.index(old)] = new
            return cont
    

def myReplaceString(old, new, cont):
    """
    Return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`
    """
    return cont.replace(old, new)
 
def removePosList(x, cont):
    """
    Removes an item from the list `cont` that is at `x`.
    Returns a list of all items from `cont` that are not were not at the `x` position

    Example: removePosList(1, ['a', 'b', 'c']) --> ['a', 'c']
    """
    cont.pop(x)
    return cont

def minList(lst):
    """
    Find the minimum value in the list
    """
    return min(lst)

def maxList(lst):
    """
    Find the maximum value in the list
    """
    return max(lst)

def minIndex(lst):
    """
    Find the index of the minimum value
    """
    return lst.index(min(lst))

def maxIndex(lst):
    """
    Find the index of the minimum value
    """
    return lst.index(max(lst))

def getIndex(char, strng):
    """
    Gets the index of the character in the string

    Assume the character is in the string. 

    We will not test on any char that does not exist
    """
    return strng.find(char)

def areEqual(str1, str2):
    """
    Determines if 2 strings are equal

    Input: 2 strings of any length (Both can be different lengths)

    Return: Boolean

    """
    return str1 == str2

if __name__ == "__main__":
    print("TODO: Here is where tests will be written")
    print()
    print("Remove an item in a list (myRemoveList function):")
    print(myRemoveList("dog", ["dog", "cat", "dig", "claw"]))
    print(myRemoveList("woof", ["horse", "hoot", "woof", "hound"]))
    print(myRemoveList("food", ["steak", "food", "dog", "chicken"]))
    print()
    print("Remove an a letter in a string (myRemoveString function):")
    print(myRemoveString("g", "tiger"))
    print(myRemoveString("r", "rabbit"))
    print(myRemoveString("o", "woof"))
    print()

    print("Replacing an item in a string (myReplaceList function):")
    print(myReplaceList("food", "cat", ["dog", "food", "meow", "woof"]))
    print(myReplaceList("read", "write", ["read", "type", "revise"]))
    print(myReplaceList("weird", "abnormal", ["unusual", "awkard", "weird", "uncomfortable"]))
    print()

    print("Replacing a letter in a string (myReplaceString function):")
    print(myReplaceString("d", "n", "old"))
    print(myReplaceString("k", "d", "kevin"))
    print(myReplaceString("w", "e", "wheel"))
    print()

    print("Remove a postion in a list (removePosLst function):")
    print(removePosList(1, ["people", "dogs", "sharks", "monkey"]))
    print(removePosList(2, ["a", "b", "c", "d"]))
    print(removePosList(4, [0, 1, 2, 3, 4, 5, 6]))
    print()

    print("Return the minimum value in a list (minList function):")
    print(minList([2, 5, 3, 6, 1, 12]))
    print(minList([4, 7, 2, 10, 199, 3]))
    print(minList([99, 65, 483, 58, 475, 22]))
    print()

    print("Return the maximum value in a list (maxList function):")
    print(maxList([3, 4, 6, 2, 7, 2, 4]))
    print(maxList([100, 39, 47, 281, 394, 382]))
    print(maxList([99, 65, 483, 58, 475, 22]))
    print()

    print("Return the min index in a list (minIndex function):")
    print(minIndex([2, 5, 3, 6, 1, 12]))
    print(minIndex([4, 7, 2, 10, 199, 3]))
    print(minIndex([99, 65, 483, 58, 475, 22]))
    print()


    print("Return the maximum value in a list (maxIndex function):")
    print(maxIndex([3, 4, 6, 2, 7, 2, 4]))
    print(maxIndex([100, 39, 47, 281, 394, 382]))
    print(maxIndex([99, 65, 483, 58, 475, 22]))
    print()

    print("Returns the index of a letter/character in a string (getIndex function):")
    print(getIndex("i", "string"))
    print(getIndex("e", "fed"))
    print(getIndex('6', 're6d'))
    print()

    print("Returns the boolean if two strings are equal (areEqual function):  ")
    print(areEqual("my cat", "my cat"))
    print(areEqual("string1", "string2"))
    print(areEqual("True", "False"))
