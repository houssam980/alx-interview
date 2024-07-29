#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter
    """
    # determ
    rowss = len(grid)
    colms = len(grid[0])

    # Initialize
    perimeter = 0

    # Lp each
    for lp_1 in range(rowss):
        for lp_2 in range(colms):
            if grid[lp_1][lp_2] == 1:
                # Check part
                if lp_1 == 0 or grid[lp_1-1][lp_2] == 0:
                    perimeter += 1
                # Check buttom
                if lp_1 == rowss-1 or grid[lp_1+1][lp_2] == 0:
                    perimeter += 1
                # Check left
                if lp_2 == 0 or grid[lp_1][lp_2-1] == 0:
                    perimeter += 1
                # Check right
                if lp_2 == colms-1 or grid[lp_1][lp_2+1] == 0:
                    perimeter += 1

    # Return result
    return perimeter
