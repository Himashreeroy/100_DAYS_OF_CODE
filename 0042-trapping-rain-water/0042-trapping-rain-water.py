from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Initialize left and right pointers
        left_max = right_max = trapped_water = 0
        
        while left < right:
            # Update left_max and right_max if the current height is greater
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # Calculate trapped water based on the smaller of left_max and right_max
            if left_max < right_max:
                trapped_water += left_max - height[left]
                left += 1
            else:
                trapped_water += right_max - height[right]
                right -= 1
        
        return trapped_water

# Example usage
sol = Solution()
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]

print(sol.trap(height1))  # Output: 6
print(sol.trap(height2))  # Output: 9

        