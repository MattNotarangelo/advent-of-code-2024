#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/1
"""


def parse_input(s):
    c1 = []
    c2 = []
    for i in s.strip().split("\n"):
        items = i.split("   ")
        c1.append(int(items[0]))
        c2.append(int(items[1]))

    return c1, c2


def solve(s: str):
    score = 0

    c1, c2 = parse_input(s)
    c1.sort()
    c2.sort()

    for i, j in zip(c1, c2):
        score += abs(i - j)

    return score
