class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        print(d)
        large =-1
        for x, y in d.items():
            if(x == y):
                large = max(large, y)
        return large