# https://adventofcode.com/2024/day/11


import collections
from part_1 import iterate as part_1_iterate

TARGET_DEPTH = 75


def parse_input(s):
    return s.split(" ")


def solve(s):
    s = parse_input(s)

    count = 0
    for i in s:
        count += part_1_iterate(i, 0, collections.defaultdict(dict), TARGET_DEPTH)
    return count
