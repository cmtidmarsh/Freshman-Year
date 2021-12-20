class Stack:

    def __init__(self):
        self.st = []

    def pop(self):

        if not self.empty():
            return self.st.pop()

    def push(self, item):
        self.st.append(item)

    def empty(self):
        return self.st == []

def balancing(a):
    stack = Stack()
    for i in range(len(a)):
        p = a[i]
        if p == "(" or p == "{" or p == "[":
            stack.push(p)
        if p == ")" or p == "}" or p == "]":
            c = stack.pop()
            if c == "(" and p != ")":
                return False
            if c == "{" and p != "}":
                return False
            if c == "[" and p != "]":
                return False
            
    if not stack.empty():
        return False
    
    return True
        
    

print(balancing("()"))
print(balancing("()[]"))
print(balancing("()[]{}"))