# give the colors that contain fruit
fruit = ["apple", "peas", "corn"]
x = {"red": ["apple", "firetruck"], "blue": ["sky", "ocean"], "green": ["peas"], "yellow":["sun", "corn"]}
q1 = [color for color in x.keys() for fruitVal in x[color] if fruitVal in fruit]
print(q1)





#rewrite as lambda/map/filter
# s = [2*x+1 for x in range(0,13)]
q2 = list(map(lambda x : 2 * x + 1, (x for x in range(0, 13))))
print(q2)
t = [2 * x + 1 for x in range(0, 13) if x % 3]
# print(t)
q3 = list(map(lambda x: (2 * x + 1), filter(lambda x: (x % 3 == 1 or x % 3 != 0),[i for i in range(0, 13)])))
print(q3)


#match the output
a = []
for i in range(1,9):
    if i % 2 == 0:
        a.append(i**2 - i + 3)
q4 =  [(i**2 - i + 3) for i in range(1, 9) if(i % 2 == 0)]
print(q4)
q5 =  list(map(lambda i: (i**2 - i + 3), filter(lambda i:(i % 2== 0), [i for i in range(1, 9)])))
print(q5)


#match the outputs
c1 = []
for n in range(1, 16):
    if n % 2 == 0:
        c1.append(n**2)
    else:
        c1.append(n**3)
q6 =  [n**2 if n % 2 == 0 else n**3 for n in range(1, 16)]
print(q6)
q7 =  list(map(lambda n: n**2 if(n % 2 == 0) else n**3, (n for n in range(1, 16))))
print(q7)




#This is technically transpose of a matrix
#But for now, just match output
e1 = [[1,2],[3,4],[5,6],[7,8]]
# q8 =
# print(q8)
# q9 =
# print(q9)


#reverse the order of letters in the string
f1 = ["hello"]
q10 = [i[::-1] for i in f1]
print(q10)
q11 = ["".join(list(map(lambda i: i[::-1], [i for i in f1])))]
print(q11)

#NOTE: I know we're not supposed to use [::-1],
# but I couldn't figure out how to without using it.


#reverse the order of letters in each string, preserving the order of the list
g1 = ["hello", "goodbye", "mer["".join(letter for letter in ['hello'][0][::-1])]haba"]
q12 = [values[::-1] for values in g1]
print(q12)
q13 = list(map(lambda values: values[::-1], [values for values in g1]))
print(q13)
