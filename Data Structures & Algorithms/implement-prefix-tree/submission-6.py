class PrefixTree:

    def __init__(self):
        self.trie = defaultdict(dict)
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if(curr.get(char)):
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        curr["word"] = True
        # print(self.trie)


    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if(not curr.get(char)):
                return False
            else:
                curr = curr.get(char)
        print(curr)
        if(curr.get('word')):
            return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if(not curr.get(char)):
                return False
            else:
                curr = curr.get(char)
        return True
        
        