class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        cheap = float('inf')

        dp = []
        for x in prices:
            cheap = min(cheap, x)
            profit = max(profit, x - cheap)
        return profit
            