from typing import Any

class QueueNode:

    """ QueueNode class for Queue data structure using double linkedlist"""

    def __init__(self, data: Any):
        """
        Constructor for a QueueNode object
        Arguments
            data (Any): data
            prev (QueueNode): points to the previous QueueNode object
            next(QueueNode): points to the next QueueNode object
        """
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    """Queue data structure class """

    def __init__(self):
        """
        Constructor for a Queue object
        Arguments
            head (QueueNode): points to the head node
            rear (QueueNode): points to the rear node
            size (int): size of the Queue
        """
        self.head = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        """Check if queue is empty.
        Returns True if empty and False if otherwise """
        if self.head is None:
            return True
        else:
            return False

    def getSize(self):
        """Returns size of queue"""
        return self.size

    def enqueue(self, data: Any):
        """Push a new element to the queue"""
        if self.rear is None:
            self.head = QueueNode(data)
            self.rear = self.head
        else:
            temp = QueueNode(data)
            self.rear.next = temp
            temp.prev = self.rear
            self.rear = temp
        self.size+=1

    def dequeue(self):
        """Pop the first element"""
        if self.isEmpty():
            print("Empty queue")
        else:
             temp = self.head.data
             self.head = self.head.next
             self.head.prev = None
             self.size-=1
             return temp

    def peek(self):
        """Returns the first data in the queue"""
        if self.isEmpty():
            print("Empty queue")
        else:
            return self.head.data

    def printQueue(self):
        """Print all the data in the queue"""
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


myQueue = Queue()
myQueue.enqueue(14)
myQueue.enqueue(50)
myQueue.enqueue(2)
print(myQueue.peek())
myQueue.dequeue()
myQueue.enqueue(88)
print(myQueue.getSize())
myQueue.printQueue()
