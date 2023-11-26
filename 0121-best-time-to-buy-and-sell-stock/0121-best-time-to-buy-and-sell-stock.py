class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            # Update the minimum price
            if prices[i] < min_price:
                min_price = prices[i]
            # Update the maximum profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit