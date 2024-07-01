#!/usr/bin/python3
"""
nqueens
"""
import sys


def backtrack(ro, n, cols, pos, neg, board):
    """
    backtrack
    """
    if ro == n:
        resu = []
        for leaps in range(len(board)):
            for k in range(len(board[leaps])):
                if board[leaps][k] == 1:
                    resu.append([leaps, k])
        print(resu)
        return

    for c in range(n):
        if c in cols or (ro + c) in pos or (ro - c) in neg:
            continue

        cols.add(c)
        pos.add(ro + c)
        neg.add(ro - c)
        board[ro][c] = 1

        backtrack(ro+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(ro + c)
        neg.remove(ro - c)
        board[ro][c] = 0


def nqueens(n):
    """
    Solution
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
