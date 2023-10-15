class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case: if n is 0, return 1
        if n == 0:
            return 1
        
        # If n is negative, calculate reciprocal of x and negate n
        if n < 0:
            x = 1 / x
            n = -n
        
        # Initialize the result to 1
        result = 1
        
        # Perform exponentiation by squaring
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            # Square x and halve n
            x *= x
            n //= 2
        
        return result
