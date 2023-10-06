
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first pair of adjacent numbers where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If no such pair is found, reverse the array
        if i == -1:
            nums.reverse()
            return
        
        # Step 3: Find the first number larger than nums[i] from the right end
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 4: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: Reverse the subarray to the right of index i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
