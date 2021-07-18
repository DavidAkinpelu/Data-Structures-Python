from typing import Any

class Node:

    """ Node class for a singly linkedlist data structure"""

    def __init__(self, data: Any):
        """
        Constructor for a node object
        Arguments
            data (Any): data
            next(Node): points to a node objects
        """
        self.data = data
        self.next = None


class SinglyLinkedlist:
    """SinglyLinkedlist data structure class """

    def __init__(self):
        """
        Constructor for a SinglyLinkedlist object
        Arguments
            head (Node): head pointer
            size (int): size of the SinglyLinkedlist
        """
        self.head = None
        self.size = 0

    def isEmpty(self):
        """Check if singly linkedlist is empty.
        Returns True if empty and False if otherwise """
        if self.head is None:
            return True
        else:
            return False

    def getSize(self):
        """Returns size of List"""
        return self.size

    def insertFirst(self, data: Any):
        """insert a new node at the beginning of the singlyLinkedList"""
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.size+=1

    def insertEnd(self, data: Any):
        """insert a new node at the end of the singlyLinkedList"""
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        self.size+=1

    def insertAfter(self,  data: Any, prevdata: Any):
        """Insert a new node after a Node with prevdata"""
        temp = Node(data)
        prevnode = self.head
        while prevnode.data != prevdata:
                prevnode = prevnode.next
        temp.next = prevnode.next
        prevnode.next = temp
        self.size+=1

    def delete(self, data: Any):
        """delete data"""
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head
            if temp.data == data:
                output = self.head.data
                self.head = temp.next
            else:
                while temp.next.data != data:
                    temp = temp.next
                output = temp.next.data
                temp.next = temp.next.next
            self.size-=1
            return output

    def search(self, data: Any):
        """Search for data in singly linkedlist"""
        if self.isEmpty():
            print("Empty list")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    return True
                temp = temp.next

            return False

    def printSinglyLinkedList(self):
        """Print all the data in the singly linkedlist"""
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


myList = SinglyLinkedlist()
myList.insertFirst(10)
myList.insertFirst(33)
myList.insertEnd(47)
myList.insertAfter(82, 33)
print(myList.delete(10))
print(myList.search(100))
myList.printSinglyLinkedList()


