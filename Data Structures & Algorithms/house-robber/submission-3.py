class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i):
            if(i in dp):
                return dp[i]

            if i >= len(nums):
                return 0
            
            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            ans = max(take, skip)
            dp[i] = ans
            return ans
        
        return dfs(0)