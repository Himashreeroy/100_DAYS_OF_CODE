class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Create a table to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]
