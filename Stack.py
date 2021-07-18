from typing import Any

class StackNode:

    """ StackNode class for stack data structure using linkedlist"""

    def __init__(self, data: Any):
        """
        Constructor for a stacknode object
        Arguments
            data (Any): data
            next(StackNode): points to a stacknode objects
        """
        self.data = data
        self.next = None


class Stack:
    """Stack data structure class """

    def __init__(self):
        """
        Constructor for a stack object
        Arguments
            top (StackNode): head pointer
            size (int): size of the stack
        """
        self.top = None
        self.size = 0

    def isEmpty(self):
        """Check if stack is empty.
        Returns True if empty and False if otherwise """
        if self.top is None:
            return True
        else:
            return False

    def getSize(self):
        """Returns size of stack"""
        return self.size

    def push(self, data: Any):
        """Push a new element to the stack"""
        temp = StackNode(data)
        temp.next = self.top
        self.top = temp
        self.size+=1

    def pop(self):
        """Pop the top element"""
        if self.isEmpty():
            print("Empty stack")
        else:
            temp = self.top
            self.top = self.top.next
            self.size-=1
            return temp.data

    def peek(self):
        """Returns the data at the top of the stack"""
        if self.isEmpty():
            print("Empty stack")
        else:
            return self.top.data

    def printStack(self):
        """Print all the data in the stack"""
        currentNode = self.top
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

myStack = Stack()
myStack.push(14)
myStack.push(50)
myStack.push(2)
myStack.peek()
myStack.pop()
myStack.push(88)
print(myStack.getSize())
myStack.printStack()

