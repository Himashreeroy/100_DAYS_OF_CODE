class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)
        numbers = [str(i) for i in range(1, n + 1)]
        result = []
        
        # Calculate factorials from 1 to n
        for i in range(2, n + 1):
            factorial[i] = i * factorial[i - 1]
        
        k -= 1  # Convert k to 0-based index
        
        # Generate the kth permutation
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(numbers.pop(index))
        
        return ''.join(result)
