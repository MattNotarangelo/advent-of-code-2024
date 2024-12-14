# https://adventofcode.com/2024/day/14
import re
import collections

ITERS = 100
SIZE = (101, 103)


def parse_input(s):
    ret = []
    s = s.split("\n")
    for i in s:
        m = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", i)
        ret.append({"p": [int(m[0][0]), int(m[0][1])], "v": [int(m[0][2]), int(m[0][3])]})
    return ret


def calculate_score(s):
    buckets = collections.defaultdict(int)
    for i in s:
        if i["p"][0] < SIZE[0] // 2 and i["p"][1] < SIZE[1] // 2:
            buckets[0] += 1
        elif i["p"][0] > SIZE[0] // 2 and i["p"][1] < SIZE[1] // 2:
            buckets[1] += 1
        elif i["p"][0] < SIZE[0] // 2 and i["p"][1] > SIZE[1] // 2:
            buckets[2] += 1
        elif i["p"][0] > SIZE[0] // 2 and i["p"][1] > SIZE[1] // 2:
            buckets[3] += 1

    score = 1
    for i in buckets:
        score *= buckets[i]
    return score


def solve(s):
    s = parse_input(s)

    for idx, i in enumerate(s):
        i["p"][0] = (i["p"][0] + i["v"][0] * ITERS) % SIZE[0]
        i["p"][1] = (i["p"][1] + i["v"][1] * ITERS) % SIZE[1]
        s[idx] = i

    return calculate_score(s)
