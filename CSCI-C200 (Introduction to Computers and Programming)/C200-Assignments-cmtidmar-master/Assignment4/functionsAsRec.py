"""
None of the functions are allow to use loops (for or while).

Not allowed to use any built-in string or list methods 
(.append, .remove, .find, .index, or anything else that would avoid recursion).

Not allowed to use built-in max or min. 
"""

def myRemove(x, cont):
    """
    Recursively remove every occurence of `x` in `cont` and return a list 
    that has all the contents of `cont` that are not `x`

    Not allowed to use list operation .remove()
    """
    if len(cont) == 0:
        return []
    elif x == cont[0]:
        return myRemove(x, cont[1:])
    else:
        return list(cont[0]) + myRemove(x, cont[1:])



def myReplace(old, new, cont):
    """
    Recursively return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`
    """
    if len(cont) == 0:
        return []
    elif cont[0] != old:
        return list(cont[0]) + myReplace(old, new, cont[1:])
    else:
        return list(new) + myReplace(old, new, cont[1:])
    



def isPalindrome(string):
    """ 
    Recursively returns true if the string is a palindrome. 

    Not allowed to use list / string iteration i.e. myList[::-1]
    """
    forwards = string[0]
    backwards = string[-1]
    if len(string) == 0:
        return []
    elif forwards == backwards:
        return True
    else:
        return False

def lengthOfString(string):
    """
    Recursively returns the length of the cont
    """
    if len(string) == 0:
        return ''
    elif len(string) >= 1:
        return len(string)


def removePos(x, cont):
    """
    Recursively removes an item from the list `cont` that is at `x`.
    Returns a list of all items from `cont` that are not were not at the `x` position

    Example: removePos(1, ['a', 'b', 'c']) --> ['a', 'c']
    """
    if len(cont) == 0:
        return []
    elif len(cont) - 1 == x:
        return removePos(x, cont[0:-1])
    else:
        return removePos(x, cont[0:-1]) + list(cont[-1])

def sum2Dlist(mat):
    """
    Recursively go through and sum all the values from each row and add the result of
    each row together to get a final value
    ex) 
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] ---> 45
    Returns an integer
    """
    if not mat:
        return 0
    else:
        return sum(mat[0]+ sum2Dlist(mat[1:]))

def fibonnaci(n):
    """
    Complete this to return the fibonacci sequence

    Input: The n-th fibonnaci number to find

    Return: The value of the n-th fibonnaci number

    Extra Credit Opportunity: 
    - Add memoization. Refer to Monday's lecture 
    - Do not use the internet to figure it out.
    - It is extra credit, implementation is practice
    - Before the exam, understand the idea
    """
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return (n-1) + (n-2)
