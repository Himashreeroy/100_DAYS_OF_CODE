from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set([beginWord])
        
        while queue:
            current_word, steps = queue.popleft()
            if current_word == endWord:
                return steps
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in wordSet and next_word not in visited:
                        queue.append((next_word, steps + 1))
                        visited.add(next_word)
        
        return 0
