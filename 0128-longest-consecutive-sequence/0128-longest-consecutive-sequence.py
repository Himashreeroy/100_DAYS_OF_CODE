class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # Check if num is the start of a new sequence
                current_num = num
                current_length = 1
                
                # Count consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length of the sequence
                max_length = max(max_length, current_length)
        
        return max_length
