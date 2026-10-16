class PrefixTree:

    class Node:
        def __init__(self, ch: str, end: bool=False):
            self.ch = ch 
            self.children = {}
            self.end = False

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root:
                root[char] = self.Node(ch=char)
            node = root[char]
            root = node.children
        node.end = True


    def search(self, word: str) -> bool:
        root = self.trie
        for char in word:
            node = root.get(char)
            if not node:
                return False
            root = node.children
        if node.end:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for char in prefix:
            node = root.get(char)
            if not node:
                return False
            root = node.children
        return True
        
        