class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack  # If the stack is empty, it's valid; otherwise, it's not.

# Example usage:
solution = Solution()
print(solution.isValid("()"))          # Output: True
print(solution.isValid("()[]{}"))      # Output: True
print(solution.isValid("(]"))          # Output: False
