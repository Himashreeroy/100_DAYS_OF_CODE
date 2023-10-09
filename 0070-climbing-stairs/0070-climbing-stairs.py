class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize an array to store the number of ways to climb each step
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # Calculate the number of ways to climb each step using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the number of ways to climb n steps
        return dp[n]
