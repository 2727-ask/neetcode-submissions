class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        maxlen = 1
        dp = set(nums)
        for x in nums:
            if x - 1 not in dp:
                c = 1
                start = x
                while(start + 1 in dp):
                    c = c + 1
                    start = start + 1
                    maxlen = max(maxlen, c)
        return maxlen


        