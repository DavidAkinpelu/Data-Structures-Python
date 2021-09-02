from typing import Any, Tuple

class HashNode:

    """ HashNode class for hashmap structure using linkedlist"""

    def __init__(self, key: str, val: Any):
        """
        Constructor for a hashnode object
        Arguments:
          val (Any): data
          key (str): key
          next(hashNode): points to a stacknode objects
        """
        self.key = key
        self.val = val
        self.next = None

class Hashmap:
    """Hashmap data structure"""

    def __init__(self, size: int) -> None:
        """ Constructor for a hashmap object
        Argument:
          size (int): size of hashmap
        """
        self.size = size
        self.buckets = []
        for _ in range(self.size):
            self.buckets.append(HashNode("", None))

    def hash(self, key: str) -> int:
        """Hash key and retruns the index"""
        hashval = 0
        for idx, char in enumerate(key):
            hashval += (idx + len(key)) ** ord(char)
            hashval= hashval % self.size
            return hashval

    def insert(self, key: str, val: Any) -> None:
        """insert key and value to hashmap"""
        index = self.hash(key)
        current = self.buckets[index]
        if current:
            self.buckets[index] = HashNode(key, val)
            return

        while current is not None:
            current = current.next

        current.node = HashNode(key, val)

    def search(self, key: str) -> Any:
        """search for key in Hashmap returns val if present"""
        index = self.hash(key)
        current = self.buckets[index]

        if current is None:
            return

        while current is not None and current.key !=key:
            current = current.next

        return current.val

    def remove(self, key: str) -> Any:
        """delete val mapped to a specified val if key exists"""
        index = self.hash(key)
        current = self.buckets[index]

        if current is None:
            return

        prev = None
        while current is not None and current.key != key:
            prev = current
            current = current.next

        output = current.val
        if prev is None:
            self.buckets[index] = None
        else:
            prev.next = prev.next.next
        return output


hashobj = Hashmap(10)
hashobj.insert('milk', 2)
hashobj.insert('tea', 4)
hashobj.insert('sugar', 10)
hashobj.insert('coffee', "starbucks")
print(hashobj.remove('tea'))
print(hashobj.search('sugar'))
print(hashobj.search('tea'))
