class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for price in prices[1:]:
            # Calculate potential profit by selling at the current price
            potential_profit = price - min_price
            
            # Update max profit if the potential profit is greater
            max_profit = max(max_profit, potential_profit)
            
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
        
        return max_profit
