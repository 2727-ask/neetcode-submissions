class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return nums[0]
        

        dp = {}

        def dfs(i, end):
            if(i in dp):
                return dp[i]

            if(i >= end):
                return 0

            take = nums[i] + dfs(i+2, end)
            skip = dfs(i+1, end)

            ans = max(take, skip)
            dp[i] = ans

            return ans
        
        takefirst = dfs(0, len(nums) - 1)
        dp = {}
        nottakefirst = dfs(1, len(nums))

        return max(takefirst, nottakefirst)


