def palindrome(x):
    """
    For a given string, determine if the string is a palindrome. (The same forward and back)

    Input: String of any size (including empty)

    Return: Boolean (True if palindrome, False otherwise)

    Limitation: You must use a loop. Only function allowed to be used is len (if needed). Cannot use "in" besides "for var in container"
    """
    forward = x[0]
    backward = x[-1]
    for i in range(len(x)):
        if forward[i] == backward[-1-i]:
            return True
        else:
            return False


def getCount(char, strng):
    """
    Get the number of times a character appears in a string.

    Input: A character (length 1) and a string of any length

    Return: Number of times a character appears

    Limitation: Only functions we have been taught in class. Must use a loop. Cannot use "in" besides "for var in container"
    """
    count = 0
    for i in range(len(strng)):
        if strng[i] == char:
            count = count + 1
    return count



def getIndex(char, strng):
    """
    Gets the index of the character in the string

    Input: Character of length 1 and a string of any length

    Return: The first occurence of the character appearing in the string. 
    Return: the length of the string if the character does not exist

    Limitation: Only functions we have been taught in class. Must use a loop. Cannot use "in" besides "for var in container"
    """
    for i in range(len(strng)):
        if char == strng[i]:
            return i
    return len(strng)



def areEqual(str1, str2):
    """
    Determines if 2 strings are equal

    Input: 2 strings of any length (Both can be different lengths)

    Return: Boolean

    Limitation:  Must use a single loop, and only 1 return statement in the code. Cannot use "in" besides "for var in container"
    """
    for i in str1 and str2:
        if str1 == str2:
            return bool(i)
        else:
            return bool()

print("Palindrome")
print("Actual: ", palindrome("aba"), " Expected: ",  True)
print("Actual: ", palindrome("a"), " Expected: ",  True)
print("Actual: ", palindrome("abba"), " Expected: ",  True)
print("Actual: ", palindrome("amanaplanacanalpanama"), " Expected: ",  True)
print("Actual: ", palindrome("abca"), " Expected: ",  False)
print("Actual: ", palindrome("ac"), " Expected: ",  False)
print("Actual: ", palindrome("adabbba"), " Expected: ",  False)
print("Actual: ", palindrome("amandaplanacanalpanama"), " Expected: ",  False)

print()
print("Total Count")
print("Actual: ", getCount("t", "Tomato"), "Expected: ", 1)
print("Actual: ", getCount("a", "supercalifragilisticexpialidocious"), "Expected: ", 3)
print("Actual: ", getCount(" ", "The tomato is not a vegatable but a fruit. Into the salad"), "Expected: ", 11)

print()
print("Get Index")
print("Actual: ", getIndex("t", "Tomato"), "Expected: ", 4)
print("Actual: ", getIndex("a", "supercalifragilisticexpialidocious"), "Expected: ", 6)
print("Actual: ", getIndex(" ", "The tomato is not a vegatable but a fruit. Into the salad"), "Expected: ", 3)

print()
print("Are Equal")
s1 = "Tomato"
s2 = "Potato"
s3 = "Jotato"
s4 = "Lotato"
print("Actual: ", areEqual(s4, s4), "Expected: ", True)
print("Actual: ", areEqual(s1, s2), "Expected: ", False)
print("Actual: ", areEqual(s3, s2), "Expected: ", False)
print("Actual: ", areEqual(s1, s1), "Expected: ", True)
