class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        max_profit = 0
        
        for i in range(1, len(prices)):
            # If the current price is greater than the previous day's price, accumulate the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
