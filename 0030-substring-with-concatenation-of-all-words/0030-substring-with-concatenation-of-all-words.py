from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_freq = Counter(words)
        result = []
        
        for i in range(word_len):
            left, right = i, i
            word_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    word_count[word] += 1
                    while word_count[word] > word_freq[word]:
                        word_count[s[left:left + word_len]] -= 1
                        left += word_len
                        
                    if right - left == total_len:
                        result.append(left)
                else:
                    word_count.clear()
                    left = right
        
        return result
