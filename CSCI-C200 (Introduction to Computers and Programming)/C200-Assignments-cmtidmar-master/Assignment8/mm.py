import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    #TODO: Implement function
    matrix = []                 #make an empty list, this will be the outer list of the matrix
    for i in range(len(a)):        #take the elements in a and basically scan through a
        matrix.append([])       #append a with the empty/starting matrix, this makes
                                # matrix = [[1,2,4],
                                #           [3,4,3]]
        
        for j in range(len(b[0])):
            matrix[i].append(0)
            
            for k in range(len(b)):
                matrix[i][j] += a[i][k] * b[k][j]
    return matrix




#INPUT scalar n and matrix a
#RETURN scalar product na
#same lay out as problem one
def sm(n,a):
    #TODO:Implement function
    matrix = []                 
    for i in range(len(a)):
        matrix.append([])
        for j in range(len(a[i])):
            matrix[i].append(n*a[i][j])
    return matrix


#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    #TODO:Implement function
    matrix = []
    for i in range(len(a[0])):
        matrix.append([])
        for j in range(len(a)):
            matrix[i].append(a[j][i])
    return matrix



#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    #TODO:Implement function
    matrix = []
    for i in range(len(a)):
        matrix.append([])
        for j in range(len(b[0])):
            matrix[i].append(a[i][j] +b[i][j])
    return matrix


a = np.array([[1,2,4],[3,4,3]])
b = np.array([[-1,0],[1,-5],[-3,1]])
print("numpy product\n", np.dot(a,b))
d = mm(a,b)
print(d)

print("numpy scalar product\n", 4*a)
e = sm(4,a)
print(e)

print("numpy tranpose\n", np.transpose(a))
f = tp(a)
print(f)

print("numpy addition\n", a + a)
g = add_m(a,a)
print(g)
