"""
For this file, store the lambda expression into a variable, then call the lambda expression and show that it works for a couple of inputs 
"""

#a) Write a lambda function that takes 3 strings and combines them together into 1
print("PART A")
print((lambda x, y, z: x+y+z)("string1 ", "string2 ", "string3 "))

#b) Write a lambda function that takes 2 arguments and returns one raised the the power of the other
print("PART B")
print((lambda x, y: x**y)(2, 3))
#----------using lst1, lst2, lst3-------------------------------------

lst1 = [5, 2, 5, 7, 10]
lst2 = [10, 5, 1, 8, 15]
lst3 = ["deep", "in", "the", "hundred", "acre", "wood"]
#c) using lst1 and map, return a list that is the inverse (1/x) of each number of lst1
# print(map(lambda x: (1/x), (lst1)))
print("PART C")
print(list(map((lambda x : 1/x), lst1)))

#d) using lst1, lst2, and map, multiply lst1 by lst2 for each item
# print(list(map(lambda x, y : x * y), lst1, lst2))
print("PART D")
print(list(map((lambda x, y : x * y), lst1, lst2)))


#e) using lst3 and filter, return all words that have the letter r
print("PART E")
print(list(filter(lambda x : "r" in x, lst3)))




#----Demonstrate parts c, d, e with some of your own tests-----------------

#Testing part c
print()
print("TESTING PART C")
lst4 = [1,2, 3, 4]
print(list(map((lambda x : 1/x), lst4)))
print(list(map((lambda x : 1/x), lst2)))
print(list(map((lambda x : 1/x), lst1)))
print()

#Testing part d 
print("TESTING PART D")
lst5 = [2, 4, 6, 8]
lst6 = [20, 40, 60, 80]
print(list(map((lambda x, y : x * y), lst5, lst6)))
print(list(map((lambda x, y : x * y), lst1, lst6)))
print(list(map((lambda x, y : x * y), lst3, lst1)))
print()

print("TESTING PART E")
# print("Testing part e")
lst7 = ["cat", "dog", "rat", "pig", "cow"]
print(list(filter(lambda x : "c" in x, lst7)))
print(list(filter(lambda x : "o" in x, lst7)))
print(list(filter(lambda x : "p" in x, lst7)))
print()
#------------------------------------------------------------------------

#-----a-e: Repeat with equivalent loops and no lambda functions----------

#a) Write a function that takes 3 strings and combines them together into 1
print()
print("PART A, NO LAMBDA")
def threeStrings(x, y, z):
    result = " "
    for i in result:
        result = x + y + z
        return result

print(threeStrings("string1", "string2", "string3"))

#b) Write a function that takes 2 arguments and returns one raised the the power of the other
print()
print("PART B, NO LAMBDA")
def power(x, y):
    result = 1
    for i in range(result):
        result = x**y
        return result

print(power(1, 2))
print(power(2, 1))
print(power(2, 3))

#c) using lst1 and map, return a list that is the inverse (1/x) of each number of lst1
print()
print("PART C, NO LAMBDA ")
def mathLst(lst):
    return [1/x for x in lst]

lst1 = [5, 2, 5, 7, 10]
print(mathLst(lst1))


        

#d) using lst1, lst2, and map, multiply lst1 by lst2 for each item
print()
print("PART D, NO LAMBDA:")
def multiply(x, y):
    return [x[i]*y[i] for i in range(len(x))]

lst1 = [5, 2, 5, 7, 10]
lst2 = [10, 5, 1, 8, 15]
print(multiply(lst1, lst2))

# #e) using lst3 and filter, return all words that have the letter r
print()
print("PART E, NO LAMBDA:")
lst3 = ["deep", "in", "the", "hundred", "acre", "wood"]
print("print e, no lambda: ")
def returnNewLst(x):
    return [i for i in x if "r" in i]


print(returnNewLst(lst3))




