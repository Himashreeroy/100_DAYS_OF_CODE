class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product_ending_here = nums[0]
        min_product_ending_here = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product_ending_here, min_product_ending_here = min_product_ending_here, max_product_ending_here

            max_product_ending_here = max(nums[i], max_product_ending_here * nums[i])
            min_product_ending_here = min(nums[i], min_product_ending_here * nums[i])

            max_product = max(max_product, max_product_ending_here)

        return max_product
