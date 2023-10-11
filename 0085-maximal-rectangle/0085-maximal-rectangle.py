class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        heights = [0] * len(matrix[0])
        max_area = 0
        
        for row in matrix:
            for i in range(len(row)):
                # Update the heights array based on the current row
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            stack = []
            for i, h in enumerate(heights + [0]):
                # While the stack is not empty and the current height is less than the height at the top of the stack
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        
        return max_area
