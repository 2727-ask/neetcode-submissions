class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def dfs(n):

            if(n <= 3):
                return n
            
            if(n in  dp):
                return dp[n]
            
            dp[n] = dfs(n-1) + dfs(n-2)

            return dp[n]
        
        return dfs(n)

