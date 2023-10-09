class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables to store the result and carry
        result = []
        carry = 0
        
        # Convert binary strings to lists of integers and reverse them for easier processing
        a = list(map(int, a[::-1]))
        b = list(map(int, b[::-1]))
        
        # Iterate through the binary strings and perform addition
        for i in range(max(len(a), len(b))):
            # Get the digits at the current position, or 0 if the position is out of range
            digit_a = a[i] if i < len(a) else 0
            digit_b = b[i] if i < len(b) else 0
            
            # Calculate the sum and carry
            total = digit_a + digit_b + carry
            result.append(str(total % 2))  # Append the least significant bit of the sum
            carry = total // 2  # Calculate the carry for the next iteration
        
        # If there is a remaining carry, append it to the result
        if carry:
            result.append(str(carry))
        
        # Reverse the result list and join it into a string
        return ''.join(result[::-1])
