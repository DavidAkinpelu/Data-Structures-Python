from typing import Any

class TrieNode:

    """ Node class for a Trie data structure

    Attributes:
    char (char): char.
    children (list): list of children.
    isEndofWord (bool): True if Node is the end of the word.
    """

    def __init__(self, char: str) -> None:
        """
        Constructor for a node object
        Argument:
            char (char): char
        """
        self.char = char
        self.children = [None]*26
        self.isEndofWord = True

class Trie:
    """
    Trie data structure for text matching
    """

    def __init__(self) -> None:
        """constructor"""
        self.root = TrieNode("")

    def _charToIndex(self, char: str) -> int:
        """convert char to integers"""
        char = char.lower()
        return ord(char)-ord('a')

    def insert(self, word) -> None:
        """insert word to a trie"""
        rootnode = self.root
        length = len(word)
        for char in word:
            index = self._charToIndex(char)

            if not rootnode.children[index]:
                rootnode.children[index] = TrieNode(char)

            rootnode = rootnode.children[index]

        rootnode.isEndofWord = True

    def search(self, word) -> bool:
        """Search for a word in a Trie"""
        rootnode = self.root
        length = len(word)
        for char in word:
            index = self._charToIndex(char)

            if not rootnode.children[index]:
                return False
            rootnode = rootnode.children[index]
        return rootnode.isEndofWord



keys = ["Trie", "Implementation", "In", "Python"]

# Trie object
t = Trie()

# Construct trie
for key in keys:
    t.insert(key)
print(t.search("Trie"))
print(t.search("strings"))
