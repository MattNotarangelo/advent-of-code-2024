# https://adventofcode.com/2024/day/6


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
    visited_points = set()
    while x >= 0 and x < len(arr) and y >= 0 and y < len(arr[0]):
        if arr[x][y] == OBSTACLE:
            # reverse back
            x -= DIRECTIONS[direction][0]
            y -= DIRECTIONS[direction][1]
            direction = (direction + 1) % 4

        visited_points.add((x, y))
        x += DIRECTIONS[direction][0]
        y += DIRECTIONS[direction][1]

    return len(visited_points)


def solve(arr):
    arr = parse_input(arr)
    res = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] in ROTATIONS_INV:
                res = iterate(arr, row, col, ROTATIONS_INV[arr[row][col]])
    return res
