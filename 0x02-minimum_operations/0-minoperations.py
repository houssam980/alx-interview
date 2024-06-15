#!/usr/bin/python3
""" Min op
    """

def minOperations(n: int) -> int:

    nxt = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            nxt = body
            body += body
        else:
            op += 1
            body += nxt
    if len(body) != n:
        return 0
    return op
