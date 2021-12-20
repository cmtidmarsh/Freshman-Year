class Stack:

    def __init__(self):
        """
        Initializes the stack as a dara structure such as a list or an array
        """
        self.s = []

    def pop(self):
        """
        Removes the first item from the stack

        Implemented so not error if start is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.s.pop() # Refer to Python 3 documentation

    def push(self, item):
        """
        Pushes item onto a stack
        """
        self.s.append(item)

    def isEmpty(self):
        """
        Returns True if stack is empty, False otherwise
        """
        return self.s == []

    def peek(self):
        """
        Shows what the frist item on the Stack is.
        Will keep the Stack the same,
        since you just want to see what the value is.
        
        Returns the item on the top of the stack.
        """
        item = self.pop()
        self.push(item)
        return item #self.s[-1] #self.s[len(self.s)-1]
    
    def __str__(self):
        return "Stack: {}".format(self.s)

if __name__ == "__main__":
    s1 = Stack()

    s1.push(5)
    print(s1)
    i1 = s1.pop()
    print(i1)

