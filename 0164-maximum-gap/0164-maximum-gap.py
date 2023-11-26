from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # Helper function for Radix Sort
        def radix_sort(nums):
            # Find the maximum number to know the number of digits
            max_num = max(nums)
            exp = 1
            
            while max_num // exp > 0:
                counting_sort(nums, exp)
                exp *= 10
            
        # Helper function for Counting Sort
        def counting_sort(nums, exp):
            n = len(nums)
            output = [0] * n
            count = [0] * 10
            
            for i in range(n):
                index = nums[i] // exp
                count[index % 10] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            i = n - 1
            while i >= 0:
                index = nums[i] // exp
                output[count[index % 10] - 1] = nums[i]
                count[index % 10] -= 1
                i -= 1
            
            for i in range(n):
                nums[i] = output[i]
        
        # Perform Radix Sort on the input array
        radix_sort(nums)
        
        # Find the maximum gap
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        
        return max_gap

# Example usage:
solution = Solution()
print(solution.maximumGap([3, 6, 9, 1]))  # Output: 3
print(solution.maximumGap([10]))          # Output: 0
