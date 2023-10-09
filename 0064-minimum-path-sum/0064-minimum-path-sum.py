class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Create a 2D array to store minimum sum
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the top-left cell
        dp[0][0] = grid[0][0]
        
        # Initialize the first row
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Initialize the first column
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # Fill the dp table using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        # The bottom-right cell contains the minimum sum path
        return dp[m - 1][n - 1]

# Example usage
grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid2 = [[1, 2, 3], [4, 5, 6]]

sol = Solution()
print(sol.minPathSum(grid1))  # Output: 7
print(sol.minPathSum(grid2))  # Output: 12
