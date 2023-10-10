from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx):
            # If the current index is equal to the length of the word, it means the word is found
            if idx == len(word):
                return True
            
            # Check if the current cell is out of the grid or doesn't match the word character
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            
            # Save the current cell value and mark it as visited
            temp, board[i][j] = board[i][j], '/'
            
            # Explore neighboring cells in DFS manner
            found = dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i, j - 1, idx + 1)
            
            # Restore the original cell value (backtrack)
            board[i][j] = temp
            
            return found

        m, n = len(board), len(board[0])
        
        # Start DFS from each cell to find the word
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
