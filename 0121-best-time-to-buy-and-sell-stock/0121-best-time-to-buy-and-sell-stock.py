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

        for price in prices[1:]:
            # Update the minimum price
            min_price = min(min_price, price)
            # Update the maximum profit
            max_profit = max(max_profit, price - min_price)

        return max_profit