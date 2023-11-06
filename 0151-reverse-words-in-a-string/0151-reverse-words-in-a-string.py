class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the input string into words
        reversed_words = words[::-1]  # Reverse the order of words
        result = ' '.join(reversed_words)  # Join the reversed words with a single space
        return result
if __name__ == "__main__":
    obj = Solution()
    s1 = "the sky is blue"
    s2 = "  hello world  "
    s3 = "a good   example"

    result1 = obj.reverseWords(s1)
    result2 = obj.reverseWords(s2)
    result3 = obj.reverseWords(s3)

    print(result1)  # Output: "blue is sky the"
    print(result2)  # Output: "world hello"
    print(result3)  # Output: "example good a"
