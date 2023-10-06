class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)  # Initialize the stack with -1 to handle edge cases
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # Pop the top element (either '(' or -1)
                if len(stack) != 0:
                    # If stack is not empty, calculate the length of the current valid parentheses substring
                    max_length = max(max_length, i - stack[-1])
                else:
                    # If stack is empty, push the current index to indicate the start of a new valid substring
                    stack.append(i)
        
        return max_length

        