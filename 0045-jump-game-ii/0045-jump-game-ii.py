class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        jumps = 1
        curr_max_reach = nums[0]
        max_reach = nums[0]
        
        for i in range(1, len(nums)):
            if i > curr_max_reach:
                jumps += 1
                curr_max_reach = max_reach
            max_reach = max(max_reach, i + nums[i])
        
        return jumps
