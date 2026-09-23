class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for i, x in enumerate(s):
            counter[x] = i
        
        res = []
        end = -1
        start = 0
        for i in range(len(s)):
            end = max(end, counter[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

        
            

