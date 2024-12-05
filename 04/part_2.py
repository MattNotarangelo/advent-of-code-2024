# https://adventofcode.com/2024/day/4

import collections

DIRECTIONS = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

LETTERS = ["M", "A", "S"]


def parse_input(s: str):
    rows = s.strip().split("\n")

    return [list(row) for row in rows]


def search(s, i, j, direction, letter_idx, pos):
    if i < 0 or i >= len(s) or j < 0 or j >= len(s[i]):
        return False
    if s[i][j] != LETTERS[letter_idx]:
        return False
    if letter_idx == len(LETTERS) - 1:
        pos[(i - direction[0], j - direction[1])] += 1
        return True
    return search(s, i + direction[0], j + direction[1], direction, letter_idx + 1, pos)


def solve(s):
    pos = collections.defaultdict(int)

    s = parse_input(s)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == LETTERS[0]:
                for direction in DIRECTIONS:
                    search(s, i + direction[0], j + direction[1], direction, 1, pos)
    res = 0
    for i in pos:
        if pos[i] > 1:
            res += 1
    return res
