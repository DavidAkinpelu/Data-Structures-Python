from typing import Any

class Node:

    """ Node class for a circular singly linkedlist data structure"""

    def __init__(self, data: Any):
        """
        Constructor for a node object
        Arguments
            data (Any): data
            next(Node): points to a node objects
        """
        self.data = data
        self.next = None


class CircularSinglyLinkedlist:
    """Circular singlyLinkedlist data structure class """

    def __init__(self):
        """
        Constructor for a circular singly Linkedlist object
        Arguments
            head (Node): head node
            tail (Node): tail node
            size (int): size of the SinglyLinkedlist
        """
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        """Check if circular singly linkedlist is empty.
        Returns True if empty and False if otherwise """
        if self.head is None:
            return True
        else:
            return False

    def getSize(self):
        """Returns size of List"""
        return self.size

    def insertFirst(self, data: Any):
        """insert a new node at the beginning of the circular singlyLinkedList"""
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
            self.tail.next = self.head
        else:
            temp.next = self.head
            self.head = temp
            self.tail.next = self.head
        self.size+=1

    def insertEnd(self, data: Any):
        """insert a new node at the end of the circular singlyLinkedList"""
        temp = Node(data)
        if self.tail is None:
            self.head = temp
            self.tail = temp
            self.tail.next = self.head
        else:
            self.tail.next = temp
            self.tail = temp
            self.tail.next = self.head
        self.size+=1

    def insertAfter(self,  data: Any, prevdata: Any):
        """Insert a new node next to a Node with prevdata"""
        temp = Node(data)
        if self.tail.data == prevdata:
            self.insertEnd(data)
        else:
            prevnode = self.head
            while prevnode.data != prevdata:
                prevnode = prevnode.next
            temp.next = prevnode.next
            prevnode.next = temp
        self.size+=1

    def delete(self, data: Any):
        """delete the Node with data"""
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head
            if temp.data == data:
                output = self.head.data
                self.head = temp.next
                self.tail.next = self.head
            else:
                while temp.next.data != data:
                    temp = temp.next
                output = temp.next.data
                temp.next = temp.next.next
                if self.tail.data == data:
                    self.tail = temp
                    self.tail.next = self.head
            self.size-=1
            return output

    def search(self, data: Any):
        """Search for data in circualr singly linkedlist"""
        if self.isEmpty():
            print("Empty list")
        else:
            if self.head.data == data:
                return True
            elif self.tail.data == data:
                return True
            else:
                temp = self.head.next
                while temp.next != self.head:
                    if temp.data == data:
                        return True
                    temp = temp.next

                return False

    def printList(self):
        """Print all the data in the circualr singly linkedlist"""
        print(self.head.data)
        currentNode = self.head.next
        while currentNode !=  self.head:
            print(currentNode.data)
            currentNode = currentNode.next


myList = CircularSinglyLinkedlist()
myList.insertFirst(10)
myList.insertFirst(33)
myList.insertEnd(47)
myList.insertEnd(2)
myList.insertAfter(82, 33)
myList.insertAfter(15, 2)
print(myList.delete(10))
print(myList.search(10))
print(myList.search(82))
myList.printList()