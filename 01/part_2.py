#!/usr/bin/env python3
"""
https://adventofcode.com/2024/day/1
"""

from collections import Counter


def parse_input(s: str) -> tuple[list[int], list[int]]:
    c1 = []
    c2 = []
    for i in s.strip().split("\n"):
        items = i.split("   ")
        c1.append(int(items[0]))
        c2.append(int(items[1]))

    return c1, c2


def solve(s: str) -> int:
    score = 0

    c1, c2 = parse_input(s)
    counter_c2 = Counter(c2)

    for i in c1:
        score += counter_c2[i] * i

    return score
