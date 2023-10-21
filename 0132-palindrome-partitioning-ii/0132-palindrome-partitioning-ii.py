class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        # Fill the is_palindrome table to check if substrings are palindromes
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2 and s[i] == s[j]:
                    is_palindrome[i][j] = True
                elif s[i] == s[j] and is_palindrome[i+1][j-1]:
                    is_palindrome[i][j] = True

        # Calculate minimum cuts using dynamic programming
        min_cuts = [0] * n
        for j in range(1, n):
            min_cuts[j] = j
            for i in range(j, -1, -1):
                if is_palindrome[i][j]:
                    min_cuts[j] = 0 if i == 0 else min(min_cuts[j], min_cuts[i - 1] + 1)

        return min_cuts[n - 1]
