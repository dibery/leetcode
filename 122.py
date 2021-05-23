class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(i for i in [prices[i + 1] - prices[i] for i in range(len(prices) - 1)] if i > 0)
