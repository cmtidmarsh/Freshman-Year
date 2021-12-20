import math


X = float(input("Enter a number for the radius >>>"))
V = 4 / 3 * math.pi * X ** 3
Y = round(V, 2)
print("A ball of radius", X, "is of volume", Y)
