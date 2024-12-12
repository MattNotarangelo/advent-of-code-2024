# https://adventofcode.com/2024/day/10


def parse_input(s):
    return [list(map(int, list(i))) for i in s.strip().split("\n")]


def search(s, x, y, curr):
    if x < 0 or x >= len(s[0]) or y < 0 or y >= len(s):
        return []
    elif s[y][x] != curr:
        return []
    elif curr == 9:
        return [(x, y)]

    ret = []
    ret.extend(search(s, x + 1, y, curr + 1))
    ret.extend(search(s, x - 1, y, curr + 1))
    ret.extend(search(s, x, y + 1, curr + 1))
    ret.extend(search(s, x, y - 1, curr + 1))
    return ret


def solve(s):
    s = parse_input(s)
    score = 0
    for idy in range(len(s)):
        for idx in range(len(s[0])):
            score += len(set(search(s, idx, idy, 0)))
    return score
