class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
        
        # Base case: strings of length 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        
        # Check for all lengths starting from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if (dp[k][i][j] and dp[length - k][i + k][j + k]) or \
                           (dp[k][i][j + length - k] and dp[length - k][i + k][j]):
                            dp[length][i][j] = True
                            break
        
        return dp[n][0][0]
