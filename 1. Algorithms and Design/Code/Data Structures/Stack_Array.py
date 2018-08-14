# Implementation of the Stack ADT using an array.

class Stack() :

    """ Array-based stack implementation """

    DEFAULT_CAPACITY = 10   # Class variable applies to all stacks
    
    # Creates an empty stack.
    def __init__(self):
        self.theItems = [None]*Stack.DEFAULT_CAPACITY
        self.size= 0
        self.top = -1


    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        if self.top == -1:  #or self.size == 0
            return True
        else:
            return False


    # Returns True if the stack is full or False otherwise.
    def isFull(self):
        return self.size == Stack.DEFAULT_CAPACITY


    # Returns the number of items in the stack.
    def __len__ (self):
        return self.size

       
    # Returns the top item on the stack without removing it.
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            return self.theItems[self.top]


    # Removes and returns the top item on the stack.
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            oldItem = self.theItems[self.top]
            self.top -= 1
            self.size -= 1
            return oldItem

    
    # Push an item onto the top of the stack.
    def push(self, item):
        if self.isFull():
            return "Stack is full!"
        else:
            self.top += 1
            self.theItems[self.top] = item
            self.size += 1
            
            
def main():

    s = Stack()


    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    print ("Popping items (top to bottom):", end = ' ')
    print (s.pop())


    print ('--------------------------------------')
    print ("Push 1-10")
    for i in range(10):
        s.push(i + 1)
    print ("Peeking:", s.peek()) 
    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    

    print ('--------------------------------------')
    print ("Push 11")
    s.push(11)
    print ("Popping items (top to bottom):", end = ' ')
    while not s.isEmpty():
        print (s.pop(), end = ' ')
    print ("\nLength:", len(s))
    print ("Empty:", s.isEmpty())    

main()
