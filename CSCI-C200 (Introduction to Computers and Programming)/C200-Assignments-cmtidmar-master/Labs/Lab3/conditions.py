def  myMin(x, y):
    if x > y:
        return y
    else:
        return x

def myMin2(x, y):
    if x > y:
        return y
    elif x == y:
        return y
    elif x < y:
        return x

# print(myMin(1, 1))
# print(myMin(2, 3))
# print(myMin(5, 4))
# print(myMin2(1, 1))
# print(myMin2(2, 3))
# print(myMin2(5, 4))

# Demonstrating the difference between if if if else
# versus if elif elif else

x = 9
y = 32
z = "Hello"

if x>10:
    print("Condition 1")
if y>30:
    print("Condition 2")
if z != "Hello":
    print("Condition 3")
else:
    print("Condition 4")

if x>10:
    print("Condition 1")
elif y>30:
    print("Condition 2")
elif z != "Hello":
    print("Condition 3")
else: 
    print("Condition 4")

def canBePresident(isCitizen, age, residency):
    if isCitizen and age>=35 and residency>=14:
        return True
    else:
        return False
#  print(canBePresident(True, 35, 15))
#  print(canBePresident(True, 22, 15))

def minThree(v1, v2, v3):
     if v1<v2:
         if v1<v3:
             return v1
         else:
             return v3
     else:
         if v2<v3:
             return v2
         else:
             return v3

# print(minThree(1, 1, 1))
# print(minThree(1, 2, 3))
# print(minThree(5, 4, 6))
# print(minThree(3, 2, 1))


def sumMin2(x, y, z):
    # Find the 2 smallest numbers and return the sum of the 2
    # smallest numbers
    # smallestNum = minThree(x, y, z)
    if (x <= y and y <= z) or (y <= x and x <= z):
        return x+y
    elif x <= y and y >= z:
        return x+z
    # elif y <= x and x <= z:
    #     return y+x
    elif y <= x and x >= z:
        return y+z
    elif z <= x and x <= y:
        return z+x
    elif z <= x and x >= y:
        return z+y

# print(sumMin2(1, 1, 1))
# print(sumMin2(1, 2, 3))
# print(sumMin2(3, 2, 1))
# print(sumMin2(5, 4, 6))
# print(sumMin2(8, 10, 7))

myBigVariable = 100

def myFunction(x, y):
    #print(myBigVariable)
    myBigVariable = 123
    print(myBigVariable)
    return myBigVariable + x * y

print(myBigVariable)
print(myBigVariable(1, 2))
print(myBigVariable)

