import numpy as np
import matplotlib.pyplot as plt


def error(s, x):
    """
    TODO: Implement this function. 
    """
    return (abs(s-x**2)/(2*x))

def square_root(s, epsilon, estimate) -> list:
    """
    TODO: Calculates the approximation of the square root
    """

    lst = []
    while epsilon < error(s, estimate):
        estimate = ((1/2) * (estimate + (s/estimate)))
        lst.append(error(s, estimate))
    return lst


"""
TODO: Explain why we need iteration in this case. 
What value would you change to make the number of iterations increase?

Because you are constantly checking to see if epsilon is less than the error function with
new estimate.
You would change the original estimate.
"""


plt.ylabel("Error")
plt.xlabel("Iterations")
plt.title("Convergence of Square Root")

g = square_root(1000,.00005,500)
print(g)
plt.plot([i for i in range(len(g))], g,'r-o')

g = square_root(1000,.00005,775)
print(g)
plt.plot([i for i in range(len(g))], g,'b-o')

g = square_root(1000,.00005,3)
print(g)
plt.plot([i for i in range(len(g))], g,'g-o')

plt.show()
