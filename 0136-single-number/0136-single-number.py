class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        # XOR all elements in the array
        for num in nums:
            result ^= num
        
        return result
