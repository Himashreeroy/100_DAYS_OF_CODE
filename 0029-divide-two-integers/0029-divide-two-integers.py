class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge cases
        if divisor == 0:
            return INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        
        # Take the absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            # Keep subtracting divisor from dividend until dividend becomes smaller
            # than divisor
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign to the quotient
        quotient *= sign
        
        # Ensure the quotient is within the 32-bit signed integer range
        quotient = max(INT_MIN, min(quotient, INT_MAX))
        return quotient

        