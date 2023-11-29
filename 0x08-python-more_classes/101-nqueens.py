#!/usr/bin/python3
import sys
"""
Nqueens

places N non-attackig queens on a N*N chessboard"""


class NQueensSolver:
    """NQueensSolver class, checking for exit signals and corrct code output"""
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[i] == row or abs(board[i] - row) == abs(i - col):
                return False
        return True

    def solve_n_queens(self, board, col):
        if col == self.n:
            self.solutions.append(list(board))
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(board, i, col):
                board[col] = i
                res = self.solve_n_queens(board, col + 1) or res
                board[col] = -1

        return res

    def solve(self):
        board = [-1] * self.n
        self.solve_n_queens(board, 0)

        for sol in self.solutions:
            formatted_solution = [[row, col] for col, row in enumerate(sol)]
            print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.solve()
