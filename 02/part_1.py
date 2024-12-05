#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/1
"""


def parse_input(s):
    out = []
    for line in s.strip().split("\n"):
        items = line.split(" ")
        items = [int(i) for i in items]
        out.append(items)

    return out


def solve(s):
    reports = parse_input(s)
    count = 0
    for report in reports:
        tmp = []
        for i in range(1, len(report)):
            tmp.append(report[i] - report[i - 1])

        if all([3 >= i >= 1 for i in tmp]) or all([-3 <= i <= -1 for i in tmp]):
            count += 1
    return count
