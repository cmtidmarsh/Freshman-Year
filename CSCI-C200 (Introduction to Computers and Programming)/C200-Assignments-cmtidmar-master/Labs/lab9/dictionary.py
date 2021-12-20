

def flipKeyValue(d):
    """
    Given a dictionary, flips all values to make them keys

    Returns: A new dictionary
    """
    newD = {}
    for k in d:
        val = d[k]
        newD[val] = k
    return newD

def add(m1, m2):
    """
    Take in 2 dict., where the keys are numbers
    representing the row and the values are the corresponding
    columns
    """
    finalD = {}
    for k in m1:
        finalD[k] = []
        #row = []
        for i in range(len(m1[k])):
            v1 = m2[k][i]
            v2 = m1[k][i]
            finalD[k] += [v1 + v2]
    return finalD

if __name__ == "__main__":
    d1 = {1:2, 3:4, 5:6}
    d2 = {"a":1, "D":2, "C":1}
    d3 = {"1": [1], "2": [2], "3": [3]}
    print(flipKeyValue(d1))
    print(flipKeyValue(d2))
    # print(flipKeyValue(d3))
    matrix1 = {1:  [1, 2], 2: [3, 4]}
    matrix2 = {1:  [3, 4], 2: [5, 6]}
    print(add(matrix1, matrix2))


