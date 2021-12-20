def mySum(lst):
    """
    Adds all the numbers together in a list
    """
    returnValue = 0
    for item in lst:
        returnValue += item # returnValue = returnValue + item
    return returnValue

# print(mySum([100]))
# print(mySum([1, 2, 3, 4]))
# print(mySum([]))
# print(mySum((1, 2, 3)))


def evenList(lst):
    """
    Returns true if the sum of the list is even
    """
    s = mySum(lst)
    # return s % 2 == 0
    if s % 2 == 0:
        return True
    else:
        return False

def oddList(lst):
    """
    Returns true if the sum of the list is odd
    """
    s = mySum(lst)
    return s % 2 == 1

# print(evenList([100]))
# print(evenList([1, 2, 3, 7]))
# print(oddList([100]))
# print(oddList([1, 2, 3, 7]))

def numEvenOdd(lstoflst):
    """
    returns a typle of the number of even sub-lists and the number of odd sub-lists
    """

    returnTuple = [0, 0]
    for i in range(len(lstoflst)): # etting the possible values for an index
        item = lstoflst[i]          # Gets me the item at position 1
        theSum = mySum(item)
        if theSum % 2 == 0:
            returnTuple[0] += 1
        if theSum % 2 == 1:
            returnTuple[1] += 1
    return tuple(returnTuple)

ll = [[100], [1, 2, 3, 7], [], [4, 5, 6]]
print(numEvenOdd(ll))

def numEvenOdd2(lstoflst):
    """
    A different way to count the number of even or odd lists
    """
    evenCount=0
    oddCount=0
    for item in lstoflst:
        v = evenList(item)
        if v:
            evenCount += 1
        else:
            oddCount += 1
    return (evenCount, oddCount)

# ll = [[100], [1, 2, 3, 7], [], [4, 5, 6]]
# print(numEvenOdd(ll))
# print(numEvenOdd2(ll))

exp = ["a", "b", "c", "d"]
for i in range(len(exp)):
    print("Index value: ", i)
    print("value at index ", i, "is ", exp[i])
    i += 2 # i = i + 2
    print("Index value: ", i)

print(list(range(10)))
print(list(range(-10)))
#print(list(range(10.5))) #needs to be integer
print(list(range(5, 14)))
print(list(range(-14, -5)))
print(list(range(5, -5, -1)))
print(list(range(5, -5, -2)))
print(list(range(5, -5, 1)))
print(list(range(1, 10, 100)))
print(list(range(2, 100, 2)))
print(list(range(2, 99, 2)))
print(iter(range(0, 10)))
r = iter(range(0, 10))
print(r)