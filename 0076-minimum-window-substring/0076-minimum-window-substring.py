from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        required_chars = len(t_counter)
        left, right = 0, 0
        formed_chars = 0
        window_counts = {}
        ans = float("inf"), 0, 0  # length, left, right
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_counter and window_counts[char] == t_counter[char]:
                formed_chars += 1
            
            while formed_chars == required_chars:
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right + 1
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_counter and window_counts[left_char] < t_counter[left_char]:
                    formed_chars -= 1
                left += 1
            
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]]

    