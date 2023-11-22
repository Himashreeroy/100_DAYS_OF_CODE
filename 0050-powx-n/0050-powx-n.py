class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: x^0 = 1
        if n == 0:
            return 1.0
        
        # If n is negative, calculate reciprocal and change n to positive
        if n < 0:
            x = 1 / x
            n = -n

        # Recursive calculation using the property x^n = (x^(n/2))^2
        half_pow = self.myPow(x, n // 2)
        
        # If n is even, x^n = (x^(n/2))^2
        if n % 2 == 0:
            return half_pow * half_pow
        # If n is odd, x^n = x * (x^(n/2))^2
        else:
            return x * half_pow * half_pow

# Example usage:
solution = Solution()
print(solution.myPow(2.00000, 10))  # Output: 1024.00000
print(solution.myPow(2.10000, 3))   # Output: 9.26100
print(solution.myPow(2.00000, -2))  # Output: 0.25000
