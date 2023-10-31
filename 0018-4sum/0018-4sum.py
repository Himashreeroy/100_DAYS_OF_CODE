class Solution:
    def fourSum(self, nums, target):
        def kSum(nums, target, k, start, end):
            result = []
            if k == 2:
                while start < end:
                    current_sum = nums[start] + nums[end]
                    if current_sum == target:
                        result.append([nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif current_sum < target:
                        start += 1
                    else:
                        end -= 1
                return result
            else:
                for i in range(start, end - k + 2):
                    if i == start or (i > start and nums[i] != nums[i - 1]):
                        sub_results = kSum(nums, target - nums[i], k - 1, i + 1, end)
                        for sub_result in sub_results:
                            result.append([nums[i]] + sub_result)
                return result

        nums.sort()
        return kSum(nums, target, 4, 0, len(nums) - 1)

# Example usage:
solution = Solution()
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
result1 = solution.fourSum(nums1, target1)
print(result1)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

nums2 = [2, 2, 2, 2, 2]
target2 = 8
result2 = solution.fourSum(nums2, target2)
print(result2)  # Output: [[2, 2, 2, 2]]
