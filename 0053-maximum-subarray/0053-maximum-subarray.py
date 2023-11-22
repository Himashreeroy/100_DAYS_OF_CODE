from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            # Choose the maximum of the current number and the running sum plus the current number
            current_sum = max(num, current_sum + num)
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example usage:
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(solution.maxSubArray([1]))                       # Output: 1
print(solution.maxSubArray([5,4,-1,7,8]))               # Output: 23
