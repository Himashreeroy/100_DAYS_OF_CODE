class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Convert wordDict into a set for faster lookup
        word_set = set(wordDict)
        n = len(s)
        # Initialize dp array with False values
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Iterate through the string
        for i in range(1, n + 1):
            # Check if the substring from 0 to i can be segmented
            for j in range(i):
                # If dp[j] is True (substring from 0 to j can be segmented)
                # and s[j:i] is in the wordDict, then dp[i] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        # dp[n] will be True if the entire string can be segmented
        return dp[n]
