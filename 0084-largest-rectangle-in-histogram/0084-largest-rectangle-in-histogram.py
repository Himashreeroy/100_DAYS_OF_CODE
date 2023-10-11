class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        # Iterate through the heights list
        for i, h in enumerate(heights):
            # While the stack is not empty and the current height is less than the height at the top of the stack
            while stack and h < heights[stack[-1]]:
                # Pop the index from the stack and calculate the area with the popped height as the height
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            # Push the current index onto the stack
            stack.append(i)
        
        # Calculate the remaining areas for the heights left in the stack
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
 