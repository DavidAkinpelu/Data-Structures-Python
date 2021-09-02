from typing import Any
from math import floor
import sys

class Heap:

    """
    Heap class for a Heap data structure

    Atrributes:
    max_size (int): maximum heap size
    size (int): current heap size
    array (list): input list
    k (int): max number of children for each node
    """

    def __init__(self, max_size, k: int) -> None:
        """constructor"""
        self._array = [None]*max_size
        self._size = 0
        self._max_size = max_size
        self._k = k

    def get_size(self) -> None:
        """get the current size of the heap"""
        return self._size

    def _parent(self, n: int) -> None:
        """Parent of node at posiiton n"""
        return int(floor((n-1)/2))

    def heapify(self) -> None:
        """heapify all internal nodes starting from the last non-leaf
        node all the way to the root node and calling restore down on each"""
        i = self.size

        while i <=0:
            self.restore_down(i)
            i -=1

    def extract_min(self) -> int:
        """ extract minimum val i.e root node"""
        min_val = self._array[0]

        self._array[0] = self._array[self._size-1]

        self._size -= 1

        self.restore_down(0)

        return min_val

    def insert(self, val: Any) -> None:
        """insert a new node"""
        self._array[self._size] = val

        self._size += 1

        self.restore_up(self._size-1)
        return

    def restore_down(self, index: int) -> None:
        """re-organize heap from up to down"""

        while index <=self._size/self._k:
            child = []
            for i in range(self._k):
                if self._k * index + i <= self._size:
                    child.append(self._k*index + i)

            min_child = sys.maxsize

            for i in range(len(child)):
                if self._array[child[i]] < min_child:
                    min_child_index = child[i]
                    min_child = self._array[child[i]]

            if min_child >= self._array[index]:
                break

            if self._array[index] > self._array[min_child_index]:
                temp = self._array[index]
                self._array[index] = self._array[min_child_index]
                self._array[min_child_index] = temp

            index = min_child_index


    def restore_up(self, index: int) ->None:
        """re-organize heap from down to up"""
        parent = self._parent(index)

        while parent >=0:
            if self._array[index] < self._array[parent]:
                temp = self._array[index]
                self._array[index] = self._array[parent]
                self._array[parent] = temp
                index = parent
                parent = self._parent(index)

            else:
                break

min_heap = Heap(20, 2)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(13)
min_heap.insert(59)
min_heap.insert(28)
min_heap.insert(45)
min_heap.insert(18)
min_heap.insert(33)
min_heap.insert(61)
print(min_heap.extract_min())
