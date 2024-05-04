class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        less = float("inf")
        max_profit = 0
        for price in prices:
            less = min(less, price)
            max_profit = max(max_profit, price - less)
        return max_profit
