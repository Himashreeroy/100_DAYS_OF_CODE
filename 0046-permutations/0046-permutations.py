from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == len(nums):
                # If all elements are used, add the permutation to the result
                result.append(nums[:])
                return
            for i in range(first, len(nums)):
                # Swap the current element with the first element in the remaining elements
                nums[first], nums[i] = nums[i], nums[first]
                # Recur with the next index
                backtrack(first + 1)
                # Undo the swap to backtrack and try other permutations
                nums[first], nums[i] = nums[i], nums[first]
        
        result = []
        backtrack(0)
        return result

# Example usage
sol = Solution()
nums1 = [1, 2, 3]
nums2 = [0, 1]
nums3 = [1]

print(sol.permute(nums1))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(sol.permute(nums2))  # Output: [[0, 1], [1, 0]]
print(sol.permute(nums3))  # Output: [[1]]
