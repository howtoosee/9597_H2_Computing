# Implementation of the Queue ADT using a singly linked list.


class Node(object):
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""

        self.data = data
        self.next = next
        
        

class Queue(object):
    """ Link-based queue implementation."""

    def __init__(self):

        self.front = None
        self.rear = None
        self.size = 0



    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""

        newNode = Node(newItem, None)

        if self.size == 0:
            self.front = newNode
        else:
            self.rear.next = newNode
        
        self.rear = newNode
        self.size += 1



    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""

        if self.isEmpty():
            return "Queue is empty!"
        else:
            oldItem = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None

        self.size -= 1        
        return oldItem



    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""

        if self.isEmpty():
            return "Queue is empty!"
        else:
            return self.front.data


      
    def __len__(self):
        """Returns the number of items in the queue."""

        return self.size



    def isEmpty(self):

        return self.size == 0

       

    def __str__(self):
        """Items strung from front to rear."""

        result = ""
        probe = self.front

        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next

        return result
        

       
#------------------------------------------------------------------#

def main():
    q = Queue()
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())
    print ("Enqueue 1-10")
    for i in range(10):
        q.enqueue(i + 1)
    print ("Peeking:", q.peek())
    print ("Items (front to rear):", q)
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())
    print ("Enqueue 11")
    q.enqueue(11)
    print ("Dequeuing items (front to rear):", end = ' ')
    while not q.isEmpty(): print (q.dequeue(), end = ' ')
    print ("\nLength:", len(q))
    print ("Empty:", q.isEmpty())
    input('\nPlease press Enter or Return to quit the program.')

main()
