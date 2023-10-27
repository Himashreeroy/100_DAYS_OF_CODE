class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store the index of each character in the string
        char_index = {}
        # Initialize pointers for the start and end of the sliding window
        start = 0
        max_length = 0
        
        # Iterate through the string using the end pointer
        for end in range(len(s)):
            # If the current character is in the dictionary and its index is greater than or equal to the start pointer,
            # move the start pointer to the right of the last occurrence of the character
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            # Update the index of the current character in the dictionary
            char_index[s[end]] = end
            # Update the maximum length of the substring without repeating characters
            max_length = max(max_length, end - start + 1)
        
        return max_length
