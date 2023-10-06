class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_result = self.countAndSay(n - 1)
        result = ""
        count = 1
        
        for i in range(1, len(prev_result)):
            if prev_result[i] == prev_result[i - 1]:
                count += 1
            else:
                result += str(count) + prev_result[i - 1]
                count = 1
        
        # Handle the last digit(s)
        result += str(count) + prev_result[-1]
        
        return result

        