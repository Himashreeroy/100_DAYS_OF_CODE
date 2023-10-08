class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip leading and trailing spaces, split the string by spaces, and return the length of the last word
        words = s.strip().split()
        return len(words[-1])
