class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col):
            # Check if there is a queen in the same column
            for prev_row in range(row):
                if board[prev_row] == col or \
                   board[prev_row] - prev_row == col - row or \
                   board[prev_row] + prev_row == col + row:
                    return False
            return True

        def solve(row):
            if row == n:
                solutions.append(["".join(["Q" if col == board[row] else "." for col in range(n)]) for row in range(n)])
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    board[row] = col
                    solve(row + 1)
                    board[row] = 0  # backtrack

        board = [0] * n
        solutions = []
        solve(0)
        return solutions
