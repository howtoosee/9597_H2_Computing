# Implementation of the Stack ADT using a singly linked list.

# The private storage class for creating stack nodes.
class StackNode :
    def __init__(self, item, link) :
        self.item = item
        self.next = link

class Stack() :
    """ Link-based stack implementation."""
    
    # Creates an empty stack.
    def __init__(self):
        self.top = None
        self.size = 0


    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return self.top == None


    # Returns the number of items in the stack.
    def __len__(self):
        return self.size


    # Returns the top item on the stack without removing it.
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            node = self.top
            return node.item


    # Removes and returns the top item on the stack.
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.item


    # Pushes an item onto the top of the stack.
    def push(self, item):
        self.top = StackNode(item, self.top)
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

