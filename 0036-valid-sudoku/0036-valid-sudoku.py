from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
        
        # Check columns
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
        
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] != '.':
                            if board[x][y] in sub_box:
                                return False
                            sub_box.add(board[x][y])
        
        return True

        