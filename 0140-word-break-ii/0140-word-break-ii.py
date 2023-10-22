class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(index):
            if index == len(s):
                return [""]
            if index in memo:
                return memo[index]
            
            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in wordSet:
                    next_sentences = backtrack(end)
                    for sentence in next_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            
            memo[index] = sentences
            return sentences
        
        return backtrack(0)
 