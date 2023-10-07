class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            carry = 0
            for j in range(len2 - 1, -1, -1):
                temp = int(num1[i]) * int(num2[j]) + carry + result[i + j + 1]
                carry = temp // 10
                result[i + j + 1] = temp % 10

            result[i] += carry

        # Convert the list of integers to a string
        result_str = ''.join(map(str, result))

        # Remove leading zeros, if any
        return result_str.lstrip('0') or '0'

# Example usage
sol = Solution()
num1_1, num2_1 = "2", "3"
num1_2, num2_2 = "123", "456"

print(sol.multiply(num1_1, num2_1))  # Output: "6"
print(sol.multiply(num1_2, num2_2))  # Output: "56088"
