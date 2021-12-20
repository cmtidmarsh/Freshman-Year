class Queue:

    def __init__(self):
        """
        Initializes the queue with a data structure such as list or an array
        """
        self.lst = [] 
    
    def isEmpty(self):
        """
        Checks to see if the queue is empty.

        Returns True if empty, False otherwise
        """
        return self.lst == []

    def dequeue(self):
        """
        Removes an item from the front of the queue and returns it.
        
        This implementation checks to make sure the queue is not empty.
    
        """
        if not self.isEmpty():
            return self.lst.pop(0) #Remove from the FRONT of the lst
        else:
            return None
    def enqueue(self, item):
        """
        Adds an item to the back of the queue
        """
        self.lst.append(item) # Append to end of lst
    
    def __str__(self):
        return "Queue: {}".format(self.lst)

if __name__ == "__main__":
    q = Queue()
    print(q)

    q.enqueue(5)
    print(q)
    print(q.isEmpty())
    print(q.dequeue())
