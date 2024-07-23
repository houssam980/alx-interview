""" Making changes """


def makeChange(coins, total):
    """ Generate changes
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for lp in coins:
        while check < total:
            check += lp
            temp += 1
        if check == total:
            return temp
        check -= lp
        temp -= 1
    return -1
