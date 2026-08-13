class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit = 0, 0
        right = 1

        if len(prices) < 2:
            return 0

        while right < len(prices):
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
                right = right +1

            else:
                right = right +1

        return max_profit

        