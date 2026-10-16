class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            node = node.setdefault(char, {})
        
        node["is_word"] = True 



    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return "is_word" in node
            
            char = word[index]

            if char == ".":
                for key, child in node.items():
                    if key != "is_word" and dfs(index + 1, child):
                        return True
                return False

            
            if char not in node:
                return False 

            return dfs(index+1, node[char])
        
        return dfs(0, self.root)
        
