class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle base cases
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        # Binary search for the square root
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            # Check if mid squared is equal to x
            if mid * mid == x:
                return mid
            # If mid squared is less than x, search in the right half
            elif mid * mid < x:
                left = mid + 1
            # If mid squared is greater than x, search in the left half
            else:
                right = mid - 1
        
        # Return the floor value of the square root
        return right

        