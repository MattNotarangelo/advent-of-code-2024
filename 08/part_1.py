# https://adventofcode.com/2024/day/8

import collections

NOTHING = "."
ANTINODE = "#"


def parse_input(arr):
    return [list(i) for i in arr.split("\n")]


def print_board(board):
    for row in board:
        print("".join(row))
    print()


def set_board(board, i, j, val):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
        return
    board[i][j] = val


def solve(board):
    board = parse_input(board)
    d = collections.defaultdict(list)
    for idy, row in enumerate(board):
        for idx, val in enumerate(row):
            if val != NOTHING:
                d[val].append((idy, idx))

    for key in d:
        if len(d[key]) < 2:
            continue

        for i in range(0, len(d[key])):
            for j in range(i + 1, len(d[key])):
                diff_y = d[key][j][0] - d[key][i][0]
                diff_x = d[key][j][1] - d[key][i][1]

                set_board(board, d[key][j][0] + diff_y, d[key][j][1] + diff_x, ANTINODE)
                set_board(board, d[key][i][0] - diff_y, d[key][i][1] - diff_x, ANTINODE)

    res = 0
    for idx, row in enumerate(board):
        for idy, val in enumerate(row):
            if val == ANTINODE:
                res += 1
    return res
