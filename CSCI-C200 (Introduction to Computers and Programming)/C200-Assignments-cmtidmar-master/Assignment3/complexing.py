def positionalSum(a, b):
    """
    Given 2 lists, add the 2 lists together. The list will be as long as the shortest list. 

    Input: 2 lists of numbers

    Return: A new list of the size of the smaller list of the 2 lists added together positional.

    Example:
    >>> positionalSum([1, 2, 3, 4], [4, 3, 2]) # [5, 5, 5]
    >>> positionalSum([1, 2, 3, 4], [1, 1, 1, 4]) # [2, 3, 4, 8]
    """
    # for sum in range(len(a, b)):
    #     for sum in range(:
    #         sum = a + b
    #         print(sum)

    sum = []
    while a:
        while b:
            sum = a + b
            return sum
positionalSum([1, 2, 3, 4], [4, 3, 2])            

def scalarMatrix(n, m):
    """
    Given a matrix, size a x b, multiply each position by n. 

    Input: an number to multiply each item in the matrix (list of list)

    Return: A new list of lists that multiplies all values by n

    Limitation: No using numpy

    Examples: n = 3

    [[4, 4, 4]
     [1, 2, 4]
     [10, -1, 2]]

     Result:

     [[12, 12, 12]
      [3, 6, 12]
      [30, -3, 6]]

    """
    lst = []
    for row in m:
        for col in row:
            lst = lst + col*n
    return lst

scalarMatrix(4, [[4, 4, 4], [1, 2, 4], [10, -1, 2]])



def isSubString(sub, longStr):
    """
    Determine if a string exists in another string. 

    Not allowed to check for direct membership. You need to use looping

    Input: 2 strings

    Returns: Boolean if there is substring.

    Limitation: No "in" membership

    Example:

    >>> isSubString("cat", "Concatenate")  # True
    >>> isSubString("orange", "Concatenate")  # False
    >>> isSubString("acsd", "car")  # False
    """
    while longStr:
       while sub:
           if longStr.find(Concatenate) and sub.find(Concatenate):
               return True

isSubString("cat", "Concatenate")
isSubString("orange", "Concatenate")
def whereSubString(sub, longStr):
    """
    Determine last position of the start of a substring occurs. 

    Not allowed to check for direct membership. You need to use looping

    Input: 2 strings

    Returns: Integer showing where the substring starts in the longStr. Return -1 if 
    the substring doesn't exist

    Limitation: No "in" membership

    Example:

    >>> whereSubString("cat", "Concatenate")  # 3
    >>> whereSubString("orange", "Concatenate")  # -1
    >>> whereSubString("acsd", "car")  # -1
    """
    pass
