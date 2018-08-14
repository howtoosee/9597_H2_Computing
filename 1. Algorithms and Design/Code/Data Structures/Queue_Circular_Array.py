# Implementation of the Queue ADT (circular_queue) using an array.


class Queue(object):
    """ Array-based queue implementation (circular_queue)"""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        self.items = [None] * Queue.DEFAULT_CAPACITY
        self.rear = -1
        self.front = 0
        self.size = 0


    def enqueue(self, newItem):
        """Adds newItem to the rear of queue.
        Precondition: the queue is not full."""
       
        if self.isFull():
           print("Queue is full!")
           return ''
        else:
            if self.rear == self.DEFAULT_CAPACITY - 1:  #end of array
                self.rear = 0
            else:
                self.rear += 1
            
            self.items[self.rear] = newItem
            self.size += 1


    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""

        if self.isEmpty():
            print("Queue is empty!")
            return ''
        else:
            oldItem = self.items[self.front]
            
            if self.front == self.DEFAULT_CAPACITY - 1: #end of array
                self.front = 0
            else:
                self.front += 1 #move pointer to point to next element

            self.size -= 1
            return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        
        if self.isEmpty():
            print("Queue is empty!")
            return ''
        else:
            return self.items[self.front]


    def __len__(self):
        """Returns the number of items in the queue."""

        return self.size


    def isEmpty(self):
        return self.size == 0


    def isFull(self):
        return self.size == self.DEFAULT_CAPACITY

       
    def __str__(self):
        """Items strung from front to rear."""
        
        result = ""
        temp = self.front
        
        for index in range(self.size):
            result += str(self.items[temp]) + " "
            if temp == Queue.DEFAULT_CAPACITY -1:   #end of array
                temp = 0
            else:
                temp += 1

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
