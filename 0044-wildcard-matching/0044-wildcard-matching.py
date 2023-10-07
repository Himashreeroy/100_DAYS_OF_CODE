class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D DP table with False values
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty pattern matches empty string
        
        # Fill the first row of the DP table
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' can match either 0 characters or 1 or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or characters match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[len(s)][len(p)]

# Example usage
sol = Solution()
s1, p1 = "aa", "a"
s2, p2 = "aa", "*"
s3, p3 = "cb", "?a"

print(sol.isMatch(s1, p1))  # Output: False
print(sol.isMatch(s2, p2))  # Output: True
print(sol.isMatch(s3, p3))  # Output: False

        