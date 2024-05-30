#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of ints
    """
    key = []
    if n <= 0:
        return key
    key = [[1]]
    for iter in range(1, n):
        temp = [1]
        for j in range(len(key[iter - 1]) - 1):
            curr = key[iter - 1]
            temp.append(key[iter - 1][j] + key[iter - 1][j + 1])
        temp.append(1)
        key.append(temp)
    return key
