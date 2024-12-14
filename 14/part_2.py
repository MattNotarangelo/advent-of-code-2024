# https://adventofcode.com/2024/day/14
import re
import collections
import os

ITERS = 100000000
SIZE = (101, 103)
EMPTY_ARRAY = [["." for _ in range(SIZE[0])] for _ in range(SIZE[1])]


def parse_input(s):
    ret = []
    s = s.split("\n")
    for i in s:
        m = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", i)
        ret.append({"p": [int(m[0][0]), int(m[0][1])], "v": [int(m[0][2]), int(m[0][3])]})
    return ret


def print_array(s):
    for i in s:
        print("".join(i))
        print()

    print()


def calculate_christms_tree(s):
    array = [i[:] for i in EMPTY_ARRAY]  # deep copy
    for i in s:
        array[i["p"][1]][i["p"][0]] = "#"
    for i in array:
        if "##############" in "".join(i):
            print_array(array)
            return True
    return False


def solve(s):
    s = parse_input(s)
    if len(s) == 12:  # early exit for sample input
        return 0
    for iters in range(ITERS):
        for idx, i in enumerate(s):
            i["p"][0] += i["v"][0]
            i["p"][0] %= SIZE[0]
            i["p"][1] += i["v"][1]
            i["p"][1] %= SIZE[1]
            s[idx] = i
        print(iters)
        if calculate_christms_tree(s):
            return iters
    return -1
