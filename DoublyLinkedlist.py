from typing import Any

class Node:

    """ Node class for a Doubly linkedlist data structure"""

    def __init__(self, data: Any):
        """
        Constructor for a node object
        Arguments
            data (Any): data
            prev(Node): points to the previous node object
            next(Node): points to the next node object
        """
        self.data = data
        self.next = None


class DoublyLinkedlist:
    """DoublyLinkedlist data structure class """

    def __init__(self):
        """
        Constructor for a doublyLinkedlist object
        Arguments
            head (Node): head
            tail (Node): tail
            size (int): size of the doublyLinkedlist
        """
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        """Check if doubly linkedlist is empty.
        Returns True if empty and False if otherwise """
        if self.head is None:
            return True
        else:
            return False

    def getSize(self):
        """Returns size of List"""
        return self.size

    def insertFirst(self, data: Any):
        """insert a new node at the beginning of the doublyLinkedList"""
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            temp.next.prev = temp
            self.head = temp
        self.size+=1

    def insertEnd(self, data: Any):
        """insert a new node at the end of the doublyLinkedList"""
        temp = Node(data)
        if self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            temp.prev = self.tail
            temp.prev.next= temp
            self.tail = temp
        self.size+=1

    def insertAfter(self,  data: Any, prevdata: Any):
        """Insert a new node next to a Node with prevdata"""
        temp = Node(data)
        prevnode = self.head
        while prevnode.data != prevdata:
                prevnode = prevnode.next
        temp.next = prevnode.next
        temp.prev = prevnode
        prevnode.next.prev = temp
        prevnode.next = temp
        self.size+=1

    def deleteFirst(self):
        """Delete the node at the beginning of the doublyLinkedList"""
        if self.head is None:
            print("empty list")
        elif self.head == self.tail:
            output = self.head.data
            self.head = None
            self.tail = None
        else:
            output = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
        self.size-=1
        return output

    def deleteLast(self):
        """Delete the node at the end of the doublyLinkedList"""
        if self.tail is None:
            print("empty list")
        elif self.tail == self.head:
            output = self.tail.data
            self.head = None
            self.tail = None
        else:
            output = self.tail.data
            self.tail.prev.next = None
            self.tail = self.head.prev
        self.size-=1
        return output

    def delete(self, data: Any):
        """delete the Node with data"""
        if self.isEmpty():
            print("Empty list")
        else:
            if self.head.data == data:
                self.deleteFirst()
                return
            elif self.tail.data == data:
                self.deleteLast()
                return
            else:
                temp = self.head
                while temp.data != data:
                    temp = temp.next
                output = temp.data
                temp.prev.next = temp.next
                self.size-=1
                return output

    def search(self, data: Any):
        """Search for data in doubly linkedlist"""
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    return True
                temp = temp.next

            return False

    def printDoublyLinkedList(self):
        """Print all the data in the doubly linkedlist"""
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


myList = DoublyLinkedlist()
myList.insertFirst(10)
myList.insertFirst(33)
myList.insertEnd(47)
myList.insertEnd(2)
myList.insertAfter(82, 33)
print(myList.delete(10))
print(myList.deleteFirst())
print(myList.deleteLast())
print(myList.search(100))
myList.printDoublyLinkedList()
