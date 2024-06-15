#!/usr/bin/python3
""" Minimum op
    """


def minOperations(n: int) -> int:
    """ Minimum Operations """
    next = 'H'
    bdy = 'H'
    op = 0
    while (len(bdy) < n):
        if n % len(bdy) == 0:
            op += 2
            next = bdy
            bobdydy += bdy
        else:
            op += 1
            bdy += next
    if len(bdy) != n:
        return 0
    return op
