class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        # If the sum of the lengths of s1 and s2 is not equal to the length of s3, it's impossible to interleave
        if len_s1 + len_s2 != len_s3:
            return False
        
        # dp[i][j] is True if the first i characters of s1 and the first j characters of s2 can form the first i+j characters of s3
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        dp[0][0] = True
        
        # Fill the first row
        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the first column
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill the rest of the dp table
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len_s1][len_s2]
