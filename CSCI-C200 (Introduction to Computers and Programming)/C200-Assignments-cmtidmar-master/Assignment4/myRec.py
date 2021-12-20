def func1(n):
    if n == 0:
        return 0
    else:
        return func1(n-1) + n

def closedfunc1(n):
        return (n * (n+1)/ 2)

def func2(n):
    if n == 0:
        return 10000
    else:
        return func2(n-1)+func2(n-1)

def closedFunc2(n):
        return (1.02)^n + 10000

def func3(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return func3(n-1) + func3(n-2)

def func4(n):
    if n == 1:
        return 9
    else:
        return 9 * func4(n-1) + 10^(n-1) - func4(n-1)

def func5(n):
    if n == 0:
        return 1
    else:
        return 3 * func5(n-1) + 1

def closedFunc5(n):
    return (3^(n+1) - 1)/2




