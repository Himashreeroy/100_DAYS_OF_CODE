class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the elements and their indices
        num_dict = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement needed to achieve the target sum
            complement = target - num
            
            # If the complement is in the dictionary, return its index and the current index
            if complement in num_dict:
                return [num_dict[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = index

            