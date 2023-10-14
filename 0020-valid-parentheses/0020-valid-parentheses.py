class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}  # Mapping of closing to opening brackets
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'  # Use '#' to handle empty stack
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack  # If the stack is empty, all brackets were closed properly, so it's valid
