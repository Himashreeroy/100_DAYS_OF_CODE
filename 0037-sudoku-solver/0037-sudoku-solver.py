from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False
            return True
        
        solve(board)
