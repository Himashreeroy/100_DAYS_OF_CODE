class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left_to_right = [1] * n
        right_to_left = [1] * n
        
        # Traverse from left to right and assign candies to children
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] = left_to_right[i - 1] + 1
        
        # Traverse from right to left and update candies if necessary
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1
        
        # Calculate the total candies required
        total_candies = 0
        for i in range(n):
            total_candies += max(left_to_right[i], right_to_left[i])
        
        return total_candies
