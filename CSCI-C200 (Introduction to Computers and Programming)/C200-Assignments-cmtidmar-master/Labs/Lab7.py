def myRangeList(start, stop, step):
    """
    Given a start, a stop, and a step, ensure that you can produce a valid list
    If you can't produce a valid list, return an empty list
    """
    ### Check out values work 
    if start < stop and step < 0:
        print("Check 1")
        return []
    elif start > stop and step > 0:
        print("Check 2")
        return []

    ### Base Case
    if start == stop:
        print("Base Case 1")
        return []
    elif start > stop and step > 0:
        print("Base Case 2")
        return []
    else:
        ### Inductive step
        print("Inductive step")
        r = myRangeList(start+step, stop, step)
        return [start] + r

# print(myRangeList(0, 10, 1))
# print(myRangeList(5, 5, 1))
# print(myRangeList(1, 5, 2))
# print(myRangeList(10, 5, -1))
# print(myRangeList(10, 5, -2))


def sumOfSquares(nums):
    """
    Given a list of numbers, add all the numbers 
    together to find the sum of all the numbers squared.
    Allowed to use slicing
    """
    ##Base case involves 0
    if not nums: 
        return 0
    else:
        s = nums[0]*nums[0]
        return s + sumOfSquares(nums[1:]) 
# print(sumOfSquares([1, 1, 1, 1]))
# print(sumOfSquares([4, 5, 7, 1]))


def printFib(n, indent):
    """
    Return the n-th fibonacci and display the progress
    """
    print("\t" * indent + "fib(" + str(n) + ")")
    if n == 0 or n == 1:
        print("\t" * indent + "return: " + str(n))
        return n
    else:
        print("\t" * indent + "calling fib(" + str(n - 1) + ") and fib(" + str(n - 2)+ ")")
        temp = printFib(n - 1, indent + 1) + printFib(n - 2, indent + 1)
        print("\t"*indent +"return: " + str(temp))
        return temp

# print(printFib(4,0))
# printFib(7,0)

def power(a, b):
    """
    Take a to the b
    a**b
    """
    if b==0:
        return 1
    if b==1:
        return a
    if b<0:
        return 1 / power(a, abs(b))
    else:
        return a * power(a, b - 1)
print(power(2, 4))
print(power(2, -2))