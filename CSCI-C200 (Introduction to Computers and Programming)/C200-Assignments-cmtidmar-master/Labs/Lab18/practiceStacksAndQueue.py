#First 20 minutes

class Stacks:
    def __init__(self):
        self.stack = []
    
    def empty(self):
        if self.stack == []: # may or may not be correct
            return []

    
    def pop(self):
        if self.empty():
            return self.stack.pop()

    def push(self, x):
        self.stack.append(x) #Append the x value to the stack
        self.stack.remove(x) #Remove it from the back
        self.stack.insert(0, x) #Move it to the front
        return self.stack

class Queue: 
    def __init__(self):
        self.queue = []
    
    def empty(self):
         if self.queue == 0: # may or may not be correct
            return []
    
    def dequeue(self):
        if self.empty():
            return self.queue.dequeue()
        else:
            return False
    
    def enqueue(self, x):
        self.queue.append(x)
        return self.queue






