import math #This brings in the math module

def  quadraticFormula(a, b, c):
    dis = b ** 2 - 4 * a * c
    n = -b + math.sqrt(dis)
    d = 2 * a
    return n / d
print(quadraticFormula(1, 4, 4))

def convertToString(y):
    return str(y)

def combinesStrings(a, b):
    finalString = convertToString(a) + convertToString(b)
    return finalString

print(combinesStrings(1, 2))

def nothing(a, b, c, d, e, f):
    a + b + c + d + e + f

print(nothing(6, 6, 6, 6, 6, 6))

x = 6
x = x + 2
print(x)