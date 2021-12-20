import myRec

"""
Test Code
Using a loop, compute the first 10 values for any function.
"""

# TODO: import the functions and use a loop to show the values.

for i in range(10):
    if i == 0:
        print(myRec.func1(i))
        print(myRec.func2(i))
        print(myRec.func5(i))
    elif i == 1:
        print(myRec.func3(i))
        print(myRec.func4(i))
    elif i > 0 or i > 1:
        print(myRec.func1(i))
        print(myRec.func2(i))
        print(myRec.func3(i))
        print(myRec.func4(i))
        print(myRec.func5(i))
