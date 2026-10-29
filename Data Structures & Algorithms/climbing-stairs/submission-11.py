class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        ans = 0

        if n <= 2:
            return n
        
        for step in range(2, n):
            ans = first + second
            first = second 
            second = ans
        
        return ans

        
