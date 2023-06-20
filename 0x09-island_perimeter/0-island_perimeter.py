#!/usr/bin/python3
"""
   Island Perimeter module
"""


def island_perimeter(grid):
    """
       function def island_perimeter(grid): that returns the perimeter
       of the island described in grid:
       args:
             grid
       Return:
             perimeter of the island
    """
    area = 0
    for i in grid + list(map(list, zip(*grid))):
        for j, k in zip([0] + i, i + [0]):
            area += int(j != k)
    return area
