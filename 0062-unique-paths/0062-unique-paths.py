class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp array with all elements set to 1
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The bottom-right cell contains the number of unique paths
        return dp[m-1][n-1]
