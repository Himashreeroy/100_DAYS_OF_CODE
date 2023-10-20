class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert the string to lowercase and remove non-alphanumeric characters
        clean_s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Use two pointers approach to check if the cleaned string is a palindrome
        left, right = 0, len(clean_s) - 1
        
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
