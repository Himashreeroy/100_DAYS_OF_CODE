class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            # If there is no carry, return the updated digits array
            if digits[i] < 10:
                return digits
            # If there is a carry, set the current digit to 0 and continue to the next digit
            digits[i] = 0
        
        # If there is a carry after iterating through all digits, insert 1 at the beginning
        digits.insert(0, 1)
        return digits
