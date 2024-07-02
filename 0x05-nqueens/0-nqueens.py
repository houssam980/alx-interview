#!/usr/bin/python3
"""
Solution to the nqueens problem
"""


import sys

def is_valid(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        if board[i] == j:
            return False

    return True

def solve_nqueens_util(board, row, n):
    if row >= n:

        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        print(solution)
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)
            board[row] = -1

def solve_nqueens(n):
    board = [-1] * n
    solve_nqueens_util(board, 0, n)

def main():
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

    solve_nqueens(N)

if __name__ == "__main__":
    main()

