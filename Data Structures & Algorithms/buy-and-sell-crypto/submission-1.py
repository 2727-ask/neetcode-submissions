class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = float('inf')
        profit = 0

        for i in range(len(prices)):
            if(prices[i] < cheapest_price):
                cheapest_price = prices[i]
            else:
                profit = max(profit,prices[i] - cheapest_price)
        return profit