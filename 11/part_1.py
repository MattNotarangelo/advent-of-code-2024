# https://adventofcode.com/2024/day/11

import collections

TARGET_DEPTH = 25


def parse_input(s):
    return s.split(" ")


def iterate(val, depth, mapping, target_depth):

    if depth == target_depth:
        return 1

    if val in mapping and depth in mapping[val]:
        return mapping[val][depth]

    count = 0

    if val == "0":
        count += iterate("1", depth + 1, mapping, target_depth)
    elif len(val) % 2 == 0:
        count += iterate(str(int(val[: len(val) // 2])), depth + 1, mapping, target_depth)
        count += iterate(str(int(val[len(val) // 2 :])), depth + 1, mapping, target_depth)
    else:
        count += iterate(str(int(val) * 2024), depth + 1, mapping, target_depth)
    mapping[val][depth] = count
    return count


def solve(s):
    s = parse_input(s)

    count = 0
    for i in s:
        count += iterate(i, 0, collections.defaultdict(dict), TARGET_DEPTH)
    return count
