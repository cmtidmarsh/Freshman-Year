def letterFrequency(strng):
    '''Given any string, return a dictionary containing the number of times each character present in the string occurred
    For example, the string "Hi, Larry" would yield the dictionary {"H" : 1, "i" : 1, " ": 1, "L" : 1, "a" : 1, "r" : 2, "y": 1}
    (order of entries does not matter)
    '''
    dictionary = {}
    for i in strng:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary     




def primeList(n):
    '''Return a list containing the first n Prime numbers'''
    primelst = []
    i = 2
    count = 0
    while True:
        if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) or (i == 2) or (i == 3) or (i == 5) or (i == 7): # prime numbers
            count = count + 1
            if count <= n:
                primelst = primelst + [i]
            else:
                break
        i = i + 1
    return(primelst)

