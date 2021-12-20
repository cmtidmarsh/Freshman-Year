def whileSum(lst):
    """

    Using a while loop, sum all the values in a list
    """
    s = 0
    i = 0
    while i < len(lst):
        s += lst[i]
        i += 1

    return s
print(whileSum([1, 2, 3, 4]))

def whileMultiplication(lst):
    """
    Using a while loop, multiply all of the values in a list together
    """

    s = 1
    while lst:
        s *= list[0]
        lst = lst[1:]
    return s 

# print(whileMultiplication([1, 2, 3, 4]))

def interactiveProgram():
    myDict = {}
    while True:
        name = input("What is your name? >>")
        if name == "":
            return myDict
        num = int(input("What is your favourite number? >>"))
        myDict[name] = num #Adding it to the dictionary


def matrixStuff(m):
    """
    Do through a maxtrix and double any even number"

    """
    for r in range(len(m)): # Give me the number of rows
        row = m[r]
        for c in range(len(row)):
            col = row[c]
            v = m[r][c]
            if col != v:
                print("uh oh")
            if v%2 == 0:
                m[r][c] *= 2
m1 = [[1, 2], [3, 4]]
matrixStuff(m1)
print(m1)

def anotherStuff(m):
    lst = []
    for row in m:
        #lst += [  []  ]
        temp = []
        for col in row:
            if col % 2 == 0:
                temp += [col *2]
            else:
                temp += [col]
        lst += [ temp ]
    return lst

m1 = [[1, 2], [3, 4]]
m2 = anotherStuff(m1)
print(m1)
print(m2)

