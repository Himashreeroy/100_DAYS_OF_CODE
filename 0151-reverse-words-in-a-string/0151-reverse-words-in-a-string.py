class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words using space as the delimiter
        words = s.split()

        # Reverse the order of the words
        words = words[::-1]

        # Join the reversed words with a single space between them
        reversed_s = ' '.join(words)

        return reversed_s
