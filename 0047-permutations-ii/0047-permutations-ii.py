from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, result):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # Explore permutations with the current number removed from nums
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], result)
        
        # Sort the input array to handle duplicates efficiently
        nums.sort()
        result = []
        backtrack(nums, [], result)
        return result

# Example usage
sol = Solution()
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]

print(sol.permuteUnique(nums1))
# Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

print(sol.permuteUnique(nums2))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        