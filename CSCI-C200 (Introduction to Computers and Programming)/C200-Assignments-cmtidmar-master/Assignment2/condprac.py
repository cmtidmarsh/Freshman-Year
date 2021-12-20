'''
 NOTE only modify functions with 'reworked' in the name
 They should produce identical output to the supplied function with the same number
 (i.e. fun1_reworked should have identical output to fun1)
 '''

# Problem 1
def fun1(x, y, z):
    output = ""
    if type(x) == list:
        output += 'x is a list'
    elif y < len(z):
        return
    elif len(x) + len(z) > y:
        output += 'These are some long iterables'
    elif y:
        output += 'Yeah, ' + str(y) + ' is a pretty good number.'
    else:
        output += 'Made it to the end!'
    return output

def fun1_reworked(x, y, z):
    '''Rewrite fun1, but do not use elif or else. Only if is allowed.'''
    output = ""
    if type(x) == list:
        output += 'x is a list'
        return output
    if y < len(z):
        return
    if len(x) + len(z) > y:
        output += 'These are some long iterables'
        return output
    if y:
        output += 'Yeah, ' + str(y) + ' is a pretty good number.'
    if x or z:
        output += 'Made it to the end!'
    return output


# Problem 2
def fun2(a, b, c):
    return bool(b and not ((not (a and b) and (not b or not c)) or (not c and not a)))

def fun2_reworked(a, b, c):
    '''Rewrite fun2, but do not use 'not' at all.'''
    return bool(b and not ((not (a and b) and (not b or not c)) or (not c and not a)))
    if a == b and b != c or c != a:
        return bool

print('Testing fun1 and fun1_reworked (Problem 1):')
print('-----------------------------------------------------')
print('Testing ([3, 7, 2], 14, "Nice String"): output: ', fun1_reworked([3, 7, 2], 14, 'Nice String'), ' expected: ', fun1([3, 7, 2], 14, 'Nice String'))
print('Testing ("Not a list",14,"lil"): output: ', fun1_reworked("Not a list",14,"lil"), ' expected: ', fun1("Not a list",14,"lil"))
print('Testing ([1],0,"bigger"): output: ', fun1_reworked([1],0,"bigger"), ' expected: ', fun1([1],0,"bigger"))
print('Testing ("Nope",0,"bigger"): output: ', fun1_reworked("Nope",0,"bigger"), ' expected: ', fun1("Nope",0,"bigger"))
print('Testing ("a",1000,"b"): output: ', fun1_reworked("a",1000,"b"), ' expected: ', fun1("a",1000,"b"))
print('Testing ("word1",3,"word2"): output: ', fun1_reworked("word1",3,"word2"), ' expected: ', fun1("word1",3,"word2"))
print('Testing ("",0,"")): output: ', fun1_reworked("",0,""), ' expected: ', fun1("",0,""))
print('Testing ("Big string here",6,"Another big string"): output: ', fun1_reworked("Big string here",6,"Another big string"), ' expected: ', fun1("Big string here",6,"Another big string"))
print('-----------------------------------------------------')
print('')
print('Testing fun2 and fun2_reworked (Problem 2):')
print('-----------------------------------------------------')
print('Testing (0, 0, 0): output: ' + str(fun2_reworked(0, 0, 0)) + ' expected: ' + str(fun2(0, 0, 0)))
print('Testing (0, 0, 1): output: ' + str(fun2_reworked(0, 0, 1)) + ' expected: ' + str(fun2(0, 0, 1)))
print('Testing (0, 1, 0): output: ' + str(fun2_reworked(0, 1, 0)) + ' expected: ' + str(fun2(0, 1, 0)))
print('Testing (0, 1, 1): output: ' + str(fun2_reworked(0, 1, 1)) + ' expected: ' + str(fun2(0, 1, 1)))
print('Testing (1, 0, 0): output: ' + str(fun2_reworked(1, 0, 0)) + ' expected: ' + str(fun2(1, 0, 0)))
print('Testing (1, 0, 1): output: ' + str(fun2_reworked(1, 0, 1)) + ' expected: ' + str(fun2(1, 0, 1)))
print('Testing (1, 1, 0): output: ' + str(fun2_reworked(1, 1, 0)) + ' expected: ' + str(fun2(1, 1, 0)))
print('Testing (1, 1, 1): output: ' + str(fun2_reworked(1, 1, 1)) + ' expected: ' + str(fun2(1, 1, 1)))
print('-----------------------------------------------------')
