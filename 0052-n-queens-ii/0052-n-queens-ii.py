class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            # Check if there is a queen in the same column
            for prev_row in range(row):
                if board[prev_row] == col or \
                   board[prev_row] - prev_row == col - row or \
                   board[prev_row] + prev_row == col + row:
                    return False
            return True

        def solve(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    board[row] = col
                    solve(row + 1)
                    board[row] = 0  # backtrack

        board = [0] * n
        count = 0
        solve(0)
        return count

        