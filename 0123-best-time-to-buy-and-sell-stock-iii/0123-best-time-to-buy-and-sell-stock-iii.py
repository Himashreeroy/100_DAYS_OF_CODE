class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        # Initialize variables to keep track of the minimum prices and maximum profits.
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0

        for price in prices:
            # Update the first buy and profit variables.
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)

            # Update the second buy and profit variables.
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2

# Example usage:
# Create an instance of the Solution class and call maxProfit with your input prices.
solution = Solution()
prices = [3,3,5,0,0,3,1,4]
print(solution.maxProfit(prices))  # Output: 6
