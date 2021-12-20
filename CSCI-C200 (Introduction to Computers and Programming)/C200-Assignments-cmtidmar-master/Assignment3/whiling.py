def minVal(theLst):
    """
    Given a list, determine the minimum value in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Value of minimum value

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    minimum = theLst[0]
    i = 1
    while (i < len(theLst)):
        if theLst[i] < minimum:
            minimum = theLst[i]
        i += + 1
    return minimum




def minValIndex(theLst):
    """
    Given a list, determine the index of the minimum value (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Index of the smallest value (the last occurence)

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    index = theLst[0]
    min_index = 0
    i = 1
    while (i < len(theLst)):
        if theLst[i] < index:
            index = theLst[i]
            min_index = i
        i = i + 1
    return min_index
        



def minValTuple(theLst):
    """
    Given a list, determine the minimum value and index in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Tuple, first item is the smallest value, second item is the index of the value (the last occurence)

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    minVal = theLst[0]
    min_Index = 0
    i = 1
    while (i < len(theLst)):
        if theLst[i] < minVal:
            minVal = theLst[i]
            min_Index = i
        i += 1
    return (minVal, min_Index)

def maxVal(theLst):
    """
    Given a list, determine the maximum value in the list

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Value of maximum value

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    maximum = theLst[0]
    i = 1
    while (i < len(theLst)):
        if theLst[i] > maximum:
            maximum = theLst[i]
        i += 1
    return maximum


def maxValIndex(theLst):
    """
    Given a list, determine the index of the maximum value (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Index of the largest value (the last occurence)

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    index = theLst[0]
    max_index = 0
    i = 1
    while (i < len(theLst)):
        if theLst[i] > index:
            index = theLst[i]
            max_index = i
        i += 1
    return max_index


def maxValTuple(theLst):
    """
    Given a list, determine the maximum value and index in the list (the last occurence)

    Input: A list numbers of any length (at least 1 item in the list)

    Return: Tuple, first item is the largest value, second item is the index of the value (the last occurence)

    Limitation: The only function you can use is len(). Cannot use "in" besides "for var in container"
    """
    maxVal = theLst[0]
    max_Index = 0
    i = 1
    while (i < len(theLst)):
        if theLst[i] > maxVal:
            maxVal = theLst[i]
            max_Index = i
        i += 1
    return (maxVal, max_Index)

def tripTotal(logs):
    """
    Given a list containing sublists of size 2, each sublist 
    [number of miles traveled, speed traveled at that distance]. 
    You will find the total time of the trip

    Input: List of lists, containing at least 1 item.
    [[m1, s1], [m2, s2], [m3, s3], ...]

    Return: The total time the trip took.

    Required to use a single for loop
    """


print("Testing Cases")
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lst2 = [15, 12, 10, 95, 101]
lst3 = [5, 4, 3, 2]
print("Min Val of LST1: ", minVal(lst1))
print("Min Index of LST1: ", minValIndex(lst1))
print("Min Val and Index of LST1: ", minValTuple(lst1))
print("Max Val of LST1: ", maxVal(lst1))
print("Max Index of LST1: ", maxValIndex(lst1))
print("Max Val and Index of LST1: ", maxValTuple(lst1))
print()
print("Min Val of LST2: ", minVal(lst2))
print("Min Index of LST2: ", minValIndex(lst2))
print("Min Val and Index of LST2: ", minValTuple(lst2))
print("Max Val of LST2: ", maxVal(lst2))
print("Max Index of LST2: ", maxValIndex(lst2))
print("Max Val and Index of LST2: ", maxValTuple(lst2))
print()
print("Min Val of LST3: ", minVal(lst3))
print("Min Index of LST3: ", minValIndex(lst3))
print("Min Val and Index of LST3: ", minValTuple(lst3))
print("Max Val of LST3: ", maxVal(lst3))
print("Max Index of LST3: ", maxValIndex(lst3))
print("Max Val and Index of LST3: ", maxValTuple(lst3))
print()
testingLog = [[100, 50], [10, 10], [60, 60]]
print("Testing the tripTotal function: ", tripTotal(testingLog))
