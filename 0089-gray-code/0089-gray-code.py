class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        gray_code = [0, 1]

        for i in range(1, n):
            mask = 1 << i
            for j in range(len(gray_code) - 1, -1, -1):
                gray_code.append(gray_code[j] | mask)

        return gray_code
