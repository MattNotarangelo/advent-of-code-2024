# https://adventofcode.com/2024/day/4

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

LETTERS = ["X", "M", "A", "S"]


def parse_input(s: str):
    rows = s.strip().split("\n")

    return [list(row) for row in rows]


def search(s, i, j, direction, letter_idx):
    if i < 0 or i >= len(s) or j < 0 or j >= len(s[i]):
        return False
    if s[i][j] != LETTERS[letter_idx]:
        return False
    if letter_idx == len(LETTERS) - 1:
        return True

    return search(s, i + direction[0], j + direction[1], direction, letter_idx + 1)


def solve(s):
    s = parse_input(s)
    res = 0

    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == LETTERS[0]:
                for direction in DIRECTIONS:
                    if search(s, i + direction[0], j + direction[1], direction, 1):
                        res += 1
    return res
