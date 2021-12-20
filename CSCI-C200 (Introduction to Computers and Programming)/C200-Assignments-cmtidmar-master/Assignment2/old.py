import math

# Problem 2

def themath(tomato):
    tomato = 10
    newTomato = (tomato * 150) - 15
    # print(newTomato)

    theLast = math.sqrt(newTomato)
    # print(theLast)
    return theLast
print("Assignment 1 Problem 2: " + str(themath(10)))

# Problem 3
def thecost(numColorpages, numBWPages):
    # colorPages = input("What is the number of pages in color? >>>")
    # numColorPages = int(colorPages)

    # bwPages = input("What is the number of page in b&w? >>>")
    # numBWPages = int(bwPages)

    theCost = (0.25 * numColorpages) + (0.04 * numBWPages)
    return theCost

print("Assignment 1 Problem 3: " + str(thecost(4, 2)))

# # Problem 4 
def bouncing(radius):
# X = float(input("Enter a number for the radius >>>"))
    V = 4 / 3 * math.pi * radius ** 3
    Y = round(V, 2)
    return Y
# print("A ball of radius", X, "is of volume", Y)
print("Assignment 1 Problem 4: " + str(bouncing(5.5)))
