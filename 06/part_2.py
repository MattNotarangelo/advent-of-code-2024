# https://adventofcode.com/2024/day/6

from collections import defaultdict

ROTATIONS_INV = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3,
}

DIRECTIONS = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


OBSTACLE = "#"


def parse_input(s):
    rows = s.strip().split("\n")
    return [list(row) for row in rows]


def iterate(arr, x, y, direction):
    visited_points = defaultdict(set)
    while x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]):
        if arr[x][y] == OBSTACLE:
            # reverse back
            x -= DIRECTIONS[direction][0]
            y -= DIRECTIONS[direction][1]
            direction = (direction + 1) % 4

        visited_points[(x, y)].add(direction)  # need to store direction too for proper cycle detection
        x += DIRECTIONS[direction][0]
        y += DIRECTIONS[direction][1]

        # check cycles
        if (x, y) in visited_points and direction in visited_points[(x, y)]:
            return True

    return False


def solve(arr):
    arr = parse_input(arr)
    res = 0
    x_start = -1
    y_start = -1

    # find starting point
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] in ROTATIONS_INV:
                x_start = row
                y_start = col

    # brute force all obstacles
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            copy = [row.copy() for row in arr]
            copy[row][col] = OBSTACLE
            res += iterate(copy, x_start, y_start, ROTATIONS_INV[arr[x_start][y_start]])
    return res
