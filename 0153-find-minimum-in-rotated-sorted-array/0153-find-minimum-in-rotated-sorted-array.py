class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If the mid element is greater than the rightmost element, the minimum is on the right side.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is less than the rightmost element, the minimum is on the left side.
            elif nums[mid] < nums[right]:
                right = mid
            # If the mid element is equal to the rightmost element, it's safe to decrement right.
            else:
                right -= 1

        return nums[left]
