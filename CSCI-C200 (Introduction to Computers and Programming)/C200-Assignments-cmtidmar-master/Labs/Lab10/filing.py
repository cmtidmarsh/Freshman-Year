def readingExample(fileName):
    """
    Given a file name, read the whole file

    Return everything in a string
    """

    f = open(fileName) #By default, mode is "r"
    s = f.read()
    f.close()
    return s

# print(readingExample("Labs/Lab10/files.py"))
# print([readingExample("Labs/Lab10/files.py")])

def readingExample2(fileName):
    """
    Given a file name, read the whole file
    """
    f = open(fileName, "r")
    string = "" #Initialize string to be empty
    for line in f:
        string += line
    f.close()
    return string


# print(readingExample2("Labs/Lab10/files.py"))
# print([readingExample2("Labs/Lab10/files.py")])

def readingExample3(file):
    """
    Passing in a file object, read the file
    """
    return file.readlines()
f = open("Labs/Lab10/files.py", "r")
# doNotCare = f.readline()
print(readingExample3(f))
f.close()

def writingLines(string):
    """
    Given a string, split the string by the "," character to make
    a new line for each item in the string. Write to the file
    "hello.txt"
    """
    split = string.split(",")
    anotherFile = open("Labs/Lab10/hello.txt", "a")
    for item in split:
        anotherFile.write(item + "\n")
    #anotherFile.writelines(split)
    anotherFile.close()

writingLines("a,b,c,d")

import os

path = os.getcwd()
print(path)
