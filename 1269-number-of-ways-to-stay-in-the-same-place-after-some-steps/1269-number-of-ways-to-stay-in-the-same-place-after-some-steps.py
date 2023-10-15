class Solution(object):
    MOD = 10**9 + 7
    
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        maxPos = min(arrLen - 1, steps)
        dp = [[0] * (maxPos + 1) for _ in range(steps + 1)]
        dp[0][0] = 1
        
        for i in range(1, steps + 1):
            for j in range(maxPos + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % self.MOD
                if j < maxPos:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % self.MOD
        
        return dp[steps][0]

# Example usage
solution = Solution()
print(solution.numWays(3, 2))  # Output: 4
print(solution.numWays(2, 4))  # Output: 2
print(solution.numWays(4, 2))  # Output: 8
