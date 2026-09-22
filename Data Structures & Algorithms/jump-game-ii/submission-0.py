class Solution:
    def jump(self, nums: List[int]) -> int:
        
        mini = float("inf")
        dp = {}

        def dfs(i, count):
            nonlocal mini

            if(i in dp):
                return dp[i]
           
            if(i >= len(nums) - 1):
                mini = min(mini, count)
                return

            for jump in range(nums[i], 0, -1):
                dp[i] = count + 1
                dfs(i + jump, count + 1)

        dfs(0, 0)

        return mini

        