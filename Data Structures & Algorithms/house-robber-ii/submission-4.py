class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        dp = {}
        
        def dfs(i,end):
            if((i, end) in dp):
                return dp[(i, end)]

            if(i >= end or i >= len(nums)):
                return 0

            rob = nums[i] + dfs(i+2, end)
            skip = dfs(i+1, end)


            ans = max(rob, skip)
            dp[(i, end)] = ans
            return dp[(i, end)]

        
        take = dfs(0, len(nums)-1)
        skip = dfs(1, len(nums))

        return max(take, skip)
