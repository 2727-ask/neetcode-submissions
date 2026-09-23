class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)

        queue = deque([])
        queue.append((1, beginWord))

        while queue:
            count, pop = queue.popleft()
            for i in range(len(pop)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = pop[:i] + ch + pop[i+1:]
                    if(newWord == endWord):
                        return count + 1
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((count + 1, newWord))
        return 0

