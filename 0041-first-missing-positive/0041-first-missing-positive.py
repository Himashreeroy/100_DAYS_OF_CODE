from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # Place each number at its correct position if it's a positive integer and within the range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first index where nums[i] != i + 1, indicating the missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers in the range [1, n] are present, the missing one is n + 1
        return n + 1

# Example usage
sol = Solution()
nums1 = [1, 2, 0]
nums2 = [3, 4, -1, 1]
nums3 = [7, 8, 9, 11, 12]

print(sol.firstMissingPositive(nums1))  # Output: 3
print(sol.firstMissingPositive(nums2))  # Output: 2
print(sol.firstMissingPositive(nums3))  # Output: 1
